"""velogger 로 받은 velog 최근 글을 README 의 posts 표시 사이에 넣는다.

GitHub Actions(.github/workflows/readme-svgs.yml)가 SVG 와 함께 주기적으로 실행한다.

    pipx run velogger posts lcs3947 --limit 5 | python3 scripts/render_posts.py README.md

글을 못 받았으면(빈 입력, 에러, 글 0개) README 를 건드리지 않고 실패로 끝난다.
"""

import json
import sys
from datetime import datetime, timedelta, timezone
from html import escape
from pathlib import Path

KST = timezone(timedelta(hours=9))
START, END = "<!-- posts:start -->", "<!-- posts:end -->"


def released_date(value):
    """velog 의 UTC 시각(예: "2026-10-22T22:19:16.386Z")을 한국 날짜로."""
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(KST).strftime("%Y-%m-%d")


def block(posts):
    lines = ["# 직접 만든 velogger 로 6시간마다 가져옵니다"]
    for post in posts:
        lines.append(f'{released_date(post["released_at"])}  <a href="{escape(post["url"])}">{escape(post["title"])}</a>')
    return "\n".join([START, "<pre>", *lines, "</pre>", END])


def main():
    readme = Path(sys.argv[1] if len(sys.argv) > 1 else "README.md")
    posts = json.load(sys.stdin)["posts"]
    if not posts:
        sys.exit("velog 글을 하나도 받지 못해 README 를 그대로 둡니다")
    text = readme.read_text()
    head, sep, rest = text.partition(START)
    _, sep_end, tail = rest.partition(END)
    if not sep or not sep_end:
        sys.exit(f"README 에 {START} … {END} 표시가 없습니다")
    readme.write_text(head + block(posts) + tail)
    print(f"velog 글 {len(posts)}개")


if __name__ == "__main__":
    main()
