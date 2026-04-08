---
title: "하네스 엔지니어링 1단계 — 개요 및 핵심 개념"
description: Harness가 무엇인지, 왜 기존 CI/CD 도구와 다른지, 핵심 개념을 정리합니다.
date: 2026-04-08
category: Harness
tags: [harness, ci-cd, devops, platform-engineering]
---

## Harness란 무엇인가

Harness는 소프트웨어 딜리버리 전 과정을 자동화하는 **플랫폼 엔지니어링 툴**입니다. CI, CD, Feature Flags, Cloud Cost Management, Chaos Engineering까지 하나의 플랫폼에서 관리합니다.

기존 Jenkins나 GitHub Actions가 "빌드·배포 자동화 도구"라면, Harness는 여기에 **지능형 롤백**, **배포 검증**, **비용 최적화**까지 포함한 엔지니어링 플랫폼입니다.

## 왜 Harness인가

<div class="callout why">
  <div class="callout-title">Why</div>
  Jenkins는 플러그인 관리 부담이 크고, GitHub Actions는 복잡한 배포 전략(Canary, Blue/Green)을 구현하기 어렵습니다. Harness는 이를 기본 기능으로 제공합니다.
</div>

| 비교 항목 | Jenkins | GitHub Actions | Harness |
|-----------|---------|---------------|---------|
| 배포 전략 | 플러그인 필요 | 수동 구현 | 기본 내장 |
| 자동 롤백 | 없음 | 없음 | ML 기반 자동화 |
| Feature Flags | 없음 | 없음 | 기본 내장 |
| 비용 관리 | 없음 | 없음 | Cloud Cost 모듈 |
| 설정 방식 | Groovy DSL | YAML | YAML + UI |

## 핵심 개념

### Pipeline
하네스의 기본 실행 단위. **Stage**의 묶음으로 구성됩니다.

### Stage
파이프라인 안의 독립 실행 블록. CI, CD, Feature Flag, Approval 등의 타입이 있습니다.

### Step
Stage 안의 개별 작업. 빌드, 테스트, 배포, 알림 등을 정의합니다.

### Connector
외부 서비스(GitHub, GCP, Docker Hub 등)와의 연결 설정. 한 번 등록하면 모든 파이프라인에서 재사용합니다.

### Delegate
Harness가 실제 인프라에 명령을 실행하기 위한 **에이전트**. 클러스터 또는 VM에 설치합니다.

```
Harness Platform
    └── Pipeline
          ├── Stage (CI)
          │     ├── Step: Git Clone
          │     ├── Step: Build & Test
          │     └── Step: Push Image
          └── Stage (CD)
                ├── Step: Canary Deploy 10%
                ├── Step: Verify (metrics)
                └── Step: Promote to 100%
```

## Harness 모듈 구성

| 모듈 | 역할 |
|------|------|
| **CI** | 빌드, 테스트, 이미지 푸시 |
| **CD** | Kubernetes, ECS, VM 배포 |
| **FF (Feature Flags)** | 기능 플래그 관리 |
| **CCM** | 클라우드 비용 가시성 및 최적화 |
| **STO** | 보안 테스트 오케스트레이션 |
| **Chaos** | 장애 주입 및 복원력 테스트 |

다음 단계에서는 실제 환경을 구성하고 Delegate를 설치하는 방법을 다룹니다.
