---
title: "하네스 엔지니어링 3단계 — CI/CD 파이프라인 구축"
description: Harness로 빌드부터 Canary 배포까지 실전 파이프라인을 구성하는 방법을 다룹니다.
date: 2026-04-08
order: 3
category: Harness
tags: [harness, pipeline, ci, cd, canary, blue-green]
---

## 파이프라인 전체 구조

이 포스트에서 구축할 파이프라인은 다음과 같습니다.

```
Pipeline: deploy-production
  ├── Stage 1: CI — Build & Test
  │     ├── Git Clone
  │     ├── Run Tests
  │     ├── Build Docker Image
  │     └── Push to Artifact Registry
  └── Stage 2: CD — Canary Deploy
        ├── Canary Deployment (20%)
        ├── Verify (HTTP / Metrics)
        └── Promote to 100%
```

## CI Stage 구성

```yaml
stages:
  - stage:
      name: Build
      type: CI
      spec:
        cloneCodebase: true
        infrastructure:
          type: KubernetesDirect
          spec:
            connectorRef: gcp-prod
            namespace: harness-builds
        execution:
          steps:
            - step:
                name: Run Tests
                type: Run
                spec:
                  connectorRef: docker-hub
                  image: python:3.12-slim
                  command: |
                    pip install -r requirements.txt
                    pytest tests/ -v --tb=short

            - step:
                name: Build & Push Image
                type: BuildAndPushGAR
                spec:
                  connectorRef: gcp-prod
                  host: asia-northeast3-docker.pkg.dev
                  projectID: your-project
                  imageName: your-service
                  tags:
                    - <+pipeline.sequenceId>
                    - latest
```

## CD Stage — Canary 배포

<div class="callout why">
  <div class="callout-title">Why Canary</div>
  전체 트래픽의 일부만 새 버전으로 라우팅해 문제를 조기에 발견합니다. 이상 감지 시 자동 롤백이 트리거됩니다.
</div>

```yaml
  - stage:
      name: Deploy Production
      type: Deployment
      spec:
        deploymentType: Kubernetes
        service:
          serviceRef: your-service
        environment:
          environmentRef: production
          infrastructureDefinitions:
            - identifier: k8s-prod-cluster
        execution:
          steps:
            - stepGroup:
                name: Canary Deployment
                steps:
                  - step:
                      name: Canary Deploy
                      type: K8sCanaryDeploy
                      spec:
                        instanceSelection:
                          type: Percentage
                          spec:
                            percentage: 20

                  - step:
                      name: Verify
                      type: Verify
                      spec:
                        type: Canary
                        monitoredService:
                          type: Default
                        healthSources:
                          - identifier: prometheus
                        failureStrategies:
                          - onFailure:
                              errors: [Verification]
                              action:
                                type: ManualIntervention

                  - step:
                      name: Canary Delete
                      type: K8sCanaryDelete

            - step:
                name: Rolling Deploy
                type: K8sRollingDeploy
                spec:
                  skipDryRun: false
```

## 변수 및 표현식 활용

Harness는 `<+ >` 문법으로 동적 값을 참조합니다.

| 표현식 | 값 |
|--------|----|
| `<+pipeline.sequenceId>` | 파이프라인 실행 번호 |
| `<+artifact.tag>` | 배포할 이미지 태그 |
| `<+env.name>` | 현재 환경 이름 |
| `<+trigger.commitSha>` | 트리거된 커밋 SHA |
| `<+secrets.getValue("db_password")>` | Secret Manager 값 참조 |

## Failure Strategy

```yaml
failureStrategies:
  - onFailure:
      errors:
        - AllErrors
      action:
        type: StageRollback
```

스테이지 실패 시 자동으로 이전 버전으로 롤백합니다. Verification 실패는 별도로 `ManualIntervention` 을 설정해 승인 게이트를 둘 수 있습니다.

다음 단계에서는 Feature Flags, 배포 전략 심화, 운영 팁을 다룹니다.
