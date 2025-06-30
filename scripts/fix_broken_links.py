#!/usr/bin/env python3
"""
Script to fix broken links based on broken_links.json
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Tuple


def load_broken_links(json_file: str = "broken_links.json") -> Dict:
    """Load broken links from JSON file."""
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ File {json_file} not found. Run check_links.py first.")
        return {}
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON: {e}")
        return {}


def suggest_fix(url: str) -> str:
    """Suggest a fix for a broken URL."""
    # Primero: /index.md o index.md
    if url.endswith("/index.md"):
        return url[:-9] + "/"
    if url.endswith("index.md"):
        return url[:-8] + "/"
    # Después: cualquier otro .md
    if url.endswith(".md"):
        return url[:-3] + "/"

    # Handle meetup individual links - add trailing slash
    if re.match(r"^\d{6}-[a-z]+$", url):
        return url + "/"

    # Handle meetup individual links with .md - remove .md and add /
    if re.match(r"^\d{6}-[a-z]+\.md$", url):
        return url[:-3] + "/"

    # Handle /index/ links - remove the /index/ part
    if url.endswith("/index/"):
        return url[:-7] + "/"

    # Add trailing slash for directory-like URLs that don't have it
    if not url.endswith("/") and "." not in url.split("/")[-1]:
        return url + "/"

    # Handle specific patterns for comunidad links
    if url.startswith("/comunidad/") and not url.endswith("/"):
        return url + "/"

    if url.startswith("comunidad/") and not url.endswith("/"):
        return url + "/"

    # Handle meetup directory links
    if "meetups/" in url and url.endswith(".md"):
        return url[:-3] + "/"

    return url


def fix_file_links(file_path: str, broken_links: List[Dict]) -> Tuple[bool, List[Dict]]:
    """Fix broken links in a specific file."""
    file_links = [link for link in broken_links if link["file"] == file_path]

    if not file_links:
        return False, []

    try:
        with open(f"docs/{file_path}", "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content
        fixes_applied = []

        for link in file_links:
            old_url = link["url"]
            new_url = suggest_fix(old_url)
            link_type = link.get("link_type", "markdown")

            if new_url != old_url:
                if link_type == "markdown":
                    # Fix markdown links: [text](url)
                    pattern = (
                        f'\\[{re.escape(link["text"])}\\]\\({re.escape(old_url)}\\)'
                    )
                    replacement = f'[{link["text"]}]({new_url})'
                elif link_type == "html":
                    # Fix HTML links: <a href="url">text</a>
                    # Handle both single and double quotes
                    pattern1 = f'<a\\s+href=["\']{re.escape(old_url)}["\'][^>]*>{re.escape(link["text"])}</a>'
                    replacement1 = f'<a href="{new_url}">{link["text"]}</a>'

                    # Try with double quotes first
                    new_content = re.sub(pattern1, replacement1, content)

                    # If no change, try with single quotes
                    if new_content == content:
                        pattern2 = f'<a\\s+href=[\'"]{re.escape(old_url)}[\'"][^>]*>{re.escape(link["text"])}</a>'
                        new_content = re.sub(pattern2, replacement1, content)
                else:
                    # Fallback to markdown pattern
                    pattern = (
                        f'\\[{re.escape(link["text"])}\\]\\({re.escape(old_url)}\\)'
                    )
                    replacement = f'[{link["text"]}]({new_url})'
                    new_content = re.sub(pattern, replacement, content)

                if new_content != content:
                    content = new_content
                    fixes_applied.append(
                        {
                            "line": link["line"],
                            "text": link["text"],
                            "old_url": old_url,
                            "new_url": new_url,
                            "link_type": link_type,
                        }
                    )

        # Write the fixed content back
        if fixes_applied:
            with open(f"docs/{file_path}", "w", encoding="utf-8") as f:
                f.write(content)
            return True, fixes_applied

        return False, []

    except Exception as e:
        print(f"❌ Error fixing {file_path}: {e}")
        return False, []


def main():
    """Main function to fix broken links."""
    print("🔧 Fixing broken links...")
    print("=" * 50)

    # Load broken links
    data = load_broken_links()
    if not data:
        return

    broken_links = data.get("broken_links", [])
    if not broken_links:
        print("✅ No broken links to fix!")
        return

    print(f"📄 Found {len(broken_links)} broken links")

    # Group links by file
    files_to_fix = {}
    for link in broken_links:
        file_path = link["file"]
        if file_path not in files_to_fix:
            files_to_fix[file_path] = []
        files_to_fix[file_path].append(link)

    print(f"📁 Files to fix: {len(files_to_fix)}")

    # Fix each file
    total_fixes = 0
    files_fixed = 0

    for file_path, links in files_to_fix.items():
        print(f"\n🔧 Fixing {file_path}...")

        was_fixed, fixes = fix_file_links(file_path, links)

        if was_fixed:
            files_fixed += 1
            total_fixes += len(fixes)

            print(f"   ✅ Fixed {len(fixes)} links:")
            for fix in fixes:
                print(f"      Line {fix['line']}: {fix['old_url']} → {fix['new_url']}")
        else:
            print(f"   ⚠️  No fixes applied")

    # Summary
    print("\n" + "=" * 50)
    print("📊 FIX SUMMARY")
    print("=" * 50)
    print(f"📁 Files processed: {len(files_to_fix)}")
    print(f"🔧 Files fixed: {files_fixed}")
    print(f"✅ Total fixes applied: {total_fixes}")

    if total_fixes > 0:
        print(f"\n💡 Run 'python scripts/check_links.py' again to verify fixes!")
    else:
        print(f"\n⚠️  No automatic fixes could be applied.")
        print(f"   Some links may need manual correction.")


if __name__ == "__main__":
    main()
