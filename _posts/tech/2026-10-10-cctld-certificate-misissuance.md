---
title: "국가 도메인 운영사 침해로 Google 인증서 무단 발급"
description: "세 나라 ccTLD 운영 업체 침해로 Google·YouTube 인증서가 발급된 경위와 Chrome 의 차단, 자물쇠 표시의 한계를 정리합니다"
date: 2026-10-10
category: Tech
subcategory: News
tags: [tls-certificate, cctld, dns, chrome, web-pki]
image: /assets/og/2026-10-10-cctld-certificate-misissuance.png
---

가나(.gh), 시에라리온(.sl), 미국령 사모아(.as)의 국가 도메인을 운영하는 외부 업체가 침해되면서, 공격자가 Google·YouTube 도메인의 유효한 HTTPS 인증서를 발급받았어요. Google Chrome 팀은 2026년 10월 6일 경위를 공개하고 Chrome에서 해당 인증서를 차단했다고 밝혔습니다. Google 시스템이 침해된 사건은 아니고, Chrome 사용자는 따로 할 일이 없어요.

![Google 로고](/assets/images/tech/cctld-certificate-misissuance/01-logo-google.webp)
*Google 로고*

## 사건 경과

![ccTLD 하이재킹과 무단 인증서 발급 경과 타임라인](/assets/images/tech/cctld-certificate-misissuance/02-chart.webp)
*ccTLD 하이재킹과 무단 인증서 발급 경과 타임라인 — 출처: Google Chrome 팀 · CT 로그 조회 기반 자가 렌더*

Google에 따르면 공격자는 세 국가 도메인(ccTLD, 국가 코드 최상위 도메인)을 관리하는 외부 업체의 시스템을 장악하고, 그 아래 도메인들의 권한 DNS 레코드를 변경했어요. DNS 통제권을 확보한 공격자는 인증기관(CA)의 도메인 소유 확인을 정상적으로 통과했고, 그 결과 google.com.gh·youtube.sl 같은 Google 도메인의 인증서가 발급됐습니다.

- 대상 국가 도메인: .gh(가나)·.sl(시에라리온)·.as(미국령 사모아)
- 침해된 곳: 국가 도메인 운영을 맡은 제3자, 업체명 미공개
- 영향: Google 도메인 여러 개와 CT 로그에서 확인한 다른 글로벌 브랜드·온라인 서비스, 이름 미공개
- 공격자: 확인되지 않음

Google은 인증서를 발급한 인증기관이 잘못했다고 볼 근거는 없다고 밝혔어요. 인증기관은 DNS 기록이 바뀌었는지 알 방법 없이 정해진 절차대로 확인했을 뿐이라는 뜻이에요.

## 공격의 전제 조건

이번 공격이 성립하려면 공격자가 도메인의 DNS 기록을 변경할 수 있어야 했어요. 개인 PC나 브라우저를 노린 것이 아니라 인터넷 주소 체계의 상위 단계를 장악한 것이라, 일반 사용자가 차단할 방법은 없어요.

| 구분 | 이번 공격 | 일반 피싱 |
| :--- | :--- | :--- |
| 장악한 것 | **국가 도메인 운영 체계** | 비슷한 가짜 주소 |
| 주소창 주소 | 진짜 도메인 | 다른 도메인 |
| 자물쇠 표시 | 정상 표시 | 정상 표시 가능 |
| 사용자 판별 | 사실상 불가 | 주소 확인으로 가능 |

인증서가 실제로 사용자 공격에 악용됐는지는 공개되지 않았어요. 가짜 인증서로 사용자를 속이려면 사용자의 접속을 공격자 서버로 우회시켜야 하는데, DNS 통제권을 확보하고 있던 기간에는 그것도 가능했어요.

## CT 로그로 확인한 발급 내역

![Cert Spotter에서 youtube.sl 인증서를 조회한 터미널 화면](/assets/images/tech/cctld-certificate-misissuance/03-term-ct.webp)
*Cert Spotter에서 youtube.sl 인증서를 조회한 터미널 화면 — 출처: Cert Spotter CT 로그 조회 기반 자가 렌더*

모든 공개 HTTPS 인증서는 발급되면 인증서 투명성(CT, Certificate Transparency) 로그에 기록돼요. 2026년 10월 10일 Cert Spotter로 직접 조회해 보니, Google 자체 인증기관이 아닌 Let's Encrypt가 발급한 인증서가 아래처럼 기록돼 있었어요.

| 날짜 | 도메인 | 발급 CA |
| :--- | :--- | :--- |
| 9월 22일 | youtube.com.gh | Let's Encrypt |
| 9월 25일 | google.sl (2건) | Let's Encrypt |
| 9월 25일 | youtube.sl (2건) | **Let's Encrypt** |
| 9월 27일 | youtube.as | Let's Encrypt |

The Hacker News는 9월 22일부터 27일까지 Google·YouTube 이름으로 최소 12개 인증서가 발급됐고, 그중 11개가 Let's Encrypt, 1개가 ZeroSSL이었다고 전했어요. 직접 조회는 조회 한도 때문에 일부 도메인만 확인했어요.

## Chrome의 대응과 한계

![DNS 기록이 바뀌어 접속이 다른 서버로 향하는 개념 컷](/assets/images/tech/cctld-certificate-misissuance/04-agy-dns.webp)
*DNS 기록이 바뀌어 접속이 다른 서버로 향하는 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

Chrome은 긴급 차단 목록인 CRLSet으로 무단 인증서를 차단했고, 발급 기관과 함께 인증서를 폐기해 Chrome 밖의 프로그램도 보호하도록 했어요. CT 로그에서 확인한 다른 기관의 인증서도 먼저 차단하고, 연락 가능한 기관에는 통보했다고 해요.

Google은 두 가지 한계도 함께 적었습니다. 분석으로 영향받은 도메인을 모두 확인했다고 확신할 수 없고, Chrome의 조치는 Chrome이 아닌 브라우저 사용자를 안정적으로 보호하지 못한다는 점이에요. 그래서 브라우저 쪽 차단에만 의존하지 말고 도메인 소유자가 직접 감시하라고 권했어요.

장기적으로 Google은 인증서 유효기간과 도메인 확인 결과를 재사용하는 기간을 줄이는 방안을 CA/Browser Forum에서 추진하고 있어요.

## 도메인 운영자가 할 일

![도메인 운영자 조치 정리 카드](/assets/images/tech/cctld-certificate-misissuance/05-items.webp)
*도메인 운영자 조치 정리 카드 — 출처: Google Chrome 팀 권고 기반 자가 렌더*

Google이 권한 첫 번째 조치는 CT 로그 감시예요. 등록만 하고 사용하지 않는 도메인과 지역별 국가 도메인까지 포함해 발급 내역을 정기적으로 확인하고, .gh·.sl·.as 도메인을 가진 곳은 최근 발급 내역부터 살펴보라고 했어요.

두 번째는 CAA 레코드(DNS에 허용 인증기관을 적어 두는 기록)를 엄격하게 설정하는 것이에요. CAA는 DNS가 장악된 동안의 발급은 차단하지 못하지만, 인증기관은 한 번 완료한 도메인 확인 결과를 일정 기간 재사용할 수 있어서, 통제권을 회복한 뒤 특정 ACME 계정과 검증 방식(RFC 8657)으로만 발급되도록 제한하면 공격자가 기존 확인 결과를 재사용해 다시 발급받는 것을 차단할 수 있습니다. 쓰는 인증기관이 이런 계정·검증 방식 제한을 지원하는지도 함께 확인해야 해요.

이미 모르는 인증서를 발견했다면 그 인증서를 발급한 인증기관에 바로 폐기를 요청하는 것이 다음 순서예요. CT 로그 기록에는 발급 기관 이름이 함께 기록돼 있어 연락할 곳을 바로 알 수 있어요.

![한국인터넷진흥원 로고](/assets/images/tech/cctld-certificate-misissuance/06-logo-kisa.webp)
*한국인터넷진흥원 로고*

국내 .kr·.한국 도메인은 한국인터넷진흥원(KISA)이 관리하고 있어요. 이번 사건과 관련된 국내 피해는 보고되지 않았지만, 해외 지역 도메인을 함께 운영하는 국내 기업이라면 같은 방식으로 CT 로그를 확인할 수 있어요.

## 참고 출처

- [[Google] Chrome's response to recent ccTLD registry hijacks, 경위·CRLSet·권고 (2026-10-06)](https://blog.google/security/chromes-response-to-recent-cctld-registry-hijacks/)
- [[보안뉴스] 국가 도메인 운영 업체 침해와 구글 인증서 무단 발급 (2026-10-08)](https://www.boannews.com/news/articleView.html?idxno=146250)
- [[The Hacker News] 인증서 12개·발급 기간·CA별 개수 (2026-10)](https://thehackernews.com/2026/10/attackers-hijack-gh-sl-and-as.html)
- [[BleepingComputer] ccTLD 운영 침해와 Google 도메인 하이재킹 (2026-10)](https://www.bleepingcomputer.com/news/security/hackers-hijack-google-domains-after-breaching-cctld-registries/)
- [[Cert Spotter] CT 로그 발급 내역 조회 API (2026-10-10 조회)](https://api.certspotter.com/v1/issuances)
- [[IETF] RFC 8657, CAA 레코드의 계정·검증 방식 제한](https://www.rfc-editor.org/rfc/rfc8657)
