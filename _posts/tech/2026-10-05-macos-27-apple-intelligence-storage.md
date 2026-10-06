---
title: "macOS 27 Apple Intelligence 용량 — M3 Pro 에서 19.33GB"
description: "저장 공간 목록에 따로 표시되지 않는 Apple Intelligence 모델 파일의 실제 용량과 확인 방법, 삭제해도 다시 받는 이유를 정리합니다"
date: 2026-10-05
category: Tech
subcategory: Explainer
tags: [macos-27, apple-intelligence, storage, on-device-ai, mac]
image: /assets/og/2026-10-05-macos-27-apple-intelligence-storage.png
---

macOS 27.0.1이 설치된 MacBook Pro(M3 Pro, 통합 메모리 36GB)에서 Apple Intelligence가 차지한 용량을 확인해 보니 **19.33GB**였습니다. Apple 지원 문서가 이 사양의 Mac에 필요하다고 적은 최대 14GB보다 5.33GB 많아요.

이 숫자는 저장 공간 목록에 따로 표시되지 않고 macOS 항목에 포함돼 있습니다. 업데이트 뒤 저장 공간이 갑자기 줄었다면 여기부터 확인해 볼 만해요.

![macOS 정보 창에 표시된 Apple Intelligence 19.33GB](/assets/images/tech/macos-27-apple-intelligence-storage/01-photo-ai.webp)
*macOS 정보 창에 표시된 Apple Intelligence 19.33GB — 출처: 직접 촬영 (macOS 27.0.1)*

## 용량 확인 방법

![macOS 27 시스템 설정 저장 공간 화면](/assets/images/tech/macos-27-apple-intelligence-storage/02-photo.webp)
*macOS 27 시스템 설정 저장 공간 화면 — 출처: 직접 촬영 (macOS 27.0.1)*

저장 공간 화면의 목록에는 응용 프로그램·문서·사진 같은 항목만 있고 Apple Intelligence 줄은 없습니다.

① 시스템 설정 > 일반 > 저장 공간
② 목록 아래쪽 macOS 줄 오른쪽의 ⓘ 버튼
③ 열린 창의 Apple Intelligence 항목

측정한 Mac에서 macOS 항목은 31.88GB였고, 그중 19.33GB가 Apple Intelligence였습니다. macOS 항목의 60%가 Apple Intelligence 모델이었던 셈이에요.

256GB 모델 Mac이라면 19.33GB는 전체 용량의 7.6%입니다. 512GB에서는 3.8%라 체감이 덜하지만, 업데이트 직후 여유 공간이 빠듯했던 Mac은 이 차이로 저장 공간 경고가 뜰 수 있어요.

## 공식 수치와 실측 비교

![Mac 기기별 Apple Intelligence 용량 비교 차트](/assets/images/tech/macos-27-apple-intelligence-storage/03-chart.webp)
*Mac 기기별 Apple Intelligence 용량 비교 차트 — 출처: Apple·MacRumors·Ars Technica 보도와 직접 측정 기반 자가 렌더*

Apple 지원 문서는 M3 이상이고 통합 메모리 12GB 이상인 Mac에 최대 14GB, 그 밖의 Apple Intelligence 지원 Mac에 최대 8GB가 필요하다고 안내합니다.

| Mac | 용량 (GB) | 측정 |
| :--- | :--- | :--- |
| M1 MacBook Air | 약 14 | Ars Technica |
| M3 Pro MacBook Pro 36GB | **19.33** | 직접 측정 |
| M4 Pro Mac mini | 20.67 | MacRumors |
| M3 MacBook Air | 22.42 | Ars Technica |
| M3 Pro MacBook Pro | 24.35 | Reddit 사용자 |
| 기종 미상 (RC 버전) | <mark>30.16</mark> | Reddit 사용자 |

같은 M3 Pro MacBook Pro라도 19.33GB와 24.35GB로 5GB 차이가 났는데, 다운로드된 모델 구성이 기기마다 다른 것으로 보이고 Apple은 그 차이를 설명하지 않았어요.

## 모델 파일이 있는 곳

![모델 폴더 용량을 du로 측정한 터미널 화면](/assets/images/tech/macos-27-apple-intelligence-storage/04-term-du.webp)
*모델 폴더 용량을 du로 측정한 터미널 화면 — 출처: 직접 실행 (macOS 27.0.1)*

Apple Intelligence의 모델과 음성·번역 자산은 **/System/Library/AssetsV2** 아래 com_apple_MobileAsset_UAF로 시작하는 폴더에 있습니다. 같은 Mac에서 이 폴더들의 용량을 터미널에서 측정해 봤어요.

생성 모델이 포함된 **UAF_FM_GenerativeModels** 폴더는 macOS 보호 때문에 일반 권한으로 크기를 읽을 수 없었습니다. Siri 언어 이해 2.4GB, 번역 1.8GB, Siri 음성 합성 1.6GB처럼 읽을 수 있는 폴더도 있었지만, 이 폴더들이 19.33GB에 포함되는지는 Apple이 밝히지 않았어요.

## 꺼도 파일이 남는 이유

MacRumors는 Apple이 macOS 27과 iOS 27에서 Apple Intelligence를 끄는 토글을 없앴다고 보도했습니다. 그 결과 지원 기종이면 모델 파일이 저장 공간을 차지하게 된다는 설명이에요.

macOS 27 베타 시기의 iDownloadBlog 테스트에서는 Apple Intelligence를 비활성화한 Mac이 Wi-Fi로 모델 파일을 다시 다운로드했습니다. 끄는 것과 파일을 지우는 것이 별개라, 기능을 안 써도 용량은 그대로 남을 수 있어요.

## 비공식 정리 방법과 위험

![시스템 파일을 임의로 지울 때의 위험 개념 컷](/assets/images/tech/macos-27-apple-intelligence-storage/05-agy.webp)
*시스템 파일을 임의로 지울 때의 위험 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

Apple은 모델 파일을 지우는 공식 버튼을 제공하지 않았습니다. 해외 매체에 소개된 방법은 둘인데, 둘 다 공식 지원 밖이에요.

| 방법 | 효과 | 위험 |
| :--- | :--- | :--- |
| Mac·Siri 언어를 다르게 설정 | 모델 다운로드 차단 보고 | Siri 언어 불일치로 기능 제한 |
| 복구 모드에서 폴더 삭제 | 일시적으로 공간 확보 | **다시 다운로드됨**·시스템 손상 |

언어를 다르게 하는 방법은 Apple Intelligence가 Mac과 Siri 언어가 같을 때만 동작하는 조건을 이용합니다. 한국어는 2025년 3월 말 macOS 15.4부터 Apple Intelligence 지원 언어라, 시스템 언어와 Siri 언어를 둘 다 한국어로 쓰면 모델이 다운로드돼요.

복구 모드에서 시스템 볼륨의 폴더를 지우는 방법은 iDownloadBlog 테스트에서 저장 공간이 잠깐 확보됐다가 1분 뒤부터 모델이 다시 다운로드돼 결국 14GB 이상을 사용했습니다. 백업 없이 시스템 폴더를 지우면 업데이트 실패나 기능 오류로 이어질 수 있어 권하지 않아요.

## 현실적인 선택지

공식 경로 안에서 할 수 있는 일은 Apple Intelligence 외의 저장 공간을 정리하는 것입니다.

- 저장 공간 화면의 「권장 사항」에 표시되는 iCloud에 저장 등 정리 항목 적용
- 문서·응용 프로그램 항목의 ⓘ에서 큰 파일과 안 쓰는 앱 정리
- 개발자 항목이 큰 Mac은 Xcode 캐시·시뮬레이터 정리
- 새 Mac을 고른다면 Apple Intelligence 20GB 안팎을 시스템 사용량으로 반영해 용량을 계산

측정한 Mac은 시스템 데이터가 489.35GB로 Apple Intelligence의 25배였습니다. 저장 공간이 부족할 때 Apple Intelligence만 볼 것이 아니라 시스템 데이터와 개발자 항목부터 확인하는 편이 확보할 수 있는 양이 커요.

## 참고 출처

- [[Apple] 차세대 Apple Intelligence 사용하기 (기기별 필요 저장 공간)](https://support.apple.com/ko-kr/121115)
- [[MacRumors] Apple Intelligence Taking up 30GB+ on Some Macs Running macOS 27 (2026-09-23)](https://macrumors.com/2026/09/23/apple-intelligence-30gb-some-macs-macos-27)
- [[MacDailyNews] Apple Intelligence is eating up to 30GB on some Macs after macOS 27 (2026-09-25)](https://macdailynews.com/2026/09/25/apple-intelligence-is-eating-up-to-30gb-on-some-macs-after-macos-27/)
- [[iDownloadBlog] How to remove local Apple Intelligence files from Mac (2026-08-04)](https://www.idownloadblog.com/?p=1060545)
