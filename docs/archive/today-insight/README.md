# today-insight 자료실

네이버 발행 글의 HTML·마크다운·기존 이미지를 참고해 모바일에서 읽고 자료를 받을 수 있는 정적 웹페이지로 재구성한다. 원문은 수정하지 않는다.

- 도메인: `cailmeal.com` (사용자 확정, 2026-10-03)
- 호스팅: Firebase Hosting (사용자 선택, 2026-10-03). Cloudflare에서 DNS 관리.
- 빌드: `python3.12 web/build.py`
- 첫 자료: 판결문 RAG 1탄. 네이버 블로그 자체 검색으로 원문 URL 확인.
- 공개 파일: `public/`만 배포. 공개 노트북은 출력·원본 데이터 없이 배포한다. 판결문 데이터·가명 코퍼스·임베딩 파일을 복사하지 않는다.
- 로컬 확인: `python3.12 -m http.server 8765 --directory web/public`
- 배포·DNS·공개 확인 기록: `deployment-status.json`
- 공개 노트북의 확인한 원본: `source/legal-rag-01.ipynb`. 임시 폴더 없이 재빌드할 수 있다.

배포 명령은 `web/`에서 `npx firebase-tools deploy --only hosting --project today-insight-resources`다. 현재 프로젝트는 Spark 무료 플랜이며 과금 계정을 연결하지 않았다. 기본 공개 주소는 <https://today-insight-resources.web.app/resources/legal-rag/>이며 커스텀 도메인의 인증서 상태는 배포 기록에서 확인한다.

새 자료를 만들 때 제목·설명·조건·실제 근거·복사/다운로드·네이버 링크·출처를 함께 준비한다. 기존 HTML의 이미지 삽입 안내와 네이버 편집기 서식은 웹에 남기지 않는다.
