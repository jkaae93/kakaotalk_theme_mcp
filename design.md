# KakaoTalk iOS Theme Design Guidelines

이 문서는 카카오톡 iOS 테마를 일관되게 생성하기 위한 디자인 가이드라인이다. 테마 생성 시에는 앱의 레이아웃을 바꾸지 않고, 색상, 이미지, 투명도, 메시지 말풍선 inset 등 KakaoTalk 테마가 허용하는 범위 안에서만 표현한다.

## 1. Theme Brief

테마를 만들기 전에 아래 항목을 먼저 확정한다.

- 테마 이름: 카카오톡 설정에 표시될 이름
- 콘셉트: 예) 고요한 새벽, 빈티지 문구점, 체리 소다, 미니멀 다크
- 분위기 키워드: 3-6개
- 대상 모드: light, dark, 또는 system-neutral
- 주요 색상: 배경, 강조색, 텍스트, 보조 텍스트, 경계선
- 이미지 방향: 실사형, 일러스트형, 패턴형, 단색형
- 말풍선 스타일: 둥근 정도, 채도, 그림자 사용 여부, 송신/수신 대비
- 접근성 기준: 배경과 텍스트의 대비를 충분히 확보

## 2. Output Structure

완성 테마 폴더는 아래 구조를 따른다.

```text
ThemeName/
  KakaoTalkTheme.css
  Images/
    commonIcoTheme@2x.png
    commonIcoTheme@3x.png
    ...
```

최종 배포 파일은 `KakaoTalkTheme.css`와 `Images/`가 압축 파일의 루트에 들어간 `.ktheme` 파일이어야 한다.

## 3. Design Token Rules

테마 생성 시 먼저 디자인 토큰을 정의하고, CSS와 이미지 제작에 같은 토큰을 사용한다.

```text
background.primary
background.secondary
background.chat
surface.input
text.primary
text.secondary
text.inverse
accent.primary
accent.pressed
border.subtle
bubble.send
bubble.sendText
bubble.receive
bubble.receiveText
badge.unread
```

색상은 HEX 형식으로 기록한다. 투명도가 필요한 경우 CSS의 alpha 속성을 함께 사용한다.

## 4. Color Guidelines

- 메인 화면 배경과 채팅방 배경은 같은 계열이어도 명도 차이를 둔다.
- 송신 말풍선과 수신 말풍선은 형태보다 색으로 먼저 구분되게 한다.
- 본문 텍스트는 배경 위에서 충분히 선명해야 한다.
- 보조 텍스트, 시간, 설명 문구는 흐리게 만들되 읽을 수 있어야 한다.
- 선택/눌림 상태 색상은 기본 상태보다 약간 어둡거나 채도가 낮아야 한다.
- 다크 테마는 `ManifestStyle`에 `-kakaotalk-theme-style: 'dark';`를 사용한다.

## 5. Image Guidelines

이미지 에셋은 CSS에서 scale suffix 없이 참조하고, 실제 파일은 `@2x`, `@3x`를 제공한다.

예:

```css
-ios-background-image: 'chatroomBgImage.png';
```

```text
Images/chatroomBgImage@2x.png
Images/chatroomBgImage@3x.png
```

이미지 제작 규칙:

- `@2x`를 기준으로 디자인하고 `@3x`를 함께 생성한다.
- 같은 base filename을 유지한다.
- PNG 형식을 사용한다.
- 배경 이미지는 텍스트 가독성을 해치지 않도록 대비와 패턴 강도를 낮춘다.
- 말풍선 이미지는 늘어나는 영역을 고려해 가장자리와 중앙 질감을 단순하게 유지한다.
- `commonIcoTheme`는 테마 목록에서 보이는 대표 아이콘이며 162 x 162 px 기준으로 만든다.

## 6. User-Created Asset Checklist

사용자는 아래 에셋을 테마 콘셉트에 맞게 생성하거나 샘플 파일을 같은 base filename으로 교체한다. iOS는 CSS에서 `name.png`로 참조하더라도 실제 파일은 보통 `Images/name@2x.png`, `Images/name@3x.png` 쌍으로 만든다.

### Required Icons

| Area | Base filename | States |
| --- | --- | --- |
| Theme list | `commonIcoTheme.png` | normal |
| Main tab Friends | `maintabIcoFriends.png` | normal |
| Main tab Friends | `maintabIcoFriendsSelected.png` | selected |
| Main tab Chats | `maintabIcoChats.png` | normal |
| Main tab Chats | `maintabIcoChatsSelected.png` | selected |
| Main tab Now/Open Chats | `maintabIcoNow.png` | normal |
| Main tab Now/Open Chats | `maintabIcoNowSelected.png` | selected |
| Main tab Shopping | `maintabIcoShopping.png` | normal |
| Main tab Shopping | `maintabIcoShoppingSelected.png` | selected |
| Main tab More | `maintabIcoMore.png` | normal |
| Main tab More | `maintabIcoMoreSelected.png` | selected |
| Main tab Piccoma | `maintabIcoPiccoma.png` | normal, regional/global |
| Main tab Piccoma | `maintabIcoPiccomaSelected.png` | selected, regional/global |
| Main tab Call | `maintabIcoCall.png` | normal |
| Main tab Call | `maintabIcoCallSelected.png` | selected |
| Add friend | `findBtnAddFriend.png` | normal |

### Required Images

| Area | Base filename | Notes |
| --- | --- | --- |
| Main background | `mainBgImage.png` | optional if color-only theme |
| Chat background | `chatroomBgImage.png` | optional if color-only theme |
| Default profile | `profileImg01.png` | at least one profile image when replacing profile art |
| Sent bubble first | `chatroomBubbleSend01.png` | cap inset/stretch-aware |
| Sent bubble grouped | `chatroomBubbleSend02.png` | cap inset/stretch-aware |
| Received bubble first | `chatroomBubbleReceive01.png` | cap inset/stretch-aware |
| Received bubble grouped | `chatroomBubbleReceive02.png` | cap inset/stretch-aware |
| Passcode background | `passcodeBgImage.png` | optional if color-only theme |
| Passcode keypad pressed | `passcodeKeypadPressed.png` | pressed keypad state |

### Optional Images

| Area | Base filename | Notes |
| --- | --- | --- |
| Default profile variants | `profileImg02.png`, `profileImg03.png` | use when the sample supports multiple defaults |
| Passcode bullets | `passcodeBullet01.png` through `passcodeBullet04.png` | use the sample's exact filenames |
| Passcode selected bullets | `passcodeBulletSelected01.png` through `passcodeBulletSelected04.png` | use the sample's exact filenames |
| Main tab background | `maintabBgImage.png` | optional image background for tab bar |

정확한 파일명은 출발점으로 사용하는 iOS 샘플의 `KakaoTalkTheme.css`에 맞춘다. 샘플에 있는 이미지는 삭제하지 말고 같은 base filename으로 교체하는 것을 기본 원칙으로 한다.

## 7. Required UI Areas

아래 영역은 테마마다 반드시 점검한다.

### Manifest

- `ManifestStyle`
- 테마 이름, 버전, URL, 작성자, 고유 theme id

### Main Tabs

- `TabBarStyle-Main`
- 메인 탭 배경
- Friends, Chats, Now/Open Chats, Shopping, Call, More 아이콘의 normal/selected 상태

### Main View

- `HeaderStyle-Main`
- `MainViewStyle-Primary`
- `MainViewStyle-Secondary`
- `SectionTitleStyle-Main`
- 목록 배경, 헤더 텍스트, 본문 텍스트, 설명 텍스트, 구분선, 선택 상태

### Profile And Feature

- `DefaultProfileStyle`
- `FeatureStyle-Primary`
- `ButtonStyle-AddFriend`
- 기본 프로필 이미지와 주요 기능 버튼

### Chat Room

- `BackgroundStyle-ChatRoom`
- `InputBarStyle-Chat`
- 채팅방 배경, 입력창, 전송 버튼, 메뉴 버튼, 입력 텍스트

### Messages

- `MessageCellStyle-Send`
- `MessageCellStyle-Receive`
- 송신/수신 말풍선 이미지, 선택 상태 이미지, grouped 말풍선, 텍스트 색상, unread 색상, edge inset

### Passcode

- `BackgroundStyle-Passcode`
- `LabelStyle-PasscodeTitle`
- `PasscodeStyle`
- 배경, 제목, bullet 이미지, keypad 색상과 눌림 상태

### Notifications And Banners

- `BackgroundStyle-MessageNotificationBar`
- `LabelStyle-MessageNotificationBarName`
- `LabelStyle-MessageNotificationBarMessage`
- `BackgroundStyle-DirectShareBar`
- `BottomBannerStyle`

## 8. Bubble Rules

말풍선은 테마의 인상을 가장 크게 좌우하므로 별도 기준을 둔다.

- 송신 말풍선과 수신 말풍선의 명도 차이를 명확히 둔다.
- 긴 메시지, 짧은 메시지, 이모지만 있는 메시지 모두 어색하지 않아야 한다.
- edge inset은 텍스트가 말풍선 가장자리와 너무 붙지 않도록 설정한다.
- CSS의 inset 값은 1x 좌표 기준이며 보통 `top left bottom right` 순서다.
- 선택 상태 이미지는 기본 이미지와 충분히 구분되되 과하게 튀지 않게 한다.

예:

```css
MessageCellStyle-Send {
  -ios-background-image: 'chatroomBubbleSend01.png' 17px 17px;
  -ios-group-background-image: 'chatroomBubbleSend02.png' 17px 17px;
  -ios-title-edgeinsets: 8px 12px 8px 12px;
}
```

## 9. Generation Workflow

1. Theme Brief를 작성한다.
2. 디자인 토큰을 정의한다.
3. `KakaoTalkTheme.css`의 manifest, colors, image references를 업데이트한다.
4. `Images/`에 필요한 PNG 에셋을 같은 base filename으로 생성한다.
5. `@2x`, `@3x` 쌍이 누락되지 않았는지 확인한다.
6. 테마 폴더를 검증한다.
7. `.ktheme`로 패키징한다.
8. 최종 `.ktheme` 파일을 다시 검증한다.

## 10. Validation Checklist

- `KakaoTalkTheme.css`가 테마 폴더 루트에 있다.
- `Images/` 폴더가 테마 폴더 루트에 있다.
- CSS에서 참조한 이미지 base filename이 실제 `Images/` 안에 존재한다.
- 샘플이 `@2x`, `@3x`를 모두 사용한다면 새 이미지도 둘 다 제공한다.
- 사용자 제작 아이콘과 이미지가 샘플 CSS의 base filename과 일치한다.
- `.ktheme` 압축 루트에 불필요한 상위 폴더가 들어가지 않는다.
- `.DS_Store`, `__MACOSX/`, `._*` 파일이 포함되지 않는다.
- 텍스트와 배경 대비가 충분하다.
- 탭 selected/normal 상태가 구분된다.
- 채팅방 배경 위에서 송신/수신 말풍선이 잘 보인다.
- 입력창과 전송 버튼이 테마 색상과 조화롭다.

## 11. Theme Request Template

새 테마를 요청하거나 생성할 때 아래 형식을 사용한다.

```markdown
## Theme Brief

- Name:
- Concept:
- Mood keywords:
- Mode:
- Primary background:
- Chat background:
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

좋은 테마는 예쁜 색을 넣는 것보다 읽기 쉽고, 상태가 명확하고, 반복 사용해도 피로하지 않아야 한다. 모든 화면에서 같은 콘셉트가 느껴지되, 채팅방과 메인 화면의 역할 차이는 분명하게 유지한다.
