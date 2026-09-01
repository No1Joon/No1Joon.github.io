---
title: "자체 칩을 만들수록 브로드컴이 버는 구조"
description: "커스텀 AI 칩이 나오기까지의 세 층을 갈라, 자체 칩이라는 발표 뒤에서 도면을 실제로 그리는 설계 서비스 회사들의 자리를 정리합니다"
date: 2026-08-26
category: Tech
subcategory: Explainer
tags: [custom-asic, broadcom, marvell, tpu, ai-chip]
image: /assets/og/2026-08-26-custom-asic-design-services.png
---

자체 칩을 만들었다는 발표가 올해만 여러 번 나왔습니다. Google TPU, Amazon Trainium, Microsoft Maia, Meta MTIA, 여기에 OpenAI와 Anthropic까지 이름을 올렸어요.

그런데 그 칩의 도면을 실제로 그린 회사는 대부분 발표한 쪽이 아닙니다.

![커스텀 AI 칩 설계 서비스 층을 표현한 3D 에디터리얼 콘셉트 씬](/assets/images/tech/custom-asic-design-services/01-hero-agy.webp)
*커스텀 AI 칩 설계 서비스 층을 표현한 3D 에디터리얼 콘셉트 씬 — 출처: 개념 컷 · agy 자가 생성*

## 자체 칩이라는 말이 가리는 것

커스텀 AI 칩 하나가 나오기까지의 일은 크게 세 층으로 갈립니다. 무엇을 계산할 칩인지 정하는 층, 그것을 실제 트랜지스터 배치로 옮기는 층, 그리고 웨이퍼에 찍는 층이에요.

발표하는 쪽이 쥐고 있는 건 대개 첫 번째 층입니다. 연산기 구조, 메모리 대역폭 목표, 모델을 어떻게 태울지 같은 명세죠. 나머지 둘은 다른 회사가 맡습니다.

| 단계 | 맡는 쪽 | 예 |
|---|---|---|
| 아키텍처·명세 | **칩을 발표한 회사** | Google · Amazon |
| 물리 설계·IP·검증 | <mark>설계 서비스 회사</mark> | Broadcom · Marvell |
| 웨이퍼 제조 | 파운드리 | TSMC · 삼성 |

가운데 층이 따로 존재하는 이유는 난이도 때문입니다. 2나노 공정에서 도면을 뜨고, 칩 사이를 초당 수 테라비트로 잇는 SerDes 같은 고속 인터페이스를 붙이고, 첨단 패키징까지 검증하는 일은 세대마다 처음부터 다시 해야 합니다. 한 군데라도 틀리면 수천억 원짜리 테이프아웃이 통째로 날아가요.

그래서 하이퍼스케일러는 아키텍처만 쥐고 나머지를 산 채로 맡깁니다. 자체 칩이라는 말은 소유권을 가리키지 도면 작성을 가리키지 않아요.

![하이퍼스케일러 AI 서버 컴퓨트 ASIC 출하량 2024년 대비 2027년 전망](/assets/images/tech/custom-asic-design-services/02-chart-asic.webp)
*하이퍼스케일러 AI 서버 컴퓨트 ASIC 출하량 2024년 대비 2027년 전망 — 출처: Counterpoint Research 전망 기반 자가 렌더*

Counterpoint Research는 상위 10개 하이퍼스케일러가 쓰는 AI 서버 컴퓨트 ASIC 출하량이 2024년에서 2027년 사이 세 배가 된다고 봅니다. 자체 칩 발표가 늘어날수록 이 가운데 층으로 들어가는 돈도 같이 늘어납니다.

## 브로드컴이 앉은 자리

![브로드컴 로고](/assets/images/tech/custom-asic-design-services/03-logo-broadcom.webp)
*브로드컴 로고 — 출처: Broadcom*

6월 3일 발표한 2026 회계연도 2분기 실적에서 브로드컴의 AI 부문 매출은 **108억 달러(약 15조 1,200억 원)** 였습니다. 1년 만에 두 배가 넘게 늘었어요. 전사 매출은 221억 8,700만 달러였습니다.

같은 발표에서 브로드컴은 커스텀 칩 핵심 고객이 여섯 곳이라고 밝혔습니다. Google, Meta, OpenAI, Anthropic이 그 안에 있어요.

계약이 적히는 단위를 보면 이 사업의 성격이 드러납니다. 칩 몇 개가 아니라 **기가와트(GW)** 로 씁니다.

### Anthropic — 2027년부터 차세대 TPU 기반 컴퓨트 5GW, 2026년분은 1GW 이상

### OpenAI — 실리콘 인도 완료, 2026년 말 양산 목표

### OpenAI — 2027년 1.3GW 배치 계약, 2029년까지 10GW

칩을 파는 게 아니라 전력을 채워 넣을 컴퓨트 용량을 파는 셈입니다. Apollo·Blackstone 등이 참여하는 AI XPU 플랫폼으로 2028년까지 20GW 넘는 용량을 배치하겠다는 계획도 같은 문법이에요.

![브로드컴의 구글·앤트로픽發 커스텀 실리콘 매출 2026년 대비 2027년 전망](/assets/images/tech/custom-asic-design-services/04-chart.webp)
*브로드컴의 구글·앤트로픽發 커스텀 실리콘 매출 2026년 대비 2027년 전망 — 출처: Mizuho 추정치 기반 자가 렌더*

Mizuho는 브로드컴이 구글과 Anthropic 두 고객에서만 2026년 210억 달러(약 29조 4,000억 원), 2027년 420억 달러(약 58조 8,000억 원)를 올린다고 추정합니다. 회사가 내놓은 2027년 AI 반도체 매출 가이던스는 **1,000억 달러(약 140조 원) 초과** 입니다.

이 자리를 브로드컴이 잡은 건 우연이 아닙니다. 고속 SerDes와 PHY 지식재산, 데이터센터를 잇는 이더넷 스위치 칩, 그리고 첨단 패키징 물량을 미리 확보해 둔 조합을 한 회사가 다 갖고 있는 경우가 드물어요.

> 자체 칩을 만들수록, 그 칩을 대신 설계해 주는 회사의 매출이 늘어납니다

## 구글 한 곳이 파트너를 넷으로 늘렸다

![구글이 공개한 TPU 세대별 사양 비교 (TPU v4 · v5p · Ironwood)](/assets/images/tech/custom-asic-design-services/05-photo-tpu.webp)
*구글이 공개한 TPU 세대별 사양 비교 (TPU v4 · v5p · Ironwood) — 출처: Google*

브로드컴은 원래 구글 TPU 설계를 사실상 독점했습니다. 그 구도가 올해 깨졌어요. 6월 실적 발표에서 브로드컴 스스로 주요 고객이 다른 공급사를 찾고 있다고 밝혔습니다.

TPU 8세대는 하나의 칩이 아니라 둘로 쪼개졌습니다. 학습용과 추론용을 나눠 서로 다른 파트너에게 맡기는 방식이에요.

| 파트너 | 맡은 것 | 비고 |
|---|---|---|
| 브로드컴 | 학습용 **Sunfish** | TSMC 2나노 |
| 미디어텍 | 추론용 **Zebrafish** | <mark>20~30% 저렴</mark> |
| 마벨 | 메모리 프로세싱 유닛 | 약 200만 개 규모 |
| 인텔 | Xeon·커스텀 IPU | TPU 둘레의 층 |

미디어텍이 맡은 Zebrafish는 원가를 깎은 추론 전용입니다. 같은 TSMC 2나노, 같은 2027년 말 목표인데 대안 대비 20~30% 저렴하다는 게 이 갈래의 존재 이유예요.

마벨은 TPU 본체가 아니라 그 옆의 메모리 프로세싱 유닛을 맡았습니다. 구글이 마벨 지분 약 122억 달러(약 17조 800억 원)어치를 취득할 수 있는 옵션이 함께 붙었어요. 인텔은 4월부터 시작한 다년 계약으로 Xeon과 커스텀 IPU를 대는데, TPU를 대체하는 게 아니라 그 둘레의 범용 연산과 네트워킹을 채웁니다.

학습과 추론을 갈라 서로 다른 회사에 맡겼다는 건 두 작업의 요구가 이제 한 칩으로 덮이지 않는다는 뜻입니다. 8월 14일에 다룬 CUDA 해자 이야기에서 전선이 추론 쪽으로 옮겨 갔다고 봤는데, 설계 발주가 그 판단을 그대로 따라가고 있어요.

## 점유율은 내려가는데 물량은 늘어난다

![2027년 AI 서버 컴퓨트 ASIC 설계 파트너 점유율 전망](/assets/images/tech/custom-asic-design-services/06-chart.webp)
*2027년 AI 서버 컴퓨트 ASIC 설계 파트너 점유율 전망 — 출처: Counterpoint Research 전망 기반 자가 렌더*

브로드컴과 마벨이 이 시장의 95%를 쥐고 있다는 설명을 아직 자주 보게 됩니다. 그 숫자는 이미 낡았습니다.

Counterpoint는 2027년 브로드컴 점유율을 약 60%로, 마벨을 약 8%로 봅니다. 여기서 눈여겨볼 건 마벨의 출하량이 같은 기간 두 배로 늘어난다는 점이에요. 물량은 늘어나는데 비율은 내려갑니다. 시장이 그보다 빨리 커지기 때문입니다.

빈자리를 채우는 쪽은 대만과 미디어텍입니다.

| 진영 | 대표 고객 | 상태 |
|---|---|---|
| Alchip | AWS **Trainium3** | 2026년 2분기 양산 |
| GUC | 다수 클라우드 | TSMC 자회사 |
| 미디어텍 | 구글 추론 TPU | <mark>2026년 4분기 첫 양산</mark> |

Alchip은 AWS Trainium3의 3나노 설계를 맡아 2026년 2분기 양산에 들어갑니다. 2024년 연간 보고서 기준 매출의 60.16%가 단일 고객 한 곳에서 나왔는데, 업계에서는 그 고객을 AWS로 봅니다. Morgan Stanley는 2026년 Trainium 계열 출하량을 150만 개 이상으로 잡았어요.

미디어텍은 첫 AI ASIC을 2026년 4분기에 양산하고 2027년 설계 서비스 점유율 목표를 15~20%로 올려 잡았습니다. 2026년 데이터센터 매출 전망은 20억 달러(약 2조 8,000억 원)예요. 스마트폰 SoC를 만들던 회사가 3나노 커스텀 ASIC 인력을 1,000명 규모로 새로 꾸리고 있습니다.

마벨 쪽 숫자는 곧 갱신됩니다. 8월 27일 실적 발표에서 커스텀 실리콘 부문 수치가 나오면 이 그림은 한 번 더 그려야 해요.

## 한국은 어느 층에 서 있나

![삼성전자 로고](/assets/images/tech/custom-asic-design-services/07-logo-samsung.webp)
*삼성전자 로고 — 출처: Samsung*

국내 기사에서 삼성 파운드리의 AI 칩 수주와 브로드컴·마벨의 설계 서비스가 같은 문단에 놓이는 경우가 많은데, 둘은 다른 층입니다. 앞에서 나눈 세 층으로 보면 삼성이 들어가 있는 자리는 세 번째, 웨이퍼를 찍는 층이에요.

삼성전자는 테슬라 차세대 칩 AI5와 AI6를 미국 테일러 팹에서 만듭니다. 총 370억 달러(약 51조 8,000억 원)가 들어간 생산 거점이고, 기존 AI4 개선판은 평택에서 돌아갑니다. Anthropic과는 2나노 기반 차세대 AI 칩을 놓고 수주 협상을 진행 중이에요.

설계 서비스 층에도 한국 회사가 있습니다. 삼성 파운드리의 SAFE 디자인 솔루션 파트너로 등록된 세미파이브, 가온칩스, 에이디테크놀로지가 그 자리입니다. 브로드컴·마벨과 같은 층이지만 다루는 공정 노드와 프로젝트 규모가 다릅니다.

| 층 | 국내 위치 | 비고 |
|---|---|---|
| 아키텍처 | 리벨리온 · 퓨리오사AI | 자체 NPU **팹리스** |
| 설계 서비스 | 세미파이브 · 가온칩스 | SAFE 파트너 |
| 파운드리 | <mark>삼성전자</mark> | 테일러·평택 |

리벨리온과 퓨리오사AI는 위치가 또 다릅니다. 남의 칩을 대신 설계하는 게 아니라 자기 NPU를 직접 만들어 파는 팹리스라서, 이 구조 안에서는 하이퍼스케일러와 같은 첫 번째 층에 섭니다.

## 정리하면

- 자체 칩이라는 발표는 아키텍처 소유를 뜻하지 도면 작성을 뜻하지 않습니다.
- 그 도면을 대신 그리는 층이 지금 가장 안정적으로 돈을 법니다.
- 2024년 사실상 한 회사였던 그 층이 2027년에는 다섯 갈래 이상으로 갈라집니다.
- 한국의 무게중심은 그 층이 아니라 아래쪽 파운드리에 있습니다.

> 누가 엔비디아를 이기느냐보다, 자체 칩이 늘어날수록 누가 청구서를 받느냐가 더 오래 가는 질문입니다.

## 참고 출처

- [[Broadcom] 2026 회계연도 2분기 실적 발표 (AI 매출·커스텀 고객 6곳·GW 단위 계약)](https://investors.broadcom.com/financial-information/quarterly-results)
- [[CNBC] Broadcom (AVGO) earnings report Q2 2026 (분기 실적 수치)](https://www.cnbc.com/2026/06/03/broadcom-avgo-earnings-report-q2-2026.html)
- [[Counterpoint Research] AI 서버 컴퓨트 ASIC 설계 파트너 점유율 전망 (2027년 브로드컴 60%·마벨 8%, 출하량 3배)](https://www.counterpointresearch.com/)
- [[The Next Web] Google assembles four-partner chip supply chain with Broadcom, MediaTek, Marvell (Sunfish·Zebrafish·MPU·IPU 분담)](https://thenextweb.com/news/google-inference-chips-nvidia-challenge-supply-chain)
- [[TrendForce] Marvell, AMD Reportedly Shake Up Google TPU Race (마벨 MPU 물량·지분 옵션)](https://www.trendforce.com/news/2026/08/20/news-marvell-amd-reportedly-shake-up-google-tpu-race-putting-broadcom-mediatek-under-pressure/)
- [[Google] Ironwood: The first Google TPU for the age of inference (본문 TPU 사양 비교표 출처)](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/)
- [[CommonWealth Magazine] How Alchip Puts Taiwan on the Frontline of the ASIC Wars (단일 고객 매출 비중·Trainium 설계)](https://english.cw.com.tw/article/article.action?id=4307)
- [[Samsung Foundry] SAFE Design Service 파트너 목록 (국내 디자인 솔루션 파트너)](https://semiconductor.samsung.com/foundry/safe/design-service/)
- [[한국경제] 삼성 파운드리 수주 행진 — 테슬라·앤트로픽 (테일러 팹 투자·2나노 협상)](https://www.hankyung.com/article/2026070349191)
- 환율: 1달러 ≈ 1,400원 기준 환산
- Mizuho·Morgan Stanley 수치는 증권사 추정치로, 회사 공식 발표가 아닙니다
