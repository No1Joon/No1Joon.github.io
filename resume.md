---
layout: resume
title: Resume
permalink: /resume/
---

# 장현준 (Jang HyunJoon)

**Senior Software Engineer · Frontend · Mobile · Backend · Data/AI**

> 웹·모바일 제품을 만들고, 그 뒤의 백엔드와 AI·데이터 파이프라인까지 직접 붙여 온 풀 사이클 엔지니어

---

## Profile

약 5년간 싱가포르 기반 AI 스타트업 Tictag의 한국 지사에서 기술 전반을 총괄하며, **React 웹·React Native 앱·Vue 3 SaaS 프론트엔드부터 NestJS 백엔드, 컴퓨터비전 파이프라인, LLM 제품 통합, 정부 지원사업**까지 풀 사이클로 담당했습니다. 요구사항을 구현하는 데 그치지 않고 비즈니스 목표에서 출발해 **기술적 의사결정을 주도**했고, 주 1회 이상의 코드 리뷰로 팀 전체의 코드 품질을 견인했습니다. 싱가포르 본사·인도네시아 팀과 영어로 상시 협업하며 한국–싱가포르 기술 브릿지 역할을 수행했고, **고객 PoC 성공, 정부 과제 수행, 신규 비즈니스 개척**에 직접 기여했습니다.

업무 밖에서도 Claude Max·Gemini·Codex를 함께 운용하며 **커스텀 스킬 11종으로 기획·설계·구현·배포까지의 개발 흐름을 자동화**해 개인 제품을 실서비스로 만들고 운영합니다.

---

## Core Skills

### Frontend

**React (웹 · React Native/Expo)** · **TypeScript** · **Vue 3 / Vuetify** · Next.js · Redux · Redux Toolkit · Zustand · Tailwind · SPA 아키텍처 · 공통 컴포넌트 표준화 · config-driven UI · i18n · 크로스플랫폼(iOS/Android)

### Backend / Infra

**Node.js / NestJS** · Python · MongoDB · PostgreSQL / pgvector · **Temporal** · Kafka · Docker / Cog · Kubernetes · GCP (Cloud Run, Vertex AI) · AWS S3 · CI/CD

### Data / AI

LLM 통합 및 비용 최적화(Gemini · OpenAI) · RAG · 임베딩 검색 · **STT (whisper-large-v3)** · Computer Vision (Detection · Tracking · ReID · Homography) · 개인정보 비식별화 파이프라인 · 데이터 품질검사 자동화

### Quality

**코드 리뷰 · 기술 리딩** · **AI 개발 워크플로**(Claude Max · Codex · Gemini, 커스텀 스킬 11종) · TypeScript 타입/데이터 모델링 · Jest · ESLint / Prettier · 제3자 공인 시험 인증 대응

---

## Professional Experience

### 틱택코리아 (Tictag) — Senior Software Engineer

2021.05 – 2026.04 | 한국 지사 기술 총괄 (싱가포르 본사 원격 협업)

리테일 영상분석 SaaS, 데이터 라벨링 플랫폼(앱·어드민), 고객 AI·하드웨어 솔루션을 프론트엔드부터 데이터 파이프라인까지 담당했습니다.

---

#### 프론트엔드 — React · Vue

- **React 기반 관리자 웹 개발** — Task Questionnaire 기능(API·다이얼로그·응답 뷰), 잡보드 속성 **실시간 입력 검증**, Task Level Review 테이블 재구성, 태거 Analytics 뷰 (React · Redux · Formik · Tailwind)
- AI 영상분석 SaaS 프론트엔드 저장소 **스캐폴딩(Vue 3 · TypeScript · Vite)** — ESLint·라우터·스토어·테마·i18n 및 import 순서까지 팀 기술 표준 수립, 타임라인 비디오 플레이어·카메라 관리·AI 파이프라인 설정 탭 구축
- **Config-driven 대시보드** — 백엔드가 내려주는 JSON config(그리드·컴포넌트·MathJS 바인딩)를 프론트가 동적 렌더링하고 config 스키마 검증을 추가해, 비개발자(BA/PM)가 코드 개입 없이 매장별 화면을 구성하게 함 — **신규 매장 대시보드 제작 기간 1주일 → 하루**, 패션 리테일 매장 첫 상용 도입(PoC) 성사
- 영어·한국어·일본어·바하사 **4개 언어 i18n 시스템 설계**(번역은 영어·한국어 담당) 및 레거시 코드 리팩토링 — 3개국 대상 서비스 기반 마련, 반응형 레이아웃 재구성

---

#### 모바일 · 디바이스 연동

- **React Native (Expo) 앱을 입사부터 퇴사까지 4년간 개발** — 단일 코드베이스로 iOS/Android 지원, 태스크 카드 UI 전면 재설계(SectionList 전환·카테고리 바·진행바), 신규 태스크 타입 2종을 화면·제출 API·튜토리얼 전 계통에 추가, 배정 알림 및 상태바 대응
- **배리어프리 음성인식 키오스크** 아키텍처 제안 및 PoC 수행 — **whisper-large-v3**(한국어 학습 모델) 기반, 맥미니 + 마이크 구성으로 발화 인식 → 화면 이미지 표출 실증, 음성 데이터 수집 프로세스 설계
- 금 순도·중량 자동검증 시스템에서 **Raspberry Pi 제어 · 360도 턴테이블 · 고해상 카메라 · XRF 분석기 연동** 및 PDF 통합 리포트 산출

---

#### 백엔드 · AI 파이프라인

- **NestJS / TypeScript 백엔드** — 분석 데이터 export API 2종, MongoDB 스키마·DAO, Role/Permission 권한 모델·멀티테넌시 설계, JWT·OAuth 인증, GCS 서명 URL 처리
- 잡보드 속성 **서버 측 검증**과 코인 카운트·완료율 계산 오류 수정으로 태거 보상 정합성 확보 — 검증을 제출 시점에서 입력 시점으로 옮겨 **잘못된 Job 설정에 따른 재작업·문의를 프로젝트당 4~5건에서 0~1건으로 감소**
- 검출·추적 **AI 모델을 Cog 컨테이너로 패키징** — SAM2MOT 프로세서 분리, 입력 max side(1024→512)·score threshold·skip frame 튜닝으로 정확도 유지하며 처리 비용 절감, K8s 볼륨 마운트 배포로 전환해 의존성 변경이 없으면 재빌드 없이 배포
- 영상 AI 파이프라인을 **Kafka → Temporal 워크플로로 전환** 설계 — 기능 플래그 라우팅으로 무중단 점진 전환, 처리 경로 가시화 및 재시도 안정성 확보
- **Homography 시스템 설계** (OpenCV RANSAC 3×3, 15% 패딩 그리드 왜곡 보정, 역행렬 검증) — reprojection error 10px 이하 달성, 약 52,000자 기술 문서 단독 작성
- LLM(Gemini) 인사이트 에이전트를 제품에 통합하고 **thinking budget 탐색으로 품질 대비 비용 최적화**

---

#### 데이터 파이프라인 · 정부 지원사업

- 데이터·AI 바우처 사업 **수요기업 13곳**(2021, 2023–2025)의 데이터 가공·품질검사 파이프라인 직접 구현(스크립트 50여 개) — **EgoBlur·랜드마크 기반 얼굴 비식별화**, Whisper 실시간 STT, 설문 데이터 정제·분석, 이미지–CSV 정합성 검사, 포맷·해상도 검증
- 수요기업별 **협약 체결 실무**부터 데이터 항목정의서·코드정의서·인수기준서 등 규격 산출물 작성과 **중간·최종 감리 통과**, 정산 증빙까지 담당, 반복 작업을 가이드라인으로 표준화해 Ops팀 이관
- **42억 원 규모 국책과제 주관기관 제안 총괄** — 과기정통부·NIA 인공지능 학습용 데이터 구축 지원사업, 기업 4개사 컨소시엄 구성·제안서 총괄·발표평가 발표 (서류 통과 후 발표평가 진출, 최종 미선정)
- 국내 **Applied AI · 데이터바우처 트랙 리드** — 고객사·정부 지원사업 **15건 이상**의 요구사항 분석·솔루션 아키텍처 설계·AI 모델 선정·납품을 전 주기로 수행
- AI 바우처 **공급기업 Pool에 자사 AI 솔루션 3종 등재**, 정부 AI 스타트업 **LLM 챌린지 서류심사 통과 및 발표** 수행
- AI 주얼리 추천 시스템으로 **공인 시험성적서 단독 취득** — 얼굴 검출 모델(YOLOv4) 선정·학습, F1·IoU·Recall 및 응답·전송 시간을 시험 항목으로 정의, 테스트 3,000건으로 성능 5개 항목 전항목 Pass
- 입사 첫해 법률 말뭉치 구축 과제에서 공공데이터 기반 판례문 5만 건 수집·정제(단어 추출·문장 길이 조정·맞춤법 검수·분포 시각화) 및 크라우드소싱 인력 관리 코드 작성, 기술·행정 감리 대응

---

#### 코드 품질 · 자동화

- 2년여간 지정 리뷰어로 중·대규모 기능을 **주 1회 이상, 누적 24건 이상 코드 리뷰** — Feature Flags 전수 리뷰에서 플래그 상태 반전 버그 사전 차단, 국가별 결제·R&D 모델 통합·다국어 AI 에이전트 등 도메인 경계를 넘는 리뷰 수행
- **QC 자동화 로봇 4종** 구축 — Gradio 기반 자동 어노테이션 툴(세션 상태 전환으로 다중 사용자 지원), Coin Decision Robot, Source-of-Truth·Training QC 로봇(정답지 기준 자동 대조·제출, 환경 분리·dry-run·오류 타입별 로깅), 광고 이미지 **12만 장 자동 QC**로 검수 소요를 **1~2일 → 1시간**으로 단축
- Ops팀 데이터 전처리·포맷 변환 자동화 도구 개발 및 지속적 기술 지원

---

#### 커뮤니케이션

- 싱가포르 본사·인도네시아 팀과 약 5년간 영어로 상시 협업하며 한국–싱가포르 기술 브릿지 역할 수행
- 클라이언트 대면 미팅 40회 이상, COEX 전시회 전 과정 리드, 한국 신규 오피스 셋업

---

## Awards

- **2023 공공데이터 기반 지역사회 현안 해결 사업 우수과제** — 한국지능정보사회진흥원(NIA), 2023.12
  공공데이터·자체 설문 데이터에 K-means 클러스터링을 적용해 서울시 흡연부스 약 500개소 입지를 도출

---

## Personal Projects

#### CaliMeal — AI 급식 식단 자동 생성 B2B SaaS
Next.js 16 · Vertex AI (Gemini) · pgvector · Terraform · GCP · 풀스택 단독

- LLM이 무엇을 생성하든 단가·중복·제철 규칙을 코드가 결정론적으로 보증하는 AI 생성 파이프라인 설계 (타임아웃·폴백·재검증 3중 방어)
- Cloud SQL의 BYPASSRLS 제약을 owner-bypass 2-풀 + `SET LOCAL`로 우회한 멀티테넌트 격리, 크로스테넌트 유출 불가를 자동 테스트로 증명
- Next.js Server Actions/SSE부터 Terraform 전 GCP 인프라 IaC까지 단독 설계·구현

---

#### JJTeam — 코트 스포츠 팀 구성·대기열 실시간 관리 앱
Expo / React Native · FastAPI · MongoDB · WebSocket · GCP · CI/CD · 풀스택 단독

- RN 클라이언트 + FastAPI/MongoDB 백엔드 + GCP 인프라 + CI/CD를 단독 아키텍팅, iOS/Android 스토어 제출까지 완주
- WebSocket 기반 다중 디바이스 실시간 동기화를 낙관적 되감기·재구독·close code 처리로 견고하게 구현
- GitHub OIDC→WIF 자격증명-zero 배포, 백엔드 pytest 221개 · ruff · mypy CI 게이트 운영

---

#### Oh My Algorithm — 알고리즘 인터랙티브 시각화 웹앱
React 19 · Vite 8 · Remotion · Puppeteer SSG · 프론트엔드 단독 · [ohmyalgorithm.com](https://ohmyalgorithm.com)

- 14개 카테고리 50개 알고리즘을 단계별 인터랙티브 시각화로 직접 구현, 한/영 이중언어 실서비스 운영
- 알고리즘 정의 하나로 웹앱 + 영상(Remotion) 두 출력을 구동하는 프레젠테이션 불가지론 데이터 레이어 설계
- Puppeteer 기반 자체 SSG로 100개 라우트 정적 프리렌더, per-page SEO(OG·JSON-LD·hreflang) 완비

---

#### 로키 (Law+Key) — 개인 맞춤형 법률 가이드 플랫폼
React / Redux Toolkit · NestJS · Prisma · MongoDB · Redis · OpenAI · 소셜 로그인

- OpenAI 연동 AI 법률 상담 플랫폼 기획·개발 (광명시 청년동 팀 프로젝트, 2025.11 – 2026.01)
- 구조화 사전 질문지 + 공감 페르소나·의도 확인 프롬프트 엔지니어링으로 상담 품질 개선
- OpenAI 직접 호출을 공식 라이브러리로 전환해 응답 안정성·스트리밍 대응 개선

---

#### AI 개발 워크플로 구축 — 기획부터 배포·발행까지 자동화
Claude Max · Codex · Gemini · 커스텀 스킬 11종

- 세 가지 AI 코딩 도구를 동시에 운용하며, 기획·설계·구현·배포로 이어지는 작업 흐름을 커스텀 스킬로 직접 구성
- 기술 콘텐츠 생산·포스팅을 파이프라인화해 주 5편 이상 발행, 월평균 조회수 500회 이상

---

#### 그 외
- **네이버 카페 정보 자동 수집 데스크톱 앱** — Playwright · Windows exe 패키징 · GitHub Actions 자동 배포, 실사용자 보유
- **privacy-policy-apps** — 개인 앱들의 약관·지원 페이지 허브 (Astro · Firebase) 운영

---

## Education

**동양미래대학교** — 전기공학과
2016.03 – 2021.02

---

## Languages

- **한국어:** Native
- **영어:** Professional Working Proficiency — 싱가포르 본사와 약 5년간 매일 영어로 협업 (데일리 스탠드업 포함)
