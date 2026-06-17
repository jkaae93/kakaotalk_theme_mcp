# KakaoTalk Theme Local MCP

This is a local stdio MCP server for the KakaoTalk theme maker workspace. It exposes the local iOS/Android design guides, theme brief prompts, and validation/packaging tools without requiring external Python packages.

## Run

```bash
python3 /Users/kaae/dev/projects/카톡 테마 메이커/mcp/kakaotalk_theme_mcp.py
```

## Example Client Config

Use this shape in an MCP client that accepts stdio server configuration:

```json
{
  "mcpServers": {
    "kakaotalk-theme-local": {
      "command": "python3",
      "args": [
        "/Users/kaae/dev/projects/카톡 테마 메이커/mcp/kakaotalk_theme_mcp.py"
      ],
      "env": {
        "KAKAOTALK_THEME_ALLOWED_ROOTS": "/Users/kaae/dev/projects/카톡 테마 메이커:/private/tmp"
      }
    }
  }
}
```

## Tools

- `read_theme_guide`
- `create_theme_brief`
- `list_required_assets`
- `validate_android_theme`
- `validate_ios_theme`
- `package_ios_ktheme`
- `list_theme_assets`

## Resources

- `kakaotalk://design/ios`
- `kakaotalk://design/android`
- `kakaotalk://guide/android`
- `kakaotalk://guide/dual-platform`

## Safety

The server only accepts file paths inside the workspace, `/tmp`, `/private/tmp`, and `~/Downloads/kakaotalk_theme_user_guide` by default. Add more local roots with `KAKAOTALK_THEME_ALLOWED_ROOTS` when needed.
