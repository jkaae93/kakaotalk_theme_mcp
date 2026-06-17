---
name: kakaotalk-dual-platform-theme
description: Create coordinated KakaoTalk themes for both iOS and Android from one design brief. Use when Codex needs to generate matching iOS .ktheme and Android APK theme outputs, map shared theme tokens to KakaoTalkTheme.css and Android colors.xml/drawable resources, keep visual parity across platforms, or plan/validate a dual-platform KakaoTalk theme package.
---

# KakaoTalk Dual Platform Theme

## Overview

Use this skill to create matching KakaoTalk themes for iOS and Android from a shared design system. It coordinates the existing iOS `.ktheme` workflow with the Android APK theme workflow while preserving each platform's package rules.

## Workflow

1. Build one shared Theme Brief with name, concept, mood, mode, palette, bubble style, image style, and package identifiers.
2. Define shared design tokens for background, text, accent, bubble, tab, passcode, notification, and input surfaces.
3. Map tokens to iOS `KakaoTalkTheme.css` selectors and Android `src/main/theme/values/colors.xml`.
4. Generate platform-specific images using the same art direction but each platform's filename, density, scale, and 9-patch rules.
5. Produce or update the iOS theme folder, then validate and package to `.ktheme`.
6. Produce or update the Android sample project, then validate and build to APK.
7. Compare the two outputs for visual parity: main background, chat background, tab icons, bubbles, input bar, passcode, notifications.
8. Re-run platform validators after packaging/building.

## Platform Boundaries

- iOS output is a `.ktheme` ZIP archive containing `KakaoTalkTheme.css` and `Images/` at archive root.
- Android output is an Android app project built into an APK.
- iOS image references usually omit scale suffixes while files use `@2x`/`@3x`.
- Android image references are Android resources under `drawable-*`; stretchable assets use `.9.png`.
- Do not force identical asset dimensions across platforms. Preserve shared visual language, not identical files.
- Keep layout fixed on both platforms.

## Use Other Skills

Use platform skills for the actual build details:

- Use `kakaotalk-ios-theme` for iOS CSS, image, validation, and `.ktheme` packaging.
- Use `kakaotalk-android-theme` for Android resource, manifest, validation, and APK build work.

## References

Read `references/platform-mapping.md` when converting shared tokens to platform-specific selectors, colors, images, package outputs, or validation checklists.

## Dual Output Checklist

- Shared brief exists.
- Shared palette and tokens are defined.
- iOS theme name, id, author, version, and optional dark style are set.
- Android app name, theme title, package/application id, version, and optional dark metadata are set.
- iOS `Images/` has required `@2x`/`@3x` variants when the sample uses both.
- Android `src/main/theme/drawable-*` assets preserve resource names and 9-patch files.
- Both platforms have readable text over main and chat backgrounds.
- Sent and received bubbles are distinguishable on both platforms.
- Both platform outputs pass validation before handoff.
