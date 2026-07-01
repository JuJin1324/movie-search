---
name: build-pdf
description: "Markdown 파일을 PDF로 변환한다. Mermaid 다이어그램 렌더링 포함. 포트폴리오·이력서를 제출 가능한 PDF로 만들 때 사용."
---

# Build PDF

## 목적

Markdown 파일을 PDF로 변환한다. Mermaid 다이어그램이 포함된 포트폴리오와 이력서를 제출 가능한 PDF로 만드는 것이 주 용도다.

## 파이프라인

```
Markdown → Mermaid PNG 렌더링(mmdc) → pandoc HTML → weasyprint PDF
```

## 포함 파일

- `build_pdf.py` — 빌드 스크립트
- `portfolio-pdf.css` — PDF 스타일 (A4, 한글 폰트, 표, Mermaid 그림 레이아웃)

## 사용 방법

사용자가 PDF 빌드를 요청하면 아래 명령어를 실행한다.

```bash
python3 .claude/skills/build-pdf/build_pdf.py \
  --sources [소스 md 파일들] \
  --output-dir [출력 디렉터리] \
  --names [출력 pdf 파일명들] \
  --combined [합본 pdf 파일명] \   # 선택
  --css .claude/skills/build-pdf/portfolio-pdf.css
```

## 인자

| 인자 | 필수 | 설명 |
|------|------|------|
| `--sources` | ✅ | 변환할 Markdown 파일 경로 목록 (공백 구분) |
| `--output-dir` | ✅ | PDF를 저장할 디렉터리 |
| `--names` | ✅ | 각 소스에 대응하는 출력 PDF 파일명 목록 |
| `--combined` | ☐ | 합본 PDF 파일명. 지정 시 sources 순서로 합본 생성 |
| `--css` | ✅ | CSS 파일 경로. 통상 `.claude/skills/build-pdf/portfolio-pdf.css` 사용 |

## 예시

### 정규직 포트폴리오 + 이력서

```bash
python3 .claude/skills/build-pdf/build_pdf.py \
  --sources \
    problems/career-move/fulltime/fulltime-resume.md \
    problems/career-move/fulltime/order-platform-portfolio.md \
    problems/career-move/fulltime/concurrency-poc-portfolio.md \
  --output-dir problems/career-move/fulltime/epic4/pdf \
  --names \
    fulltime-resume.pdf \
    order-platform-portfolio.pdf \
    concurrency-poc-portfolio.pdf \
  --combined fulltime-portfolio-combined.pdf \
  --css .claude/skills/build-pdf/portfolio-pdf.css
```

### 프리랜서 포트폴리오

```bash
python3 .claude/skills/build-pdf/build_pdf.py \
  --sources \
    problems/career-move/freelance/order-platform-portfolio.md \
    problems/career-move/freelance/concurrency-poc-portfolio.md \
  --output-dir problems/career-move/freelance/epic1 \
  --names \
    order-platform-portfolio.pdf \
    concurrency-poc-portfolio.pdf \
  --combined freelance-portfolio-combined.pdf \
  --css .claude/skills/build-pdf/portfolio-pdf.css
```

## 의존성

- `npx @mermaid-js/mermaid-cli` — Mermaid PNG 렌더링
- `pandoc` — Markdown → HTML 변환
- `weasyprint` — HTML → PDF 변환

## 작동 방식

1. 각 소스 파일에서 ` ```mermaid ` 블록을 추출해 PNG로 렌더링 (3배율)
2. Mermaid 블록을 PNG 이미지 태그로 교체한 rendered.md 생성
3. pandoc으로 HTML 변환 (CSS 적용)
4. weasyprint로 PDF 생성
5. `--combined` 지정 시 모든 rendered 텍스트를 페이지 구분자로 합쳐 합본 PDF 생성
6. 빌드 임시 파일 자동 정리
