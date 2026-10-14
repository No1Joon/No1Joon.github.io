---
title: "BC카드, ChatGPT 에서 페이북 쇼핑적립 비교 — 연결 전에 알 것"
description: "ChatGPT 대화 안에서 적립률을 비교하는 BC카드 퍼스널 쇼퍼의 동작과 연결할 때 전달되는 정보를 정리합니다"
date: 2026-10-13
category: AI
subcategory: News
tags: [chatgpt, bc-card, chatgpt-apps, shopping, privacy]
image: /assets/og/2026-10-13-bc-card-chatgpt-shopping.png
---

BC카드가 2026년 10월 7일 ChatGPT 안에서 상품을 찾다가 페이북 쇼핑적립 혜택을 바로 확인하고 구매로 넘어가는 퍼스널 쇼퍼 서비스를 출시했어요. 국내 카드사가 ChatGPT 대화에 혜택 안내 기능을 통합한 첫 사례입니다.

한 번 연결해 두면 페이북 앱을 따로 열지 않아도 적립률을 비교할 수 있어요. 대신 연결하는 순간 ChatGPT 대화의 일부 맥락이 BC카드 쪽으로 전달될 수 있어서, 무엇이 공유되는지를 알고 연결하는 편이 좋습니다.

![BC카드 로고](/assets/images/ai/bc-card-chatgpt-shopping/01-logo-bccard.webp)
*BC카드 로고*

## 서비스 흐름

![ChatGPT 대화 속에서 쇼핑몰별 적립률을 비교하는 개념 컷](/assets/images/ai/bc-card-chatgpt-shopping/02-agy.webp)
*ChatGPT 대화 속에서 쇼핑몰별 적립률을 비교하는 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

BC카드 발표에 따르면 흐름은 세 단계예요. 페이북 안내에 따라 ChatGPT와 페이북을 처음 한 번 연결하고, 그 뒤로는 ChatGPT에서 상품을 검색하거나 구매를 고민하다 할인·적립에 관심을 보이면 페이북 쇼핑적립 정보가 대화에 함께 표시됩니다. 쇼핑몰을 선택하면 페이북의 쇼핑적립 화면으로 이동하고, 거기서 구매하면 기존 페이북 쇼핑적립과 같은 리워드를 지급받아요.

| 단계 | 어디서 | 하는 일 |
| :--- | :--- | :--- |
| 1 | 페이북·ChatGPT | 최초 1회 연결 |
| 2 | ChatGPT | 상품 검색 중 <mark>적립률 비교</mark> |
| 3 | 페이북 | 쇼핑적립 화면에서 구매 |

적립 대상 상품이면 최대 3개 제휴 쇼핑몰의 적립률을 나란히 표시해 구매할 쇼핑몰을 선택할 수 있어요. 상품권·기프티콘처럼 원래 쇼핑적립에서 제외되는 상품에는 정보가 표시되지 않습니다. 결제와 적립은 ChatGPT가 아니라 페이북 화면에서 이뤄지고, ChatGPT 안에서 결제까지 완료되는 구조는 아니에요.

출시 기념으로 10월 한 달 동안 ChatGPT를 거쳐 페이북 쇼핑적립 페이지에 들어온 고객 중 500명을 추첨해 페이북머니 3,000원을 지급합니다. 진입 한 번에 응모권 1장이 자동으로 부여되고 하루 최대 2장까지예요. BC카드는 앞으로 쿠폰·카드 할인·프로모션 같은 다른 페이북 혜택도 대화 안에서 확인할 수 있도록 확대하겠다고 밝혔습니다.

## ChatGPT에서 BC카드로 전달되는 정보

BC카드 보도자료와 언론 보도에는 연결할 때 어떤 정보가 공유되는지가 명시되지 않았어요. 기준이 되는 것은 OpenAI의 ChatGPT 앱 도움말입니다.

![OpenAI 도움말 What does ChatGPT share with apps 절](/assets/images/ai/bc-card-chatgpt-shopping/03-capture.webp)
*OpenAI 도움말 What does ChatGPT share with apps 절 — 출처: OpenAI*

도움말에 따르면 앱을 활성화하면 그 앱은 요청을 처리하는 데 필요한 맥락을 ChatGPT 대화에서 참조할 수 있어요. 메모리 기능을 활성화했다면 저장된 메모리 중 관련 내용도 참조할 수 있습니다. 여기에 웹사이트를 방문할 때 흔히 전달되는 IP 주소, 기기·브라우저 종류, 언어·지역 설정, IP 기준 대략적인 위치(시·지역 단위)도 앱이 확인할 수 있어요.

- 대화 맥락: 쇼핑 요청과 관련된 부분 (예: 찾는 상품, 예산)
- 메모리: 켜 둔 경우 관련 항목
- 접속 정보: IP, 기기·브라우저, 언어·지역, 대략 위치
- 처리 기준: 연결 전에 보여 주는 그 앱의 약관과 개인정보처리방침

연결 화면에서 이 문서를 확인하고, 쇼핑과 관계없는 건강·금융 정보는 별도 대화에서 다루면 공유 범위를 줄일 수 있어요.

ChatGPT Free·Plus·Go·Pro 사용자는 「모두를 위한 모델 개선」 설정이 활성화돼 있으면 앱에서 전달받은 정보가 OpenAI 모델 학습에 사용될 수 있다고 도움말에 적혀 있습니다. 적립률 정보가 학습에 쓰여도 문제 될 것은 적지만, 이 설정은 다른 앱 연결에도 똑같이 적용돼요.

## 연결 전에 확인할 것

![BC카드 ChatGPT 퍼스널 쇼퍼 연결 전 확인 정리 카드](/assets/images/ai/bc-card-chatgpt-shopping/04-items.webp)
*BC카드 ChatGPT 퍼스널 쇼퍼 연결 전 확인 정리 카드 — 출처: BC카드 발표·OpenAI 도움말 기반 자가 렌더*

연결을 해제하고 싶으면 ChatGPT 설정의 Plugins 메뉴에서 해당 앱을 선택해 연결을 해제하면 되고, 페이북 쪽에도 자체 해제 메뉴가 있을 수 있다고 OpenAI는 안내합니다. 앱 권한 설정은 ChatGPT가 앱을 사용하기 전에 매번 승인을 요청할지 정하는 것이라, 앱에 이미 부여한 접근 범위를 제한하지는 않아요. 접근 자체를 없애려면 연결을 끊어야 합니다.

BC카드 회원이 아니어도 페이북 회원이면 쇼핑적립을 쓸 수 있는지, 연결 동의 항목이 무엇인지는 공개 자료로 확인되지 않아 페이북 앱 공지에서 직접 확인해야 해요.

## 참고 출처

- [[뉴스핌] BC카드, 카드사 최초 ChatGPT 연계 쇼핑적립 서비스 출시 (2026-10-07)](https://www.newspim.com/news/view/20261007000582)
- [[더빅데이터] BC카드, 카드사 최초 ChatGPT 통한 퍼스널 쇼퍼 서비스 제공 (2026-10-07, 이벤트·담당자 발언)](https://www.thebigdata.co.kr/view.php?ud=202610070943199935df3c2a17b7_23)
- [[SBS Biz] BC카드, 카드사 최초 챗지피티 통한 쇼핑 서비스 제공 (2026-10-07)](https://biz.sbs.co.kr/amp/article/20000338675)
- [[OpenAI Help Center] Connected apps in ChatGPT (앱에 공유되는 정보, 연결 해제, 학습 사용, 본문 이미지 1점 출처)](https://help.openai.com/en/articles/11487775-connected-apps-in-chatgpt)
