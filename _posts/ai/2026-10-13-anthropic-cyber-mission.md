---
title: "Anthropic Cyber Mission — 전력·수도 보안에 Claude 지원"
description: "기반시설·오픈소스 방어자를 지원하는 Anthropic Cyber Mission 과 개편된 사이버 검증 프로그램의 접근 단계를 정리합니다"
date: 2026-10-13
category: AI
subcategory: News
tags: [anthropic, cybersecurity, critical-infrastructure, open-source, claude]
image: /assets/og/2026-10-13-anthropic-cyber-mission.png
---

Anthropic이 2026년 10월 8일 방어자에게 모델과 인력을 지원하는 장기 프로그램 Anthropic Cyber Mission을 시작했어요. 첫 대상은 전력망·수도·교통을 운영하는 제어 시스템과, 여러 소프트웨어의 기반이 되는 오픈소스 코드입니다.

이틀 앞선 10월 6일에는 보안 전문가에게 Claude의 사이버 기능에 단계별 접근을 허용하는 Cyber Verification Program(CVP)을 개편했어요. 10월 7일 글에서 다룬 아르텍스 AI가 공격 쪽 자율 도구였다면, 이번 발표는 같은 능력을 방어자에게 먼저 제공하려는 시도입니다.

![Anthropic Cyber Mission 공지 대표 이미지](/assets/images/ai/anthropic-cyber-mission/01-hero-cybermission.webp)
*Anthropic Cyber Mission 공지 대표 이미지 — 출처: Anthropic*

## 발표된 두 프로그램

![Anthropic 로고](/assets/images/ai/anthropic-cyber-mission/02-logo-anthropic.webp)
*Anthropic 로고*

첫째는 핵심 인프라 방어 프로그램(Critical Infrastructure Defense Program, CIDP)이에요. 발전소·정수장의 제어기와 산업용 네트워크 같은 운영 기술(OT) 설비는 수십 년 쓰도록 만들어져 패치를 위해 가동을 중단하기 어렵고, 알려진 취약점이 몇 년씩 남는 경우가 많습니다. CIDP는 이런 현장의 보안을 실제로 관리하는 업체·장비 제조사에 최신 Claude 모델과 상주 엔지니어, Anthropic의 위협 연구를 지원해요.

창립 파트너는 11곳으로, 성격에 따라 세 유형으로 분류됩니다.

- 컨설팅·기술 서비스: Accenture, Booz Allen, Deloitte, PwC
- 보안 업체: CrowdStrike, Dragos, Insane Cyber, Nozomi Networks, Palo Alto Networks
- 장비 제조사: Hitachi, Rockwell Automation

처음에는 소규모 코호트로 어떤 방식이 실제로 효과가 있는지부터 확인하겠다고 밝혔어요. 6월 시작한 미국 주·지방정부 대상 사이버 방어 프로그램은 이미 미국 주의 절반 이상에 모델과 기술 지원을 제공했다고 합니다.

둘째는 OSS Scanner예요. 신청한 오픈소스 프로젝트를 Anthropic이 가장 강력하다고 밝힌 모델로 주기적으로 무료 스캔하고, 취약점마다 악용 시연 코드(PoC), 설명, 가능하면 수정안을 포함한 리포트를 전달합니다. Google의 OSS-Fuzz를 본뜬 신청형 서비스입니다.

## 사람 검토 없는 자동 리포트

OSS Scanner에서 논쟁이 될 부분은 리포트가 모델이 만든 그대로, 사람 검토 없이 메인테이너에게 전송된다는 점이에요. Anthropic은 참 양성률(실제 취약점일 비율) 90% 이상을 기대한다고 밝혔고, 심각도 등급이 틀리는 식의 오류가 포함될 수 있다고 미리 적었습니다.

대량의 리포트를 검토할 여력이 있는 프로젝트만 OSS Scanner를 쓰고, 그렇지 않은 프로젝트는 지금처럼 사람이 검증한 뒤 비공개로 알리는 조정 공개(CVD) 절차를 계속 받습니다. 실제로 Project Glasswing 때 일부 메인테이너가 검토 여부와 상관없이 모델이 발견한 취약점 정보를 전부 제공해 달라고 요청한 것이 이 서비스의 출발이었다고 해요.

![Project Glasswing 취약점 처리 단계별 건수 막대](/assets/images/ai/anthropic-cyber-mission/03-chart.webp)
*Project Glasswing 취약점 처리 단계별 건수 막대 — 출처: Anthropic 공개 수치 기반 자가 렌더*

4월부터 진행한 Project Glasswing에서 파트너 33곳과 Anthropic이 발견한 실제 취약점은 135,610건, 그중 고위험·치명 등급이 33,669건이었는데 패치 완료로 보고된 것은 9,333건이었습니다. 파트너 절반 이상이 패치 수를 밝히지 않아 실제보다 과소 집계된 수치지만, Anthropic도 취약점을 발견한 뒤 수정하기까지 몇 달이 걸리는 경우가 많았다고 적었어요.

[ARTEX AI — 은행 연쇄 해킹에 흔적 남긴 자율 침투테스트 도구](/posts/artex-ai-pentest-tool/)

## Cyber Verification Program 3단계

일반에 공개된 Claude 모델에는 사이버 작업 대부분을 차단하는 보수적인 안전장치가 적용돼 있어요. 방어자가 그 제한을 완화해 사용하려면 CVP를 거쳐야 하고, 10월 6일 개편으로 Project Glasswing이 CVP에 통합되면서 접근 등급이 셋으로 나뉘었습니다.

![Cyber Verification Program 등급별 대상·용도·요건 비교표](/assets/images/ai/anthropic-cyber-mission/04-capture-cvp.webp)
*Cyber Verification Program 등급별 대상·용도·요건 비교표 — 출처: Anthropic*

| 등급 | 대상 | 심사 |
| :--- | :--- | :--- |
| Defense Access | 보안팀·인프라 운영사·개인 연구자 | <mark>며칠</mark> |
| Red Team Access | 모의해킹 기업·레드팀 (조직만) | 몇 주 |
| Specialized Access | 전력망·은행 간 이체망 등 시험 기관 | **미국 정부와 심사** |

세 등급 모두 Claude Opus 5.5, Sonnet 5.5, Mythos 5.1을 쓸 수 있고 접근 등급이 높아질수록 차단이 완화돼요. 대신 오용 감시를 위해 데이터 보존이 필수입니다.

![CyScenarioBench 등급별 Claude Opus 5.5 해결률](/assets/images/ai/anthropic-cyber-mission/05-capture-cyscenariobench.webp)
*CyScenarioBench 등급별 Claude Opus 5.5 해결률 — 출처: Anthropic*

Anthropic은 다단계 공격 시나리오 평가 CyScenarioBench로 등급별 차단을 시험했어요. 일반 모델은 10개 과제 모두 첫 요청에서 차단됐고, Defense Access에서는 50회 시도 중 46회가 진행 도중 차단됐습니다. Red Team Access에서는 차단 없이 50회 중 34회를 성공했는데, 안전장치를 모두 비활성화했을 때의 성공률 67.6%와 거의 같은 수준이에요.

Red Team Access라도 랜섬웨어 배포, 물리 설비 손상, 고위험 안전 시스템 모의해킹처럼 사람이 다치거나 대규모 장애로 이어질 수 있는 행동은 실시간으로 차단된다고 Anthropic은 밝혔어요. 허가받은 대상에만 공격 시험을 할 수 있다는 조건도 붙습니다.

전력망·항공 운항 시스템·통신망처럼 인명과 시장에 영향을 주는 안전 시스템을 시험하는 일은 가장 높은 Specialized Access에서만 가능하고, Project Glasswing 기존 참여 기관은 이 등급으로 전환됐어요.

## 국내 접점과 신청 경로

공지에는 한국 기관·기업 언급이 없고, CIDP 창립 파트너에도 국내 회사는 없어요. 국내 보안팀이 바로 신청할 수 있는 프로그램은 CVP와 OSS Scanner입니다. CVP는 Claude Platform, Google Cloud Vertex AI, Microsoft Foundry에서 쓸 수 있고, Defense Access는 개인 연구자도 신청 대상이에요.

![Anthropic 사이버 미션 신청 경로 정리 카드](/assets/images/ai/anthropic-cyber-mission/06-items.webp)
*Anthropic 사이버 미션 신청 경로 정리 카드 — 출처: Anthropic 공지 기반 자가 렌더*

국내 전력·수도·교통 제어 시스템은 정보통신기반 보호법에 따라 주요정보통신기반시설로 지정돼 관리돼요. 이런 시설은 제어망을 외부와 분리해 운영하는 것이 원칙이라, CIDP처럼 외부 클라우드 모델과 상주 엔지니어를 투입하는 방식이 국내에서 그대로 가능한지는 확인되지 않습니다. 생성형 AI를 이런 망에 도입하는 기준을 다룬 공개 지침도 찾지 못했어요.

Anthropic은 몇 달 안에 CIDP의 파트너와 적용 분야를 확대하고, 효과가 없었던 방식까지 공유하겠다고 밝혔습니다. 2년 뒤에는 AI가 방어에 유리해질 것으로 보지만 당분간은 공격 비용이 더 빨리 감소한다고 본 것이 이번 발표의 전제예요.

## 참고 출처

- [[Anthropic] Introducing the Anthropic Cyber Mission (2026-10-08, 본문 이미지 1점 출처)](https://www.anthropic.com/news/anthropic-cyber-mission)
- [[Anthropic] Expanding the Cyber Verification Program (2026-10-06, 등급·평가·Glasswing 수치, 본문 이미지 2점 출처)](https://www.anthropic.com/news/cyber-verification-program)
