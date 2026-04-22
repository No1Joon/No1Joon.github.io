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

| 상황                    | 선택                      |
| ----------------------- | ------------------------- |
| 아키텍처·컴포넌트 관계  | mermaid `flowchart`       |
| 시간 순 호출 흐름       | mermaid `sequenceDiagram` |
| 상태 전이·라이프사이클  | mermaid `stateDiagram-v2` |
| 옵션·타입 비교          | Markdown table            |
| 디렉토리 트리·설정 계층 | plain code block          |

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

- [x] **2.1** `_posts/2026-04-20-terraform-iac-01-overview.md`
  - 제목: `Terraform 기본 구조`
  - description: `HCL 문법과 provider·resource·data·output 구성 요소가 선언적 IaC를 어떻게 구성하는지 정리해요.`
  - tags: `[terraform, iac, hcl, provider, infrastructure]`
  - 다룰 것: Terraform vs CloudFormation vs Pulumi, HCL 구조(provider/resource/variable/output), plan → apply 흐름, 선언적 사고

- [x] **2.2** `_posts/2026-04-20-terraform-iac-02-modules.md`
  - 제목: `모듈과 재사용 설계`
  - description: `인프라 중복을 제거하는 Terraform 모듈 구조와 root·child 모듈 설계 원칙을 정리해요.`
  - tags: `[terraform, module, reusable, iac, design]`
  - 다룰 것: module 개념, public vs private module, input/output 설계, 버전 고정, 폴더 구조 패턴

- [x] **2.3** `_posts/2026-04-20-terraform-iac-03-state.md`
  - 제목: `State 관리와 협업`
  - description: `tfstate 원격 백엔드와 state locking으로 팀 협업을 안전하게 만드는 방법을 정리해요.`
  - tags: `[terraform, state, backend, s3, locking]`
  - 다룰 것: state가 뭐고 왜 중요한가, remote backend (S3+DynamoDB, Terraform Cloud), state locking, import/mv/rm 기본

- [x] **2.4** `_posts/2026-04-20-terraform-iac-04-cicd.md`
  - 제목: `Terraform CI와 테스트`
  - description: `plan 리뷰·tflint·terratest로 IaC를 코드처럼 검증하는 파이프라인을 구성해요.`
  - tags: `[terraform, cicd, testing, terratest, tflint]`
  - 다룰 것: PR 기반 plan 자동 포스팅 (Atlantis/TFC), tflint·tfsec, terratest, drift detection

#### AWS (5편)

- [x] **3.1** `_posts/2026-04-20-aws-01-iam.md`
  - 제목: `AWS 계정 구조와 IAM`
  - description: `Organizations·SCP·IAM Role 기반의 멀티 계정 권한 모델을 정리해요.`
  - tags: `[aws, iam, organizations, scp, security]`
  - 다룰 것: 멀티 계정 왜(분리·청구·격리), Organizations·OU·SCP, IAM User vs Role, AssumeRole 플로우, 최소 권한

- [x] **3.2** `_posts/2026-04-20-aws-02-network.md`
  - 제목: `VPC와 네트워킹`
  - description: `VPC·Subnet·Route Table·NAT Gateway가 맞물리는 방식과 멀티 AZ 네트워크 설계를 정리해요.`
  - tags: `[aws, vpc, network, subnet, nat]`
  - 다룰 것: VPC/CIDR 설계, Public/Private Subnet, IGW·NAT·Route Table, Transit Gateway/PrivateLink 개요

- [x] **3.3** `_posts/2026-04-20-aws-03-compute.md`
  - 제목: `EC2·ECS·EKS 선택 기준`
  - description: `AWS 컴퓨트 옵션을 워크로드 성격에 따라 어떻게 선택할지 기준을 정리해요.`
  - tags: `[aws, ec2, ecs, eks, fargate]`
  - 다룰 것: EC2 vs ECS vs EKS vs Fargate vs Lambda, 각 오퍼링의 책임 경계, 마이그레이션 경로, Auto Scaling

- [x] **3.4** `_posts/2026-04-20-aws-04-storage.md`
  - 제목: `S3와 RDS 설계`
  - description: `S3 스토리지 클래스와 RDS 엔진별 운영 특성을 비교해요.`
  - tags: `[aws, s3, rds, storage, database]`
  - 다룰 것: S3 스토리지 클래스·라이프사이클·버저닝, RDS vs Aurora, Multi-AZ·Read Replica, 백업·스냅샷

- [x] **3.5** `_posts/2026-04-20-aws-05-serverless.md`
  - 제목: `Lambda와 서버리스 패턴`
  - description: `Lambda·API Gateway·EventBridge로 서버리스 아키텍처를 구성하는 실전 패턴을 정리해요.`
  - tags: `[aws, lambda, serverless, api-gateway, eventbridge]`
  - 다룰 것: Lambda 실행 모델·cold start, API Gateway 통합, EventBridge·SQS·SNS 역할, Step Functions 오케스트레이션

#### GCP (4편)

- [x] **4.1** `_posts/2026-04-20-gcp-01-iam.md`
  - 제목: `GCP 프로젝트와 IAM`
  - description: `GCP의 Organization·Folder·Project 계층과 IAM Role 모델을 AWS와 비교해서 정리해요.`
  - tags: `[gcp, iam, project, organization, security]`
  - 다룰 것: Resource Hierarchy(Org/Folder/Project), Predefined vs Custom Role, Service Account 사용법, AWS IAM과의 차이

- [x] **4.2** `_posts/2026-04-20-gcp-02-gke.md`
  - 제목: `GKE 운영의 핵심`
  - description: `GKE Autopilot·Standard 모드 차이와 노드풀·Workload Identity 중심의 운영 포인트를 정리해요.`
  - tags: `[gcp, gke, kubernetes, autopilot, workload-identity]`
  - 다룰 것: Autopilot vs Standard, 노드풀 설계, Workload Identity(IAM 연동), Multi-cluster 지원, 자동 업그레이드

- [x] **4.3** `_posts/2026-04-20-gcp-03-network.md`
  - 제목: `VPC와 Load Balancing`
  - description: `GCP의 글로벌 VPC와 7계층 Load Balancer 구조를 AWS와 대비해서 정리해요.`
  - tags: `[gcp, vpc, load-balancer, network, global]`
  - 다룰 것: 글로벌 VPC 개념(AWS와 가장 큰 차이), Subnet은 Region 스코프, HTTP(S) LB 구조, Cloud Armor

- [x] **4.4** `_posts/2026-04-20-gcp-04-data.md`
  - 제목: `BigQuery와 데이터 플랫폼`
  - description: `서버리스 데이터 웨어하우스 BigQuery와 Pub/Sub·Dataflow의 조합을 정리해요.`
  - tags: `[gcp, bigquery, pubsub, dataflow, analytics]`
  - 다룰 것: BigQuery 컬럼 스토리지·파티셔닝·슬롯 과금, Pub/Sub, Dataflow(Apache Beam), Looker Studio 개요

#### Azure (3편)

- [x] **5.1** `_posts/2026-04-20-azure-01-rbac.md`
  - 제목: `Azure 계정과 RBAC`
  - description: `Management Group·Subscription·Resource Group 계층과 Azure AD 기반 RBAC를 정리해요.`
  - tags: `[azure, rbac, azure-ad, subscription, management-group]`
  - 다룰 것: 계정 계층, Azure AD와 RBAC 연동, Built-in Role, Conditional Access 개요

- [x] **5.2** `_posts/2026-04-20-azure-02-aks.md`
  - 제목: `AKS와 네트워킹`
  - description: `AKS의 네트워크 모델(Kubenet·Azure CNI)과 ingress 구성을 정리해요.`
  - tags: `[azure, aks, kubernetes, cni, ingress]`
  - 다룰 것: AKS 아키텍처, Kubenet vs Azure CNI, Managed Identity 연동, Application Gateway Ingress Controller

- [x] **5.3** `_posts/2026-04-20-azure-03-services.md`
  - 제목: `주요 컴퓨트와 DB 서비스`
  - description: `VM·App Service·Functions·Cosmos DB 등 Azure 핵심 PaaS 서비스의 선택 기준을 정리해요.`
  - tags: `[azure, vm, app-service, functions, cosmos-db]`
  - 다룰 것: VM vs App Service vs Functions vs Container Apps, Azure SQL vs Cosmos DB, Service Bus

---

### 👁️ Observability

#### Monitoring (4편)

- [x] **6.1** `_posts/2026-04-20-monitoring-01-metrics.md`
  - 제목: `메트릭 설계와 분류`
  - description: `USE·RED·Four Golden Signals로 어떤 메트릭을 수집해야 할지 기준을 잡아요.`
  - tags: `[monitoring, metrics, use-method, red-method, sre]`
  - 다룰 것: Gauge/Counter/Histogram/Summary 차이, USE·RED·Golden Signals, 메트릭 네이밍·라벨 설계

- [x] **6.2** `_posts/2026-04-20-monitoring-02-prometheus.md`
  - 제목: `Prometheus 아키텍처`
  - description: `Pull 기반 수집·TSDB·PromQL·Alertmanager가 맞물리는 구조를 정리해요.`
  - tags: `[monitoring, prometheus, promql, tsdb, alertmanager]`
  - 다룰 것: Pull 모델 왜, ServiceMonitor/PodMonitor, TSDB 구조, PromQL 기본, Alertmanager 라우팅

- [x] **6.3** `_posts/2026-04-20-monitoring-03-grafana.md`
  - 제목: `Grafana 대시보드 설계`
  - description: `잘 읽히는 대시보드를 만드는 레이아웃·시각화 선택 원칙을 정리해요.`
  - tags: `[monitoring, grafana, dashboard, visualization, ux]`
  - 다룰 것: 대시보드 계층(Overview → Detail), 패널 유형별 쓰임, 변수/템플릿, 대시보드 as code (Grafonnet/JSON)

- [x] **6.4** `_posts/2026-04-20-monitoring-04-slo.md`
  - 제목: `SLO와 알람 전략`
  - description: `SLI·SLO·Error Budget 기반 알람으로 피로도를 줄이는 방법을 정리해요.`
  - tags: `[monitoring, slo, sli, error-budget, alerting]`
  - 다룰 것: SLI vs SLO vs SLA, Error Budget 개념, Multi-window Multi-burn-rate 알람, 알람 피로 해결

#### Logging (3편)

- [x] **7.1** `_posts/2026-04-20-logging-01-structured.md`
  - 제목: `구조화 로깅 원칙`
  - description: `텍스트 로그에서 JSON 구조화로 전환할 때의 설계 포인트와 필드 네이밍을 정리해요.`
  - tags: `[logging, structured-logging, json, observability, schema]`
  - 다룰 것: 왜 구조화, 표준 필드(timestamp/level/trace_id/service), PII·민감정보 필터링, 레벨 철학

- [x] **7.2** `_posts/2026-04-20-logging-02-pipeline.md`
  - 제목: `로그 수집 파이프라인`
  - description: `Fluent Bit·Vector·Loki·ELK가 각자 어떤 역할을 맡는지 수집 파이프라인 구조로 정리해요.`
  - tags: `[logging, fluent-bit, loki, elk, pipeline]`
  - 다룰 것: Agent (Fluent Bit/Vector), Aggregator, Storage(Loki/Elasticsearch/S3), 사이드카 vs DaemonSet

- [x] **7.3** `_posts/2026-04-20-logging-03-search.md`
  - 제목: `검색과 보존 정책`
  - description: `로그 보존 비용과 검색 요구 사이의 트레이드오프를 해결하는 계층화 전략을 정리해요.`
  - tags: `[logging, retention, search, cost, archival]`
  - d 다룰 것: Hot/Warm/Cold tier, LogQL vs Lucene, 샘플링·집계, 규제(GDPR)와 보존 기간

#### Tracing (3편)

- [x] **8.1** `_posts/2026-04-20-tracing-01-concept.md`
  - 제목: `분산 추적의 이해`
  - description: `Trace·Span·Context Propagation이 마이크로서비스 요청을 어떻게 꿰는지 정리합니다.`
  - tags: `[tracing, distributed-tracing, span, context, microservices]`
  - 다룰 것: Span·Trace·Context 개념, W3C Trace Context, Sampling 필요성, Service Map

- [x] **8.2** `_posts/2026-04-20-tracing-02-otel.md`
  - 제목: `OpenTelemetry 구조`
  - description: `OTel SDK·Collector·Exporter가 벤더 중립적 관측성을 어떻게 만드는지 정리합니다.`
  - tags: `[tracing, opentelemetry, otel, collector, exporter]`
  - 다룰 것: OTel의 세 축(API/SDK/Collector), Auto vs Manual Instrumentation, Collector 파이프라인, 백엔드 선택(Tempo/Jaeger/Honeycomb)

- [x] **8.3** `_posts/2026-04-20-tracing-03-sampling.md`
  - 제목: `샘플링과 운영 전략`
  - description: `Head·Tail 샘플링 전략과 트레이스 비용을 관리하는 프로덕션 패턴을 정리합니다.`
  - tags: `[tracing, sampling, tail-sampling, cost, production]`
  - 다룰 것: Head vs Tail Sampling, 에러·느린 요청 보존, 비용 모델, 관측성 예산

---

### 🛠 DevOps & SRE

#### Platform Engineering (3편)

- [x] **9.1** `_posts/2026-04-20-platform-engineering-01-overview.md`
  - 제목: `플랫폼 엔지니어링이란`
  - description: `DevOps의 한계를 극복하려는 Platform Engineering의 등장 배경과 팀 구성을 정리해요.`
  - tags: `[platform-engineering, devops, team-topologies, idp, culture]`
  - 다룰 것: DevOps vs PlatformEng, Team Topologies의 Stream-aligned/Platform 팀, 플랫폼의 "제품" 관점

- [x] **9.2** `_posts/2026-04-20-platform-engineering-02-idp.md`
  - 제목: `내부 개발자 플랫폼 설계`
  - description: `Backstage·Port 같은 IDP가 제공하는 Self-service와 Catalog 구조를 정리해요.`
  - tags: `[platform-engineering, idp, backstage, port, self-service]`
  - 다룰 것: IDP란, Backstage의 Software Catalog·Template, Scaffolder 개념, 성공하는 IDP의 조건

- [x] **9.3** `_posts/2026-04-20-platform-engineering-03-paths.md`
  - 제목: `골든 패스와 생산성`
  - description: `Golden Path로 반복되는 결정을 플랫폼 기본값에 담아 개발 속도를 올리는 방법을 정리해요.`
  - tags: `[platform-engineering, golden-path, productivity, paved-road, dx]`
  - 다룰 것: Golden Path/Paved Road 개념, 기본값의 중요성, 측정(DORA 메트릭), 안티패턴

#### Security/DevSecOps (4편)

- [x] **10.1** `_posts/2026-04-20-security-devsecops-01-overview.md`
  - 제목: `DevSecOps의 전환 철학`
  - description: `보안을 릴리즈 직전 단계에서 파이프라인 전반으로 옮기는 Shift-left의 실제 의미를 정리해요.`
  - tags: `[devsecops, shift-left, security, culture, sdlc]`
  - 다룰 것: 보안팀 병목 문제, shift-left가 아닌 shift-everywhere, 개발자 경험·자동화 균형

- [x] **10.2** `_posts/2026-04-20-security-devsecops-02-supply-chain.md`
  - 제목: `공급망 보안과 이미지 서명`
  - description: `SLSA·Sigstore·SBOM으로 빌드 아티팩트의 출처를 검증 가능하게 만드는 방법을 정리해요.`
  - tags: `[devsecops, supply-chain, slsa, sigstore, sbom]`
  - 다룰 것: SolarWinds 같은 공급망 공격, SLSA 레벨, Cosign keyless 서명, SBOM(CycloneDX/SPDX), in-toto attestation

- [x] **10.3** `_posts/2026-04-20-security-devsecops-03-scanning.md`
  - 제목: `SAST·DAST·의존성 스캔`
  - description: `정적·동적·의존성 스캔이 어디에서 어떤 종류의 취약점을 잡는지 비교해요.`
  - tags: `[devsecops, sast, dast, sca, scanning]`
  - 다룰 것: SAST(Semgrep) / DAST(ZAP) / SCA(Trivy·Snyk), IaC 스캔(tfsec·checkov), CI 통합 전략

- [x] **10.4** `_posts/2026-04-20-security-devsecops-04-policy.md`
  - 제목: `Secrets와 정책 자동화`
  - description: `Vault·Sealed Secrets·OPA로 비밀 관리와 정책을 코드화하는 방법을 정리해요.`
  - tags: `[devsecops, secrets, vault, opa, policy-as-code]`
  - 다룰 것: Secrets 저장 옵션(Vault/ExternalSecrets/SealedSecrets), OPA·Gatekeeper·Kyverno, Policy as Code

#### Incident Management (3편)

- [x] **11.1** `_posts/2026-04-20-incident-management-01-oncall.md`
  - 제목: `온콜과 알람 체계`
  - description: `지속 가능한 온콜 로테이션과 알람 신호·소음을 구분하는 기준을 정리해요.`
  - tags: `[incident-management, oncall, alerting, pagerduty, sre]`
  - 다룰 것: 로테이션 패턴(Follow-the-Sun), alert vs notification, 에스컬레이션, 온콜 피로 대응

- [x] **11.2** `_posts/2026-04-20-incident-management-02-response.md`
  - 제목: `장애 대응 플레이북`
  - description: `심각도 분류·Incident Commander·커뮤니케이션 채널로 혼돈을 구조화하는 방법을 정리해요.`
  - tags: `[incident-management, playbook, severity, communication, ics]`
  - 다룰 것: Severity 레벨 정의, 역할 분담(IC/Ops/Comms), 상태 페이지, chatops

- [x] **11.3** `_posts/2026-04-20-incident-management-03-postmortem.md`
  - 제목: `포스트모템과 학습`
  - description: `Blameless 포스트모템으로 장애를 조직 학습 자산으로 바꾸는 방법을 정리해요.`
  - tags: `[incident-management, postmortem, blameless, retrospective, learning]`
  - 다룰 것: Blameless 원칙, 5 Whys vs 시스템 사고, Action Item 추적, Incident Review 문화

#### Cost Optimization (3편)

- [x] **12.1** `_posts/2026-04-20-cost-optimization-01-finops.md`
  - 제목: `FinOps 기본 원칙`
  - description: `FinOps 3단계(Inform·Optimize·Operate)와 태그·Showback·Chargeback으로 비용을 가시화해요.`
  - tags: `[finops, cost, tagging, chargeback, cloud]`
  - 다룰 것: FinOps 정의, 3 Phases, Tagging 전략, Showback vs Chargeback, 책임 분산

- [x] **12.2** `_posts/2026-04-20-cost-optimization-02-compute.md`
  - 제목: `컴퓨트·스토리지 최적화`
  - description: `Spot/Reserved·Rightsizing·Lifecycle Policy로 컴퓨트와 스토리지 비용을 줄이는 방법을 정리해요.`
  - tags: `[finops, spot, reserved, rightsizing, storage]`
  - 다룰 것: Spot/Reserved/Savings Plan, Rightsizing 기준, S3 스토리지 클래스 전환, 비용 알람

- [x] **12.3** `_posts/2026-04-20-cost-optimization-03-kubernetes.md`
  - 제목: `Kubernetes 비용 관리`
  - description: `Kubecost·Karpenter로 쿠버네티스 워크로드의 비용을 투명하게 관리해요.`
  - tags: `[finops, kubernetes, kubecost, karpenter, autoscaling]`
  - 다룰 것: 요청/한도 기반 비용 분배, Kubecost, Karpenter 클러스터 오토스케일러, bin-packing

---

### 💻 Development

#### Backend (3편)

- [x] **13.1** `_posts/2026-04-20-backend-01-architecture.md`
  - 제목: `백엔드 아키텍처 스타일`
  - description: `Layered·Hexagonal·Clean 아키텍처가 같은 문제를 다르게 푸는 방식을 비교해요.`
  - tags: `[backend, architecture, layered, hexagonal, clean]`
  - 다룰 것: Layered의 문제, Hexagonal(Port/Adapter), Clean의 원 구조, 언제 어떤 스타일

- [x] **13.2** `_posts/2026-04-20-backend-02-concurrency.md`
  - 제목: `동시성과 성능`
  - description: `스레드·이벤트 루프·코루틴이 동시성을 어떻게 다르게 처리하는지 정리해요.`
  - tags: `[backend, concurrency, thread, event-loop, coroutine]`
  - 다룰 것: 스레드 기반(Java/Go) vs 이벤트 루프(Node) vs 코루틴(Kotlin/Python asyncio), 선택 기준, backpressure

- [x] **13.3** `_posts/2026-04-20-backend-03-caching.md`
  - 제목: `캐싱과 메시지 큐`
  - description: `Redis 캐시 전략과 Kafka·RabbitMQ 메시지 큐가 백엔드 부하를 분산시키는 방식을 정리해요.`
  - tags: `[backend, caching, redis, kafka, message-queue]`
  - 다룰 것: Cache-aside/Write-through/Write-behind, Cache Stampede·Thundering Herd, Queue(Kafka) vs Broker(RabbitMQ) 특성

#### Database (4편)

- [ ] **14.1** `_posts/2026-04-20-database-01-relational.md`
...