# Blog Post Series — Gemini 작업 지시서

## 미션

No1Joon Tech Blog(Jekyll·GitHub Pages)에 **총 69편**의 한국어 기술 포스트를 20개 시리즈로 작성한다. 기존 포스트와 **동일한 톤·구조·시각화 수준**을 유지하는 것이 최우선.

- 저장소: `/Users/joon/Documents/blog/No1Joon.github.io`
- 포스트 위치: `_posts/`
- 라이브 URL: <https://no1joon.github.io>
- 카테고리 정의: `_data/categories.yml`

---

## 준비 — 반드시 먼저 읽을 것

### 스타일 기준 파일 (내용을 Gemini 컨텍스트에 로드)

1. `.claude/skills/blog-post/SKILL.md` — 목소리·구조·시각화 규칙
2. `.claude/skills/post-plan/SKILL.md` — 제목 규칙
3. `.claude/skills/mermaid/SKILL.md` — mermaid 색상 팔레트·노드 모양

### 톤 레퍼런스 (작성 전 3개 이상 정독)

- `_posts/2026-04-20-kubernetes-01-overview.md`
- `_posts/2026-04-20-helm-01-overview.md`
- `_posts/2026-04-20-docker-01-image.md`
- `_posts/2026-04-15-github-actions-01-overview.md`

---

## 절대 규칙 (위반 시 재작성)

### 1. 언어와 톤 (자유)

- 한국어로 작성
- **해요체·합쇼체 자유** — 어느 쪽이든, 섞어도 됨. 단 **한 포스트 안에서는 톤 일관성** 유지
- 표·리스트 내부 짧은 구절은 명사형·사전형 허용 (예: "빌드 결과물 전달")
- 과장·마케팅 표현은 사용 언어와 무관하게 금지 ("최고의", "혁신적인" 등)

### 2. 제목 규칙 (post-plan)

- 15자 내외, 최대 25자
- **부제 금지** (`—`로 설명 붙이지 않음)
- "Part 2" 같은 모호한 제목 금지

### 3. 코드 최소화

- 전체 설정 덤프 금지 → **핵심 5~15줄만 발췌**
- 같은 개념을 코드로 반복하지 않음 → 표·문장으로 대체
- 코드는 기본값이 아니라 **개념 보조 선택지**

### 4. 시각화 우선

구조 여러 겹·순서 있는 흐름·추상 관계 설명 시 시각화 필수. 고정 개수 규칙 없음.

| 상황 | 선택 |
|---|---|
| 아키텍처·컴포넌트 관계 | mermaid `flowchart` |
| 시간 순 호출 흐름 | mermaid `sequenceDiagram` |
| 상태 전이·라이프사이클 | mermaid `stateDiagram-v2` |
| 옵션·타입 비교 | Markdown table |
| 디렉토리 트리·설정 계층 | plain code block |

### 5. Mermaid 색상 팔레트 (필수 통일)

모든 mermaid 블록 끝에 아래 classDef 정의 및 적용.

```
classDef primary fill:#2563eb,stroke:#1e40af,color:#ffffff
classDef success fill:#059669,stroke:#047857,color:#ffffff
classDef info fill:#0891b2,stroke:#0e7490,color:#ffffff
classDef warning fill:#d97706,stroke:#b45309,color:#ffffff
classDef danger fill:#dc2626,stroke:#991b1b,color:#ffffff
classDef neutral fill:#475569,stroke:#334155,color:#ffffff
```

ASCII 아트 금지. 다이어그램은 반드시 mermaid.

### 6. 줄바꿈·문단 규칙

- 한 문단 2~4문장, 넘으면 빈 줄로 분리
- 한 문장 80자 초과 시 쉼표·접속사 지점에서 **문장 자체를 쪼개기**
- 리스트·코드·표·다이어그램·callout 앞뒤로 **항상 빈 줄 한 줄**

### 7. Front Matter (모든 포스트 필수)

```yaml
---
title: "제목"
description: 한 줄 요약 (자연스러운 문장 또는 명사형)
date: 2026-04-20
order: 1
category: (categories.yml의 name 값 그대로)
subcategory: (categories.yml의 name 값 그대로)
tags: [kebab-case, 5~8개]
---
```

### 8. Liquid 충돌 방지

Helm·Jekyll 같이 `{{ ... }}` 문법이 본문에 등장하면 본문 전체를 `{% raw %}` / `{% endraw %}` 로 감쌀 것. 아니면 Jekyll 빌드 경고.

### 9. 금지 사항

- 이모지 (명시 요청 없는 한)
- 과장 ("최고의", "혁신적인")
- 근거 없는 성능 수치
- 한 포스트에 `##` 섹션 10개 초과 (그 이상이면 분할 고려)

---

## 포스트 구조 템플릿

```markdown
---
(front matter)
---

(오프닝: 1~2문단, 실무 문제 제기 또는 맥락 설명. "~팀이라면 공통적으로 겪는 문제가 있어요" 류)

## (첫 섹션 — 개념·전체 그림)

(한 문단 설명 → 표 또는 다이어그램 → 필요 시 짧은 코드)

## (두 번째 섹션)

...

<div class="callout why">
  <div class="callout-title">핵심 인사이트</div>
  (한 문단으로 "왜 이게 중요한가" 또는 "흔한 오해"를 짚음. 남발 금지, 포스트당 1~2개)
</div>

## 정리

- 3~6개 불릿으로 핵심 요약
- 시리즈의 다음 편 티저 ("다음 글에서는 ~를 다뤄요.")
```

**길이 가이드**: 250~450 라인이 적정. 150 미만은 부족, 600 초과는 분할 검토.

---

## 작업 흐름 (Per-Post Workflow)

각 포스트마다 반복:

1. **읽기** — 해당 시리즈의 직전 포스트(있으면) + 아래 작업 지시
2. **작성** — `Write` 도구로 `_posts/YYYY-MM-DD-slug.md` 생성
3. **검증** — `bundle exec jekyll build 2>&1 | grep -iE "warning|error"` 실행, Liquid error 없는지 확인
4. **다음으로** — 시리즈 한 편씩 순서대로

### 커밋 정책

- **시리즈 단위로 커밋** (3~5편 단위)
- 커밋 메시지 한국어, **Co-Authored-By 라인 넣지 않음**
- 커밋 후 즉시 `git push origin HEAD:main` (현재 브랜치가 main을 track하지만 이름이 다를 수 있음)

커밋 메시지 예시:

```
Service Mesh 시리즈 3편 추가

- 01-overview: 개념·구조
- 02-traffic: 트래픽 관리·라우팅
- 03-security: mTLS·관측성

코드 최소화·mermaid 색상 규칙 준수.
```

---

## 작업 목록 (69편)

각 항목은 완료 시 `[ ]` → `[x]`로 체크. 포스트별 **핵심 다룰 내용**을 힌트로 제공 — 이 항목들을 모두 **커버**하되 순서·구성은 자유.

### ⚙️ Container & Orchestration

#### Service Mesh (3편)

- [x] **1.1** `_posts/2026-04-20-service-mesh-01-overview.md`
  - 제목: `Service Mesh 개념과 구조`
  - description: `사이드카 기반 Service Mesh가 해결하는 문제와 Istio·Linkerd 데이터 플레인 구조를 정리해요.`
  - tags: `[service-mesh, istio, linkerd, sidecar, kubernetes]`
  - 다룰 것: 왜 Service Mesh인가(라이브러리 대비 장점), 데이터 플레인 vs 컨트롤 플레인, Envoy 사이드카 동작, Istio·Linkerd 간단 비교

- [x] **1.2** `_posts/2026-04-20-service-mesh-02-traffic.md`
  - 제목: `트래픽 관리와 라우팅 정책`
  - description: `VirtualService·DestinationRule로 Canary·재시도·타임아웃을 구현하는 패턴을 정리해요.`
  - tags: `[service-mesh, istio, traffic, canary, circuit-breaker]`
  - 다룰 것: VirtualService/DestinationRule 역할, Canary·Weight 분산, Retry·Timeout·Circuit Breaker, Fault Injection

- [x] **1.3** `_posts/2026-04-20-service-mesh-03-security.md`
  - 제목: `mTLS와 관측성 통합`
  - description: `Service Mesh가 제공하는 자동 mTLS와 분산 추적·메트릭 수집의 원리를 정리해요.`
  - tags: `[service-mesh, mtls, observability, istio, security]`
  - 다룰 것: 자동 mTLS 동작 원리, PeerAuthentication/AuthorizationPolicy, Envoy 메트릭, 분산 추적 전파, 성능 오버헤드

---

### ☁️ Cloud Infrastructure

#### Terraform/IaC (4편)

- [ ] **2.1** `_posts/2026-04-20-terraform-iac-01-overview.md`
  - 제목: `Terraform 기본 구조`
  - description: `HCL 문법과 provider·resource·data·output 구성 요소가 선언적 IaC를 어떻게 구성하는지 정리해요.`
  - tags: `[terraform, iac, hcl, provider, infrastructure]`
  - 다룰 것: Terraform vs CloudFormation vs Pulumi, HCL 구조(provider/resource/variable/output), plan → apply 흐름, 선언적 사고

- [ ] **2.2** `_posts/2026-04-20-terraform-iac-02-modules.md`
  - 제목: `모듈과 재사용 설계`
  - description: `인프라 중복을 제거하는 Terraform 모듈 구조와 root·child 모듈 설계 원칙을 정리해요.`
  - tags: `[terraform, module, reusable, iac, design]`
  - 다룰 것: module 개념, public vs private module, input/output 설계, 버전 고정, 폴더 구조 패턴

- [ ] **2.3** `_posts/2026-04-20-terraform-iac-03-state.md`
  - 제목: `State 관리와 협업`
  - description: `tfstate 원격 백엔드와 state locking으로 팀 협업을 안전하게 만드는 방법을 정리해요.`
  - tags: `[terraform, state, backend, s3, locking]`
  - 다룰 것: state가 뭐고 왜 중요한가, remote backend (S3+DynamoDB, Terraform Cloud), state locking, import/mv/rm 기본

- [ ] **2.4** `_posts/2026-04-20-terraform-iac-04-cicd.md`
  - 제목: `Terraform CI와 테스트`
  - description: `plan 리뷰·tflint·terratest로 IaC를 코드처럼 검증하는 파이프라인을 구성해요.`
  - tags: `[terraform, cicd, testing, terratest, tflint]`
  - 다룰 것: PR 기반 plan 자동 포스팅 (Atlantis/TFC), tflint·tfsec, terratest, drift detection

#### AWS (5편)

- [ ] **3.1** `_posts/2026-04-20-aws-01-iam.md`
  - 제목: `AWS 계정 구조와 IAM`
  - description: `Organizations·SCP·IAM Role 기반의 멀티 계정 권한 모델을 정리해요.`
  - tags: `[aws, iam, organizations, scp, security]`
  - 다룰 것: 멀티 계정 왜(분리·청구·격리), Organizations·OU·SCP, IAM User vs Role, AssumeRole 플로우, 최소 권한

- [ ] **3.2** `_posts/2026-04-20-aws-02-network.md`
  - 제목: `VPC와 네트워킹`
  - description: `VPC·Subnet·Route Table·NAT Gateway가 맞물리는 방식과 멀티 AZ 네트워크 설계를 정리해요.`
  - tags: `[aws, vpc, network, subnet, nat]`
  - 다룰 것: VPC/CIDR 설계, Public/Private Subnet, IGW·NAT·Route Table, Transit Gateway/PrivateLink 개요

- [ ] **3.3** `_posts/2026-04-20-aws-03-compute.md`
  - 제목: `EC2·ECS·EKS 선택 기준`
  - description: `AWS 컴퓨트 옵션을 워크로드 성격에 따라 어떻게 선택할지 기준을 정리해요.`
  - tags: `[aws, ec2, ecs, eks, fargate]`
  - 다룰 것: EC2 vs ECS vs EKS vs Fargate vs Lambda, 각 오퍼링의 책임 경계, 마이그레이션 경로, Auto Scaling

- [ ] **3.4** `_posts/2026-04-20-aws-04-storage.md`
  - 제목: `S3와 RDS 설계`
  - description: `S3 스토리지 클래스와 RDS 엔진별 운영 특성을 비교해요.`
  - tags: `[aws, s3, rds, storage, database]`
  - 다룰 것: S3 스토리지 클래스·라이프사이클·버저닝, RDS vs Aurora, Multi-AZ·Read Replica, 백업·스냅샷

- [ ] **3.5** `_posts/2026-04-20-aws-05-serverless.md`
  - 제목: `Lambda와 서버리스 패턴`
  - description: `Lambda·API Gateway·EventBridge로 서버리스 아키텍처를 구성하는 실전 패턴을 정리해요.`
  - tags: `[aws, lambda, serverless, api-gateway, eventbridge]`
  - 다룰 것: Lambda 실행 모델·cold start, API Gateway 통합, EventBridge·SQS·SNS 역할, Step Functions 오케스트레이션

#### GCP (4편)

- [ ] **4.1** `_posts/2026-04-20-gcp-01-iam.md`
  - 제목: `GCP 프로젝트와 IAM`
  - description: `GCP의 Organization·Folder·Project 계층과 IAM Role 모델을 AWS와 비교해서 정리해요.`
  - tags: `[gcp, iam, project, organization, security]`
  - 다룰 것: Resource Hierarchy(Org/Folder/Project), Predefined vs Custom Role, Service Account 사용법, AWS IAM과의 차이

- [ ] **4.2** `_posts/2026-04-20-gcp-02-gke.md`
  - 제목: `GKE 운영의 핵심`
  - description: `GKE Autopilot·Standard 모드 차이와 노드풀·Workload Identity 중심의 운영 포인트를 정리해요.`
  - tags: `[gcp, gke, kubernetes, autopilot, workload-identity]`
  - 다룰 것: Autopilot vs Standard, 노드풀 설계, Workload Identity(IAM 연동), Multi-cluster 지원, 자동 업그레이드

- [ ] **4.3** `_posts/2026-04-20-gcp-03-network.md`
  - 제목: `VPC와 Load Balancing`
  - description: `GCP의 글로벌 VPC와 7계층 Load Balancer 구조를 AWS와 대비해서 정리해요.`
  - tags: `[gcp, vpc, load-balancer, network, global]`
  - 다룰 것: 글로벌 VPC 개념(AWS와 가장 큰 차이), Subnet은 Region 스코프, HTTP(S) LB 구조, Cloud Armor

- [ ] **4.4** `_posts/2026-04-20-gcp-04-data.md`
  - 제목: `BigQuery와 데이터 플랫폼`
  - description: `서버리스 데이터 웨어하우스 BigQuery와 Pub/Sub·Dataflow의 조합을 정리해요.`
  - tags: `[gcp, bigquery, pubsub, dataflow, analytics]`
  - 다룰 것: BigQuery 컬럼 스토리지·파티셔닝·슬롯 과금, Pub/Sub, Dataflow(Apache Beam), Looker Studio 개요

#### Azure (3편)

- [ ] **5.1** `_posts/2026-04-20-azure-01-rbac.md`
  - 제목: `Azure 계정과 RBAC`
  - description: `Management Group·Subscription·Resource Group 계층과 Azure AD 기반 RBAC를 정리해요.`
  - tags: `[azure, rbac, azure-ad, subscription, management-group]`
  - 다룰 것: 계정 계층, Azure AD와 RBAC 연동, Built-in Role, Conditional Access 개요

- [ ] **5.2** `_posts/2026-04-20-azure-02-aks.md`
  - 제목: `AKS와 네트워킹`
  - description: `AKS의 네트워크 모델(Kubenet·Azure CNI)과 ingress 구성을 정리해요.`
  - tags: `[azure, aks, kubernetes, cni, ingress]`
  - 다룰 것: AKS 아키텍처, Kubenet vs Azure CNI, Managed Identity 연동, Application Gateway Ingress Controller

- [ ] **5.3** `_posts/2026-04-20-azure-03-services.md`
  - 제목: `주요 컴퓨트와 DB 서비스`
  - description: `VM·App Service·Functions·Cosmos DB 등 Azure 핵심 PaaS 서비스의 선택 기준을 정리해요.`
  - tags: `[azure, vm, app-service, functions, cosmos-db]`
  - 다룰 것: VM vs App Service vs Functions vs Container Apps, Azure SQL vs Cosmos DB, Service Bus

---

### 👁️ Observability

#### Monitoring (4편)

- [ ] **6.1** `_posts/2026-04-20-monitoring-01-metrics.md`
  - 제목: `메트릭 설계와 분류`
  - description: `USE·RED·Four Golden Signals로 어떤 메트릭을 수집해야 할지 기준을 잡아요.`
  - tags: `[monitoring, metrics, use-method, red-method, sre]`
  - 다룰 것: Gauge/Counter/Histogram/Summary 차이, USE·RED·Golden Signals, 메트릭 네이밍·라벨 설계

- [ ] **6.2** `_posts/2026-04-20-monitoring-02-prometheus.md`
  - 제목: `Prometheus 아키텍처`
  - description: `Pull 기반 수집·TSDB·PromQL·Alertmanager가 맞물리는 구조를 정리해요.`
  - tags: `[monitoring, prometheus, promql, tsdb, alertmanager]`
  - 다룰 것: Pull 모델 왜, ServiceMonitor/PodMonitor, TSDB 구조, PromQL 기본, Alertmanager 라우팅

- [ ] **6.3** `_posts/2026-04-20-monitoring-03-grafana.md`
  - 제목: `Grafana 대시보드 설계`
  - description: `잘 읽히는 대시보드를 만드는 레이아웃·시각화 선택 원칙을 정리해요.`
  - tags: `[monitoring, grafana, dashboard, visualization, ux]`
  - 다룰 것: 대시보드 계층(Overview → Detail), 패널 유형별 쓰임, 변수/템플릿, 대시보드 as code (Grafonnet/JSON)

- [ ] **6.4** `_posts/2026-04-20-monitoring-04-slo.md`
  - 제목: `SLO와 알람 전략`
  - description: `SLI·SLO·Error Budget 기반 알람으로 피로도를 줄이는 방법을 정리해요.`
  - tags: `[monitoring, slo, sli, error-budget, alerting]`
  - 다룰 것: SLI vs SLO vs SLA, Error Budget 개념, Multi-window Multi-burn-rate 알람, 알람 피로 해결

#### Logging (3편)

- [ ] **7.1** `_posts/2026-04-20-logging-01-structured.md`
  - 제목: `구조화 로깅 원칙`
  - description: `텍스트 로그에서 JSON 구조화로 전환할 때의 설계 포인트와 필드 네이밍을 정리해요.`
  - tags: `[logging, structured-logging, json, observability, schema]`
  - 다룰 것: 왜 구조화, 표준 필드(timestamp/level/trace_id/service), PII·민감정보 필터링, 레벨 철학

- [ ] **7.2** `_posts/2026-04-20-logging-02-pipeline.md`
  - 제목: `로그 수집 파이프라인`
  - description: `Fluent Bit·Vector·Loki·ELK가 각자 어떤 역할을 맡는지 수집 파이프라인 구조로 정리해요.`
  - tags: `[logging, fluent-bit, loki, elk, pipeline]`
  - 다룰 것: Agent (Fluent Bit/Vector), Aggregator, Storage(Loki/Elasticsearch/S3), 사이드카 vs DaemonSet

- [ ] **7.3** `_posts/2026-04-20-logging-03-search.md`
  - 제목: `검색과 보존 정책`
  - description: `로그 보존 비용과 검색 요구 사이의 트레이드오프를 해결하는 계층화 전략을 정리해요.`
  - tags: `[logging, retention, search, cost, archival]`
  - 다룰 것: Hot/Warm/Cold tier, LogQL vs Lucene, 샘플링·집계, 규제(GDPR)와 보존 기간

#### Tracing (3편)

- [ ] **8.1** `_posts/2026-04-20-tracing-01-concept.md`
  - 제목: `분산 추적의 이해`
  - description: `Trace·Span·Context Propagation이 마이크로서비스 요청을 어떻게 꿰는지 정리해요.`
  - tags: `[tracing, distributed-tracing, span, context, microservices]`
  - 다룰 것: Span·Trace·Context 개념, W3C Trace Context, Sampling 필요성, Service Map

- [ ] **8.2** `_posts/2026-04-20-tracing-02-otel.md`
  - 제목: `OpenTelemetry 구조`
  - description: `OTel SDK·Collector·Exporter가 벤더 중립적 관측성을 어떻게 만드는지 정리해요.`
  - tags: `[tracing, opentelemetry, otel, collector, exporter]`
  - 다룰 것: OTel의 세 축(API/SDK/Collector), Auto vs Manual Instrumentation, Collector 파이프라인, 백엔드 선택(Tempo/Jaeger/Honeycomb)

- [ ] **8.3** `_posts/2026-04-20-tracing-03-sampling.md`
  - 제목: `샘플링과 운영 전략`
  - description: `Head·Tail 샘플링 전략과 트레이스 비용을 관리하는 프로덕션 패턴을 정리해요.`
  - tags: `[tracing, sampling, tail-sampling, cost, production]`
  - 다룰 것: Head vs Tail Sampling, 에러·느린 요청 보존, 비용 모델, 관측성 예산

---

### 🛠 DevOps & SRE

#### Platform Engineering (3편)

- [ ] **9.1** `_posts/2026-04-20-platform-engineering-01-overview.md`
  - 제목: `플랫폼 엔지니어링이란`
  - description: `DevOps의 한계를 극복하려는 Platform Engineering의 등장 배경과 팀 구성을 정리해요.`
  - tags: `[platform-engineering, devops, team-topologies, idp, culture]`
  - 다룰 것: DevOps vs PlatformEng, Team Topologies의 Stream-aligned/Platform 팀, 플랫폼의 "제품" 관점

- [ ] **9.2** `_posts/2026-04-20-platform-engineering-02-idp.md`
  - 제목: `내부 개발자 플랫폼 설계`
  - description: `Backstage·Port 같은 IDP가 제공하는 Self-service와 Catalog 구조를 정리해요.`
  - tags: `[platform-engineering, idp, backstage, port, self-service]`
  - 다룰 것: IDP란, Backstage의 Software Catalog·Template, Scaffolder 개념, 성공하는 IDP의 조건

- [ ] **9.3** `_posts/2026-04-20-platform-engineering-03-paths.md`
  - 제목: `골든 패스와 생산성`
  - description: `Golden Path로 반복되는 결정을 플랫폼 기본값에 담아 개발 속도를 올리는 방법을 정리해요.`
  - tags: `[platform-engineering, golden-path, productivity, paved-road, dx]`
  - 다룰 것: Golden Path/Paved Road 개념, 기본값의 중요성, 측정(DORA 메트릭), 안티패턴

#### Security/DevSecOps (4편)

- [ ] **10.1** `_posts/2026-04-20-security-devsecops-01-overview.md`
  - 제목: `DevSecOps의 전환 철학`
  - description: `보안을 릴리즈 직전 단계에서 파이프라인 전반으로 옮기는 Shift-left의 실제 의미를 정리해요.`
  - tags: `[devsecops, shift-left, security, culture, sdlc]`
  - 다룰 것: 보안팀 병목 문제, shift-left가 아닌 shift-everywhere, 개발자 경험·자동화 균형

- [ ] **10.2** `_posts/2026-04-20-security-devsecops-02-supply-chain.md`
  - 제목: `공급망 보안과 이미지 서명`
  - description: `SLSA·Sigstore·SBOM으로 빌드 아티팩트의 출처를 검증 가능하게 만드는 방법을 정리해요.`
  - tags: `[devsecops, supply-chain, slsa, sigstore, sbom]`
  - 다룰 것: SolarWinds 같은 공급망 공격, SLSA 레벨, Cosign keyless 서명, SBOM(CycloneDX/SPDX), in-toto attestation

- [ ] **10.3** `_posts/2026-04-20-security-devsecops-03-scanning.md`
  - 제목: `SAST·DAST·의존성 스캔`
  - description: `정적·동적·의존성 스캔이 어디에서 어떤 종류의 취약점을 잡는지 비교해요.`
  - tags: `[devsecops, sast, dast, sca, scanning]`
  - 다룰 것: SAST(Semgrep) / DAST(ZAP) / SCA(Trivy·Snyk), IaC 스캔(tfsec·checkov), CI 통합 전략

- [ ] **10.4** `_posts/2026-04-20-security-devsecops-04-policy.md`
  - 제목: `Secrets와 정책 자동화`
  - description: `Vault·Sealed Secrets·OPA로 비밀 관리와 정책을 코드화하는 방법을 정리해요.`
  - tags: `[devsecops, secrets, vault, opa, policy-as-code]`
  - 다룰 것: Secrets 저장 옵션(Vault/ExternalSecrets/SealedSecrets), OPA·Gatekeeper·Kyverno, Policy as Code

#### Incident Management (3편)

- [ ] **11.1** `_posts/2026-04-20-incident-management-01-oncall.md`
  - 제목: `온콜과 알람 체계`
  - description: `지속 가능한 온콜 로테이션과 알람 신호·소음을 구분하는 기준을 정리해요.`
  - tags: `[incident-management, oncall, alerting, pagerduty, sre]`
  - 다룰 것: 로테이션 패턴(Follow-the-Sun), alert vs notification, 에스컬레이션, 온콜 피로 대응

- [ ] **11.2** `_posts/2026-04-20-incident-management-02-response.md`
  - 제목: `장애 대응 플레이북`
  - description: `심각도 분류·Incident Commander·커뮤니케이션 채널로 혼돈을 구조화하는 방법을 정리해요.`
  - tags: `[incident-management, playbook, severity, communication, ics]`
  - 다룰 것: Severity 레벨 정의, 역할 분담(IC/Ops/Comms), 상태 페이지, chatops

- [ ] **11.3** `_posts/2026-04-20-incident-management-03-postmortem.md`
  - 제목: `포스트모템과 학습`
  - description: `Blameless 포스트모템으로 장애를 조직 학습 자산으로 바꾸는 방법을 정리해요.`
  - tags: `[incident-management, postmortem, blameless, retrospective, learning]`
  - 다룰 것: Blameless 원칙, 5 Whys vs 시스템 사고, Action Item 추적, Incident Review 문화

#### Cost Optimization (3편)

- [ ] **12.1** `_posts/2026-04-20-cost-optimization-01-finops.md`
  - 제목: `FinOps 기본 원칙`
  - description: `FinOps 3단계(Inform·Optimize·Operate)와 태그·Showback·Chargeback으로 비용을 가시화해요.`
  - tags: `[finops, cost, tagging, chargeback, cloud]`
  - 다룰 것: FinOps 정의, 3 Phases, Tagging 전략, Showback vs Chargeback, 책임 분산

- [ ] **12.2** `_posts/2026-04-20-cost-optimization-02-compute.md`
  - 제목: `컴퓨트·스토리지 최적화`
  - description: `Spot/Reserved·Rightsizing·Lifecycle Policy로 컴퓨트와 스토리지 비용을 줄이는 방법을 정리해요.`
  - tags: `[finops, spot, reserved, rightsizing, storage]`
  - 다룰 것: Spot/Reserved/Savings Plan, Rightsizing 기준, S3 스토리지 클래스 전환, 비용 알람

- [ ] **12.3** `_posts/2026-04-20-cost-optimization-03-kubernetes.md`
  - 제목: `Kubernetes 비용 관리`
  - description: `Kubecost·Karpenter로 쿠버네티스 워크로드의 비용을 투명하게 관리해요.`
  - tags: `[finops, kubernetes, kubecost, karpenter, autoscaling]`
  - 다룰 것: 요청/한도 기반 비용 분배, Kubecost, Karpenter 클러스터 오토스케일러, bin-packing

---

### 💻 Development

#### Backend (3편)

- [ ] **13.1** `_posts/2026-04-20-backend-01-architecture.md`
  - 제목: `백엔드 아키텍처 스타일`
  - description: `Layered·Hexagonal·Clean 아키텍처가 같은 문제를 다르게 푸는 방식을 비교해요.`
  - tags: `[backend, architecture, layered, hexagonal, clean]`
  - 다룰 것: Layered의 문제, Hexagonal(Port/Adapter), Clean의 원 구조, 언제 어떤 스타일

- [ ] **13.2** `_posts/2026-04-20-backend-02-concurrency.md`
  - 제목: `동시성과 성능`
  - description: `스레드·이벤트 루프·코루틴이 동시성을 어떻게 다르게 처리하는지 정리해요.`
  - tags: `[backend, concurrency, thread, event-loop, coroutine]`
  - 다룰 것: 스레드 기반(Java/Go) vs 이벤트 루프(Node) vs 코루틴(Kotlin/Python asyncio), 선택 기준, backpressure

- [ ] **13.3** `_posts/2026-04-20-backend-03-caching.md`
  - 제목: `캐싱과 메시지 큐`
  - description: `Redis 캐시 전략과 Kafka·RabbitMQ 메시지 큐가 백엔드 부하를 분산시키는 방식을 정리해요.`
  - tags: `[backend, caching, redis, kafka, message-queue]`
  - 다룰 것: Cache-aside/Write-through/Write-behind, Cache Stampede·Thundering Herd, Queue(Kafka) vs Broker(RabbitMQ) 특성

#### Database (4편)

- [ ] **14.1** `_posts/2026-04-20-database-01-relational.md`
  - 제목: `관계형 DB와 인덱스`
  - description: `B-Tree 인덱스와 실행 계획을 읽는 감각을 기본부터 정리해요.`
  - tags: `[database, rdbms, index, b-tree, execution-plan]`
  - 다룰 것: B-Tree/Hash Index, Clustered vs Non-clustered, Covering Index, EXPLAIN 읽기

- [ ] **14.2** `_posts/2026-04-20-database-02-transaction.md`
  - 제목: `트랜잭션과 격리 수준`
  - description: `ACID와 4가지 격리 수준에서 발생하는 현상과 MVCC의 작동 원리를 정리해요.`
  - tags: `[database, transaction, isolation, mvcc, acid]`
  - 다룰 것: ACID, Dirty Read/Non-repeatable/Phantom, 4 Isolation Level, MVCC(PostgreSQL), Serializable 비용

- [ ] **14.3** `_posts/2026-04-20-database-03-nosql.md`
  - 제목: `NoSQL 유형별 선택`
  - description: `Document·Key-Value·Wide-Column·Graph DB가 각자 어떤 모델에 적합한지 비교해요.`
  - tags: `[database, nosql, mongodb, cassandra, dynamodb]`
  - 다룰 것: 4가지 NoSQL 패턴, CAP/PACELC, DynamoDB·MongoDB·Cassandra 쓰임, SQL과의 경계선

- [ ] **14.4** `_posts/2026-04-20-database-04-scaling.md`
  - 제목: `복제와 샤딩 전략`
  - description: `Read Replica·Sharding·Partitioning으로 DB를 수평 확장하는 기본 패턴을 정리해요.`
  - tags: `[database, replication, sharding, partition, scaling]`
  - 다룰 것: Master-Replica, Sync vs Async Replication, Sharding 키 선택, Partitioning 종류, Global DB

#### API Design (3편)

- [ ] **15.1** `_posts/2026-04-20-api-design-01-styles.md`
  - 제목: `REST·GraphQL·gRPC 비교`
  - description: `API 스타일 선택이 팀·클라이언트·성능에 미치는 영향을 세 프로토콜로 비교해요.`
  - tags: `[api, rest, graphql, grpc, design]`
  - 다룰 것: REST 원칙·HATEOAS, GraphQL 장단점, gRPC 스트리밍·Protocol Buffer, 선택 기준

- [ ] **15.2** `_posts/2026-04-20-api-design-02-versioning.md`
  - 제목: `버전닝과 호환성`
  - description: `URL·Header·Media Type 버저닝과 Breaking Change를 관리하는 원칙을 정리해요.`
  - tags: `[api, versioning, backward-compatibility, semver, deprecation]`
  - 다룰 것: Versioning 방식 3가지, Breaking vs Non-breaking, Deprecation 프로세스, Consumer-driven

- [ ] **15.3** `_posts/2026-04-20-api-design-03-auth.md`
  - 제목: `인증·인가와 문서화`
  - description: `OAuth2·JWT 인증 흐름과 OpenAPI 기반 문서 자동화를 정리해요.`
  - tags: `[api, auth, oauth2, jwt, openapi]`
  - 다룰 것: OAuth2 Grant Type, JWT 구조·주의점, API Key vs Token, OpenAPI/Swagger, API Linter

#### Testing (3편)

- [ ] **16.1** `_posts/2026-04-20-testing-01-pyramid.md`
  - 제목: `테스트 피라미드 재해석`
  - description: `Unit·Integration·E2E 비율을 결정할 때 실무적으로 고려할 점을 정리해요.`
  - tags: `[testing, pyramid, unit, integration, strategy]`
  - 다룰 것: 고전 피라미드·Trophy 모델, Fast/Reliable/Cheap 삼각 트레이드오프, Unit의 정의 논쟁

- [ ] **16.2** `_posts/2026-04-20-testing-02-integration.md`
  - 제목: `통합과 E2E 테스트`
  - description: `TestContainers·Playwright로 외부 의존성을 포함한 테스트를 안정적으로 만드는 방법을 정리해요.`
  - tags: `[testing, integration, e2e, testcontainers, playwright]`
  - 다룰 것: Integration Test 경계, TestContainers, E2E Tool 비교, Flaky test 관리

- [ ] **16.3** `_posts/2026-04-20-testing-03-contract.md`
  - 제목: `계약과 성능 테스트`
  - description: `Pact 기반 Consumer-driven Contract와 k6·Gatling 성능 테스트의 역할을 정리해요.`
  - tags: `[testing, contract, pact, performance, k6]`
  - 다룰 것: Contract Test 개념, Consumer-driven (Pact), 성능 테스트 종류(Load/Stress/Spike), k6

---

### 🏛 Architecture

#### System Design (4편)

- [ ] **17.1** `_posts/2026-04-20-system-design-01-thinking.md`
  - 제목: `시스템 설계 사고법`
  - description: `요구사항·제약·트레이드오프에서 시작하는 시스템 설계의 사고 프레임을 정리해요.`
  - tags: `[system-design, trade-off, requirements, architecture, thinking]`
  - 다룰 것: Functional vs Non-functional Requirement, 트레이드오프 축(일관성·지연·비용), 설계 인터뷰 프레임워크

- [ ] **17.2** `_posts/2026-04-20-system-design-02-scale.md`
  - 제목: `확장성과 부하 분산`
  - description: `Vertical·Horizontal Scaling과 Load Balancer·CDN 계층이 부하를 나누는 방법을 정리해요.`
  - tags: `[system-design, scalability, load-balancer, cdn, horizontal-scaling]`
  - 다룰 것: Scale-up vs Scale-out, L4 vs L7 LB, Sticky Session, CDN 계층, DNS 기반 LB

- [ ] **17.3** `_posts/2026-04-20-system-design-03-consistency.md`
  - 제목: `일관성과 CAP 정리`
  - description: `CAP·PACELC와 다양한 일관성 모델이 분산 시스템 설계에 주는 의미를 정리해요.`
  - tags: `[system-design, consistency, cap, pacelc, distributed]`
  - 다룰 것: CAP 정리, PACELC 확장, Eventual/Strong/Causal, Quorum, Linearizability

- [ ] **17.4** `_posts/2026-04-20-system-design-04-cache.md`
  - 제목: `데이터 저장과 캐시 전략`
  - description: `OLTP·OLAP·검색 엔진·캐시가 각자 맡는 역할과 데이터 흐름을 정리해요.`
  - tags: `[system-design, cache, olap, oltp, search]`
  - 다룰 것: OLTP vs OLAP, Polyglot Persistence, Cache Layer(Client/CDN/Application/DB), Search(Elasticsearch)

#### MSA/Microservices (4편)

- [ ] **18.1** `_posts/2026-04-20-msa-microservices-01-decompose.md`
  - 제목: `서비스 분해 원칙`
  - description: `DDD Bounded Context 기반으로 모놀리식을 분해할 때의 기준과 함정을 정리해요.`
  - tags: `[msa, microservices, ddd, bounded-context, decomposition]`
  - 다룰 것: 왜 분해·왜 분해하면 안 되는가, Bounded Context, Strangler Fig, Distributed Monolith 경고

- [ ] **18.2** `_posts/2026-04-20-msa-microservices-02-communication.md`
  - 제목: `동기·비동기 통신`
  - description: `서비스 간 REST·gRPC 동기 호출과 Event·Message 비동기 통신의 트레이드오프를 정리해요.`
  - tags: `[msa, communication, sync, async, event]`
  - 다룰 것: REST/gRPC 동기, Event/Message 비동기, Request-Reply over Queue, API Gateway·BFF

- [ ] **18.3** `_posts/2026-04-20-msa-microservices-03-saga.md`
  - 제목: `분산 트랜잭션과 Saga`
  - description: `Choreography·Orchestration Saga 패턴으로 분산 환경에서 일관성을 만드는 방법을 정리해요.`
  - tags: `[msa, saga, distributed-transaction, compensation, consistency]`
  - 다룰 것: 2PC의 한계, Saga 두 가지 스타일, Compensating Transaction, Outbox 패턴

- [ ] **18.4** `_posts/2026-04-20-msa-microservices-04-resilience.md`
  - 제목: `Resilience 패턴`
  - description: `Circuit Breaker·Retry·Bulkhead·Timeout이 장애 전파를 어떻게 막는지 정리해요.`
  - tags: `[msa, resilience, circuit-breaker, retry, bulkhead]`
  - 다룰 것: 장애 격리 원칙, Circuit Breaker 상태 전이, Retry with Backoff, Bulkhead, Idempotency

#### Event-Driven (3편)

- [ ] **19.1** `_posts/2026-04-20-event-driven-01-concept.md`
  - 제목: `이벤트 주도 아키텍처`
  - description: `Event·Command 차이와 Choreography·Orchestration으로 흐름을 구성하는 기본기를 정리해요.`
  - tags: `[event-driven, event, command, choreography, orchestration]`
  - 다룰 것: Event vs Command vs Query, Choreography vs Orchestration, 장단점, 적합한 도메인

- [ ] **19.2** `_posts/2026-04-20-event-driven-02-cqrs.md`
  - 제목: `Event Sourcing과 CQRS`
  - description: `상태 대신 이벤트를 저장하는 Event Sourcing과 읽기·쓰기 모델을 분리하는 CQRS를 정리해요.`
  - tags: `[event-driven, event-sourcing, cqrs, projection, replay]`
  - 다룰 것: Event Sourcing 핵심 아이디어, Projection·Materialized View, CQRS와의 관계, 리플레이, 단점

- [ ] **19.3** `_posts/2026-04-20-event-driven-03-kafka.md`
  - 제목: `Kafka 운영 관점`
  - description: `Partition·Consumer Group·Offset 관리 등 Kafka를 프로덕션에서 안전하게 운영하는 포인트를 정리해요.`
  - tags: `[event-driven, kafka, partition, consumer-group, ops]`
  - 다룰 것: Topic·Partition·Offset, Consumer Group 리밸런싱, Exactly-once, Schema Registry, 흔한 장애

#### Design Patterns (3편)

- [ ] **20.1** `_posts/2026-04-20-design-patterns-01-gof.md`
  - 제목: `GoF 패턴 재조명`
  - description: `생성·구조·행위 패턴에서 현대 언어에서도 살아남은 것들과 의미가 퇴색한 것들을 정리해요.`
  - tags: `[design-patterns, gof, oop, creational, structural]`
  - 다룰 것: 3분류, 여전히 유용한 패턴(Factory/Strategy/Observer), 구식화된 패턴, 함수형 대체

- [ ] **20.2** `_posts/2026-04-20-design-patterns-02-ddd.md`
  - 제목: `DDD 전술 패턴`
  - description: `Entity·Value Object·Aggregate·Repository가 도메인 모델을 보호하는 방식을 정리해요.`
  - tags: `[design-patterns, ddd, aggregate, entity, value-object]`
  - 다룰 것: Entity vs VO, Aggregate Root, Repository, Domain Event, 흔한 모델링 실수

- [ ] **20.3** `_posts/2026-04-20-design-patterns-03-hexagonal.md`
  - 제목: `클린·헥사고날 아키텍처`
  - description: `Port·Adapter 구조로 도메인 코어를 인프라 기술에서 분리하는 설계를 정리해요.`
  - tags: `[design-patterns, hexagonal, clean-architecture, port, adapter]`
  - 다룰 것: Dependency Inversion, Port·Adapter, Use Case 경계, 테스트 용이성, 실용적 축소 버전

---

## 최종 검증 (전체 완료 후)

1. **빌드 확인**
   ```bash
   bundle exec jekyll build 2>&1 | grep -iE "error|warning" | grep -v "Excerpt modified"
   ```
   출력이 비어있어야 정상.

2. **포스트 수 확인**
   ```bash
   ls _posts/ | wc -l
   ```
   목표: 기존 13 + 신규 13(이미 완료) + 신규 69 = **95개**

3. **Sitemap 확인**
   ```bash
   curl -s https://no1joon.github.io/sitemap.xml | grep -c "<loc>"
   ```
   목표: 95 + index + resume = 97개.

4. **모든 포스트 front matter 검증**
   ```bash
   grep -L "^category:" _posts/*.md
   grep -L "^subcategory:" _posts/*.md
   ```
   출력이 비어있어야 정상.

---

## Gemini에게 — 운영 팁

- **한 번에 한 시리즈씩** 처리. 3~5편 작성 → 커밋 → 다음 시리즈.
- 매 편마다 기존 포스트를 **실제로 읽어서** 톤을 맞춤. 기억에 의존 금지.
- 막히면 사용자에게 질문. 추측으로 밀고 나가지 않기.
- Helm·Jekyll 이중 `{{ }}`처럼 **Liquid 충돌 우려가 있으면 `{% raw %}`** 로 감쌀 것.
- 커밋 메시지 한국어, Co-Authored-By 라인 넣지 말 것.
- 커밋 후 `git push origin HEAD:main` 로 즉시 푸시.

끝.
