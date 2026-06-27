# FAQ

## What is KakaoTalk Theme MCP?

KakaoTalk Theme MCP is a local MCP server that helps creators prepare, validate, and package KakaoTalk iOS and Android theme assets. It is designed for illustrators, character artists, designers, and developers who make KakaoTalk themes.

## Who should use KakaoTalk Theme MCP?

Illustrators and designers should use it when they need a clear checklist of KakaoTalk theme icons, backgrounds, chat bubbles, passcode images, and platform-specific file names. Developers can use it to validate Android theme projects and package iOS `.ktheme` files.

## What images do I need for a KakaoTalk theme?

You usually need a theme icon, main tab icons, selected tab icons, main background, chat room background, default profile image, sent message bubbles, received message bubbles, passcode images, and optional splash images.

## Where are KakaoTalk theme tab icons used?

Tab icons appear in the main bottom tab bar. They usually need normal and selected states for Friends, Chats, Now/Open Chats, Shopping, More, Piccoma, and Call depending on the platform and regional sample.

## Why do KakaoTalk chat bubbles need special files?

Chat bubbles stretch depending on message length. iOS can use cap inset behavior through theme CSS, while Android uses `.9.png` 9-patch images. This keeps bubble corners and tails from distorting.

## What is the difference between iOS and Android KakaoTalk themes?

iOS themes are packaged as `.ktheme` archives with `KakaoTalkTheme.css` and `Images/`. Android themes are Android app projects with resources under `src/main/theme` and `src/main/theme-adv`, then built into APK files.

## Can this project generate illustrations automatically?

No. This project does not draw illustrations. It tells creators which assets to draw, where each file is used, and whether the resulting theme project is structurally valid.

## Does this support both Korean and English creators?

Yes. The repository uses Korean explanations for KakaoTalk creators and English keywords for search, GitHub discovery, and AI answer engines.

## Can I use this for character goods or creator merchandise?

Yes. This is useful for character creators who want to turn an illustration style into a KakaoTalk theme, digital goods, fan goods, or branded chat theme.

## How do I check required assets from an MCP client?

Call the `list_required_assets` tool with `platform` set to `ios`, `android`, or `dual`.

```json
{
  "platform": "dual",
  "format": "markdown"
}
```

## How do I validate an Android KakaoTalk theme?

Call `validate_android_theme` with the Android theme project path.

```json
{
  "path": "/path/to/android-theme-project"
}
```

## How do I package an iOS KakaoTalk theme?

Call `package_ios_ktheme` with a theme folder containing `KakaoTalkTheme.css` and `Images/`.

```json
{
  "theme_dir": "/path/to/ios-theme-folder",
  "output_path": "/path/to/theme.ktheme"
}
```
