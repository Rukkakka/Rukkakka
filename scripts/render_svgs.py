"""README 용 터미널 스타일 SVG (히어로 배너, 프로젝트 카드) 를 그린다.

프로젝트 버전은 각 저장소의 최신 GitHub Release 에서 읽는다. 릴리스가 없으면 "in progress" 로 표시한다.
GitHub Actions(.github/workflows/readme-svgs.yml)가 주기적으로 실행해 바뀐 SVG 를 커밋한다.

    python3 scripts/render_svgs.py assets
"""

import json
import os
import sys
import urllib.error
import urllib.request
from html import escape
from pathlib import Path

OWNER = "Rukkakka"

# (저장소, 한글 이름, 카드 설명 두 줄, 히어로 주석, 태그)
PROJECTS = [
    ("jibsa", "집사", ("직방·네이버·당근 부동산 매물 조회 CLI", "지금 거래 가능한 매물만, 만원 단위 JSON"),
     "# 집사 · 부동산 매물 조회", "python · typer · httpx"),
    ("baenggipyo", "뱅기표", ("네이버 항공권·스카이스캐너 항공권 조회 CLI", "지금 살 수 있는 운임만, 원 단위 JSON"),
     "# 뱅기표 · 항공권 조회", "python · typer · httpx"),
]

# Catppuccin Mocha
BASE, MANTLE, SURFACE = "#1e1e2e", "#181825", "#313244"
TEXT, SUBTEXT, OVERLAY = "#cdd6f4", "#a6adc8", "#6c7086"
GREEN, YELLOW, MAUVE, PINK, BLUE = "#a6e3a1", "#f9e2af", "#cba6f7", "#f38ba8", "#89b4fa"

FONT = (
    "font-family:'JetBrains Mono','SFMono-Regular',Menlo,Consolas,'DejaVu Sans Mono',"
    "'Apple SD Gothic Neo','Malgun Gothic','Noto Sans CJK KR',monospace"
)

ART = [
    "     ██╗██╗   ██╗███╗   ██╗ ██████╗ ██╗  ██╗ ██████╗  ██████╗ ",
    "     ██║██║   ██║████╗  ██║██╔════╝ ██║  ██║██╔═══██╗██╔═══██╗",
    "     ██║██║   ██║██╔██╗ ██║██║  ███╗███████║██║   ██║██║   ██║",
    "██   ██║██║   ██║██║╚██╗██║██║   ██║██╔══██║██║   ██║██║   ██║",
    "╚█████╔╝╚██████╔╝██║ ╚████║╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝",
    " ╚════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ",
]


def latest_release(repo):
    """최신 릴리스 태그 (예: "v0.1.0"). 릴리스가 없으면 None. 그 밖의 API 오류는 예외로 올려 SVG 를 덮어쓰지 않는다."""
    req = urllib.request.Request(
        f"https://api.github.com/repos/{OWNER}/{repo}/releases/latest",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "readme-svgs"},
    )
    if token := os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            tag = json.load(resp)["tag_name"]
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise
    return tag if tag.startswith("v") else f"v{tag}"


def window(w, h, title):
    """둥근 터미널 창 바탕과 신호등 버튼이 있는 제목 표시줄."""
    return f"""
  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="12" fill="{BASE}" stroke="{SURFACE}"/>
  <path d="M1 12.5a12 12 0 0 1 12-12h{w - 26}a12 12 0 0 1 12 12V34H1z" fill="{MANTLE}"/>
  <circle cx="22" cy="17.5" r="6" fill="#ff5f57"/>
  <circle cx="42" cy="17.5" r="6" fill="#febc2e"/>
  <circle cx="62" cy="17.5" r="6" fill="#28c840"/>
  <text x="{w / 2}" y="22" text-anchor="middle" font-size="12" fill="{OVERLAY}">{escape(title)}</text>"""


def hero(releases):
    w, h = 860, 396
    art = "\n".join(
        f'  <text class="art fade" x="32" y="{78 + i * 17}" style="animation-delay:{i * 0.06:.2f}s">{escape(line)}</text>'
        for i, line in enumerate(ART)
    )

    boot = [
        ("OK", "Started data-pipeline.service", "# 천만 건 배치 · 실패 단계부터 재실행"),
        ("OK", "Started automation.service", "# UiPath RPA → Python"),
    ]
    for repo, _, _, comment, _ in PROJECTS:
        version = releases[repo]
        if version:
            boot.append(("OK", f"Loaded {repo}.cli {version}", comment))
        else:
            boot.append(("WAIT", f"Building {repo}.cli", comment))
    boot.append(("OK", "Reached target llm-agent-tools.", ""))

    lines = []
    for i, (state, msg, comment) in enumerate(boot):
        y = 246 + i * 24
        delay = 0.9 + i * 0.35
        color = GREEN if state == "OK" else YELLOW
        label = "  OK  " if state == "OK" else " WAIT "
        status = f'<tspan fill="{OVERLAY}">[</tspan><tspan fill="{color}">{label}</tspan><tspan fill="{OVERLAY}">]</tspan>'
        note = f'<tspan x="420" fill="{OVERLAY}">{escape(comment)}</tspan>' if comment else ""
        lines.append(
            f'  <text class="fade" x="32" y="{y}" font-size="14" fill="{TEXT}" xml:space="preserve" '
            f'style="animation-delay:{delay:.2f}s">{status} {escape(msg)}{note}</text>'
        )
    prompt_delay = 0.9 + len(boot) * 0.35 + 0.2

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="JUNGHOO — Data Engineer · Automation · LLM Tooling">
  <defs>
    <linearGradient id="g" gradientUnits="userSpaceOnUse" x1="32" y1="0" x2="610" y2="0" spreadMethod="reflect">
      <stop offset="0" stop-color="{BLUE}"/>
      <stop offset="0.5" stop-color="{MAUVE}"/>
      <stop offset="1" stop-color="{PINK}"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0; 578 0; 0 0" dur="8s" repeatCount="indefinite"/>
    </linearGradient>
    <style>
      text {{ {FONT} }}
      .art {{ font-size: 15.5px; fill: url(#g); white-space: pre; }}
      .fade {{ animation: in .35s ease-out both; }}
      .cursor {{ animation: blink 1.1s steps(1) infinite; }}
      @keyframes in {{ from {{ opacity: 0; }} }}
      @keyframes blink {{ 50% {{ opacity: 0; }} }}
    </style>
  </defs>
{window(w, h, "rukkakka@github: ~")}
{art}
  <text class="fade" x="32" y="206" font-size="14" fill="{SUBTEXT}" xml:space="preserve" style="animation-delay:.5s">Data Engineer  <tspan fill="{OVERLAY}">·</tspan>  Automation  <tspan fill="{OVERLAY}">·</tspan>  LLM Tooling</text>
  <line x1="32" y1="222" x2="{w - 32}" y2="222" stroke="{SURFACE}"/>
{chr(10).join(lines)}
  <g class="fade" style="animation-delay:{prompt_delay:.2f}s">
    <text x="32" y="{246 + len(boot) * 24 + 10}" font-size="14" xml:space="preserve"><tspan fill="{GREEN}">rukkakka@github</tspan><tspan fill="{TEXT}">:</tspan><tspan fill="{BLUE}">~</tspan><tspan fill="{TEXT}">$ </tspan></text>
    <rect class="cursor" x="{32 + 19 * 8.4}" y="{246 + len(boot) * 24 - 4}" width="8.5" height="17" fill="{TEXT}"/>
  </g>
</svg>
"""


def card(name, kr, desc, version, tags):
    w, h = 420, 196
    released = version is not None
    label = version if released else "in progress"
    color = GREEN if released else YELLOW
    pulse = "" if released else ' class="pulse"'
    pill_w = 22 + len(label) * 7.6
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(name)} ({escape(kr)}) — {escape(desc[0])}">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{BLUE}"/>
      <stop offset="0.55" stop-color="{MAUVE}"/>
      <stop offset="1" stop-color="{PINK}"/>
    </linearGradient>
    <style>
      text {{ {FONT} }}
      .pulse {{ animation: pulse 1.6s ease-in-out infinite; }}
      @keyframes pulse {{ 50% {{ opacity: .25; }} }}
    </style>
  </defs>
{window(w, h, f"~/projects/{name}")}
  <text x="24" y="80" font-size="28" font-weight="700" fill="url(#g)">{escape(name)}<tspan dx="12" font-size="17" font-weight="400" fill="{SUBTEXT}">{escape(kr)}</tspan></text>
  <text x="24" y="114" font-size="14" fill="{TEXT}">{escape(desc[0])}</text>
  <text x="24" y="136" font-size="14" fill="{OVERLAY}">{escape(desc[1])}</text>
  <rect x="24" y="157" width="{pill_w}" height="22" rx="11" fill="{color}" fill-opacity=".14" stroke="{color}" stroke-opacity=".5"/>
  <circle{pulse} cx="36" cy="168" r="3.5" fill="{color}"/>
  <text x="45" y="172.5" font-size="12" fill="{color}">{escape(label)}</text>
  <text x="{24 + pill_w + 12}" y="172.5" font-size="12" fill="{OVERLAY}">{escape(tags)}</text>
  <text x="{w - 24}" y="172.5" text-anchor="end" font-size="13" fill="{MAUVE}">open →</text>
</svg>
"""


def render(out, releases):
    out.mkdir(parents=True, exist_ok=True)
    (out / "hero.svg").write_text(hero(releases))
    for repo, kr, desc, _, tags in PROJECTS:
        (out / f"card-{repo}.svg").write_text(card(repo, kr, desc, releases[repo], tags))


def main():
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "assets")
    releases = {repo: latest_release(repo) for repo, *_ in PROJECTS}
    for repo, version in releases.items():
        print(f"{repo}: {version or 'in progress'}")
    render(out, releases)


if __name__ == "__main__":
    main()
