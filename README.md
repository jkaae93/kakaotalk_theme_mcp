# KakaoTalk Theme MCP

KakaoTalk Theme MCP는 카카오톡 iOS/Android 테마 제작을 돕는 로컬 MCP 서버입니다. 테마 디자인 가이드, 생성 브리프, 사용자 제작 에셋 목록, Android 검증, iOS 검증 및 `.ktheme` 패키징 도구를 MCP 클라이언트에서 호출할 수 있게 해줍니다.

## What This Includes

- iOS 테마 디자인 가이드: `design.md`
- Android 테마 디자인 가이드: `android/design.md`
- Android 테마 제작 스킬과 검증 스크립트
- iOS/Android 통합 테마 매핑 가이드
- 로컬 stdio MCP 서버: `mcp/kakaotalk_theme_mcp.py`

## Requirements

- macOS, Linux, or Windows with Python 3
- MCP stdio server를 지원하는 클라이언트
- Android APK 빌드까지 하려면 Android sample theme project와 Gradle 환경
- iOS `.ktheme` 패키징은 Python 표준 라이브러리만으로 동작

외부 Python 패키지는 필요하지 않습니다.

## Clone

```bash
git clone git@github.com:jkaae93/kakaotalk_theme_mcp.git
cd kakaotalk_theme_mcp
```

HTTPS를 선호하면:

```bash
git clone https://github.com/jkaae93/kakaotalk_theme_mcp.git
cd kakaotalk_theme_mcp
```

## Quick Test

서버가 실행되는지 먼저 확인합니다.

```bash
python3 mcp/kakaotalk_theme_mcp.py
```

이 명령은 stdio MCP 서버를 실행하므로 터미널에 계속 대기 상태로 보이는 것이 정상입니다. 종료하려면 `Ctrl+C`를 누릅니다.

Python 문법 검사는 아래처럼 실행할 수 있습니다.

```bash
PYTHONPYCACHEPREFIX=/tmp/kakaotalk_theme_pycache python3 -m py_compile mcp/kakaotalk_theme_mcp.py
```

## Register In Codex

Codex에서 사용하려면 `~/.codex/config.toml`에 아래 블록을 추가합니다.

`<REPO_PATH>`는 이 저장소를 clone한 절대 경로로 바꿔주세요.

```toml
[mcp_servers.kakaotalk_theme_local]
command = "python3"
args = ["<REPO_PATH>/mcp/kakaotalk_theme_mcp.py"]
startup_timeout_sec = 30

[mcp_servers.kakaotalk_theme_local.env]
KAKAOTALK_THEME_ALLOWED_ROOTS = "<REPO_PATH>:/private/tmp"
```

예를 들어 이 저장소가 `/Users/kaae/dev/projects/카톡 테마 메이커`에 있다면:

```toml
[mcp_servers.kakaotalk_theme_local]
command = "python3"
args = ["/Users/kaae/dev/projects/카톡 테마 메이커/mcp/kakaotalk_theme_mcp.py"]
startup_timeout_sec = 30

[mcp_servers.kakaotalk_theme_local.env]
KAKAOTALK_THEME_ALLOWED_ROOTS = "/Users/kaae/dev/projects/카톡 테마 메이커:/private/tmp:/Users/kaae/Downloads/kakaotalk_theme_user_guide"
```

설정 후 Codex 앱을 재시작하거나 새 세션을 열면 MCP 서버가 로드됩니다.

## Register In Other MCP Clients

JSON 설정을 사용하는 MCP 클라이언트에서는 아래 형식을 사용합니다.

```json
{
  "mcpServers": {
    "kakaotalk-theme-local": {
      "command": "python3",
      "args": [
        "<REPO_PATH>/mcp/kakaotalk_theme_mcp.py"
      ],
      "env": {
        "KAKAOTALK_THEME_ALLOWED_ROOTS": "<REPO_PATH>:/private/tmp"
      }
    }
  }
}
```

같은 예시는 `mcp/config.example.json`에도 들어 있습니다.

## Available Tools

### `read_theme_guide`

iOS, Android, dual-platform 가이드를 읽습니다.

Input:

```json
{
  "guide": "android"
}
```

`guide` 값:

- `ios`
- `android`
- `dual-platform`

### `create_theme_brief`

테마 생성을 위한 브리프 템플릿을 만듭니다.

Input:

```json
{
  "platform": "dual",
  "name": "Soft Peach",
  "concept": "warm peach stationery",
  "mode": "light"
}
```

### `list_required_assets`

사용자가 직접 생성해야 하는 아이콘, 탭 아이콘, 배경 이미지, 말풍선, passcode 이미지 목록을 반환합니다.

Input:

```json
{
  "platform": "dual",
  "format": "markdown"
}
```

`platform` 값:

- `ios`
- `android`
- `dual`

`format` 값:

- `markdown`
- `json`

### `validate_android_theme`

Android KakaoTalk theme project 또는 APK를 검증합니다.

Input:

```json
{
  "path": "/path/to/android-theme-project"
}
```

검증 항목에는 `AndroidManifest.xml`, `colors.xml`, `strings.xml`, theme permission, KakaoTalk theme intent-filter, selector resource reference 등이 포함됩니다.

### `validate_ios_theme`

iOS KakaoTalk theme folder 또는 `.ktheme` 파일을 간단 검증합니다.

Input:

```json
{
  "path": "/path/to/ios-theme-folder"
}
```

검증 항목에는 `KakaoTalkTheme.css`, `Images/`, `.ktheme` archive root 구조, macOS metadata 포함 여부 등이 포함됩니다.

### `package_ios_ktheme`

iOS theme folder를 `.ktheme` 파일로 패키징합니다.

Input:

```json
{
  "theme_dir": "/path/to/ios-theme-folder",
  "output_path": "/path/to/output/theme.ktheme"
}
```

### `list_theme_assets`

현재 저장소 안의 테마 관련 파일 목록을 확인합니다.

Input:

```json
{
  "max_depth": 4
}
```

## Available Resources

MCP resources로 아래 문서를 읽을 수 있습니다.

- `kakaotalk://design/ios`
- `kakaotalk://design/android`
- `kakaotalk://guide/android`
- `kakaotalk://guide/dual-platform`

## Available Prompts

- `new-dual-platform-theme`: iOS/Android 동시 테마 제작 브리프 시작
- `android-theme-check`: Android theme project 검증 및 리뷰 시작

## Allowed Paths

보안을 위해 서버는 기본적으로 아래 경로 안의 파일만 다룹니다.

- repository root
- `/tmp`
- `/private/tmp`
- `~/Downloads/kakaotalk_theme_user_guide`

추가 경로가 필요하면 `KAKAOTALK_THEME_ALLOWED_ROOTS`에 `:`로 구분해서 넣습니다.

```toml
[mcp_servers.kakaotalk_theme_local.env]
KAKAOTALK_THEME_ALLOWED_ROOTS = "<REPO_PATH>:/private/tmp:/path/to/sample/themes"
```

## Suggested Workflow

1. `create_theme_brief`로 테마 브리프를 만듭니다.
2. `list_required_assets`로 사용자가 만들어야 하는 아이콘/이미지 목록을 확인합니다.
3. `read_theme_guide`로 플랫폼별 가이드를 확인합니다.
4. iOS는 `KakaoTalkTheme.css`와 `Images/`를 준비합니다.
5. Android는 sample theme project의 `src/main/theme` 리소스를 교체합니다.
6. `validate_ios_theme` 또는 `validate_android_theme`로 검증합니다.
7. iOS는 `package_ios_ktheme`로 `.ktheme`을 만듭니다.
8. Android는 Gradle로 APK를 빌드합니다.

## Troubleshooting

### Codex에서 도구가 보이지 않음

- `~/.codex/config.toml`에 MCP 서버 블록이 들어갔는지 확인합니다.
- `args`의 경로가 절대 경로인지 확인합니다.
- Codex 앱을 재시작하거나 새 세션을 엽니다.

### Path is outside allowed roots 오류

검증하거나 패키징하려는 파일 경로가 `KAKAOTALK_THEME_ALLOWED_ROOTS`에 포함되어야 합니다.

### Python cache permission 오류

일부 환경에서 Python이 홈 캐시 폴더에 `.pyc`를 쓰지 못할 수 있습니다. 이때는 아래처럼 캐시 위치를 바꿔 테스트합니다.

```bash
PYTHONPYCACHEPREFIX=/tmp/kakaotalk_theme_pycache python3 -m py_compile mcp/kakaotalk_theme_mcp.py
```

### Android build까지 하고 싶음

이 MCP는 Android theme source validation을 제공합니다. APK 빌드는 Android sample project 루트에서 Gradle로 수행합니다.

```bash
./gradlew assembleDebug
```

release signing은 각 사용자의 keystore 정책에 맞게 별도로 설정해야 합니다.
