#!/usr/bin/env python3
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ANDROID_NS = "{http://schemas.android.com/apk/res/android}"

REQUIRED_COLORS = {
    "theme_header_color",
    "theme_section_title_color",
    "theme_title_color",
    "theme_title_pressed_color",
    "theme_paragraph_color",
    "theme_paragraph_pressed_color",
    "theme_description_color",
    "theme_description_pressed_color",
    "theme_feature_primary_color",
    "theme_feature_primary_pressed_color",
    "theme_background_color",
    "theme_chatroom_background_color",
    "theme_passcode_background_color",
    "theme_header_cell_color",
    "theme_body_cell_color",
    "theme_body_cell_pressed_color",
    "theme_body_cell_border_color",
    "theme_body_secondary_cell_color",
    "theme_maintab_cell_color",
    "theme_direct_share_color",
    "theme_direct_share_button_color",
    "theme_direct_share_background_color",
    "theme_notification_color",
    "theme_notification_background_color",
    "theme_notification_background_pressed_color",
    "theme_passcode_color",
    "theme_passcode_keypad_color",
    "theme_passcode_keypad_pressed_color",
    "theme_passcode_keypad_background_color",
    "theme_passcode_keypad_pressed_background_color",
    "theme_passcode_pattern_line_color",
    "theme_chatroom_bubble_me_color",
    "theme_chatroom_bubble_you_color",
    "theme_chatroom_unread_count_color",
    "theme_chatroom_input_bar_color",
    "theme_chatroom_input_bar_background_color",
    "theme_chatroom_input_bar_menu_icon_color",
    "theme_chatroom_input_bar_menu_button_color",
    "theme_chatroom_input_bar_send_icon_color",
    "theme_chatroom_input_bar_send_button_color",
}

REQUIRED_DRAWABLE_DIRS = {
    "drawable-xhdpi",
    "drawable-xxhdpi",
    "drawable-land-xhdpi",
    "drawable-land-xxhdpi",
    "drawable-sw600dp",
    "drawable-sw600dp-land",
}

REQUIRED_MANIFEST_ACTION = "com.kakao.talk.theme.action.MAIN"
REQUIRED_PERMISSION = "com.kakao.talk.v2.theme"


def fail(message):
    print(f"ERROR: {message}")
    return 1


def read_xml(path):
    try:
        return ET.parse(path).getroot()
    except ET.ParseError as exc:
        raise ValueError(f"{path}: XML parse error: {exc}") from exc


def validate_source(root):
    errors = []
    warnings = []

    main = root / "src" / "main"
    theme = main / "theme"
    theme_adv = main / "theme-adv"
    manifest = main / "AndroidManifest.xml"
    colors = theme / "values" / "colors.xml"
    strings = theme / "values" / "strings.xml"

    for path in [manifest, colors, strings]:
        if not path.exists():
            errors.append(f"Missing {path.relative_to(root)}")

    if not (root / "build.gradle.kts").exists() and not (root / "build.gradle").exists():
        warnings.append("No Gradle build file found at project root")

    if manifest.exists():
        try:
            manifest_root = read_xml(manifest)
            permissions = {
                node.attrib.get(f"{ANDROID_NS}name")
                for node in manifest_root.findall("uses-permission")
            }
            if REQUIRED_PERMISSION not in permissions:
                errors.append(f"AndroidManifest.xml missing {REQUIRED_PERMISSION}")

            actions = {
                node.attrib.get(f"{ANDROID_NS}name")
                for node in manifest_root.findall(".//action")
            }
            if REQUIRED_MANIFEST_ACTION not in actions:
                errors.append(f"AndroidManifest.xml missing {REQUIRED_MANIFEST_ACTION} intent action")
        except ValueError as exc:
            errors.append(str(exc))

    color_names = set()
    if colors.exists():
        try:
            color_root = read_xml(colors)
            for node in color_root.findall("color"):
                name = node.attrib.get("name")
                value = (node.text or "").strip()
                if name:
                    color_names.add(name)
                if name and not (value.startswith("#") and len(value) in {7, 9}):
                    errors.append(f"Color {name} must be #rrggbb or #aarrggbb, got {value!r}")
            for name in sorted(REQUIRED_COLORS - color_names):
                errors.append(f"colors.xml missing {name}")
        except ValueError as exc:
            errors.append(str(exc))

    if strings.exists():
        try:
            string_root = read_xml(strings)
            string_names = {node.attrib.get("name") for node in string_root.findall("string")}
            for required in ["theme_title", "app_name"]:
                if required not in string_names:
                    errors.append(f"strings.xml missing {required}")
        except ValueError as exc:
            errors.append(str(exc))

    for dirname in sorted(d for d in REQUIRED_DRAWABLE_DIRS if not (theme / d).exists()):
        warnings.append(f"Missing optional/sample drawable dir src/main/theme/{dirname}")

    drawable_names = set()
    if theme.exists():
        for file_path in theme.rglob("*"):
            if file_path.is_file():
                if file_path.name.endswith(".9.png"):
                    drawable_names.add(file_path.name[:-6])
                elif file_path.suffix in {".png", ".xml"}:
                    drawable_names.add(file_path.stem)

    if theme_adv.exists():
        for xml_path in theme_adv.rglob("*.xml"):
            text = xml_path.read_text(encoding="utf-8")
            for marker, known, label in [
                ("@drawable/", drawable_names, "drawable"),
                ("@color/", color_names, "color"),
            ]:
                start = 0
                while True:
                    index = text.find(marker, start)
                    if index == -1:
                        break
                    index += len(marker)
                    end = index
                    while end < len(text) and (text[end].isalnum() or text[end] == "_"):
                        end += 1
                    resource = text[index:end]
                    if resource and resource not in known:
                        errors.append(
                            f"{xml_path.relative_to(root)} references missing {label} {resource}"
                        )
                    start = end

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        return 1
    print(f"OK: Android KakaoTalk theme source looks valid: {root}")
    return 0


def validate_apk(path):
    errors = []
    with zipfile.ZipFile(path) as apk:
        names = set(apk.namelist())
        if "AndroidManifest.xml" not in names:
            errors.append("APK missing AndroidManifest.xml")
        if not any(name.startswith("res/") for name in names):
            errors.append("APK missing res/ entries")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        return 1
    print(f"OK: APK has expected Android package structure: {path}")
    print("NOTE: Binary AndroidManifest.xml was not decoded; validate source before build when possible.")
    return 0


def main(argv):
    if len(argv) != 2:
        return fail("Usage: validate_android_theme.py /path/to/theme-project-or.apk")
    target = Path(argv[1]).expanduser().resolve()
    if not target.exists():
        return fail(f"Path does not exist: {target}")
    if target.is_file() and target.suffix == ".apk":
        return validate_apk(target)
    if target.is_dir():
        return validate_source(target)
    return fail("Target must be an Android theme project directory or .apk file")


if __name__ == "__main__":
    sys.exit(main(sys.argv))
