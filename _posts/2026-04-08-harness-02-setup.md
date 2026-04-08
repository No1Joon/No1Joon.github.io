---
title: "하네스 엔지니어링 2단계 — 환경 구성 및 Delegate 설치"
description: Harness 계정 설정부터 Kubernetes Delegate 설치까지 실전 가이드입니다.
date: 2026-04-08
order: 2
category: Harness
tags: [harness, delegate, kubernetes, setup]
---

## 사전 준비

| 항목 | 권장 사양 |
|------|-----------|
| Kubernetes 클러스터 | 1.24+ |
| Helm | 3.x |
| CPU / Memory | 0.5 vCPU / 768Mi 이상 |
| 아웃바운드 인터넷 | `app.harness.io` 443 포트 허용 |

## 1. Harness 계정 생성

`app.harness.io` 에서 무료 플랜으로 시작할 수 있습니다.

- **Account ID** — 설정 > Overview에서 확인
- **Account Secret** — Delegate 설치 시 사용

## 2. Connector 등록

### GitHub Connector

```yaml
connector:
  name: github-main
  type: Github
  spec:
    url: https://github.com/your-org
    authentication:
      type: Http
      spec:
        type: UsernameToken
        spec:
          username: your-username
          tokenRef: github_pat_secret
```

<div class="callout why">
  <div class="callout-title">Why</div>
  PAT(Personal Access Token)는 Harness Secret Manager에 저장합니다. 파이프라인 YAML에 토큰을 직접 쓰지 않아도 됩니다.
</div>

### GCP Connector

```yaml
connector:
  name: gcp-prod
  type: Gcp
  spec:
    credential:
      type: ManualConfig
      spec:
        secretKeyRef: gcp_sa_key
```

## 3. Kubernetes Delegate 설치

### Helm으로 설치

```bash
helm repo add harness https://app.harness.io/storage/harness-download/harness-helm-charts/
helm repo update

helm install harness-delegate harness/harness-delegate-ng \
  --namespace harness-delegate \
  --create-namespace \
  --set delegateName=k8s-delegate \
  --set accountId=YOUR_ACCOUNT_ID \
  --set delegateToken=YOUR_DELEGATE_TOKEN \
  --set managerEndpoint=https://app.harness.io \
  --set delegateDockerImage=harness/delegate:latest \
  --set replicas=1
```

### Delegate 상태 확인

```bash
kubectl get pods -n harness-delegate

# 정상 출력 예시
NAME                               READY   STATUS    RESTARTS
harness-delegate-xxx-yyy           1/1     Running   0
```

Harness UI에서 **Account Settings > Delegates** 로 이동하면 연결된 Delegate 목록과 상태를 확인할 수 있습니다.

## 4. Secret Manager 구성

Harness는 기본으로 내장 Secret Manager를 제공하지만, GCP Secret Manager 또는 HashiCorp Vault와 연동할 수 있습니다.

```yaml
secretManager:
  name: gcp-secret-manager
  type: GcpSecretManager
  spec:
    credentialsRef: gcp-connector
    projectId: your-gcp-project
```

## 5. 환경(Environment) 및 인프라 정의

```yaml
environment:
  name: production
  type: Production

infrastructure:
  name: k8s-prod-cluster
  type: KubernetesDirect
  spec:
    connectorRef: gcp-prod
    namespace: production
    releaseName: release-<+INFRA_KEY>
```

다음 단계에서는 이 환경 위에 실제 CI/CD 파이프라인을 구축합니다.
