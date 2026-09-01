---
title: "무료 오픈소스 STT 4종을 같은 음성으로 돌려봤습니다"
description: "같은 가중치를 쓰는 네 구현을 한국어·영어 같은 음성으로 재고, 영어 1위가 한국어에서 뒤집힌 이유가 성능이 아니었던 지점을 짚습니다"
date: 2026-08-10
category: AI
subcategory: Explainer
tags: [stt, whisper, faster-whisper, korean-asr, benchmark]
image: /assets/og/2026-08-10-open-source-stt-korean-benchmark.png
---

어 오늘은 그 클라우드 요금 비교 글을 하나 썼는데요 음 네이버
      클라우드랑 nhn 클라우드를 아니 정확히는 3군데를 놓고 봤거든요
      근데 이게 이게 좀 웃긴게 시간당 요금은 nhn 이 더 싼데 뭘로
      계산하면 어... 네이버가 더 싸게 나와요. 디스크가... 그러니까
      50기가가 요금에 포함되어 있어서... 음... 그 차이도 때문이라고요.

      [3] WhisperX                                                0.8s
      오늘은 클라우드 요금 비교 글을 하나 썼는데요 네이버 클라우드랑
      NHN 클라우드를 아니 정확히는 세 군데를 놓고 봤거든요 근데 이게
      이게 좀 웃긴게 시간당 요금은 nhn이 더 싼데 원로 계산하면
      네이버가 더 싸게 나와요 디스크가 그러니까 50기가가 요금에 포함돼
      있어서 그 차이 때문이라고요

      [4] CrisperWhisper (verbatim)                               1.1s
      [UH] 오늘은 그 클���우��� 요금 비교 ��을 하나 ���는데요 [UM]
      네이��� 클���우������ NHN 클���우���를 아니, 정확히는 세 �����를
      놓고 봤거든요. 근데 이게 이게 좀 웃긴 게, 시간당 요금은 NHN이 더
      ��데, ����� 계산하면 [UH] 네이���가 더 싸게 나와요. Disk가
      그러니까 오십기가가 요금에 포����� 있어서 [UM] 그 차이도
      때문이라고요.
  - slot: "한글 깨짐 재현 셀"
    type: colab
    file: "7_colab_hangul.png"
    cells:
      - md: |
          ## 12. 한글이 깨지는 이유

          모델 없이 토크나이저만으로 재현됩니다.
      - code: |
          from transformers import AutoTokenizer

          tok = AutoTokenizer.from_pretrained(
              "nyralabs/CrisperWhisper2.0_turbo")
          sample = "클라우드 네이버 요금 비교"

          ids = tok.encode(sample, add_special_tokens=False)
          whole = tok.decode(ids)
          per_token = "".join(tok.decode([i]) for i in ids)

          print("원문      :", sample)
          print("통째 디코딩:", whole)
          print("토큰별    :", per_token)
        out: |
          원문      : 클라우드 네이버 요금 비교
          통째 디코딩: 클라우드 네이버 요금 비교
          토큰별    : �����우��� 네이��� 요금 비교
        n: 12
  - slot: "영어 실행 출력"
    type: terminal
    file: "8_term_en.png"
    title: "bench_stt.py — english"
    text: |
      ================================================================
       STT 비교 — en · T4 · 5회 중앙값
      ================================================================

      [1] Whisper large-v3-turbo                                  1.2s
      Now, we're developing a remote control, which you probably
      already know. We want it to be original, something that people
      haven't thought of, that's not out in the shops. Trendy,
      appealing to a wide market, but, you know, not a hunk of metal.
      And user-friendly, grannies to kids, maybe even pooches should
      be able to use it.

      [3] CrisperWhisper (verbatim)                               0.5s
      Now we're developing a remote control which you probably already
      know [UM] we want it to be original, something that s- people
      haven't thought of that's not out in the shops [UM] trendy,
      appealing to a wide market but you know not a hunk of metal and
      user-friendly, grannies to kids, maybe even pooches should be
      able to use it.
  - slot: "언어별 오인식 개수 격차"
    type: chart
    file: "9_chart_오인식.png"
    form: diverging_bar
    title: "같은 모델의 오인식 개수 — 한국어와 영어"
    subtitle: "낮을수록 정확"
    series: ["한국어", "영어"]
    unit: "개"
    source: "자료: 한국어 47단어·영어 65단어 기준 · 필러와 주석 태그 제외 · Colab T4 (2026-08-10)"
    data:
      - ["Whisper", 5, 1]
      - ["faster-whisper", 6, 3]
      - ["WhisperX", 6, 3]
      - ["CrisperWhisper", 18, 0]
hashtags: ["STT", "음성인식", "Whisper", "위스퍼", "CrisperWhisper", "오픈소스STT", "faster-whisper", "WhisperX", "OpenAI", "오픈AI", "받아쓰기", "음성텍스트변환", "speech-to-text", "한국어음성인식", "AI모델비교", "머신러닝", "딥러닝", "Colab", "코랩", "T4", "GPU", "회의록작성", "자막제작", "인터뷰녹취", "무료AI도구", "AI도구추천", "개발자도구", "파이썬", "IT정보", "AI뉴스"]
---

회의 녹음을 텍스트로 옮기는 일에 돈을 쓰지 않아도 됩니다. 무료로 받아쓰는 오픈소스가 이미 여럿이고, 노트북 한 대만 있으면 돌아갑니다.

문제는 어느 걸 고르냐입니다. 벤치마크 점수는 대부분 영어로 잰 것이고, 한국어는 사정이 다릅니다. 그래서 네 가지를 **같은 음성**으로 직접 돌려봤습니다. 제 목소리로 녹음한 36초짜리 한국어와, 공개된 회의 녹음 26초짜리 영어입니다.

결과가 언어별로 갈렸습니다. 영어에서 가장 정확했던 모델이 한국어에서는 가장 나빴고, 그 이유가 성능이 아니었습니다.

![음성 파형이 문자 블록으로 바뀌는 3D 콘셉트 컷](/assets/images/ai/open-source-stt-korean-benchmark/01-agy-hero.webp)
*음성 파형이 문자 블록으로 바뀌는 3D 콘셉트 컷 — 출처: 자가 생성*

## 무엇을 어떻게 쟀나

![OpenAI 로고](/assets/images/ai/open-source-stt-korean-benchmark/02-logo-openai.webp)
*OpenAI 로고 — 출처: OpenAI*

네 가지 모두 **Whisper large-v3-turbo** 라는 같은 가중치를 씁니다. 다른 건 그 가중치를 돌리는 방식입니다.

### Whisper

OpenAI 원본입니다. **transformers** 파이프라인으로 그대로 돌립니다. 나머지를 재는 기준점입니다.

### faster-whisper

같은 가중치를 **CTranslate2** 로 다시 구현했습니다. 결과는 거의 같고 속도와 메모리가 다릅니다.

### WhisperX

faster-whisper 위에 무음 구간 검출과 단어 정렬을 얹었습니다.

### CrisperWhisper

말한 그대로 받아씁니다. **어**, **음** 같은 머뭇거림과 더듬은 말을 지우지 않고 남깁니다.

![네 모델의 호출 코드 비교](/assets/images/ai/open-source-stt-korean-benchmark/03-colab-models.webp)
*네 모델의 호출 코드 비교 — 출처: 노트북 화면 자가 렌더*

네 가지가 같은 가중치를 쓰는 만큼 호출도 비슷합니다. 다른 건 받아쓴 뒤에 무엇을 더 하느냐입니다. WhisperX만 **batch_size** 를 받고, CrisperWhisper만 **mode** 를 받습니다.

### 설치가 가장 까다롭습니다

![설치 셀 — ctranslate2 교체](/assets/images/ai/open-source-stt-korean-benchmark/04-colab-install.webp)
*설치 셀 — ctranslate2 교체 — 출처: 노트북 화면 자가 렌더*

네 가지를 한 환경에 같이 두면 **ctranslate2** 에서 부딪힙니다. WhisperX가 끌고 오는 원본과 CrisperWhisper가 요구하는 포크가 같은 폴더를 쓰기 때문입니다. 둘을 함께 지우고 포크만 다시 설치해야 넷이 같이 돕니다. 순서를 어기면 CrisperWhisper가 import 단계에서 죽습니다.

측정은 Colab 무료 티어의 **T4** 한 대에서 했습니다. 모델 크기와 정밀도를 맞추고, 조합마다 워밍업 한 번을 버린 뒤 다섯 번씩 재서 중앙값을 썼습니다. 한 번만 재면 같은 코드가 20% 넘게 흔들립니다.

## 속도는 두 배 넘게 벌어졌다

![한국어 36.4초를 받아쓰는 데 걸린 시간](/assets/images/ai/open-source-stt-korean-benchmark/05-chart.webp)
*한국어 36.4초를 받아쓰는 데 걸린 시간 — 출처: Colab T4 실측 기반 자가 렌더*

36초짜리 한국어를 받아쓰는 데 원본 Whisper는 1.75초, WhisperX는 0.82초가 걸렸습니다. 두 배 넘는 차이입니다.

WhisperX가 빠른 이유는 탐색을 덜 해서가 아닙니다. 조건을 맞춰도 여전히 가장 빨랐습니다. 무음 구간을 먼저 잘라내고 여러 조각을 한꺼번에 밀어 넣는 구조에서 나옵니다. 이건 설정이 아니라 그 라이브러리의 설계라 맞출 수가 없고, 맞추면 WhisperX를 쓸 이유가 사라집니다.

> 30초 안팎이면 어느 쪽이든 1초 내외입니다. 속도가 갈리는 건 파일이 길어질 때입니다.

## 탐색을 넓히면 정확해질 거라는 기대

faster-whisper는 기본으로 후보 문장 다섯 개를 놓고 고릅니다. 하나만 보고 지나가는 쪽보다 정확할 것 같지만, 한국어에서는 반대로 나왔습니다.

| 조건 | 한국어 오인식 | 영어 오인식 |
|---|---|---|
| 기본 (후보 5개) | 9개 | 1개 |
| <mark>후보 1개</mark> | <mark>6개</mark> | 3개 |

후보를 다섯 개 놓고 고른 쪽이 한국어에서 세 개 더 틀렸습니다. **50기가가** 를 **50기가 가** 로 쪼개고, **그 차이도** 를 **그 차이 덜** 로 뽑았습니다. 영어에서는 예상대로 넓게 보는 쪽이 나았습니다.

- 기본값이 항상 좋은 설정이라는 뜻은 아닙니다. 한국어로 쓸 거라면 양쪽을 다 재보고 정하는 편이 낫습니다.

## 한국어에서 갈렸다

![네 모델의 한국어 받아쓰기 실행 출력](/assets/images/ai/open-source-stt-korean-benchmark/06-term-ko.webp)
*네 모델의 한국어 받아쓰기 실행 출력 — 출처: bench_stt.py 실측 출력*

같은 36초를 넷이 받아쓴 결과입니다. 위 셋은 읽을 만합니다. 맨 아래가 문제입니다.

**클라우드** 가 **클우** 로, **네이버** 가 **네이** 로 뭉개졌습니다. 글자가 통째로 사라진 게 아니라 자리마다 깨진 문자가 박혔습니다. 47단어짜리 문장에서 오인식이 18개, 깨진 문자가 49개 나왔습니다.

숫자만 보면 이 모델이 한국어를 못 알아듣는다고 결론 내리게 됩니다. 그런데 같은 모델이 영어에서는 오인식 0개로 넷 중 가장 정확했습니다. 앞뒤가 맞지 않아서 원인을 따로 찾아봤습니다.

## 깨진 건 모델이 아니라 디코딩이었다

![토크나이저 왕복 재현 셀과 출력](/assets/images/ai/open-source-stt-korean-benchmark/07-colab-hangul.webp)
*토크나이저 왕복 재현 셀과 출력 — 출처: 노트북 실행 화면 자가 렌더*

모델 없이 토크나이저만으로 재현됩니다.

**클라우드 네이버 요금 비교** 를 토큰 12개로 쪼갠 뒤, 한 번에 되돌리면 원문이 그대로 나옵니다. 그런데 토큰을 하나씩 따로 되돌려 이어 붙이면 12개 중 11개가 깨집니다.

원인은 글자를 세는 단위입니다. 한글 한 글자는 UTF-8로 저장할 때 3바이트를 차지하고, 토큰 경계는 바이트 단위로 잘립니다. 한 글자를 이루는 3바이트가 서로 다른 토큰으로 갈라지면 각각은 완성된 글자가 아니라 조각입니다. 조각을 따로 해석하니 깨진 문자가 나옵니다. 영어는 한 글자가 1바이트라 이 문제를 겪지 않습니다.

CrisperWhisper는 단어마다 시각을 표시하려고 토큰을 하나씩 따로 해석합니다. 그 방식이 한국어와 부딪힙니다.

> 한국어 오인식 18개는 못 알아들은 결과가 아니라, 알아들은 것을 옮겨 적는 과정에서 깨진 결과입니다.

읽는 방향이 달라집니다. 정확도가 낮은 모델이 아니라, 한국어에서는 지금 쓸 수 없는 모델입니다. 라이브러리가 고치면 해결될 문제이고, 모델을 다시 학습시켜야 하는 문제가 아닙니다.

## 영어에서는 정반대였다

![언어별 오인식 개수 격차](/assets/images/ai/open-source-stt-korean-benchmark/08-chart.webp)
*언어별 오인식 개수 격차 — 출처: 실측 수치 기반 자가 렌더*

같은 모델이 한국어 18개, 영어 0개입니다. 나머지 셋은 언어가 바뀌어도 순위가 크게 흔들리지 않았는데 이 모델만 양 끝을 오갔습니다.

![영어 받아쓰기 실행 출력](/assets/images/ai/open-source-stt-korean-benchmark/09-term-en.webp)
*영어 받아쓰기 실행 출력 — 출처: bench_stt.py 실측 출력*

영어 출력을 나란히 놓으면 차이가 보입니다. 원본 Whisper는 화자가 말한 **um** 두 번을 지웠고, 말을 더듬은 **s-** 도 없앴습니다. 문장이 깔끔해졌지만 실제로 한 말과는 달라졌습니다. CrisperWhisper는 셋 다 남겼습니다.

| 모델 | 한국어 필러 | 영어 필러 |
|---|---|---|
| Whisper | 4개 | 0개 |
| faster-whisper | 4개 | 0개 |
| WhisperX | 0개 | 0개 |
| <mark>CrisperWhisper</mark> | <mark>4개</mark> | <mark>2개</mark> |

정답에 들어 있던 필러는 한국어 4개, 영어 3개입니다. 영어에서 이걸 남긴 건 CrisperWhisper뿐이었습니다.

말버릇을 지우는 게 나은 경우가 대부분입니다. 자막이나 회의 요약이라면 **음**, **어** 는 방해만 됩니다. 반대로 상담 기록이나 인터뷰 원문처럼 **어떻게 말했는지가 정보인** 경우에는 지우면 안 됩니다. 어느 쪽이 필요한지는 만들려는 결과물이 정합니다.

## 그래서 무엇을 골라야 하나

| 상황 | 고를 것 |
|---|---|
| 한국어 · 업무용 | faster-whisper |
| 긴 파일 · 속도 우선 | WhisperX |
| 정확도 기준점이 필요 | Whisper |
| 영어 · 말버릇 보존 | CrisperWhisper |

**가중치 라이선스를 먼저 확인해야 합니다.** Whisper와 faster-whisper는 MIT, WhisperX는 BSD입니다. 상업적으로 쓸 수 있습니다. CrisperWhisper는 코드가 MIT지만 **가중치가 비상업 연구용**입니다. 제품이나 업무에 넣으려면 별도 라이선스를 받아야 합니다.

한국어로 쓸 거라면 선택지는 사실상 셋입니다. 넷째는 디코딩이 고쳐지기 전까지 기다려야 합니다.

직접 돌려보실 수 있게 Colab 노트북을 올려뒀습니다. 설치할 것 없이 링크만 누르면 열리고, 자기 목소리를 올려 같은 비교를 할 수 있습니다.

## Colab 노트북 바로 열기

https://colab.research.google.com/github/No1Joon/oh-my-notebooks/blob/main/notebooks/korean_stt_comparison.ipynb

## 재보고 알게 된 것

수치를 그대로 믿으면 틀리는 자리가 몇 군데 있었습니다.

**오인식 개수만 보면 원인을 놓칩니다.** 18개라는 숫자는 같았어도 원인이 성능이면 대안이 없고, 디코딩이면 기다리면 됩니다. 숫자가 아니라 출력을 눈으로 봐야 갈립니다.

**기본 설정끼리 비교하면 라이브러리 차이가 모델 차이로 보입니다.** 처음 쟀을 때 CrisperWhisper가 다섯 배 빨라 보였는데, 탐색 폭이 달라서였습니다. 조건을 맞추자 차이가 줄었습니다.

**한 번 재고 결론 내리면 안 됩니다.** 같은 코드가 1.70초에서 2.13초까지 흔들렸습니다. 0.2초 차이로 순위를 매길 수 있는 측정이 아닙니다.

## 참고 출처

- [[OpenAI] Whisper 저장소 (모델·라이선스 확인)](https://github.com/openai/whisper)
- [[SYSTRAN] faster-whisper 저장소](https://github.com/SYSTRAN/faster-whisper)
- [[m-bain] WhisperX 저장소](https://github.com/m-bain/whisperX)
- [[Nyra Health] CrisperWhisper 저장소 (가중치 라이선스 확인)](https://github.com/nyrahealth/CrisperWhisper)
- [[University of Edinburgh] AMI Meeting Corpus — 영어 음성과 공식 전사 (CC BY 4.0)](https://groups.inf.ed.ac.uk/ami/corpus/)
- 측정 조건: Colab T4 · float16 · turbo 급 · 워밍업 1회 후 5회 중앙값
- 오인식은 필러와 웃음 표시를 양쪽에서 지우고 셌고, 숫자 표기 차이는 같은 값으로 봤습니다
