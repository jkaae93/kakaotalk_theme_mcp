# KakaoTalk Android Theme Guide

This reference summarizes the KakaoTalk Android user theme guide 26.x and the Apeach sample Android theme project.

## Package Model

- Android themes are built as APK files.
- Start from the official sample project when possible.
- Theme resources are read from `src/main/theme` and `src/main/theme-adv`.
- The app must declare `com.kakao.talk.v2.theme`.
- The theme activity must include the `com.kakao.talk.theme.action.MAIN` intent-filter.
- The sample uses Kotlin and Gradle. Do not rewrite app logic unless necessary.

## Important Paths

- `build.gradle.kts`: namespace, compile SDK, build tools, version, application id, source sets.
- `src/main/AndroidManifest.xml`: package, icon, label, permissions, queries, activity, theme intent-filter, dark mode metadata.
- `src/main/theme/values/colors.xml`: main editable theme colors.
- `src/main/theme/values/strings.xml`: `theme_title` and `app_name`.
- `src/main/theme/drawable-*`: theme PNG and 9-patch images.
- `src/main/theme-adv/color`: color selectors.
- `src/main/theme-adv/drawable`: drawable selectors and advanced color drawables.
- `src/main/res`: launcher/app shell resources.

## Build Settings

In the sample, `build.gradle.kts` applies Android application and Kotlin plugins and configures:

- `namespace`
- `compileSdk`
- `buildToolsVersion`
- `minSdk`
- `targetSdk`
- `versionName`
- `versionCode`
- `applicationId`
- `sourceSets.main.res.srcDirs("src/main/theme", "src/main/theme-adv")`

When creating a new theme, update `namespace` and `applicationId` consistently with `AndroidManifest.xml` and Kotlin package paths when needed.

## Dark Mode

For a theme intentionally designed as dark mode, add this inside `<application>` in `src/main/AndroidManifest.xml`:

```xml
<meta-data
    android:name="com.kakao.talk.theme_style"
    android:value="dark" />
```

If this metadata is absent, the theme behaves as light mode.

## Color Resources

Use `#rrggbb` or `#aarrggbb`.

Core text and list colors:

- `theme_header_color`: main tab header title and icons.
- `theme_section_title_color`: section title.
- `theme_title_color`: names, titles, and selected chip text.
- `theme_title_pressed_color`: pressed title/name.
- `theme_paragraph_color`: last message/body paragraph.
- `theme_paragraph_pressed_color`: pressed paragraph.
- `theme_description_color`: status message and secondary text.
- `theme_description_pressed_color`: pressed description.
- `theme_feature_primary_color`: service button text/icon.
- `theme_feature_primary_pressed_color`: pressed service text/icon.
- `theme_feature_browse_tab_color`: Browse/Now tab text.
- `theme_feature_browse_tab_focused_color`: focused Browse/Now tab text.

Background and cell colors:

- `theme_background_color`: main background.
- `theme_chatroom_background_color`: chat room background.
- `theme_passcode_background_color`: passcode background.
- `theme_header_cell_color`: header/status bar background.
- `theme_body_cell_color`: normal list/content cell.
- `theme_body_cell_pressed_color`: pressed list/content cell.
- `theme_body_cell_border_color`: dividers and borders.
- `theme_body_secondary_cell_color`: third/fourth tab body background.
- `theme_maintab_cell_color`: main tab bar background.
- `theme_tab_lightbannerbadge_background_color`: light banner badge.
- `theme_tab_bannerbadge_background_color`: tab banner badge. Prefer a dark color.

Direct share and notifications:

- `theme_direct_share_color`
- `theme_direct_share_button_color`
- `theme_direct_share_background_color`
- `theme_notification_color`
- `theme_notification_background_color`
- `theme_notification_background_pressed_color`

Passcode:

- `theme_passcode_color`
- `theme_passcode_keypad_color`
- `theme_passcode_keypad_pressed_color`
- `theme_passcode_keypad_background_color`
- `theme_passcode_keypad_pressed_background_color`
- `theme_passcode_pattern_line_color`

Chat room:

- `theme_chatroom_bubble_me_color`: sent bubble text.
- `theme_chatroom_bubble_you_color`: received bubble text.
- `theme_chatroom_unread_count_color`: unread count.
- `theme_chatroom_input_bar_color`: input text.
- `theme_chatroom_input_bar_background_color`: input bar background.
- `theme_chatroom_input_bar_menu_icon_color`: menu icon.
- `theme_chatroom_input_bar_menu_button_color`: menu button and input field background.
- `theme_chatroom_input_bar_send_icon_color`: send icon.
- `theme_chatroom_input_bar_send_button_color`: send button background.

## Image Resources

Replace images with the same filenames in the same resource-qualified folders.

Required density/orientation folders in the sample:

- `drawable-xhdpi`
- `drawable-xxhdpi`
- `drawable-land-xhdpi`
- `drawable-land-xxhdpi`
- `drawable-sw600dp`
- `drawable-sw600dp-land`

The guide recommends designing around 1080 x 1920 for xxhdpi.

Splash:

- Portrait xhdpi: 720 x 1280.
- Portrait xxhdpi/sw600dp: 1440 x 2560.
- Landscape xhdpi: 1280 x 720.
- Landscape xxhdpi/sw600dp-land: 2560 x 1440.
- Splash images may only apply below Android OS 12 because of OS policy changes.

Backgrounds:

- `theme_background_image.png`: main background, top-cropped, 1:2 ratio.
- `theme_chatroom_background_image.png`: chat room background, 1:2 ratio.
- `theme_passcode_background_image.png`: passcode background, center-cropped.

Profiles:

- `theme_profile_01_image.png` to `theme_profile_03_image.png`: default profile images, minimum 1 and maximum 3.
- Full profile images may use `theme_profile_01_image_full.png` to `theme_profile_03_image_full.png` in `drawable-nodpi` when present.

Main tab:

- `theme_maintab_cell_image.9.png`: main tab background 9-patch.
- `theme_maintab_ico_friends_image.png` and `_focused_image.png`.
- `theme_maintab_ico_chats_image.png` and `_focused_image.png`.
- `theme_maintab_ico_now_image.png` and `_focused_image.png`.
- `theme_maintab_ico_shopping_image.png` and `_focused_image.png`.
- `theme_maintab_ico_more_image.png` and `_focused_image.png`.
- `theme_maintab_ico_piccoma_image.png` and `_focused_image.png` for global/Japan variants.
- `theme_maintab_ico_call_image.png` and `_focused_image.png`.
- Tab icons should be at least 56dp.

Chat bubbles:

- `theme_chatroom_bubble_me_01_image.9.png`: first sent bubble.
- `theme_chatroom_bubble_me_02_image.9.png`: grouped sent bubble.
- `theme_chatroom_bubble_you_01_image.9.png`: first received bubble.
- `theme_chatroom_bubble_you_02_image.9.png`: grouped received bubble.
- Keep `.9.png` when the sample uses 9-patch.

## Install Checks

- Build, compile, and sign the APK.
- Android KakaoTalk themes should not request runtime permissions. If installation asks for permissions, inspect the manifest.
- After install, open KakaoTalk More > Settings > Themes and apply the theme.
- If the theme does not apply, confirm that `MainActivity` declares the `com.kakao.talk.theme.action.MAIN` intent-filter.
