---
title: "NVIDIA RTX Spark 노트북 국내 출시 — 500만 원대부터"
description: "CPU·GPU 를 한 칩에 묶고 최대 128GB 메모리를 공유하는 RTX Spark 노트북의 구조와 국내 출시 가격을 정리합니다"
date: 2026-10-18
category: Tech
subcategory: News
tags: [nvidia, rtx-spark, laptop, unified-memory, windows-on-arm]
image: /assets/og/2026-10-18-nvidia-rtx-spark-korea-launch.png
---

NVIDIA의 Windows 노트북용 칩 **RTX Spark**가 국내에 출시됐어요

판매는 2026년 10월 16일 시작했습니다

CPU와 GPU를 하나의 칩에 통합해 최대 128GB 메모리를 공유하는 구조예요

국내 가격은 32GB 모델이 <mark>500만 원대</mark>부터입니다

![NVIDIA RTX Spark 보도자료 히어로 이미지](/assets/images/tech/nvidia-rtx-spark-korea-launch/01-hero-rtxspark.webp)
*NVIDIA RTX Spark 보도자료 히어로 이미지 — 출처: NVIDIA*

## 출시 내용

![NVIDIA 로고](/assets/images/tech/nvidia-rtx-spark-korea-launch/02-logo-nvidia.webp)
*NVIDIA 로고*

NVIDIA는 10월 16일 RTX Spark 노트북이 전 세계에서 판매를 시작했다고 발표했어요

6월 컴퓨텍스 2026에서 칩을 공개한 지 넉 달 만이에요

1차 출시 제품은 6개 제조사의 9개 모델입니다

| 제조사 | 모델 |
| :--- | :--- |
| ASUS | ProArt P14·**ProArt P16** |
| Dell | XPS 16 |
| HP | OmniBook Ultra·OmniBook X 14 |
| Lenovo | Yoga Pro 9n |
| Microsoft | Surface Laptop Ultra |
| MSI | Prestige N16 Flip AI+·**Prestige N16** |

국내에는 <u>ASUS·MSI 제품이 먼저</u> 출시됐어요

미국 시작가는 364만 원(2,599달러)입니다

## 사양 풀이

![RTX Spark 노트북과 11월 출시 예정 소형 데스크톱](/assets/images/tech/nvidia-rtx-spark-korea-launch/03-rtxspark-laptop-desktop.webp)
*RTX Spark 노트북과 11월 출시 예정 소형 데스크톱 — 출처: NVIDIA*

칩 이름은 **N1X**예요

AI 워크스테이션 DGX Spark의 **GB10**을 Windows 노트북용으로 사양을 조정한 칩이에요

| 항목 | N1X |
| :--- | :--- |
| CPU | Arm 20코어 (X925 10 + A725 10) |
| GPU | Blackwell, CUDA 코어 6,144개 |
| 메모리 | LPDDR5X <mark>최대 128GB</mark> |
| 메모리 대역폭 | 300GB/s |
| AI 연산 | FP4 1페타플롭스 |
| 소비전력 | 약 80W |

CPU는 MediaTek이 함께 설계했어요

CPU와 GPU가 메모리를 공유하는 통합 메모리 구조예요

큰 AI 모델의 가중치를 노트북 메모리에 모두 적재할 수 있어요

NVIDIA는 740억 파라미터 모델 Nemotron 3.5 Bolt를 예로 들었어요

24GB 메모리에 맞게 크기를 줄여 노트북에서 직접 실행합니다

코어를 18개로 줄인 하위 칩 N1도 있지만 출시 초기에는 노트북에만 탑재돼요

## 국내 가격

![RTX Spark 노트북 국내 메모리별 가격대 범위 막대](/assets/images/tech/nvidia-rtx-spark-korea-launch/04-chart.webp)
*RTX Spark 노트북 국내 메모리별 가격대 범위 막대 — 출처: 지디넷코리아·디일렉 보도 기반 자가 렌더*

32GB는 500만 원대, 64GB는 700만 원대, 128GB는 <mark>900만 원대</mark>예요

디일렉 보도로는 MSI Prestige N16이 579만 9,000원으로 국내 최저가입니다

미국 시작가 364만 원과 200만 원 넘게 차이 나요!!

미국 시작가는 24GB 구성 기준이라 국내 32GB 모델과 직접 비교하기는 어려워요

NVIDIA는 가격이 높은 이유로 메모리 가격 상승을 원인으로 들었어요

한 관계자는 <u>메모리 값이 이렇게 오를 줄 몰랐다</u>고 했습니다

## 리뷰 성능

![3DMark Time Spy Extreme 점수 비교 막대 차트](/assets/images/tech/nvidia-rtx-spark-korea-launch/05-chart-3dmark.webp)
*3DMark Time Spy Extreme 점수 비교 막대 차트 — 출처: Tech Times 리뷰 종합 기반 자가 렌더*

해외 리뷰는 10월 15~16일에 일제히 나왔어요

평가는 **GPU 성능은 높지만 CPU 성능은 상대적으로 낮다**로 모였습니다

[그래픽]
3DMark Time Spy Extreme 6,060점, Ryzen AI Max+ 395보다 29% 높음

[게임]
Cyberpunk 2077 1080p 울트라 약 70fps, QHD 약 47fps

[CPU]
멀티코어는 Apple M4 Pro 수준, 싱글코어는 M5 세대보다 성능이 낮음 (HotHardware)

[배터리]
동영상 재생 14시간 35분 (HotHardware)

NVIDIA는 1440p에서 최신 게임 100fps 이상을 내세웠지만 리뷰 수치는 그보다 낮아요

메모리 대역폭 300GB/s는 RTX 5070 노트북 GPU의 최대 672GB/s에 못 미칩니다

<mark>그래픽 점수는 비교한 내장 칩보다 높고, 게임 성능은 외장 GPU가 여전히 높습니다</mark>

## 호환성과 남은 일정

![Microsoft 로고](/assets/images/tech/nvidia-rtx-spark-korea-launch/06-logo-microsoft.webp)
*Microsoft 로고*

RTX Spark 노트북은 **Windows on Arm**으로 돌아가요

x86용 프로그램은 Microsoft의 에뮬레이터 Prism을 거쳐 실행돼 성능이 다소 저하돼요

게임 실행을 제한하는 주요 요인은 **안티치트 호환성**이에요

출시 당일 Arm용 안티치트를 갖춘 게임은 카운터 스트라이크 2·포트나이트 등이에요

Arm 빌드가 없는 커널 안티치트 게임은 Prism으로도 실행되지 않아요!!

EA 안티치트도 아직 Arm을 지원하지 않고, 콜 오브 듀티는 2027년에 지원될 예정이에요

리그 오브 레전드·배틀그라운드는 발표된 지원 목록에 없어요

즐겨 하는 게임이 있다면 <u>구매 전 꼭 확인</u>하세요~

개발 환경은 Windows on Arm용 PyTorch-CUDA 빌드가 처음 나왔어요

인기 Python 패키지 1만 5,000개 중 97%가 Arm 버전을 갖췄습니다

같은 칩을 탑재한 소형 데스크톱은 11월에 출시돼요

## 참고 출처

- [[NVIDIA Newsroom] RTX Spark PC 판매 시작 발표 (2026-10-16)](https://nvidianews.nvidia.com/news/nvidia-rtx-spark-pcs-available-today-a-new-beginning-for-windows-pcs)
- [[NVIDIA Developer Blog] RTX Spark 개발 환경·로컬 모델·11월 데스크톱 (2026-10)](https://developer.nvidia.com/blog/code-test-and-deploy-on-one-machine-with-nvidia-rtx-spark)
- [[지디넷코리아] 국내 출시 행사와 메모리별 가격대 (2026-10-17)](https://zdnet.co.kr/view/?no=20261017092606)
- [[디일렉] 국내 최저가 MSI Prestige N16 579만 9,000원·N1X 사양 (2026-10-16)](https://www.thelec.kr/news/articleView.html?idxno=63851)
- [[Tech Times] 해외 리뷰 종합, 3DMark·게임·배터리·안티치트 (2026-10-16)](https://www.techtimes.com/articles/329104/20261016/rtx-spark-reviews-are-class-leading-gpu-meets-aging-cpu-cores-launch.htm)
- [[Windows Central] 일주일 사용 리뷰 (2026-10-16)](https://www.windowscentral.com/hardware/nvidia/rtx-spark-review-benchmarks-2026)
- 환율: 1달러 ≈ 1,400원 기준 환산
