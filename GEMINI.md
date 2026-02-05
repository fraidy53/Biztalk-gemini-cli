# BizTone Converter 프로젝트 개요

이 문서는 Gemini CLI가 `BizTone Converter` 프로젝트를 이해하고 상호 작용하기 위한 지침과 정보를 제공합니다.

## 1. 프로젝트 개요

`BizTone Converter`는 AI 기반의 업무 말투 자동 변환 웹 솔루션입니다. 사용자가 입력한 텍스트를 대상(상사, 동료, 고객)에 맞춰 전문적이고 적절한 비즈니스 커뮤니케이션 어조로 변환하는 것을 목표로 합니다. 이는 특히 비즈니스 커뮤니케이션에 익숙하지 않은 직장인들의 업무 효율성을 높이고, 일관된 커뮤니케이션 품질을 유지하는 데 도움을 줍니다.

**주요 기술 스택:**
*   **백엔드**: Python, Flask, Groq AI API
*   **프론트엔드**: HTML, JavaScript, Tailwind CSS (CDN 방식)

## 2. 프로젝트 구조

프로젝트는 프론트엔드와 백엔드가 분리된 모듈화된 구조를 가집니다.

-   **`./` (프로젝트 루트)**:
    -   `.env`: 환경 변수 설정 파일 (예: `GROQ_API_KEY`)
    -   `PRD.md`: 제품 요구사항 정의 문서
    -   `프로그램개요서.md`: 프로젝트 초기 기획 및 기술 개요 문서
    -   `my-rules.md`: Gemini CLI (AI 에이전트) 지침
-   **`backend/`**: Flask 기반의 백엔드 API 서버
    -   `app.py`: Flask 애플리케이션의 메인 엔트리 포인트, Groq AI 연동 및 비즈니스 로직 처리
    -   `requirements.txt`: Python 패키지 의존성 목록
-   **`frontend/`**: 사용자 인터페이스(UI) 정적 웹 파일
    -   `index.html`: 메인 HTML 파일
    -   `js/script.js`: 클라이언트 측 JavaScript 로직 (API 호출, DOM 조작 등)
    -   `css/` (디렉토리만 존재): Tailwind CSS CDN 방식으로 스타일링 됨

## 3. 빌드 및 실행 방법

### 3.1. 환경 변수 설정

프로젝트 루트 디렉토리에 `.env` 파일을 생성하고 `GROQ_API_KEY`를 설정해야 합니다.

```
GROQ_API_KEY="YOUR_GROQ_API_KEY"
```
**주의**: `.env` 파일은 `my-rules.md`에 따라 수정하지 마십시오.

### 3.2. 백엔드 실행

1.  **Python 가상 환경 설정 및 활성화**:
    ```bash
    python -m venv .venv
    ./.venv/Scripts/activate # Windows
    # source ./.venv/bin/activate # macOS/Linux
    ```
2.  **의존성 설치**:
    ```bash
    pip install -r backend/requirements.txt
    ```
3.  **Flask 애플리케이션 실행**:
    ```bash
    python backend/app.py
    # 또는 Flask CLI 사용:
    # flask --app backend/app run --debug
    ```
    서버는 기본적으로 `http://127.0.0.1:5000`에서 실행됩니다.

### 3.3. 프론트엔드 실행

프론트엔드 파일은 Flask 백엔드에 의해 정적으로 제공됩니다. 백엔드 서버가 실행되면 웹 브라우저에서 `http://127.0.0.1:5000`에 접속하여 애플리케이션에 접근할 수 있습니다. 별도의 프론트엔드 빌드 또는 실행 단계는 필요하지 않습니다. Tailwind CSS는 CDN 방식을 사용하여 `index.html`에 직접 포함되어 있습니다.

## 4. 개발 컨벤션 및 지침

*   **AI 에이전트 지침**: `my-rules.md` 파일을 참조하여 Gemini CLI (AI 에이전트)의 행동 원칙 및 소통 방식을 확인하십시오.
*   **프로젝트 요구사항 및 아키텍처**: `PRD.md` 및 `프로그램개요서.md` 문서는 프로젝트의 상세 요구사항, 사용자 시나리오, 기술 스택, 시스템 아키텍처 및 릴리즈 계획을 포함하고 있습니다. 개발 진행 시 이 문서들을 최우선으로 참고하십시오.
*   **버전 관리**: `PRD.md`에 명시된 `main`, `develop`, `feature` 브랜치 전략을 따릅니다. Pull Request를 통한 코드 리뷰를 권장합니다.

---