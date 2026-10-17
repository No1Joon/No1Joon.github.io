---
title: "Citizen Lab — 광고만 봐도 감염되는 제로클릭 스파이웨어 첫 확인"
description: "표적 광고 경매를 거쳐 클릭 없이 스파이웨어를 심은 AdFection 공격의 경위와 광고 ID 를 줄이는 대응을 정리합니다"
date: 2026-10-16
category: Tech
subcategory: News
tags: [spyware, zero-click, malvertising, citizen-lab, ad-tech]
image: /assets/og/2026-10-16-adfection-zero-click-ad-spyware.png
---

광고 하나를 화면에 띄웠을 뿐인데 기기가 감염됐습니다. 캐나다 토론토대 Citizen Lab이 2026년 10월 15일 낸 보고서 *Exposing AdFection*은 표적 광고 경매를 거쳐 클릭 없이 스파이웨어를 설치한 공격을 처음으로 기술적으로 확인했어요. 보고서는 이 수법에 **AdFection**이라는 이름을 붙였고, 알자지라 기기 최소 45대가 2024~2025년에 이 경로로 공격받았다고 밝혔습니다.

![스파이웨어 업체와 광고 생태계를 잇는 Discover-Tech 구조](/assets/images/tech/adfection-zero-click-ad-spyware/01-hero.webp)
*스파이웨어 업체와 광고 생태계를 잇는 Discover-Tech 구조 — 출처: Citizen Lab*

## 사건 경과

Citizen Lab은 이스라엘 광고 업체 Discover-Tech가 자체 플랫폼 **Controlium**으로 광고 경매에 참여하고, 특정 기기에 광고가 표시될 때 공격 코드를 전송했다고 발표했어요. 같은 날 광고 보안 업체 Confiant도 같은 활동에 대한 조사를 함께 냈습니다.

- 보고서 번호: Citizen Lab Report 195, 저자 Bill Marczak·John Scott-Railton·Ron Deibert 등 6명
- 확인된 피해: 알자지라 기기 최소 45대, 2024~2025년 공격
- 연결된 스파이웨어: Candiru(현재 이름 Integrity Labs)와의 연관성은 확신도가 높음, Bindecy도 Controlium 사용
- 노출 범위: 4개월 동안 앱 75,373개·웹사이트 120,768개에 Discover-Tech 광고가 실림
- 업계 인증: Google·IAB Europe 인증 업체 목록에 2020~2026년 올라 있었음

TechCrunch는 이를 정부가 쓰는 제로클릭 스파이웨어가 온라인 광고로 전달된 첫 확인 사례라고 보도했어요. 제로클릭(zero-click)은 링크를 누르거나 파일을 열지 않아도 감염되는 공격을 말합니다.

## 공격이 성립하는 조건

이 공격은 특정 표적 기기만 대상으로 해요. 보고서가 밝힌 구조로는 공격자가 표적 기기의 **광고 ID나 IP 주소**를 먼저 알고 있어야 합니다. 서버가 광고를 받은 기기를 확인해 표적이면 JavaScript 코드를 응답으로 반환하고, 표적이 아니면 아무런 코드를 반환하지 않아요. 그래서 표적이 아닌 사용자에게는 평범한 쇼핑 광고로만 보이고, 광고 거래소도 악성 코드를 탐지할 수 없었습니다.

| 구분 | 확인된 것 | 확인 안 된 것 |
| :--- | :--- | :--- |
| 표적 선별 | **광고 ID·쿠키 ID·IP** | 번호 수집 경로 일부 |
| 감염 기기 | 알자지라 Windows 등 45대 | 그 밖의 감염 수 |
| 노출 기관 | NATO·UN·EU 기관망 | <mark>노출 = 감염 여부</mark> |
| 사용한 취약점 | Candiru 과거 제로데이 | AdFection 공격 사슬 |

광고가 떴다는 기록이 곧 감염을 뜻하지는 않는다는 점을 보고서도 따로 강조했어요. NATO·UN·EU 기관과 20여 개국 정부망, 반도체·방산 기업에서 광고 노출 기록이 나왔지만, 실제 감염이 확인된 것은 알자지라 사례입니다.

## 광고 경매를 통한 스파이웨어 전달 방식

![광고주에서 사용자까지 이어지는 온라인 광고 경매 구조](/assets/images/tech/adfection-zero-click-ad-spyware/02-fig.webp)
*광고주에서 사용자까지 이어지는 온라인 광고 경매 구조 — 출처: Citizen Lab*

웹페이지나 앱이 광고 지면을 입찰에 등록하면 0.1초 안팎의 실시간 입찰(RTB, Real-Time Bidding)이 진행돼요. 이때 광고 거래소는 입찰 참가자에게 기기 종류·위치·광고 ID·IP 같은 정보를 함께 보냅니다. Discover-Tech는 이 입찰 정보로 표적 기기를 찾아 낙찰을 받고, 광고 안에 자체 서버(NOAS)에 요청을 보내는 스크립트 태그를 넣었어요.

### 감염까지 걸린 시간

![광고 표시부터 C&C 연결까지 Candiru 감염 시간 순서](/assets/images/tech/adfection-zero-click-ad-spyware/03-fig.webp)
*광고 표시부터 C&C 연결까지 Candiru 감염 시간 순서 — 출처: Citizen Lab*

보고서가 재구성한 순서는 이렇습니다. 0초에 광고가 표시되면서 스크립트가 로드되고, 1~2초 사이 표적 기기의 브라우저가 1×1 크기의 iframe을 불러와 Candiru 검증 서버에 연결돼요. 5~10초 뒤 검증을 통과한 기기가 익스플로잇(exploit, 취약점을 공격하는 코드) 서버에 접속하고, 1~3분 안에 스파이웨어가 C&C(명령 제어) 서버와 통신을 시작합니다. 사용자가 한 일은 광고가 있는 페이지를 연 것뿐이에요.

Citizen Lab은 Candiru 인프라로 2022~2026년 사이 도메인 305개, IP 319개를 찾아냈습니다. 알자지라에서 나온 표본은 Candiru가 2021년에 쓴 감염 사슬과 지속성·난독화 특징이 같았어요.

## 숫자로 보는 규모

![입찰 37.7억 건에서 감염 확인 45대까지 규모 비교](/assets/images/tech/adfection-zero-click-ad-spyware/04-chart.webp)
*입찰 37.7억 건에서 감염 확인 45대까지 규모 비교 — 출처: Citizen Lab Report 195 기반 자가 렌더*

Discover-Tech가 쓴 입찰 플랫폼 MyDSP는 2026년 3~6월에 약 37억 7천만 건의 광고 노출에 입찰했고 그중 약 11.7%를 낙찰받았어요. 입찰의 약 19%에는 공격용 NOAS 스크립트 태그가 실려 있었습니다. 입찰 건수 기준으로 입찰 시도가 많았던 국가는 예멘·파키스탄·몬테네그로·브라질·멕시코 순이었고, Citizen Lab의 MyDSP 기록 분석에서는 인구 대비 입찰 건수가 몬테네그로에서 가장 높았어요.

Citizen Lab은 광고 대부분을 실제 광고주 없이 Discover-Tech가 직접 집행한 것으로 추정했습니다. AliExpress·UGREEN 할인 광고처럼 꾸몄지만 두 회사와 실제 광고 계약은 찾지 못했고, 구매 전환도 한 건도 없었어요.

![CBC·Yahoo 웹사이트와 스도쿠 앱에 실린 Discover-Tech 광고](/assets/images/tech/adfection-zero-click-ad-spyware/05-fig.webp)
*CBC·Yahoo 웹사이트와 스도쿠 앱에 실린 Discover-Tech 광고 — 출처: Citizen Lab*

캐나다 공영방송 CBC 사이트, Yahoo, Android 스도쿠 게임 앱처럼 평범한 곳에 이런 광고가 실렸습니다.

## 업계 대응

![Google 로고](/assets/images/tech/adfection-zero-click-ad-spyware/06-logo-google.webp)
*Google 로고*

Google과 IAB Europe은 2026년 10월 초 인증 업체 목록에서 Discover-Tech를 삭제했고, Google은 광고 거래소 접근도 차단했어요. 광고 기술 업체 Beeswax는 Discover-Tech의 플랫폼 이용을 중단시켰고, Vungle(Liftoff)은 검토 기간 동안 플랫폼 접근을 일시 중지했으며, Eskimi는 계정과 도메인을 차단했습니다. Bindecy·Intelos·Xandr는 보고서 마감까지 답하지 않았어요.

Citizen Lab은 업계 인증 절차의 문제를 지적했습니다. Discover-Tech는 약 6년 동안 스파이웨어와 연결돼 있었는데도 Google의 인증 외부 업체 목록 약 2,400곳과 IAB 글로벌 업체 목록 약 1,000곳에 등재돼 있었어요. 보고서는 광고 업계에 실시간 악성 광고 탐지, 거래 상대 신원 확인(KYC) 의무화, 인증 업체 외부 감사를 권고했습니다.

Candiru는 2021년 11월 미국 상무부 제재 목록에 오른 업체입니다. 그해 Microsoft는 Candiru 피해자를 10개국 최소 100명으로 집계했어요.

## 국내 접점

![개인정보보호위원회 로고](/assets/images/tech/adfection-zero-click-ad-spyware/07-logo-pipc.webp)
*개인정보보호위원회 로고*

보고서에는 한국 사례나 국내 광고망 언급이 없습니다. 아시아에서는 부탄·인도네시아·말레이시아·파키스탄·태국 정부망 노출이 언급됐어요. 국내 사용자도 같은 글로벌 광고 거래소를 거쳐 광고를 받기 때문에 구조상 무관하다고 볼 수는 없지만, 국내 피해가 확인되지는 않았습니다.

국내에서 맞춤형 광고에 쓰이는 정보는 개인정보보호위원회가 **행태정보**로 다뤄 왔어요.

2022년 9월 개인정보위는 동의 없이 다른 사이트 행태정보를 맞춤형 광고에 쓴 Google에 692억 원, Meta에 308억 원의 과징금을 매겼고(2025년 1월 서울행정법원이 처분이 정당하다고 판결), 2024년 1월에는 맞춤형 광고에 쓰이는 행태정보 보호 정책 방안을 발표했습니다.

이 규제는 광고 정보의 수집·동의를 다루고, 입찰 정보가 공격 표적 선별에 쓰이는 문제까지 다루지는 않아요. Citizen Lab은 각국 규제 당국에 입찰 과정에서 오가는 개인정보를 줄이고 정부 기기의 광고 ID를 비활성화하라고 권고했습니다.

## 지금 할 수 있는 조치

![광고 경유 공격을 줄이는 조치 다섯 가지](/assets/images/tech/adfection-zero-click-ad-spyware/08-items.webp)
*광고 경유 공격을 줄이는 조치 다섯 가지 — 출처: Citizen Lab 권고 기반 자가 렌더*

광고 ID는 표적을 고르는 첫 단서라 삭제하거나 사용을 제한하면 이 경로로 특정되기 어려워져요. Android에서는 설정의 광고 메뉴에서 광고 ID를 삭제할 수 있고, 삼성 갤럭시는 보안 및 개인정보 보호 > 기타 개인정보 보호 설정 > 광고에 있습니다. iPhone은 설정 > 개인정보 보호 및 보안 > 추적에서 앱이 추적을 요청하도록 허용을 끄면 됩니다. 메뉴 이름은 기기와 버전에 따라 조금 달라요.

Citizen Lab은 신뢰할 수 있는 광고 차단 확장 프로그램, 추적을 막는 브라우저, 공유기나 DNS 단위의 광고 차단을 권했습니다. 다만 IP 주소만으로도 표적을 고를 수 있어서 광고 ID를 삭제해도 공격을 완전히 차단할 수는 없어요. 운영체제와 브라우저를 최신으로 유지해 알려진 취약점을 막는 것도 함께 해야 합니다.

일반 사용자가 이 공격으로 감염됐는지 스스로 확인할 방법은 없습니다. 기자·인권 활동가·공무원처럼 국가 단위 공격의 표적이 될 수 있는 사람은 Citizen Lab 같은 전문 기관에 기기 점검을 요청하라고 보고서는 권했어요. 국내에서 해킹이 의심되면 KISA 118 상담센터에 문의할 수 있습니다.

🔗 링크 첨부 - https://www.boho.or.kr/kr/main.do

## 앞으로 주목할 점

- Citizen Lab이 예고한 후속 보고서: 이동통신사 취약점으로 광고 ID와 전화번호를 연결해 온 DARK CARTOGRAPHER 분석
- 응답하지 않은 Bindecy·Intelos·Xandr의 입장
- 각국 규제 당국의 Discover-Tech·Candiru 조사 착수 여부
- 광고 거래소의 인증 업체 심사 절차 변화

## 참고 출처

- [[Citizen Lab] Exposing AdFection, Report 195 (2026-10-15, 수치·구조·권고 전체)](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/)
- [[TechCrunch] Citizen Lab says governments are abusing online ads to hack people with zero-click spyware (2026-10-15)](https://techcrunch.com/2026/10/15/citizen-lab-says-governments-are-abusing-online-ads-to-hack-people-with-zero-click-spyware/)
- [[The Register] Spyware vendors found a way to make targeted ads even worse (2026-10-15)](https://www.theregister.com/security/2026/10/15/spyware-vendors-found-a-way-to-make-targeted-ads-even-worse/5303334)
- [[아주경제] 구글·메타에 1000억원 과징금, 개인정보위 행태정보 무단 수집 제재 (2022-09-14)](https://www.ajunews.com/view/20220914131004945)
- [[한경비즈니스] 구글 692억·메타 308억 과징금, 서울행정법원 처분 정당 판결 (2025-01)](https://magazine.hankyung.com/business/article/202501316327b)
