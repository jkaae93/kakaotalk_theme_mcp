# KakaoTalk Android Theme Design Guidelines

이 문서는 카카오톡 Android 테마를 일관되게 생성하기 위한 디자인 가이드라인이다. Android 테마는 iOS `.ktheme`와 다르게 Android 앱 프로젝트를 수정한 뒤 APK로 빌드, 서명, 설치하는 방식으로 배포한다.

## 1. Theme Brief

- 테마 이름: Android 런처와 카카오톡 테마 목록에 표시될 이름
- 패키지명: 예) `com.kakao.talk.theme.mytheme`
- 콘셉트: 예) 새벽 정원, 복숭아 젤리, 잉크 다이어리, 미니멀 다크
- 분위기 키워드: 3-6개
- 대상 모드: light 또는 dark
- 주요 색상: 메인 배경, 채팅방 배경, 헤더, 본문, 보조 텍스트, 강조색
- 이미지 방향: 일러스트, 패턴, 단색, 캐릭터 중심, 사진 중심
- 말풍선 스타일: 9-patch 기준의 둥근 정도, 여백, 송신/수신 대비
- 접근성 기준: 배경과 텍스트의 대비를 충분히 확보

## 2. Output Structure

Android 테마는 샘플 프로젝트 구조를 유지한다.

```text
ThemeName/
  build.gradle.kts
  gradlew
  src/
    main/
      AndroidManifest.xml
      res/
      theme/
        values/
          colors.xml
          strings.xml
        drawable-xhdpi/
        drawable-xxhdpi/
        drawable-land-xhdpi/
        drawable-land-xxhdpi/
        drawable-sw600dp/
        drawable-sw600dp-land/
      theme-adv/
        color/
        drawable/
```

최종 산출물은 APK다. 작업이 끝나면 Gradle로 compile 및 sign을 수행하고, 설치 후 카카오톡 더보기 탭 > 설정 > 테마 설정에서 적용한다.

## 3. Design Token Rules

먼저 디자인 토큰을 정의하고 Android 리소스에 매핑한다.

```text
background.main
background.chat
background.passcode
surface.header
surface.body
surface.bodyPressed
surface.tab
text.header
text.title
text.titlePressed
text.paragraph
text.description
accent.primary
accent.pressed
border.body
bubble.me
bubble.meText
bubble.you
bubble.youText
badge.unread
input.background
input.text
input.menuIcon
input.sendButton
input.sendIcon
```

색상은 `#rrggbb` 또는 `#aarrggbb` 형식으로 `src/main/theme/values/colors.xml`에 기록한다.

## 4. Color Mapping

- `theme_header_color`: 메인탭 헤더 타이틀 및 아이콘
- `theme_header_cell_color`: 헤더와 상태바 배경
- `theme_title_color`: 이름, 타이틀, 주요 텍스트
- `theme_title_pressed_color`: 주요 텍스트 pressed 상태
- `theme_paragraph_color`: 마지막 메시지
- `theme_description_color`: 상태 메시지, 보조 정보
- `theme_section_title_color`: 섹션 타이틀
- `theme_background_color`: 메인 배경
- `theme_chatroom_background_color`: 채팅방 배경
- `theme_passcode_background_color`: 잠금화면 배경
- `theme_body_cell_color`: 기본 리스트와 콘텐츠 셀
- `theme_body_cell_pressed_color`: 리스트 pressed 상태
- `theme_body_cell_border_color`: 리스트와 콘텐츠 보더
- `theme_maintab_cell_color`: 메인 탭바 배경
- `theme_chatroom_bubble_me_color`: 보낸 말풍선 텍스트
- `theme_chatroom_bubble_you_color`: 받은 말풍선 텍스트
- `theme_chatroom_unread_count_color`: 읽지 않음 숫자
- `theme_chatroom_input_bar_color`: 인풋바 텍스트
- `theme_chatroom_input_bar_background_color`: 인풋바 배경
- `theme_chatroom_input_bar_menu_icon_color`: 메뉴 아이콘
- `theme_chatroom_input_bar_menu_button_color`: 메뉴 버튼 및 입력 필드 배경
- `theme_chatroom_input_bar_send_icon_color`: 보내기 아이콘
- `theme_chatroom_input_bar_send_button_color`: 보내기 버튼 배경

## 5. Image Guidelines

이미지는 샘플과 동일한 파일명으로 교체한다. 이미지와 컬러가 같은 요소에 동시에 쓰이면 이미지가 우선 적용된다.

필수 폴더:

- `drawable-xhdpi`
- `drawable-xxhdpi`
- `drawable-land-xhdpi`
- `drawable-land-xxhdpi`
- `drawable-sw600dp`
- `drawable-sw600dp-land`

이미지 제작 기준:

- 기본 제작 기준은 1080 x 1920 해상도, `xxhdpi`다.
- 메인 배경과 채팅방 배경 이미지는 가로:세로 1:2 비율을 유지한다.
- 스플래시는 OS 12 미만에서만 적용될 수 있다.
- 세로 스플래시: `drawable-xhdpi` 720 x 1280, `drawable-xxhdpi` 1440 x 2560, `drawable-sw600dp` 1440 x 2560
- 가로 스플래시: `drawable-land-xhdpi` 1280 x 720, `drawable-land-xxhdpi` 2560 x 1440, `drawable-sw600dp-land` 2560 x 1440
- 기본 프로필 이미지는 최소 1개, 최대 3개까지 준비할 수 있다.
- 탭 아이콘은 최소 56dp 크기로 제작한다.

## 6. User-Created Asset Checklist

사용자는 아래 에셋을 테마 콘셉트에 맞게 생성하거나 샘플 파일을 같은 filename으로 교체한다. Android는 동일한 base filename을 density/resource qualifier 폴더별로 유지해야 한다.

### App And Theme Icons

| Area | Filename | Folders |
| --- | --- | --- |
| Launcher icon | `ic_launcher.png` | `src/main/res/mipmap-*` |
| Launcher round icon | `ic_launcher_round.png` | `src/main/res/mipmap-*` |
| Launcher foreground | `ic_launcher_foreground.png` | `src/main/res/mipmap-*` |
| Launcher background | `ic_launcher_background.png` | `src/main/res/mipmap-*` |
| Web/high-res icon | `ic_launcher-web.png` | `src/main/` |

### Main Tab Icons

| Area | Filename | State |
| --- | --- | --- |
| Friends tab | `theme_maintab_ico_friends_image.png` | normal |
| Friends tab | `theme_maintab_ico_friends_focused_image.png` | selected |
| Chats tab | `theme_maintab_ico_chats_image.png` | normal |
| Chats tab | `theme_maintab_ico_chats_focused_image.png` | selected |
| Now tab | `theme_maintab_ico_now_image.png` | normal |
| Now tab | `theme_maintab_ico_now_focused_image.png` | selected |
| Shopping tab | `theme_maintab_ico_shopping_image.png` | normal |
| Shopping tab | `theme_maintab_ico_shopping_focused_image.png` | selected |
| More tab | `theme_maintab_ico_more_image.png` | normal |
| More tab | `theme_maintab_ico_more_focused_image.png` | selected |
| Piccoma tab | `theme_maintab_ico_piccoma_image.png` | normal, regional/global |
| Piccoma tab | `theme_maintab_ico_piccoma_focused_image.png` | selected, regional/global |
| Call tab | `theme_maintab_ico_call_image.png` | normal |
| Call tab | `theme_maintab_ico_call_focused_image.png` | selected |

### Common Images

| Area | Filename | Notes |
| --- | --- | --- |
| Main background | `theme_background_image.png` | optional if color-only theme |
| Chat background | `theme_chatroom_background_image.png` | optional if color-only theme |
| Splash portrait/landscape | `theme_splash_image.png` | OS 12 미만에서만 적용될 수 있음 |
| Main tab background | `theme_maintab_cell_image.9.png` | 9-patch |
| Add friend button | `theme_find_add_friend_button_image.png` | normal |
| Add friend button | `theme_find_add_friend_button_pressed_image.png` | pressed |
| Default profile 1 | `theme_profile_01_image.png` | minimum 1 profile image |
| Default profile 2 | `theme_profile_02_image.png` | optional |
| Default profile 3 | `theme_profile_03_image.png` | optional |
| Full profile 1 | `theme_profile_01_image_full.png` | optional, when sample includes full profile |
| Full profile 2 | `theme_profile_02_image_full.png` | optional |
| Full profile 3 | `theme_profile_03_image_full.png` | optional |

### Chat Bubble Images

| Area | Filename | Notes |
| --- | --- | --- |
| Sent bubble first | `theme_chatroom_bubble_me_01_image.9.png` | 9-patch |
| Sent bubble grouped | `theme_chatroom_bubble_me_02_image.9.png` | 9-patch |
| Received bubble first | `theme_chatroom_bubble_you_01_image.9.png` | 9-patch |
| Received bubble grouped | `theme_chatroom_bubble_you_02_image.9.png` | 9-patch |

### Passcode Images

| Area | Filename | Notes |
| --- | --- | --- |
| Passcode background | `theme_passcode_background_image.png` | optional if color-only theme |
| Passcode bullet 1 | `theme_passcode_01_image.png` | normal |
| Passcode bullet 2 | `theme_passcode_02_image.png` | normal |
| Passcode bullet 3 | `theme_passcode_03_image.png` | normal |
| Passcode bullet 4 | `theme_passcode_04_image.png` | normal |
| Passcode bullet 1 | `theme_passcode_01_checked_image.png` | checked |
| Passcode bullet 2 | `theme_passcode_02_checked_image.png` | checked |
| Passcode bullet 3 | `theme_passcode_03_checked_image.png` | checked |
| Passcode bullet 4 | `theme_passcode_04_checked_image.png` | checked |

샘플에 존재하는 파일은 모두 같은 이름으로 유지한다. 특정 테마에서 이미지를 쓰지 않더라도, 샘플 리소스 참조가 남아 있으면 placeholder나 투명/단색 PNG라도 유지하는 편이 안전하다.

## 7. Nine-Patch Rules

말풍선과 탭바 배경처럼 크기가 변하는 이미지는 9-patch가 필요하다.

- 9-patch 파일은 `.9.png` 확장자를 유지한다.
- 늘어나는 영역과 콘텐츠 영역을 명확히 지정한다.
- 말풍선 중앙은 단순하게 유지해 긴 메시지에서도 질감이 깨지지 않게 한다.
- 송신/수신 말풍선은 색상, 명도, 방향성이 분명히 구분되어야 한다.
- 짧은 메시지, 긴 메시지, 연속 메시지 모두에서 모서리와 꼬리가 어색하지 않아야 한다.

주요 말풍선 파일:

- `theme_chatroom_bubble_me_01_image.9.png`: 보낸 첫 번째 말풍선
- `theme_chatroom_bubble_me_02_image.9.png`: 보낸 두 번째 이후 말풍선
- `theme_chatroom_bubble_you_01_image.9.png`: 받은 첫 번째 말풍선
- `theme_chatroom_bubble_you_02_image.9.png`: 받은 두 번째 이후 말풍선

## 8. Required UI Areas

### Manifest And Build

- `build.gradle.kts`의 `namespace`, `applicationId`, `versionName`, `versionCode`
- `src/main/AndroidManifest.xml`의 package, icon, label
- `com.kakao.talk.v2.theme` permission
- `com.kakao.talk.theme.action.MAIN` intent-filter
- 다크 테마는 `com.kakao.talk.theme_style` meta-data에 `dark` 지정

### Common And Splash

- 런처 아이콘
- `theme_profile_01_image.png`부터 `theme_profile_03_image.png`
- `theme_profile_01_image_full.png`부터 `theme_profile_03_image_full.png`
- `theme_splash_image.png`

### Main

- `theme_background_color`
- `theme_background_image.png`
- `theme_header_color`
- `theme_header_cell_color`
- `theme_body_cell_color`
- `theme_body_cell_pressed_color`
- `theme_body_cell_border_color`
- `theme_body_secondary_cell_color`

### Main Tabs

- `theme_maintab_cell_color`
- `theme_maintab_cell_image.9.png`
- `theme_maintab_ico_friends_image.png`
- `theme_maintab_ico_friends_focused_image.png`
- `theme_maintab_ico_chats_image.png`
- `theme_maintab_ico_chats_focused_image.png`
- `theme_maintab_ico_now_image.png`
- `theme_maintab_ico_now_focused_image.png`
- `theme_maintab_ico_shopping_image.png`
- `theme_maintab_ico_shopping_focused_image.png`
- `theme_maintab_ico_more_image.png`
- `theme_maintab_ico_more_focused_image.png`
- `theme_maintab_ico_piccoma_image.png`
- `theme_maintab_ico_piccoma_focused_image.png`
- `theme_maintab_ico_call_image.png`
- `theme_maintab_ico_call_focused_image.png`

### Chatroom

- `theme_chatroom_background_color`
- `theme_chatroom_background_image.png`
- 송신/수신 말풍선 9-patch 이미지
- 송신/수신 말풍선 텍스트 색상
- 읽지 않음 숫자 색상
- 입력창 배경, 텍스트, 메뉴 아이콘, 전송 버튼

### Passcode

- `theme_passcode_background_color`
- `theme_passcode_background_image.png`
- `theme_passcode_color`
- `theme_passcode_keypad_color`
- `theme_passcode_keypad_pressed_color`
- `theme_passcode_keypad_background_color`
- `theme_passcode_keypad_pressed_background_color`
- `theme_passcode_pattern_line_color`

### Direct Share And Notification

- `theme_direct_share_color`
- `theme_direct_share_button_color`
- `theme_direct_share_background_color`
- `theme_notification_color`
- `theme_notification_background_color`
- `theme_notification_background_pressed_color`

## 9. Generation Workflow

1. Theme Brief를 작성한다.
2. 디자인 토큰을 확정한다.
3. 샘플 Android 테마 프로젝트를 복사한다.
4. `namespace`, `applicationId`, package, theme title을 새 테마에 맞게 변경한다.
5. `src/main/theme/values/colors.xml`의 색상 리소스를 업데이트한다.
6. `src/main/theme/values/strings.xml`의 `theme_title`, `app_name`을 업데이트한다.
7. `src/main/theme/drawable-*` 이미지를 동일한 파일명으로 교체한다.
8. 9-patch 이미지를 검토한다.
9. Android 테마 검증 스크립트를 실행한다.
10. Gradle로 APK를 빌드하고 서명한다.
11. 설치 후 카카오톡 테마 설정에서 실제 적용을 확인한다.

## 10. Validation Checklist

- `src/main/theme/values/colors.xml`이 존재한다.
- `src/main/theme/values/strings.xml`이 존재한다.
- `theme_title`과 `app_name`이 새 테마 이름으로 설정되어 있다.
- 모든 필수 색상 리소스가 누락되지 않았다.
- `AndroidManifest.xml`에 테마 permission과 intent-filter가 있다.
- 다크 테마일 경우 `com.kakao.talk.theme_style` 값이 `dark`다.
- `src/main/theme/drawable-*` 폴더가 샘플 구조와 맞다.
- 사용자 제작 아이콘과 이미지가 샘플 파일명 및 density 폴더 구조와 일치한다.
- XML selector가 참조하는 drawable/color 리소스가 존재한다.
- 9-patch 파일명이 `.9.png`로 유지되어 있다.
- APK 설치 시 불필요한 권한을 요청하지 않는다.

## 11. Theme Request Template

```markdown
## Android Theme Brief

- Name:
- Package:
- Concept:
- Mood keywords:
- Mode:
- Main background:
- Chat background:
- Header color:
- Accent color:
- Send bubble:
- Receive bubble:
- Text color:
- Image style:
- Special details:

## Notes

-
```

## 12. Quality Bar

좋은 Android 테마는 APK로 안정적으로 빌드되고, 카카오톡 안에서 읽기 쉬우며, 모든 주요 상태가 명확해야 한다. 이미지가 눈에 띄는 테마라도 텍스트 대비와 말풍선 가독성이 최우선이다.
