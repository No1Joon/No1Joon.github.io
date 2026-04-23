---
title: "통합과 E2E 테스트"
description: TestContainers·Playwright로 외부 의존성을 포함한 테스트를 안정적으로 만드는 방법을 정리해요.
date: 2026-04-20
order: 2
category: Development
subcategory: Testing
tags: [testing, integration, e2e, testcontainers, playwright]
image: /assets/og/2026-04-20-testing-02-integration.png
---

모듈 내부 로직만 검증하는 단위 테스트를 넘어서면, 실제 데이터베이스에 쿼리를 날리거나 브라우저에서 버튼을 클릭하는 **통합(Integration)** 및 **E2E**(End-to-End) 테스트 단계가 필요합니다. 이 과정에서 가장 큰 복병은 외부 환경의 불확실성으로 인해 테스트가 성공과 실패를 반복하는 **Flaky Test** 현상입니다. 테스트의 신뢰성을 높여주는 실무 도구들을 정리해요

## 인프라를 코드로 제어: TestContainers

통합 테스트를 위해 로컬에 DB를 미리 띄워두거나 공용 테스트 DB를 쓰는 방식은 데이터 오염과 환경 일관성 문제로 관리가 매우 어렵습니다. **TestContainers**는 도커(Docker)를 사용하여 테스트 코드 내에서 필요한 인프라를 즉석에서 띄우고 종료하는 라이브러리입니다

```java
// Java/JUnit 기반 TestContainers 예시
@Container
static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:16")
    .withDatabaseName("testdb")
    .withUsername("user")
    .withPassword("password");
```

- **장점**: 개발자의 로컬 환경이나 CI 환경 어디서든 **동일한 인프라 스펙**으로 테스트할 수 있습니다. 각 테스트마다 깨끗한(Clean) 환경을 보장합니다

## 사용자의 관점에서: Playwright와 Cypress

**E2E 테스트**는 실제 브라우저를 띄워 사용자의 행동 시나리오를 검증합니다

| 도구 | 특징 | 비고 |
|---|---|---|
| **Playwright** | 멀티 브라우저 지원, 속도 매우 빠름, 헤드리스 모드 기본 | MS에서 개발, 최근 가장 인기 있음 |
| **Cypress** | 직관적인 UI, 풍부한 디버깅 도구, 웹 중심 | 프론트엔드 개발자 친화적 |

E2E 테스트는 비즈니스의 **핵심 사용자 흐름**(예: 회원가입 → 로그인 → 상품 구매)에 집중해서 작성해야 합니다. 모든 사소한 UI 요소까지 E2E로 커버하려 하면 테스트 코드 관리 비용이 감당할 수 없을 만큼 커집니다

## Flaky Test 방지 전략

테스트가 이유 없이 실패하는 것을 막기 위한 세 가지 실천입니다

1. **Wait, don't Sleep**: 고정된 시간(Thread.sleep)을 기다리는 대신, 특정 조건(버튼이 나타날 때까지 등)이 만족될 때까지 기다려야 합니다
2. **Idempotency**: 테스트 데이터는 매 실행마다 독립적으로 생성되고 정리되어야 합니다
3. **Retry Logic**: 일시적인 네트워크 지연 등으로 인한 실패는 CI 단계에서 2~3회 자동 재시도하도록 설정합니다

<div class="callout why">
  <div class="callout-title">핵심 인사이트: Mock vs Real Infra</div>
  가짜 객체(Mock)를 쓰면 테스트는 빨라지지만, 실제 DB의 제약 조건이나 API 응답 형식을 놓칠 수 있습니다. <b>비즈니스 규칙 검증은 Mock</b>을 쓰고, <b>데이터 흐름과 연동 검증은 실물 인프라(TestContainers)</b>를 쓰는 계층적 접근이 필요합니다
</div>

## 정리

- **TestContainers**를 사용하여 인프라 의존성을 독립적이고 일관되게 관리합니다
- **E2E 도구**는 비즈니스의 핵심 성공 경로를 보호하는 최후의 보루입니다
- 테스트의 **안정성**이 보장되지 않으면 개발팀은 테스트 결과를 무시하게 됩니다
- 비싼 테스트(E2E)는 적게, 저렴한 테스트(Unit/Integration)는 많이 짜는 피라미드 원칙을 지키세요

다음 글에서는 마이크로서비스 간의 규약을 검증하는 **계약 테스트와 성능 테스트** 기법을 다뤄요
