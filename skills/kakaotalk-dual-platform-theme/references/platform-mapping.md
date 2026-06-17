# KakaoTalk iOS And Android Platform Mapping

Use this reference when creating one KakaoTalk design across iOS and Android.

## Output Differences

| Area | iOS | Android |
| --- | --- | --- |
| Final package | `.ktheme` ZIP archive | APK |
| Theme root | `KakaoTalkTheme.css`, `Images/` | Android project |
| Main colors | CSS-like selectors | `src/main/theme/values/colors.xml` |
| Images | `Images/name@2x.png`, `Images/name@3x.png` | `src/main/theme/drawable-*` |
| Stretchable bubbles | image + cap inset in CSS | `.9.png` 9-patch |
| Dark mode | `-kakaotalk-theme-style: 'dark';` | manifest meta-data `com.kakao.talk.theme_style=dark` |
| Install check | Open `.ktheme` with KakaoTalk | Install APK, apply in KakaoTalk themes |

## Shared Tokens

Define these once:

- `background.main`
- `background.chat`
- `background.passcode`
- `surface.header`
- `surface.body`
- `surface.bodyPressed`
- `surface.tab`
- `text.header`
- `text.title`
- `text.titlePressed`
- `text.paragraph`
- `text.description`
- `accent.primary`
- `accent.pressed`
- `border.subtle`
- `bubble.send`
- `bubble.sendText`
- `bubble.receive`
- `bubble.receiveText`
- `badge.unread`
- `input.background`
- `input.text`
- `input.menuIcon`
- `input.sendButton`
- `input.sendIcon`

## Color Mapping

| Token | iOS | Android |
| --- | --- | --- |
| `background.main` | `MainViewStyle-Primary background-color` | `theme_background_color` |
| `background.chat` | `BackgroundStyle-ChatRoom background-color` | `theme_chatroom_background_color` |
| `background.passcode` | `BackgroundStyle-Passcode background-color` | `theme_passcode_background_color` |
| `surface.header` | header/nav image or related header surface | `theme_header_cell_color` |
| `surface.body` | `MainViewStyle-Primary -ios-normal-background-color` | `theme_body_cell_color` |
| `surface.bodyPressed` | `MainViewStyle-Primary -ios-selected-background-color` | `theme_body_cell_pressed_color` |
| `surface.tab` | `TabBarStyle-Main background-color` | `theme_maintab_cell_color` |
| `text.header` | `HeaderStyle-Main -ios-text-color` | `theme_header_color` |
| `text.title` | `MainViewStyle-Primary -ios-text-color` | `theme_title_color` |
| `text.titlePressed` | `MainViewStyle-Primary -ios-highlighted-text-color` | `theme_title_pressed_color` |
| `text.paragraph` | `MainViewStyle-Primary -ios-paragraph-text-color` | `theme_paragraph_color` |
| `text.description` | `MainViewStyle-Primary -ios-description-text-color` | `theme_description_color` |
| `border.subtle` | `SectionTitleStyle-Main border-color` | `theme_body_cell_border_color` |
| `bubble.sendText` | `MessageCellStyle-Send -ios-text-color` | `theme_chatroom_bubble_me_color` |
| `bubble.receiveText` | `MessageCellStyle-Receive -ios-text-color` | `theme_chatroom_bubble_you_color` |
| `badge.unread` | `MessageCellStyle-Send/Receive -ios-unread-text-color` | `theme_chatroom_unread_count_color` |
| `input.background` | `InputBarStyle-Chat background-color` | `theme_chatroom_input_bar_background_color` |
| `input.text` | `InputBarStyle-Chat -ios-button-text-color` | `theme_chatroom_input_bar_color` |
| `input.menuIcon` | `InputBarStyle-Chat -ios-button-normal-foreground-color` | `theme_chatroom_input_bar_menu_icon_color` |
| `input.sendButton` | `InputBarStyle-Chat -ios-send-normal-background-color` | `theme_chatroom_input_bar_send_button_color` |
| `input.sendIcon` | `InputBarStyle-Chat -ios-send-normal-foreground-color` | `theme_chatroom_input_bar_send_icon_color` |

## Image Mapping

| Intent | iOS | Android |
| --- | --- | --- |
| Theme icon | `commonIcoTheme@2x/@3x.png` | `mipmap-*/ic_launcher.png`, `ic_launcher-web.png` |
| Main background | `mainBgImage@2x/@3x.png` | `theme_background_image.png` |
| Chat background | `chatroomBgImage@2x/@3x.png` | `theme_chatroom_background_image.png` |
| Default profile | `profileImg01@2x/@3x.png` | `theme_profile_01_image.png` |
| Add friend | `findBtnAddFriend@2x/@3x.png` | `theme_find_add_friend_button_image.png` |
| Sent first bubble | `chatroomBubbleSend01@2x/@3x.png` | `theme_chatroom_bubble_me_01_image.9.png` |
| Sent grouped bubble | `chatroomBubbleSend02@2x/@3x.png` | `theme_chatroom_bubble_me_02_image.9.png` |
| Received first bubble | `chatroomBubbleReceive01@2x/@3x.png` | `theme_chatroom_bubble_you_01_image.9.png` |
| Received grouped bubble | `chatroomBubbleReceive02@2x/@3x.png` | `theme_chatroom_bubble_you_02_image.9.png` |
| Passcode background | `passcodeBgImage@2x/@3x.png` | `theme_passcode_background_image.png` |

## Visual Parity Rules

- Use the same palette and mood, but respect platform-specific density and packaging.
- Keep chat readability identical in priority on both platforms.
- Recreate 9-patch stretch behavior on Android instead of directly reusing iOS cap-inset images.
- Recreate iOS `@2x/@3x` assets from the same source art instead of reusing Android density folders.
- Do not let platform-only tabs break the system. Android includes Now, Shopping, Piccoma, and Call resources; iOS samples may vary by region.
- If one platform lacks an exact UI element, apply the closest shared token rather than inventing a new palette.

## Validation Order

1. Validate shared design tokens and contrast.
2. Validate iOS source folder.
3. Package iOS `.ktheme`.
4. Validate final iOS `.ktheme`.
5. Validate Android source project.
6. Build Android APK.
7. Validate APK structure.
8. Install and smoke-test both themes when a device/simulator is available.
