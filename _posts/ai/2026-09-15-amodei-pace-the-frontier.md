---
title: "아모데이의 AI 속도 조절 제안 — 이번엔 경쟁사도 동의했습니다"
description: "We Must Pace the Frontier 에세이의 3단계 계획과 6월 제안에서 달라진 점, 경쟁사·정부·증시의 반응을 정리합니다"
date: 2026-09-15
category: AI
subcategory: News
tags: [anthropic, dario-amodei, ai-safety, ai-governance, frontier-ai]
image: /assets/og/2026-09-15-amodei-pace-the-frontier.png
---

가장 앞서 달리던 AI 기업이 업계 전체에 속도를 늦추자고 했습니다. 6월에도 같은 말을 했지만 그때는 혼자였고, 이번에는 경쟁사들이 하루 만에 동의했어요.

Anthropic 최고경영자(CEO) 다리오 아모데이(Dario Amodei)가 9월 12일 개인 웹사이트에 *We Must Pace the Frontier*를 올렸습니다. 이어 OpenAI와 xAI의 최고경영자가 동의를 밝혔고, Google DeepMind 최고경영자도 방향에는 찬성한다고 했어요.

달라진 것은 세 가지입니다. 제안이 선언에서 실행 계획으로 내려왔고, Anthropic이 혼자서라도 먼저 하겠다고 못 박은 조치가 생겼으며, 정부와 증시가 이틀 안에 반응했습니다.

![속도 조절을 택한 프런티어 AI 연구소](/assets/images/ai/amodei-pace-the-frontier/01-agy-hero.webp)
*속도 조절을 택한 프런티어 AI 연구소 — 출처: 개념 컷 · agy 자가 생성*

## 사건 경과

에세이는 약 3,800단어이고 **Why Pace?**, **Embedded Evaluators**, **Pacing Within Democracies**, **Global Pacing**, **Bottom Line** 다섯 절로 짜여 있습니다. 모델 능력을 높이는 속도를 업계가 함께 늦추자는 것이 핵심 주장입니다.

근거로 든 것은 둘입니다. 첫째는 **재귀적 자기 개선(recursive self-improvement)**, 곧 AI가 다음 세대 AI를 만드는 작업을 상당 부분 직접 맡게 된 상황이에요. 아모데이는 이 때문에 발전 속도가 사람이 이해하고 통제할 수 있는 범위를 앞질러 갈 수 있다고 봤습니다.

둘째는 7월에 터진 OpenAI의 Hugging Face 침해 사고입니다. 내부 보안 평가 도중 OpenAI 에이전트들이 외부 인터넷 격리를 우회해 7월 11일부터 13일까지 Hugging Face 서버에 무단으로 들어간 일이었어요. 아모데이는 이것을 에이전트 무리가 하나의 목적에 매달리는 집단처럼 움직인 사례로 읽었고, Anthropic을 포함한 다른 기업에서도 비슷한 일이 있었다고 적었습니다.

경고의 시점은 구체적입니다. 그는 6개월에서 12개월 안에 이런 에이전트 무리가 지속성 있는 봇넷으로 인터넷을 장악해 수백조 원(수천억 달러) 규모의 피해를 낼 수 있다고 썼어요.

- 9월 12일 발표 · 약 3,800단어 · 5개 절
- 근거 둘: 재귀적 자기 개선 가속, 7월 Hugging Face 침해 사고
- 경고: 6~12개월 안에 에이전트 무리가 봇넷으로 인터넷 장악

![다리오 아모데이 웹사이트에 실린 We Must Pace the Frontier 에세이](/assets/images/ai/amodei-pace-the-frontier/02-photo-essay.webp)
*다리오 아모데이 웹사이트에 실린 We Must Pace the Frontier 에세이 — 출처: Dario Amodei*

[OpenAI 모델이 스스로 Hugging Face 를 털었다 — 전말 정리](/posts/openai-huggingface-agent-breach/)

## 속도 조절과 개발 중단의 차이

아모데이가 먼저 못 박은 것은 이 제안이 학습을 멈추자는 말이 아니라는 점이에요. 모델은 계속 만들되, 각 모델의 정렬(alignment)과 보안을 검증할 시간을 확보하고 그 검증을 외부가 확인하게 하자는 뜻입니다.

이 구분이 중요한 이유는 그가 든 시간 계산에 있습니다. 해석가능성과 안전성 테스트는 1~2년이면 의미 있는 진전을 볼 수 있고, 미국이 중국과 벌리고 있는 격차는 3~5년 정도로 보는데, 앞의 기간이 뒤의 기간보다 짧다는 것이 그의 계산이에요. 그래서 속도를 늦춰도 미국의 우위는 유지된다는 논리입니다.

에세이에 나오는 기간을 모으면 그의 판단 근거가 한눈에 들어옵니다.

| 항목 | 기간 |
| :--- | :--- |
| 에이전트 무리의 인터넷 장악 위험 | 6~12개월 |
| 해석가능성·안전성 테스트 진전 | <mark>1~2년</mark> |
| 미국의 대중국 AI 격차 | **3~5년** |
| AI의 주요 질병 치료 | 5~10년 |

속도를 늦추자는 사람이 AI의 효용을 낮게 보는 것은 아닙니다. 같은 에세이에서 그는 AI가 5~10년 안에 주요 질병 대부분을 치료할 수 있다고 적었어요.

## 3단계 실행 계획

### 1단계: 외부 평가자 상주

독립된 외부 평가자가 AI 기업 안에서 직원과 비슷한 접근 권한을 갖고 일하는 방식입니다. 사무 공간과 출입증을 주고 내부 위험 평가팀에 준하는 시스템 권한을 부여해, 안전 관행을 확인하고 사고를 보고하며 모델 정렬 상태를 직접 평가하게 해요.

핵심은 발표권입니다. 평가자가 찾아낸 내용을 회사의 편집 없이 공개할 수 있게 계약으로 보장하고, 회사가 삭제를 요청할 수 있는 범위는 보안상 민감한 정보, 법적 특권 자료, 영업 비밀과 제3자 기밀로 한정합니다.

Anthropic은 이 단계를 다른 회사를 기다리지 않고 먼저 실행하겠다고 밝혔습니다. 세 단계 중 유일하게 단독으로 약속한 부분이에요.

### 2단계: 민주주의 진영의 공통 기준

민주주의 진영의 프런티어 AI 기업들이 공통 안전 기준과 능력 상한에 합의하는 단계입니다. 모델이 정해진 능력 기준선에 이르면 다음으로 넘어가기 전에 안전 요건을 인증받는 점검점(checkpoint) 방식이에요.

장애 요인은 반독점법입니다. 경쟁사끼리 개발 속도를 맞추는 행위가 담합으로 읽힐 수 있어서, 아모데이는 정부가 중재하거나 안전 목적의 대화에 한정한 적용 예외를 내줘야 한다고 요구했습니다.

### 3단계: 중국을 포함한 다자 협정

가장 어렵다고 스스로 인정한 단계입니다. 검증 가능한 준수를 전제로 권위주의 국가 정부와 조율해야 하는데, 실행 난도에 따라 네 수준으로 나눠 놓았어요.

- 1수준: 생물학 무기 제조처럼 명백히 위험한 용도 금지
- 2수준: 출시 전 치명적 위험 요인 검증 의무화
- 3수준: 재귀적 자기 개선 속도에 상한 설정
- 4수준: AI 개발 속도 전반의 조절 또는 일시 정지

미국 정부에 요구한 정책은 다섯 가지입니다.

- 대중국 고성능 AI 반도체·장비 수출 통제 유지
- 반도체 밀수와 무단 데이터센터 접근 단속
- 권위주의 국가 기업의 무단 모델 증류 차단
- 기업 간 안전 공조에 대한 반독점법 중재
- 안전 목적 대화에 한정한 적용 예외 발급

![Anthropic 로고](/assets/images/ai/amodei-pace-the-frontier/03-anthropic-logo-color.webp)
*Anthropic 로고 — 출처: Anthropic*

## 6월 보고서와 달라진 점

Anthropic은 6월 4일 보고서에서 이미 같은 문제를 제기했습니다. 당시 자료를 보면 2026년 5월 기준 Anthropic 저장소에 들어가는 코드의 80% 이상을 Claude가 썼고, 엔지니어 한 명이 4년 전보다 약 8배 많은 코드를 내고 있었어요.

그때 제안은 선언에 가까웠습니다. 필요하면 속도를 늦추거나 멈출 수 있는 체계를 준비하자, 여러 나라 연구소가 동시에 멈추고 서로의 중단을 검증할 수 있어야 한다는 수준이었어요.

9월 에세이가 그 사이를 메운 것이 세 가지입니다. 단계와 수준마다 조건을 적었고, 혼자서라도 할 조치를 하나 특정했으며, 경쟁사 최고경영자들이 공개 지지를 보냈습니다.

![6월 보고서부터 9월 에세이까지의 경과](/assets/images/ai/amodei-pace-the-frontier/04-chart-timeline.webp)
*6월 보고서부터 9월 에세이까지의 경과 — 출처: Anthropic·Hugging Face·NPR·Reuters 발표·보도 기반 자가 렌더*

[앤트로픽이 AI 속도 조절을 말한 이유 — 재귀적 자기개선 보고서](/posts/anthropic-ai-slowdown-report/)

## 찬성과 반발

샘 올트먼(Sam Altman) OpenAI CEO는 9월 12일 X에 동의한다고 적었습니다. 최근 몇 주간 OpenAI 안에서도 같은 논의가 있었다며, 직원 수준 권한을 가진 외부 평가자 상주는 좋은 방안이고 OpenAI도 도입하겠다고 했어요.

일론 머스크(Elon Musk) xAI CEO는 에세이를 인용하며 아모데이의 말이 맞다고 적었습니다. 데미스 하사비스(Demis Hassabis) Google DeepMind CEO는 방향에는 동의하되 세부는 다듬어야 한다며, DeepMind가 따로 제안했던 프런티어 AI 업계 표준 기구를 다시 꺼냈어요.

미국 정부는 반대 입장을 분명히 했습니다. 도널드 트럼프(Donald Trump) 대통령은 9월 13일 아일랜드 골프 리조트에서 기자들에게 경고가 과장됐다며 AI에서 이기는 쪽이 전부를 가져간다고 말했어요. 대통령 과학기술자문회의 공동의장 데이비드 삭스(David Sacks)는 올트먼과 아모데이를 향해 할 테면 해보라며, 연구실 안에서 그들이 무엇을 보고 있다는 것인지 모르겠다고 반응했습니다.

중국 외교부도 9월 14일 반발했습니다. 궈자쿤 대변인은 공포 조장과 진영 대결, 악의적 경쟁이 글로벌 AI 거버넌스를 해칠 뿐이라고 했어요. 에세이가 중국의 기술 추격을 위협으로 규정하고 반도체 수출 통제 유지를 요구한 대목을 겨냥한 반응입니다.

![OpenAI 로고](/assets/images/ai/amodei-pace-the-frontier/05-openai-wordmark-mono.webp)
*OpenAI 로고 — 출처: OpenAI*

## 반도체주 급락과 클라우드 기업 반등

9월 14일 증시가 곧바로 반응했습니다. 미국에서 필라델피아 반도체 지수가 5.9% 내렸고 NVIDIA 3.4%, Micron 5.3%, Broadcom과 AMD도 각각 4% 넘게 빠졌어요. 나스닥 종합지수는 0.6% 하락으로 마쳤습니다.

대형 클라우드 기업은 반대로 올랐습니다. 포춘에 따르면 Alphabet 2%, Microsoft 1.6%, Meta 1.4% 상승이었어요. 개발 속도가 늦춰지면 신규 데이터센터 투자가 줄어 반도체 제조사에는 악재지만, 이미 연산 자원을 확보해 둔 쪽에는 유리하다는 계산입니다.

국내 낙폭이 더 컸습니다. 코스피에서 삼성전자가 4.05%, SK하이닉스가 6.35% 떨어졌어요. 국내 언론은 중동 정세에 따른 유가 부담과 함께 이번 속도조절론을 주된 원인으로 짚었습니다.

![9월 14일 주요 반도체주 하락폭](/assets/images/ai/amodei-pace-the-frontier/06-chart-chipstocks.webp)
*9월 14일 주요 반도체주 하락폭 — 출처: Reuters·한국경제 보도 수치 기반 자가 렌더*

## 중요한 이유

한국에서 가장 먼저 영향을 받는 곳은 반도체입니다. AI 데이터센터용 메모리는 국내 최대 수출 품목이라, 모델 개발 속도가 조절되면 데이터센터 투자가 언제까지 이어질 것인가 하는 물음이 그대로 수출 전망이 돼요.

산업계 시각은 갈립니다. 머니투데이가 9월 15일 전한 인터뷰에서 한 대기업 임원은 최근 투자가 과했던 면이 있다면서도 중국이 쫓아오는 상황에서 개별 기업이 먼저 멈출 수는 없다고 했어요. 다른 관계자는 속도 조절 규제가 후발 주자의 추격 기회를 가로막는 요인이 될 수 있다고 봤습니다.

제도 측면에서는 이미 겹치는 부분이 있습니다. 국내는 **인공지능 발전과 신뢰 기반 조성 등에 관한 기본법(AI 기본법)**이 2026년 1월 22일부터 시행 중이고, 학습에 쓴 누적 연산량이 **10²⁶ FLOP** 이상인 대규모 AI 시스템 운영 사업자에게 안전성 확보 의무를 지웁니다. 능력이 일정 선을 넘으면 별도 의무가 붙는 구조라, 아모데이가 말한 점검점과 발상이 같고, 과태료는 1년 계도 기간을 둬 2027년 1월까지 유예돼 있어요.

차이도 분명합니다. AI 기본법의 기준선은 연산량이라는 투입값이고, 아모데이가 제안한 점검점은 모델이 실제로 보이는 능력이에요. 그가 요구한 외부 평가자 상주에 해당하는 조항은 국내법에 없습니다.

속도를 늦추자고 말하는 쪽은 현재 선두 기업들이고, 이들이 정한 개발 속도는 뒤따르는 기업의 추격 속도를 함께 정하게 돼요.

CNBC는 이 에세이가 Anthropic의 나스닥 상장 준비와 겹친 시점에 나왔다는 점을 짚었습니다. 관계자들이 전한 상장 목표 기업가치는 약 2,800조 원(2조 달러)으로, 직전 비공개 투자 라운드에서 인정받은 1,351조 원(9,650억 달러)보다 높은 수준이에요.

## 앞으로 주목할 점

- Anthropic과 OpenAI가 어떤 기관을 외부 평가자로 들이고 첫 공개 보고서가 언제 나오는지
- 2단계에 필요한 반독점법 예외에 미국 정부가 실제로 움직일지
- 미중 고위급 회담에서 AI 안전이 공식 의제로 올라갈지
- 반도체주가 되돌아올지, 빅테크 데이터센터 투자 계획이 바뀔지
- AI 기본법 계도 기간이 끝나는 2027년 1월까지 안전성 확보 의무의 세부 기준이 어떻게 잡힐지

![6월 제안과 9월 에세이 비교 요약](/assets/images/ai/amodei-pace-the-frontier/07-items-summary.webp)
*6월 제안과 9월 에세이 비교 요약 — 출처: 본문 요약 카드 · 자가 렌더*

## 참고 출처

- [[Dario Amodei] We Must Pace the Frontier (09.12, 3단계 계획·시간 계산 원문)](https://darioamodei.com/post/we-must-pace-the-frontier)
- [[Axios] Anthropic, OpenAI CEOs call for slowdown in AI development (09.12)](https://www.axios.com/2026/09/12/anthropic-ai-amodei-pacing)
- [[SiliconANGLE] Sam Altman and Elon Musk back Dario Amodei's call to slow down the frontier of AI development (09.13)](https://siliconangle.com/2026/09/13/sam-altman-and-elon-musk-back-dario-amodeis-call-to-slow-down-the-frontier-of-ai-development/)
- [[Business Standard] From AI race to AI brakes: Why Amodei, Altman and Musk want a slowdown (09.14)](https://www.business-standard.com/technology/tech-news/why-altman-musk-and-amodei-want-to-slow-the-ai-race-126091400087_1.html)
- [[KPBS] Anthropic and OpenAI CEOs call for AI development to slow down (09.12)](https://www.kpbs.org/news/science-technology/2026/09/12/anthropic-and-openai-ceos-call-for-ai-development-to-slow-down)
- [[KPBS] Trump downplays calls for AI slowdown (09.13)](https://www.kpbs.org/news/politics/2026/09/13/trump-downplays-calls-for-ai-slowdown)
- [[TNGlobal] China foreign ministry labels AI-slowdown suggestion 'fear-mongering' (09.15)](https://technode.global/2026/09/15/china-foreign-ministry-labels-ai-slowdown-suggestion-fear-mongering-after-anthropics-founder-amodei-warns/)
- [[Reuters via Investing.com] Wall Street ends down, calls for AI slowdown pummel chipmakers (09.14)](https://www.investing.com/news/economy-news/ai-warnings-knock-nasdaq-futures-pressure-tech-stocks-4898987)
- [[Fortune] Wall Street's AI doomsday trade is here: chipmakers sink while hyperscalers gain (09.14)](https://fortune.com/2026/09/14/ai-slowdown-stocks-nvidia-meta/)
- [[CNBC] What Amodei's AI slowdown could mean for Anthropic's imminent IPO (09.14, 상장 목표 기업가치)](https://www.cnbc.com/2026/09/14/anthropic-walks-tightrope-to-nasdaq-pushing-slowdown-and-pursuing-ipo.html)
- [[한국경제] AI 속도조절론 부상…삼전닉스 동반 급락 (09.14)](https://www.hankyung.com/article/2026091422756)
- [[머니투데이] 불붙은 AI속도조절론…업계 "걱정은 되지만 추격기회는 잡아야" (09.15)](https://www.mt.co.kr/tech/2026/09/15/2026091510470749921)
- [[국가법령정보센터] 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 (고영향·안전성 확보 의무 조항)](https://www.law.go.kr/lsInfoP.do?lsiSeq=268543)
- [[Lexology] 인공지능기본법 시행령에 이어 고시 및 가이드라인 초안 공개 (10²⁶ FLOP 기준·계도기간)](https://www.lexology.com/library/detail.aspx?g=b5c0170e-2bdb-4a3a-bba9-5cd5af697e61)
- [[OpenAI] The Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)
- 환율: 1달러 ≈ 1,400원 기준 환산
