---
title: "gcloud CLI 다중 계정과 프로젝트 관리 상세 가이드"
description: gcloud CLI 다중 계정과 프로젝트 관리 상세 가이드. 설정 프로필(Configuration)과 필터링 기능을 활용해 복잡한 구글 클라우드 환경을 완벽하게 제어하는 방법을 정리합니다
date: 2026-04-25
order: 4
category: Daily Dev
subcategory: Tips & Tools
tags: [gcloud, gcp, cli, devops, tips-tools, cloud-computing]
image: /assets/og/2026-04-25-gcloud-cli-profile-management.png
---

Google Cloud(GCP)를 실무에서 사용하다 보면 개인 프로젝트, 사내 공용 프로젝트, 그리고 고객사별 환경까지 수십 개의 프로젝트를 오가게 됩니다. 이때 가장 위험한 상황은 '엉뚱한 프로젝트'에 명령어를 내리는 것입니다. 이를 방지하기 위한 `gcloud` CLI의 핵심 관리 기법을 상세히 정리합니다

## 방법

가장 중요한 개념은 **Configuration(설정 프로필)**입니다. 이는 로컬 환경에 저장되는 독립적인 설정 세트로, 계정·프로젝트·지역 정보를 하나의 묶음으로 관리하게 해줍니다

### 1. 프로필(Configuration) 완벽 제어
단순히 프로젝트 ID만 바꾸는 것이 아니라, 환경 자체를 스위칭하는 방식입니다

- **환경별 프로필 생성**: 업무용(work), 개인용(personal) 등으로 분리합니다
  ```bash
  gcloud config configurations create work
  gcloud config configurations create personal
  ```

- **프로필 세부 설정**: 현재 활성화된 프로필에 정보를 주입합니다
  ```bash
  # 활성 계정 설정
  gcloud config set account joon@company.com
  
  # 대상 프로젝트 연결
  gcloud config set project my-prod-1234
  
  # 기본 리전 및 존 설정 (명령어 입력 시 생략 가능해짐)
  gcloud config set compute/region asia-northeast3
  gcloud config set compute/zone asia-northeast3-a
  ```

- **프로필 확인 및 전환**:
  ```bash
  # 전체 리스트와 현재 활성 상태(*) 확인
  gcloud config configurations list
  
  # 프로필 즉시 전환
  gcloud config configurations activate personal
  ```

### 2. 계정 및 인증 관리
계정 관리는 보안의 시작입니다. 사용하지 않는 권한은 즉시 회수해야 합니다

- **로그인 및 활성 계정 확인**:
  ```bash
  # 새로운 계정 추가 로그인
  gcloud auth login
  
  # 현재 로컬에 인증된 모든 계정 확인
  gcloud auth list
  ```

- **인증 회수 (Revoke)**: 더 이상 필요 없는 계정은 로컬에서 삭제합니다
  ```bash
  # 특정 계정 제거
  gcloud auth revoke joon@old-project.com
  
  # 모든 계정 일괄 로그아웃
  gcloud auth revoke --all
  ```

### 3. 프로젝트 리스트와 필터링
수백 개의 프로젝트 중 필요한 것만 골라내는 능력이 필요합니다

- **커스텀 리스트 출력**: 원하는 정보만 표 형태로 출력합니다
  ```bash
  # 프로젝트 이름, ID, 번호만 출력
  gcloud projects list --format="table(name, projectId, projectNumber)"
  ```

- **강력한 필터링**: 특정 조건에 맞는 프로젝트만 찾습니다
  ```bash
  # 'prod'라는 단어가 포함된 프로젝트만 찾기
  gcloud projects list --filter="name:prod"
  
  # 삭제 대기 상태인 프로젝트만 확인
  gcloud projects list --filter="lifecycleState:DELETE_REQUESTED"
  ```

### 4. 프로젝트 삭제 및 복구 (자원 관리)
프로젝트 삭제는 해당 프로젝트 내의 모든 자원(VM, DB, Network)을 함께 파괴합니다

- **삭제 실행**: 명령어를 실행하면 약 30일간의 유예 기간 후 영구 삭제됩니다
  ```bash
  gcloud projects delete [PROJECT_ID]
  ```

- **복구**: 실수로 삭제했다면 유예 기간 내에 되살릴 수 있습니다
  ```bash
  gcloud projects undelete [PROJECT_ID]
  ```

## 옵션 / 변형

### 환경 변수를 이용한 프로필 전환
터미널 세션별로 다른 프로필을 쓰고 싶다면 환경 변수를 활용할 수 있습니다
```bash
export CLOUDSDK_ACTIVE_CONFIG_NAME=personal
# 이 터미널 세션에서는 별도의 activate 명령 없이 personal 프로필이 고정됩니다
```

### 일회성 프로젝트 지정
기본 설정을 바꾸지 않고 딱 한 번만 다른 프로젝트에 명령을 내릴 때 사용합니다
```bash
gcloud compute instances list --project [SUB_PROJECT_ID]
```

## 참고

- [Google Cloud CLI Configuration 가이드](https://cloud.google.com/sdk/docs/configurations)
- [gcloud 프로젝트 관리 명령 참조](https://cloud.google.com/sdk/gcloud/reference/projects)
- [gcloud 필터 및 포맷 구문 상세](https://cloud.google.com/sdk/gcloud/reference/topic/filters)
