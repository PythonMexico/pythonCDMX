#!/usr/bin/env python3
"""
Simple script to check internal links with HTTP requests.
"""

import json
import re
from pathlib import Path
from urllib.parse import urljoin

import requests


def find_internal_links(content):
    """Find all internal links in markdown and HTML content."""
    links = []

    # Markdown link pattern: [text](url)
    md_pattern = r"\[([^\]]+)\]\(([^)]+)\)"

    # HTML link pattern: <a href="url">text</a> or <a href='url'>text</a>
    html_pattern = r'<a\s+href=["\']([^"\']+)["\'][^>]*>([^<]+)</a>'

    # Find markdown links
    for match in re.finditer(md_pattern, content):
        text = match.group(1)
        url = match.group(2)

        # Skip external links
        if url.startswith(("http://", "https://", "mailto:", "tel:")):
            continue

        links.append((text, url, "markdown", match.start()))

    # Find HTML links
    for match in re.finditer(html_pattern, content):
        url = match.group(1)
        text = match.group(2).strip()

        # Skip external links
        if url.startswith(("http://", "https://", "mailto:", "tel:")):
            continue

        links.append((text, url, "html", match.start()))

    return links


def resolve_link_url(base_url, md_file, link_url):
    """Resolve the real URL as a browser would from the markdown file location."""
    # If link is absolute (starts with /), join with base_url
    if link_url.startswith("/"):
        return urljoin(base_url, link_url)
    # If link is relative, join with the file's directory path
    else:
        # Get the directory of the markdown file relative to docs/
        md_dir = Path(md_file).parent
        # Build the relative path as it would be in the site
        rel_path = (md_dir / link_url).as_posix()
        # Remove any leading './' for clean URLs
        if rel_path.startswith("./"):
            rel_path = rel_path[2:]
        return urljoin(base_url + "/", rel_path)


def check_link(base_url, link_url, current_file):
    """Check if a link returns 200 or 404."""
    try:
        # Handle anchor links - they should resolve from current page
        if link_url.startswith("#"):
            # Build URL from current file path
            file_path = current_file.replace(".md", "/")
            if not file_path.startswith("/"):
                file_path = "/" + file_path
            full_url = urljoin(base_url, file_path + link_url)
        else:
            # For relative links, resolve from current file's directory
            if not link_url.startswith("/"):
                # Get current file's directory
                current_dir = str(Path(current_file).parent)
                if current_dir != ".":
                    # Resolve relative to current directory
                    resolved_path = str(Path(current_dir) / link_url)
                else:
                    resolved_path = link_url

                # Convert to URL format
                if not resolved_path.startswith("/"):
                    resolved_path = "/" + resolved_path
                full_url = urljoin(base_url, resolved_path)
            else:
                # Absolute path from site root
                full_url = urljoin(base_url, link_url)

        # Make request
        response = requests.get(full_url, timeout=5)

        if response.status_code == 200:
            return True, "200 OK"
        elif response.status_code == 404:
            return False, "404 Not Found"
        else:
            return False, f"HTTP {response.status_code}"

    except requests.RequestException as e:
        return False, f"Error: {e}"


def main():
    base_url = "http://127.0.0.1:8000"
    docs_dir = Path("docs")

    print(f"🔍 Checking internal links against {base_url}")
    print("=" * 50)

    broken_links = []
    working_links = []

    # Find all markdown files
    for md_file in docs_dir.rglob("*.md"):
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()

            links = find_internal_links(content)

            for text, url, link_type, line_start in links:
                is_working, status = check_link(
                    base_url, url, str(md_file.relative_to(docs_dir))
                )

                # Calculate full URL for display
                if not url.startswith("#"):
                    full_url = urljoin(base_url, url)
                else:
                    full_url = urljoin(
                        base_url,
                        str(md_file.relative_to(docs_dir)).replace(".md", "/") + url,
                    )

                result = {
                    "file": str(md_file.relative_to(docs_dir)),
                    "text": text,
                    "url": url,
                    "full_url": full_url,
                    "status": status,
                    "line": content[:line_start].count("\n") + 1,
                    "link_type": link_type,
                }

                if is_working:
                    working_links.append(result)
                else:
                    broken_links.append(result)

        except Exception as e:
            print(f"❌ Error reading {md_file}: {e}")

    # Print summary
    print(f"✅ Working links: {len(working_links)}")
    print(f"❌ Broken links: {len(broken_links)}")

    # Save results to JSON
    results = {
        "summary": {
            "total_files_scanned": len(list(docs_dir.rglob("*.md"))),
            "working_links": len(working_links),
            "broken_links": len(broken_links),
            "base_url": base_url,
        },
        "broken_links": broken_links,
        "working_links": working_links,
    }

    # Save to JSON file
    output_file = "broken_links.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n📄 Results saved to: {output_file}")

    # Show some broken links in console
    if broken_links:
        print(f"\n🔴 BROKEN LINKS (showing first 10):")
        print("-" * 50)
        for link in broken_links[:10]:
            print(f"📄 {link['file']}:{link['line']}")
            print(f"   Text: {link['text']}")
            print(f"   URL: {link['url']}")
            print(f"   Full URL: {link['full_url']}")
            print(f"   Status: {link['status']}")
            print()


if __name__ == "__main__":
    main()
