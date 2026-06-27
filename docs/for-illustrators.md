# KakaoTalk Theme Guide For Illustrators

이 문서는 카카오톡 테마를 그리고 싶은 일러스트 작가, 캐릭터 작가, 디지털 굿즈 제작자, 디자이너를 위한 시작 가이드입니다.

## Who This Is For

Use this project if you:

- want to create a KakaoTalk theme from your illustration style
- need a checklist of KakaoTalk theme icons and images
- want to know where each file appears inside KakaoTalk
- are preparing assets for a developer or theme packager
- want to make both iOS and Android versions of the same character theme

## What You Need To Draw First

Start with the visual identity:

- theme icon
- main tab icons
- selected/focused tab icons
- chat room background
- main screen background
- sent message bubble
- received message bubble
- default profile image
- passcode bullets and background
- optional splash/background variants

## iOS Asset Mindset

iOS KakaoTalk themes usually use:

- `KakaoTalkTheme.css`
- `Images/`
- `@2x` and `@3x` PNG variants
- `.ktheme` package output

Example:

```text
Images/chatroomBgImage@2x.png
Images/chatroomBgImage@3x.png
```

The CSS may reference `chatroomBgImage.png` while the actual files include scale suffixes.

## Android Asset Mindset

Android KakaoTalk themes use an Android app project:

```text
src/main/theme/
src/main/theme-adv/
src/main/res/
```

The same base filename must be preserved across resource folders. Stretchable bubbles and tab backgrounds often use `.9.png` 9-patch files.

Example:

```text
theme_chatroom_bubble_me_01_image.9.png
theme_chatroom_bubble_you_01_image.9.png
```

## Design Tips

- Make normal and selected tab icons visibly different.
- Keep chat bubbles readable over the chat room background.
- Keep message text contrast high.
- Avoid overly detailed textures inside stretchable bubble centers.
- Use the same character style across icon, profile, background, and bubbles.
- Prepare dark mode separately instead of simply darkening a light theme.

## How To Use The MCP

Ask your MCP client:

```text
List required assets for a dual-platform KakaoTalk theme.
```

or call:

```json
{
  "tool": "list_required_assets",
  "arguments": {
    "platform": "dual",
    "format": "markdown"
  }
}
```

After assets are prepared, validate the project:

```json
{
  "tool": "validate_android_theme",
  "arguments": {
    "path": "/path/to/android-theme-project"
  }
}
```

For iOS packaging:

```json
{
  "tool": "package_ios_ktheme",
  "arguments": {
    "theme_dir": "/path/to/ios-theme-folder",
    "output_path": "/path/to/theme.ktheme"
  }
}
```

## Search Phrases This Project Answers

- 카카오톡 테마 만들기
- 카톡 테마 제작 방법
- 카카오톡 테마 아이콘 파일명
- 카톡 테마 말풍선 이미지
- KakaoTalk theme assets
- KakaoTalk theme maker for illustrators
- KakaoTalk iOS .ktheme packaging
- KakaoTalk Android theme APK resources
