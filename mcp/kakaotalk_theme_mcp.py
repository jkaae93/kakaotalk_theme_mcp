#!/usr/bin/env python3
import json
import os
import subprocess
import sys
import traceback
import zipfile
from pathlib import Path

PROTOCOL_VERSION = "2025-06-18"
PROJECT_ROOT = Path(__file__).resolve().parents[1]


def default_allowed_roots():
    roots = [
        PROJECT_ROOT,
        Path("/private/tmp"),
        Path("/tmp"),
        Path.home() / "Downloads" / "kakaotalk_theme_user_guide",
    ]
    extra = os.environ.get("KAKAOTALK_THEME_ALLOWED_ROOTS", "")
    for raw in extra.split(":"):
        if raw:
            roots.append(Path(raw).expanduser())
    return [root.resolve() for root in roots if root.exists()]


ALLOWED_ROOTS = default_allowed_roots()

RESOURCE_FILES = {
    "kakaotalk://repo/llms": {
        "name": "llms.txt",
        "description": "AI-oriented overview for LLMs and generative answer engines.",
        "path": PROJECT_ROOT / "llms.txt",
    },
    "kakaotalk://repo/illustrators": {
        "name": "Illustrator onboarding guide",
        "description": "Guide for illustrators and character artists creating KakaoTalk themes.",
        "path": PROJECT_ROOT / "docs" / "for-illustrators.md",
    },
    "kakaotalk://repo/faq": {
        "name": "FAQ",
        "description": "Answer-engine-friendly Q&A for KakaoTalk theme creators.",
        "path": PROJECT_ROOT / "docs" / "faq.md",
    },
    "kakaotalk://repo/discoverability": {
        "name": "SEO/GEO/AEO notes",
        "description": "Discoverability targets and metadata for search and AI answer engines.",
        "path": PROJECT_ROOT / "docs" / "discoverability.md",
    },
    "kakaotalk://design/ios": {
        "name": "iOS design.md",
        "description": "KakaoTalk iOS theme generation guidelines.",
        "path": PROJECT_ROOT / "design.md",
    },
    "kakaotalk://design/android": {
        "name": "Android design.md",
        "description": "KakaoTalk Android theme generation guidelines.",
        "path": PROJECT_ROOT / "android" / "design.md",
    },
    "kakaotalk://guide/android": {
        "name": "Android theme guide reference",
        "description": "Android resource and APK workflow reference.",
        "path": PROJECT_ROOT
        / "skills"
        / "kakaotalk-android-theme"
        / "references"
        / "android-theme-guide.md",
    },
    "kakaotalk://guide/dual-platform": {
        "name": "Dual platform mapping reference",
        "description": "Shared iOS/Android token and asset mapping.",
        "path": PROJECT_ROOT
        / "skills"
        / "kakaotalk-dual-platform-theme"
        / "references"
        / "platform-mapping.md",
    },
}

IOS_ASSETS = {
    "icons": [
        "commonIcoTheme.png",
        "maintabIcoFriends.png",
        "maintabIcoFriendsSelected.png",
        "maintabIcoChats.png",
        "maintabIcoChatsSelected.png",
        "maintabIcoNow.png",
        "maintabIcoNowSelected.png",
        "maintabIcoShopping.png",
        "maintabIcoShoppingSelected.png",
        "maintabIcoMore.png",
        "maintabIcoMoreSelected.png",
        "maintabIcoPiccoma.png",
        "maintabIcoPiccomaSelected.png",
        "maintabIcoCall.png",
        "maintabIcoCallSelected.png",
        "findBtnAddFriend.png",
    ],
    "images": [
        "mainBgImage.png",
        "chatroomBgImage.png",
        "profileImg01.png",
        "chatroomBubbleSend01.png",
        "chatroomBubbleSend02.png",
        "chatroomBubbleReceive01.png",
        "chatroomBubbleReceive02.png",
        "passcodeBgImage.png",
        "passcodeKeypadPressed.png",
    ],
    "optional": [
        "profileImg02.png",
        "profileImg03.png",
        "passcodeBullet01.png",
        "passcodeBullet02.png",
        "passcodeBullet03.png",
        "passcodeBullet04.png",
        "passcodeBulletSelected01.png",
        "passcodeBulletSelected02.png",
        "passcodeBulletSelected03.png",
        "passcodeBulletSelected04.png",
        "maintabBgImage.png",
    ],
    "notes": [
        "Create @2x and @3x variants when the sample uses both.",
        "CSS references omit scale suffixes, e.g. chatroomBgImage.png.",
        "Keep the sample base filenames unless the CSS is updated accordingly.",
    ],
}

ANDROID_ASSETS = {
    "app_icons": [
        "src/main/res/mipmap-*/ic_launcher.png",
        "src/main/res/mipmap-*/ic_launcher_round.png",
        "src/main/res/mipmap-*/ic_launcher_foreground.png",
        "src/main/res/mipmap-*/ic_launcher_background.png",
        "src/main/ic_launcher-web.png",
    ],
    "tab_icons": [
        "theme_maintab_ico_friends_image.png",
        "theme_maintab_ico_friends_focused_image.png",
        "theme_maintab_ico_chats_image.png",
        "theme_maintab_ico_chats_focused_image.png",
        "theme_maintab_ico_now_image.png",
        "theme_maintab_ico_now_focused_image.png",
        "theme_maintab_ico_shopping_image.png",
        "theme_maintab_ico_shopping_focused_image.png",
        "theme_maintab_ico_more_image.png",
        "theme_maintab_ico_more_focused_image.png",
        "theme_maintab_ico_piccoma_image.png",
        "theme_maintab_ico_piccoma_focused_image.png",
        "theme_maintab_ico_call_image.png",
        "theme_maintab_ico_call_focused_image.png",
    ],
    "common_images": [
        "theme_background_image.png",
        "theme_chatroom_background_image.png",
        "theme_splash_image.png",
        "theme_maintab_cell_image.9.png",
        "theme_find_add_friend_button_image.png",
        "theme_find_add_friend_button_pressed_image.png",
        "theme_profile_01_image.png",
        "theme_profile_02_image.png",
        "theme_profile_03_image.png",
        "theme_profile_01_image_full.png",
        "theme_profile_02_image_full.png",
        "theme_profile_03_image_full.png",
    ],
    "chat_bubbles": [
        "theme_chatroom_bubble_me_01_image.9.png",
        "theme_chatroom_bubble_me_02_image.9.png",
        "theme_chatroom_bubble_you_01_image.9.png",
        "theme_chatroom_bubble_you_02_image.9.png",
    ],
    "passcode": [
        "theme_passcode_background_image.png",
        "theme_passcode_01_image.png",
        "theme_passcode_02_image.png",
        "theme_passcode_03_image.png",
        "theme_passcode_04_image.png",
        "theme_passcode_01_checked_image.png",
        "theme_passcode_02_checked_image.png",
        "theme_passcode_03_checked_image.png",
        "theme_passcode_04_checked_image.png",
    ],
    "notes": [
        "Place theme images in the same drawable-* folders used by the sample.",
        "Keep .9.png filenames for stretchable Android 9-patch assets.",
        "Tab icons should be at least 56dp.",
    ],
}


class McpError(Exception):
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code
        self.message = message


def is_allowed(path):
    resolved = Path(path).expanduser().resolve()
    for root in ALLOWED_ROOTS:
        if resolved == root or root in resolved.parents:
            return resolved
    allowed = ", ".join(str(root) for root in ALLOWED_ROOTS)
    raise McpError(-32602, f"Path is outside allowed roots: {resolved}. Allowed: {allowed}")


def read_message():
    headers = {}
    while True:
        line = sys.stdin.buffer.readline()
        if not line:
            return None
        line = line.decode("ascii").strip()
        if line == "":
            break
        key, _, value = line.partition(":")
        headers[key.lower()] = value.strip()

    length = headers.get("content-length")
    if not length:
        raise McpError(-32700, "Missing Content-Length header")
    body = sys.stdin.buffer.read(int(length))
    return json.loads(body.decode("utf-8"))


def send_message(message):
    body = json.dumps(message, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    sys.stdout.buffer.write(f"Content-Length: {len(body)}\r\n\r\n".encode("ascii"))
    sys.stdout.buffer.write(body)
    sys.stdout.buffer.flush()


def text_result(text, is_error=False):
    return {
        "content": [{"type": "text", "text": text}],
        "isError": is_error,
    }


def tool_schema():
    return [
        {
            "name": "read_theme_guide",
            "description": "Read one local KakaoTalk theme guide or platform mapping document.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "guide": {
                        "type": "string",
                        "enum": ["ios", "android", "dual-platform"],
                    }
                },
                "required": ["guide"],
                "additionalProperties": False,
            },
        },
        {
            "name": "create_theme_brief",
            "description": "Create a fillable KakaoTalk theme brief for iOS, Android, or both platforms.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "platform": {
                        "type": "string",
                        "enum": ["ios", "android", "dual"],
                        "default": "dual",
                    },
                    "name": {"type": "string"},
                    "concept": {"type": "string"},
                    "mode": {
                        "type": "string",
                        "enum": ["light", "dark", "system-neutral"],
                        "default": "light",
                    },
                },
                "additionalProperties": False,
            },
        },
        {
            "name": "list_required_assets",
            "description": "List user-created KakaoTalk theme icons and image assets for iOS, Android, or both platforms.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "platform": {
                        "type": "string",
                        "enum": ["ios", "android", "dual"],
                        "default": "dual",
                    },
                    "format": {
                        "type": "string",
                        "enum": ["markdown", "json"],
                        "default": "markdown",
                    },
                },
                "additionalProperties": False,
            },
        },
        {
            "name": "validate_android_theme",
            "description": "Validate a KakaoTalk Android theme project directory or APK using the local validator.",
            "inputSchema": {
                "type": "object",
                "properties": {"path": {"type": "string"}},
                "required": ["path"],
                "additionalProperties": False,
            },
        },
        {
            "name": "validate_ios_theme",
            "description": "Run a lightweight validation for an iOS KakaoTalk theme folder or .ktheme archive.",
            "inputSchema": {
                "type": "object",
                "properties": {"path": {"type": "string"}},
                "required": ["path"],
                "additionalProperties": False,
            },
        },
        {
            "name": "package_ios_ktheme",
            "description": "Package an iOS theme folder into a .ktheme archive.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "theme_dir": {"type": "string"},
                    "output_path": {"type": "string"},
                },
                "required": ["theme_dir", "output_path"],
                "additionalProperties": False,
            },
        },
        {
            "name": "list_theme_assets",
            "description": "List theme-related files under the local project root.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "max_depth": {"type": "integer", "minimum": 1, "maximum": 8, "default": 4}
                },
                "additionalProperties": False,
            },
        },
    ]


def read_text(path):
    return Path(path).read_text(encoding="utf-8")


def call_read_theme_guide(args):
    guide = args["guide"]
    uri = {
        "ios": "kakaotalk://design/ios",
        "android": "kakaotalk://guide/android",
        "dual-platform": "kakaotalk://guide/dual-platform",
    }[guide]
    info = RESOURCE_FILES[uri]
    return text_result(read_text(info["path"]))


def call_create_theme_brief(args):
    platform = args.get("platform", "dual")
    name = args.get("name", "")
    concept = args.get("concept", "")
    mode = args.get("mode", "light")
    package_line = "- Android package:\n" if platform in {"android", "dual"} else ""
    ios_line = "- iOS theme id:\n" if platform in {"ios", "dual"} else ""
    text = f"""## KakaoTalk Theme Brief

- Platform: {platform}
- Name: {name}
{ios_line}{package_line}- Concept: {concept}
- Mood keywords:
- Mode: {mode}
- Main background:
- Chat background:
- Header color:
- Accent color:
- Send bubble:
- Receive bubble:
- Primary text:
- Secondary text:
- Image style:
- Tab icon style:
- Passcode style:
- Notification style:
- Special details:

## Output Expectations

- iOS: `.ktheme` with `KakaoTalkTheme.css` and `Images/` at archive root.
- Android: APK built from a sample Android theme project.
- Include the platform-specific icon/image checklist from `list_required_assets`.
- Both: readable chat text, distinct sent/received bubbles, matching palette and mood.
"""
    return text_result(text)


def render_asset_section(title, groups):
    lines = [f"## {title}"]
    for group_name, assets in groups.items():
        if group_name == "notes":
            continue
        label = group_name.replace("_", " ").title()
        lines.append(f"\n### {label}")
        lines.extend(f"- `{asset}`" for asset in assets)
    notes = groups.get("notes", [])
    if notes:
        lines.append("\n### Notes")
        lines.extend(f"- {note}" for note in notes)
    return "\n".join(lines)


def call_list_required_assets(args):
    platform = args.get("platform", "dual")
    output_format = args.get("format", "markdown")
    payload = {}
    if platform in {"ios", "dual"}:
        payload["ios"] = IOS_ASSETS
    if platform in {"android", "dual"}:
        payload["android"] = ANDROID_ASSETS

    if output_format == "json":
        return text_result(json.dumps(payload, ensure_ascii=False, indent=2))

    sections = []
    if "ios" in payload:
        sections.append(render_asset_section("iOS User-Created Assets", payload["ios"]))
    if "android" in payload:
        sections.append(render_asset_section("Android User-Created Assets", payload["android"]))
    return text_result("\n\n".join(sections))


def call_validate_android_theme(args):
    target = is_allowed(args["path"])
    script = PROJECT_ROOT / "skills" / "kakaotalk-android-theme" / "scripts" / "validate_android_theme.py"
    completed = subprocess.run(
        [sys.executable, str(script), str(target)],
        cwd=str(PROJECT_ROOT),
        text=True,
        capture_output=True,
        timeout=60,
        check=False,
    )
    output = completed.stdout + completed.stderr
    return text_result(output.strip() or f"Exited with {completed.returncode}", completed.returncode != 0)


def validate_ios_folder(path):
    errors = []
    warnings = []
    css = path / "KakaoTalkTheme.css"
    images = path / "Images"
    if not css.exists():
        errors.append("Missing KakaoTalkTheme.css")
    if not images.exists() or not images.is_dir():
        errors.append("Missing Images/ directory")
    if images.exists():
        pngs = sorted(images.glob("*.png"))
        if not pngs:
            warnings.append("Images/ contains no PNG files")
    return errors, warnings


def validate_ios_archive(path):
    errors = []
    warnings = []
    with zipfile.ZipFile(path) as archive:
        names = set(archive.namelist())
        if "KakaoTalkTheme.css" not in names:
            errors.append("Archive root missing KakaoTalkTheme.css")
        if not any(name.startswith("Images/") for name in names):
            errors.append("Archive root missing Images/ entries")
        junk = [name for name in names if name.startswith("__MACOSX/") or "/.DS_Store" in name or name.endswith(".DS_Store")]
        if junk:
            warnings.append("Archive contains macOS metadata: " + ", ".join(sorted(junk)[:10]))
    return errors, warnings


def call_validate_ios_theme(args):
    target = is_allowed(args["path"])
    if target.is_dir():
        errors, warnings = validate_ios_folder(target)
    elif target.is_file() and target.suffix == ".ktheme":
        errors, warnings = validate_ios_archive(target)
    else:
        raise McpError(-32602, "iOS target must be a theme folder or .ktheme file")

    lines = [f"WARNING: {warning}" for warning in warnings]
    lines.extend(f"ERROR: {error}" for error in errors)
    if errors:
        return text_result("\n".join(lines), True)
    lines.append(f"OK: iOS KakaoTalk theme looks valid: {target}")
    return text_result("\n".join(lines))


def should_skip_archive_name(relative):
    parts = relative.parts
    return (
        ".DS_Store" in parts
        or "__MACOSX" in parts
        or any(part.startswith("._") for part in parts)
    )


def call_package_ios_ktheme(args):
    theme_dir = is_allowed(args["theme_dir"])
    output_path = is_allowed(args["output_path"])
    if not theme_dir.is_dir():
        raise McpError(-32602, "theme_dir must be a directory")
    errors, _ = validate_ios_folder(theme_dir)
    if errors:
        return text_result("\n".join(f"ERROR: {error}" for error in errors), True)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for child in [theme_dir / "KakaoTalkTheme.css", theme_dir / "Images"]:
            if child.is_file():
                archive.write(child, child.name)
            elif child.is_dir():
                for file_path in sorted(child.rglob("*")):
                    if not file_path.is_file():
                        continue
                    relative = file_path.relative_to(theme_dir)
                    if should_skip_archive_name(relative):
                        continue
                    archive.write(file_path, str(relative))
    return text_result(f"OK: packaged {output_path}")


def call_list_theme_assets(args):
    max_depth = int(args.get("max_depth", 4))
    rows = []
    for path in sorted(PROJECT_ROOT.rglob("*")):
        if ".git" in path.parts:
            continue
        if not path.is_file():
            continue
        relative = path.relative_to(PROJECT_ROOT)
        if len(relative.parts) <= max_depth:
            rows.append(str(relative))
    return text_result("\n".join(rows))


TOOL_HANDLERS = {
    "read_theme_guide": call_read_theme_guide,
    "create_theme_brief": call_create_theme_brief,
    "list_required_assets": call_list_required_assets,
    "validate_android_theme": call_validate_android_theme,
    "validate_ios_theme": call_validate_ios_theme,
    "package_ios_ktheme": call_package_ios_ktheme,
    "list_theme_assets": call_list_theme_assets,
}


def list_resources():
    return [
        {
            "uri": uri,
            "name": info["name"],
            "description": info["description"],
            "mimeType": "text/markdown",
        }
        for uri, info in RESOURCE_FILES.items()
        if info["path"].exists()
    ]


def list_prompts():
    return [
        {
            "name": "new-dual-platform-theme",
            "description": "Start a coordinated iOS and Android KakaoTalk theme brief.",
            "arguments": [
                {"name": "name", "description": "Theme name", "required": False},
                {"name": "concept", "description": "Visual concept", "required": False},
            ],
        },
        {
            "name": "android-theme-check",
            "description": "Review an Android theme project against KakaoTalk theme requirements.",
            "arguments": [{"name": "path", "description": "Android project path", "required": True}],
        },
    ]


def get_prompt(name, args):
    if name == "new-dual-platform-theme":
        theme_name = args.get("name", "")
        concept = args.get("concept", "")
        text = (
            "Create a coordinated KakaoTalk theme for iOS and Android.\n"
            f"Theme name: {theme_name}\n"
            f"Concept: {concept}\n"
            "Use the local iOS, Android, and dual-platform resources before generating files."
        )
    elif name == "android-theme-check":
        text = (
            "Validate and review this KakaoTalk Android theme project:\n"
            f"{args.get('path', '')}\n"
            "Use validate_android_theme first, then summarize missing resources or risks."
        )
    else:
        raise McpError(-32602, f"Unknown prompt: {name}")
    return {"messages": [{"role": "user", "content": {"type": "text", "text": text}}]}


def handle_request(request):
    method = request.get("method")
    params = request.get("params") or {}

    if method == "initialize":
        return {
            "protocolVersion": PROTOCOL_VERSION,
            "capabilities": {"tools": {}, "resources": {}, "prompts": {}},
            "serverInfo": {"name": "kakaotalk-theme-local", "version": "0.1.0"},
        }
    if method == "ping":
        return {}
    if method == "tools/list":
        return {"tools": tool_schema()}
    if method == "tools/call":
        name = params.get("name")
        args = params.get("arguments") or {}
        handler = TOOL_HANDLERS.get(name)
        if not handler:
            raise McpError(-32601, f"Unknown tool: {name}")
        return handler(args)
    if method == "resources/list":
        return {"resources": list_resources()}
    if method == "resources/read":
        uri = params.get("uri")
        info = RESOURCE_FILES.get(uri)
        if not info:
            raise McpError(-32602, f"Unknown resource: {uri}")
        return {
            "contents": [
                {
                    "uri": uri,
                    "mimeType": "text/markdown",
                    "text": read_text(info["path"]),
                }
            ]
        }
    if method == "prompts/list":
        return {"prompts": list_prompts()}
    if method == "prompts/get":
        return get_prompt(params.get("name"), params.get("arguments") or {})
    if method and method.startswith("notifications/"):
        return None
    raise McpError(-32601, f"Method not found: {method}")


def error_response(request_id, code, message):
    return {"jsonrpc": "2.0", "id": request_id, "error": {"code": code, "message": message}}


def main():
    while True:
        try:
            request = read_message()
            if request is None:
                break
            request_id = request.get("id")
            result = handle_request(request)
            if request_id is not None and result is not None:
                send_message({"jsonrpc": "2.0", "id": request_id, "result": result})
        except McpError as exc:
            request_id = None
            try:
                request_id = request.get("id")
            except Exception:
                pass
            if request_id is not None:
                send_message(error_response(request_id, exc.code, exc.message))
        except Exception as exc:
            request_id = None
            try:
                request_id = request.get("id")
            except Exception:
                pass
            message = f"{exc}\n{traceback.format_exc()}"
            if request_id is not None:
                send_message(error_response(request_id, -32603, message))
            else:
                print(message, file=sys.stderr)


if __name__ == "__main__":
    main()
