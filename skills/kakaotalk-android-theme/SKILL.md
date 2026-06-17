---
name: kakaotalk-android-theme
description: Build, modify, validate, and package KakaoTalk Android user themes from sample Android theme projects. Use when Codex needs to create or edit a KakaoTalk Android theme APK, inspect Android theme resources, update src/main/theme colors or drawable assets, map Android KakaoTalk theme resource names to UI areas, configure dark mode metadata, or prepare a buildable installable Android theme app.
---

# KakaoTalk Android Theme

## Overview

Use this skill to work on KakaoTalk Android user themes. Android themes are Android app projects that expose KakaoTalk theme resources under `src/main/theme` and `src/main/theme-adv`, then build to installable APK files.

## Workflow

1. Start from an official Android sample theme project or an existing theme project.
2. Update `build.gradle.kts`, `src/main/AndroidManifest.xml`, and theme strings for package, app name, version, and optional dark mode.
3. Edit `src/main/theme/values/colors.xml` for theme colors using `#rrggbb` or `#aarrggbb`.
4. Replace PNG and 9-patch assets in `src/main/theme/drawable-*` with the same filenames and density/resource qualifiers.
5. Keep selector XML in `src/main/theme-adv` aligned with the color and drawable resources.
6. Run `scripts/validate_android_theme.py` on the theme project.
7. Build the APK with the project Gradle wrapper, then sign according to the user's release/debug needs.
8. Install and verify in KakaoTalk Settings > Themes.

## Source Conventions

- Treat Android themes as Android app projects, not `.ktheme` archives.
- Keep layout and Kotlin app logic minimal. Change theme resources, metadata, labels, package identifiers, and assets.
- Required theme resources live under `src/main/theme`; advanced selectors live under `src/main/theme-adv`.
- Image replacement must preserve exact resource base names. Use `.9.png` for stretchable 9-patch assets when the sample uses `.9.png`.
- If both image and color are defined for the same UI element, the image generally has priority.
- Design against the xxhdpi 1080 x 1920 basis unless the guide or sample names a different size.
- Do not add permissions beyond the KakaoTalk theme permission unless the user explicitly asks and understands the risk.

## References

Read `references/android-theme-guide.md` when mapping a UI request to Android resource names, density folders, manifest metadata, dark mode, build steps, or install checks. It summarizes the KakaoTalk Android user theme guide 26.x and the Apeach sample project structure.

## Scripts

Use this from the skill directory:

```bash
python3 scripts/validate_android_theme.py /path/to/android-theme-project
```

Build from the Android project root:

```bash
./gradlew assembleDebug
```

Use release signing only when the user asks for a distributable release APK and provides or approves signing credentials.
