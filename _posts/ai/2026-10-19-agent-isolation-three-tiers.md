---
title: "AI 에이전트 코드 격리 — 컨테이너·gVisor·마이크로VM 은 어디까지 막나"
description: "코딩 에이전트 실행 격리의 세 단계인 컨테이너·gVisor·마이크로VM 을 호스트 커널 접근 정도로 비교합니다"
date: 2026-10-19
category: AI
subcategory: Explainer
tags: [ai-agent, sandbox, container, gvisor, microvm]
image: /assets/og/2026-10-19-agent-isolation-three-tiers.png
---

코딩 에이전트는 코드를 쓰고 직접 실행까지 해요
그 코드가 어떤 환경에서 실행되느냐에 따라 사고가 났을 때 피해 범위가 달라집니다

에이전트 실행 격리는 흔히 **컨테이너, gVisor, 마이크로VM** 세 단계로 나눠요
세 방식의 차이는 결국 <mark>호스트 커널에 얼마나 직접 접근하느냐</mark>입니다

![한 겹씩 두꺼워지는 세 개의 투명 격리막 안에서 코드 블록이 실행되는 장면을 표현한 개념 컷](/assets/images/ai/agent-isolation-three-tiers/01-agy-3.webp)
*한 겹씩 두꺼워지는 세 개의 투명 격리막 안에서 코드 블록이 실행되는 장면을 표현한 개념 컷 — 출처: 개념 컷, agy 자가 생성*

## 실행 코드가 위험해지는 경우

격리 단계를 고르기 전에 무엇을 막으려는지부터 정해야 해요
에이전트 실행에서 걱정하는 경우는 대체로 셋입니다

- 에이전트가 읽은 웹 문서와 이슈에 숨은 지시로 악성 명령을 실행
- 설치한 패키지 안의 악성 코드가 실행
- 에이전트가 실수로 파일 삭제나 키 유출을 일으킴

세 경우 모두 에이전트 프로세스 권한으로 코드가 실행된다는 점이 같아요
격리의 목표는 그 코드가 <u>샌드박스 밖 파일, 네트워크, 커널</u>에 접근하지 못하게 하는 것입니다

## 1단계 컨테이너

![Alpine과 Debian 컨테이너가 같은 커널 버전을 출력하는 터미널 화면](/assets/images/ai/agent-isolation-three-tiers/02-term.webp)
*Alpine과 Debian 컨테이너가 같은 커널 버전을 출력하는 터미널 화면 — 출처: 직접 실행*

컨테이너는 네임스페이스와 cgroup으로 프로세스가 접근할 수 있는 파일과 네트워크를 격리해요
커널 자체는 호스트와 **같은 것을 공유**합니다

10월 19일 Mac의 Docker Desktop에서 배포판이 다른 두 컨테이너를 띄워 봤어요
Alpine과 Debian 모두 커널 버전이 <mark>6.12.76-linuxkit</mark>으로 같았습니다

커널 취약점 하나만 악용해도 컨테이너 밖에 접근하는 **컨테이너 탈출**이 가능해요

seccomp, AppArmor 정책으로 쓸 수 있는 시스템 콜을 줄일 수는 있어요
다만 임의의 코드에 맞는 정책을 정확히 작성하기는 어렵다고 gVisor 문서는 설명합니다

## 2단계 gVisor

**gVisor**는 Google이 만든 사용자 공간 커널이에요
컨테이너의 시스템 콜을 호스트 커널에 직접 전달하지 않고, Go로 작성한 Sentry가 받아 처리합니다

파일 접근은 별도 프로세스 Gofer를 통해 처리돼요
Sentry 자신도 파일 시스템에 직접 접근하지 못하게 제한된 seccomp 환경에서 실행됩니다

호스트 커널이 받는 시스템 콜 종류가 크게 줄어드는 것이 장점이에요

대신 시스템 콜 처리에 추가 오버헤드가 발생해요
일부 시스템 콜과 /proc, /sys 파일이 구현되지 않아 호환성도 떨어집니다

Docker에서는 런타임을 **runsc**로 바꾸면 쓸 수 있어요

## 3단계 마이크로VM

![Firecracker NSDI 2020 논문의 메모리 오버헤드, 부팅 시간, 생성 속도 수치 하이라이트](/assets/images/ai/agent-isolation-three-tiers/03-photo-firecracker.webp)
*Firecracker NSDI 2020 논문의 메모리 오버헤드, 부팅 시간, 생성 속도 수치 하이라이트 — 출처: USENIX*

마이크로VM은 KVM 하드웨어 가상화로 작업마다 **게스트 커널을 따로** 둬요

에이전트 코드가 커널 취약점을 악용해도 먼저 침해되는 것은 게스트 커널이에요
호스트와는 가상화 경계가 한 번 더 있습니다

대표 구현인 **Firecracker**는 AWS가 Lambda와 Fargate에 쓰려고 만들었어요
NSDI 2020 논문에 실린 수치는 아래와 같습니다

| 항목 | 논문 수치 |
| :--- | :--- |
| 메모리 오버헤드 | 5MB 미만 |
| 부팅 시간 | **125ms 미만** |
| 생성 속도 | 호스트당 초당 150개 |
| 코드 규모 | Rust 약 5만 줄 |

코드 규모는 QEMU보다 96% 적다고 논문은 밝혔어요
기능을 줄여 공격 표면을 작게 만든 설계입니다

다만 KVM이 필요해서 리눅스 호스트에서만 직접 실행할 수 있어요
Mac이나 Windows에서는 리눅스 가상머신을 한 번 더 거쳐야 합니다

## 세 단계 비교

| 방식 | 커널 경계 | 대가 |
| :--- | :--- | :--- |
| 컨테이너 | 호스트 커널 공유 | 가장 가벼움 |
| gVisor | 사용자 공간 커널 | 시스템 콜 비용 |
| 마이크로VM | **게스트 커널 분리** | KVM 필요 |

Perplexity는 10월 공개한 에이전트 샌드박스 SPACE에서 마이크로VM을 골랐어요
루트 권한 에이전트로 108번 탈출을 시도했지만 호스트에는 닿지 못했다고 밝혔습니다

<mark>격리를 강하게 해도 허용된 네트워크 경로를 통한 외부 통신도 별도로 제한해야 해요</mark>
같은 시험에서 네트워크 일부를 허용한 설정은 DNS 스푸핑 등으로 54회 중 11회 우회됐습니다

## Claude Code를 쓸 때

Claude Code에는 운영체제 기능으로 파일과 네트워크 접근을 제한하는 **샌드박스**가 들어 있어요
macOS는 기본 내장 Seatbelt, 리눅스와 WSL2는 bubblewrap과 socat을 씁니다

이 방식은 커널을 공유하는 1단계 쪽에 가까운 프로세스 격리예요
공식 문서는 파일 격리만 하고 네트워크를 열어 두면 SSH 키 같은 파일이 밖으로 나갈 수 있다고 경고합니다

권한 승인을 생략하는 옵션은 확인만 해제할 뿐 격리를 추가하지 않아요
샌드박스 없이 권한을 넓힌 경우는 10월 7일 글에서 다뤘습니다

🔗 링크 첨부 - https://blog.naver.com/rottensweetpotato/224434104966

## 고르는 기준

![실행하는 코드 성격별 격리 단계 고르는 기준 네 가지](/assets/images/ai/agent-isolation-three-tiers/04-items.webp)
*실행하는 코드 성격별 격리 단계 고르는 기준 네 가지 — 출처: gVisor 문서, Firecracker 논문 기반 자가 렌더*

어떤 단계든 API 키와 토큰은 샌드박스 밖에 두고 <u>필요할 때만 샌드박스에 전달하는</u> 편이 안전해요
SPACE도 자격증명을 샌드박스 바깥에서 관리하는 구조를 택했습니다

## 참고 출처

- [[USENIX NSDI 2020] Agache 외, Firecracker: Lightweight Virtualization for Serverless Applications (본문 이미지 1점 출처)](https://www.usenix.org/conference/nsdi20/presentation/agache)
- [[gVisor] What is gVisor? (Sentry와 Gofer 구조, 성능과 호환성 비용)](https://gvisor.dev/docs/)
- [[Claude Code] Sandboxing 문서 (Seatbelt, bubblewrap, 네트워크 격리)](https://code.claude.com/docs/en/sandboxing)
- [[Perplexity] Escaping SPACE: Part I (2026-09-23, 탈출과 우회 시험)](https://www.perplexity.ai/hub/blog/escaping-space-part-i)
