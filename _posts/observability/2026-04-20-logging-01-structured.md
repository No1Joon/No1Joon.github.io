---
title: "구조화 로깅 원칙"
description: 텍스트 로그에서 JSON 구조화로 전환할 때의 설계 포인트와 필드 네이밍을 정리해요.
date: 2026-04-20
order: 1
category: Observability
subcategory: Logging
tags: [logging, structured-logging, json, observability, schema]
---

"사용자가 장바구니에 아이템을 3개 담았습니다"라는 평문(Plain Text) 로그는 사람이 읽기엔 좋지만, 매초 수만 건이 쌓이는 MSA 환경에서는 검색도 통계도 불가능한 쓸모없는 텍스트 조각에 불과합니다.

로그를 시스템이 이해할 수 있는 하나의 **데이터 레코드**로 승격시키는 기술이자 현대 로깅의 기본인 **구조화 로깅(Structured Logging)**을 살펴볼게요.

## 평문 로그 vs JSON 구조화 로그

기존의 텍스트 로그는 분석을 위해 복잡한 정규표현식(Regex)을 짜서 파싱을 명시해야 했습니다. 반면, JSON으로 출력하면 검색 엔진이 곧바로 다차원 속성으로 인덱싱할 수 있어요.

```json
// AS-IS: 텍스트 로깅 (분석이 어려움)
2026-04-20 10:15:30 [INFO] [Thread-5] [OrderService] User 4815 paid $50.00 for order 992.

// TO-BE: JSON 구조화 로깅
{
  "timestamp": "2026-04-20T10:15:30.123Z",
  "level": "INFO",
  "trace_id": "a1b2c3d4",
  "service": "order-api",
  "message": "User paid for order",
  "user_id": 4815,
  "order_id": 992,
  "amount_usd": 50.00
}
```

이제 통합 대시보드 창에서 `service: "order-api" AND amount_usd > 40` 이라는 직관적인 쿼리로 0.1초 만에 결과를 뽑아내고 차트를 그릴 수 있습니다.

## 표준화된 스키마 필드 설계

각 마이크로서비스마다 JSON 키 이름 규칙이 따로 놀면 (어디는 `user_id`, 어디는 `userId`) 중앙에서 집계할 수 없습니다. 사내 공통 모듈화 **표준 스키마 규약**을 반드시 강제해야 합니다.

- **timestamp**: ISO 8601 포맷 통일 (Z/UTC 기준 타임존 혼동 방지 권장).
- **level**: INFO, WARN, ERROR 대문자 통일 및 철학 준수.
- **service / host**: 이 로그가 어떤 배포 그룹의 어디서 발생했는가.
- **trace_id**: 여러 서버를 관통하는 단일 분산 요청 식별자. 앱단 프레임워크의 Mapped Diagnostic Context(MDC)나 Async Local Storage를 엮어 스레드의 모든 로그에 이 ID를 자동으로 욱여넣어야 합니다.

## PII와 민감 정보 마스킹 

로그가 JSON으로 편하게 검색 가능해졌다는 건, **해커나 내부망 직원이 로그 검색기만 털면 모든 유저의 개인정보를 원클릭으로 빼낼 수 있다**는 의미도 됩니다. 

앱 내의 로깅 라이브러리를 세팅할 때, 최후 전송 필터 단계에서 반드시 이메일, 전화번호, 카드번호 같은 개인식별정보(PII)를 정규식으로 필터 스와핑(`***` 마스킹)하여 출력해야만 치명적인 법적 컴플라이언스 위반을 피할 수 있습니다.

<div class="callout warning">
  <div class="callout-title">로그 레벨 철학: Error의 무거운 체급 통제</div>
  로그가 너무 많으면 스토리지 비용만 낭비되고 <strong>정작 중요한 크리티컬 에러가 맹목화</strong>됩니다. 사내 로깅 컨벤션으로 ERROR 레벨은 <strong>"새벽 3시에 담당자 슬랙 핑 알람이 울려도 타당한 수준, 그리고 반드시 운영자가 핫픽스 조치해야 하는 백엔드의 비정상적 결함"</strong>에만 국한해야 합니다. 사용자의 잘못된 비밀번호 입력이나 외부 파트너사 API 일시적 타임아웃은 WARN이나 INFO로 내리세요.
</div>

## 정리 요약

- 분석 불가능한 평문 로그의 한계를 버리고, 별도 파싱이 불필요한 **JSON 포맷(구조화 로깅)**을 팀 전역에 채택하세요.
- 모든 스레드를 관통하는 **MDC 컨텍스트** 툴을 엮어 `trace_id`와 `service` 같은 필수 표준 스키마 필드를 일관성 있게 자동 주입하세요.
- 로그 저장 인덱서에 적재되기 이전, 라이브러리 앞단에 **PII 마스킹 계층**을 두어 정보 유출 사고를 차단하세요.

앱 레벨에서 아름다운 일관성을 띤 통일된 JSON 스트림을 뿜어내게 설정했다면, 다음 단계는 이런 부산물을 가볍게 떠서 중앙으로 모아 이끄는 물길 공사입니다. **로그 수집 파이프라인(Fluent Bit/Loki/ELK)** 아키텍처를 이어갑니다. 
