#!/usr/bin/env python3
"""
Simple script to check internal links with HTTP requests.
"""

import json
import re
import sys
from pathlib import Path
from urllib.parse import urljoin

import requests


def is_external_link(url):
    """Check if a URL is external (http, https, mailto, tel)."""
    return url.startswith(("http://", "https://", "mailto:", "tel:"))


def convert_md_to_html(url):
    """Convert .md URLs to .html URLs."""
    return url.replace(".md", ".html") if ".md" in url else url


def find_internal_links(content):
    """Find all internal links in markdown and HTML content."""
    links = []

    # Common patterns for both markdown and HTML links
    patterns = [
        (r"\[([^\]]+)\]\(([^)]+)\)", "markdown"),  # [text](url)
        (r'<a\s+href=["\']([^"\']+)["\'][^>]*>([^<]+)</a>', "html"),
    ]

    for pattern, link_type in patterns:
        for match in re.finditer(pattern, content):
            if link_type == "markdown":
                text, url = match.group(1), match.group(2)
            else:  # html
                url, text = match.group(1), match.group(2).strip()

            # Skip external links
            if is_external_link(url):
                continue

            links.append((text, url, link_type, match.start()))

    return links


def resolve_relative_url(base_url, current_file, link_url):
    """Resolve a relative URL from the current file's directory."""
    if link_url.startswith("/"):
        return urljoin(base_url, link_url)

    # Get current file's directory
    current_dir = str(Path(current_file).parent)
    if current_dir != ".":
        resolved_path = str(Path(current_dir) / link_url)
    else:
        resolved_path = link_url

    # Ensure path starts with /
    if not resolved_path.startswith("/"):
        resolved_path = "/" + resolved_path

    return urljoin(base_url, resolved_path)


def build_full_url(base_url, link_url, current_file):
    """Build the full URL for checking or display."""
    if link_url.startswith("#"):
        # Anchor link - resolve from current page
        file_path = current_file.replace(".md", ".html")
        if not file_path.startswith("/"):
            file_path = "/" + file_path
        return urljoin(base_url, file_path + link_url)
    else:
        # Regular link - convert .md to .html and resolve
        converted_url = convert_md_to_html(link_url)
        return resolve_relative_url(base_url, current_file, converted_url)


def check_link(base_url, link_url, current_file):
    """Check if a link returns 200 or 404."""
    try:
        full_url = build_full_url(base_url, link_url, current_file)
        response = requests.get(full_url, timeout=5)

        if response.status_code == 200:
            return True, "200 OK"
        elif response.status_code == 404:
            return False, "404 Not Found"
        else:
            return False, f"HTTP {response.status_code}"

    except requests.RequestException as e:
        return False, f"Error: {e}"


def create_link_result(
    md_file, docs_dir, text, url, link_type, line_start, content, status
):
    """Create a standardized link result dictionary."""
    current_file = str(md_file.relative_to(docs_dir))
    full_url = build_full_url("http://127.0.0.1:8000", url, current_file)

    return {
        "file": current_file,
        "text": text,
        "url": url,
        "full_url": full_url,
        "status": status,
        "line": content[:line_start].count("\n") + 1,
        "link_type": link_type,
    }


def print_broken_links(broken_links):
    """Print broken links to console."""
    if not broken_links:
        return

    print("\n🔴 BROKEN LINKS (showing first 10):")
    print("-" * 50)
    for link in broken_links[:10]:
        print("📄 {}:{}".format(link["file"], link["line"]))
        print(f"   Text: {link['text']}")
        print(f"   URL: {link['url']}")
        print(f"   Full URL: {link['full_url']}")
        print(f"   Status: {link['status']}")
        print()


def save_results(broken_links, working_links, docs_dir, base_url):
    """Save results to JSON file."""
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

    output_file = "broken_links.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n📄 Results saved to: {output_file}")


def main():
    """Main function to check all internal links."""
    base_url = "http://127.0.0.1:8000"
    docs_dir = Path("docs")

    print(f"🔍 Checking internal links against {base_url}")
    print("=" * 50)

    broken_links = []
    working_links = []

    # Find all markdown files
    for md_file in docs_dir.rglob("*.md"):
        if "README.md" in md_file.name:
            continue
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()

            links = find_internal_links(content)

            for text, url, link_type, line_start in links:
                is_working, status = check_link(
                    base_url, url, str(md_file.relative_to(docs_dir))
                )

                result = create_link_result(
                    md_file, docs_dir, text, url, link_type, line_start, content, status
                )

                if is_working:
                    working_links.append(result)
                else:
                    broken_links.append(result)

        except (IOError, OSError) as e:
            print(f"❌ Error reading {md_file}: {e}")

    # Print summary
    print(f"✅ Working links: {len(working_links)}")
    print(f"❌ Broken links: {len(broken_links)}")

    # Save results and print broken links
    save_results(broken_links, working_links, docs_dir, base_url)
    print_broken_links(broken_links)

    return len(broken_links)


if __name__ == "__main__":
    broken_count = main()

    # Exit with error if there are broken links
    if broken_count > 0:
        print(f"\n💥 Script failing due to {broken_count} broken links!")
        sys.exit(1)
    else:
        print("\n✅ Script completed successfully - all links working!")
        sys.exit(0)
