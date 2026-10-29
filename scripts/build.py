#!/usr/bin/env python3
"""Build the two production pages from src/site-template.html.

The template is the reviewed single-file preview (both pages + review toolbar).
This script splits it into two independent static pages, removes the review
toolbar, switches hash links to real routes and self-hosts the Inter font.

Output: dist/work/index.html, dist/work/quilted-health/index.html, dist/404.html
Standard library only, so it runs on any machine and on Netlify.
"""
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "site-template.html"
PUBLIC = ROOT / "public"
DIST = ROOT / "dist"
SITE = "https://karenbornmann-vinta-challenge.netlify.app"

PAGES = {
    "work": {
        "path": "work/index.html",
        "title": "Healthcare software work and case studies | Vinta",
        "desc": "Healthcare software projects by Vinta, by care specialty, industry and challenge: EHR modernization, Medplum, integrations and new product builds.",
        "drop": "page-quilted",
    },
    "quilted": {
        "path": "work/quilted-health/index.html",
        "title": "Quilted Health: rebuilding a 14-year-old maternity EHR | Vinta",
        "desc": "How Quilted Health and Vinta rebuilt a midwife-led maternity EHR on Medplum: a one-month proof of concept, then a production build and migration.",
        "drop": "page-work",
    },
}

FONTS = """<link rel="preload" href="/assets/fonts/inter-latin-300-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/inter-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<style>
@font-face{font-family:"Inter";font-style:normal;font-weight:300;font-display:swap;src:url(/assets/fonts/inter-latin-300-normal.woff2) format("woff2")}
@font-face{font-family:"Inter";font-style:normal;font-weight:400;font-display:swap;src:url(/assets/fonts/inter-latin-400-normal.woff2) format("woff2")}
@font-face{font-family:"Inter";font-style:normal;font-weight:500;font-display:swap;src:url(/assets/fonts/inter-latin-500-normal.woff2) format("woff2")}
@font-face{font-family:"Inter";font-style:normal;font-weight:600;font-display:swap;src:url(/assets/fonts/inter-latin-600-normal.woff2) format("woff2")}
</style>"""


def cut(text, start, end, keep_end=False):
    """Remove text from `start` up to `end` (end excluded when keep_end)."""
    a = text.index(start)
    b = text.index(end, a)
    return text[:a] + (text[b:] if keep_end else text[b + len(end):])


def common(t):
    # self-hosted font instead of Google Fonts
    t = re.sub(r'<link rel="preconnect" href="https://fonts\.g[^>]*>\n', "", t)
    t = re.sub(r'<link href="https://fonts\.googleapis\.com[^>]*>', FONTS, t)
    # review toolbar, decisions drawer and phone frame are preview-only
    t = cut(t, '<div class="chrome"', '<aside class="drawer" id="drawer" aria-label="Decisões pendentes"></aside>\n')
    t = t.replace('<div class="stage" id="stage"><div class="viewport" id="vp"><div class="site" id="site">', '<div class="site" id="site">')
    t = t.replace("</footer>\n\n</div></div></div>", "</footer>\n\n</div>")
    t = t.replace("body{margin:0;background:#E7ECF5;", "body{margin:0;background:var(--surface);")
    t = t.replace(".stage{padding-top:var(--chrome-h)}", "")
    t = t.replace("scroll-padding-top:calc(var(--chrome-h) + 90px)", "scroll-padding-top:90px")
    # routes instead of hash views
    t = t.replace('href="#quilted"', 'href="/work/quilted-health/"').replace('href="#work"', 'href="/work/"')
    t = t.replace("href:'#quilted'", "href:'/work/quilted-health/'")
    # script: no frame, no toolbar, no review notes
    t = t.replace("const site=$('#site'),stage=$('#stage'),vp=$('#vp');",
                  "const site=$('#site'),vp=document.createElement('div');")
    t = cut(t, "/* ---------- routing / chrome ---------- */", "/* ---------- work v2 ---------- */", keep_end=True)
    t = t.replace("/* ---------- work v2 ---------- */",
                  "let frameMode=false;\nfunction goTo(sel){const el=$(sel);if(el)el.scrollIntoView({behavior:'smooth'})}\n/* ---------- work v2 ---------- */")
    t = re.sub(r"\nfunction goTo\(sel\)\{const el=\$\(sel\);if\(!el\)return;if\(frameMode\).*?\n", "\n", t)
    t = cut(t, "/* ---------- review notes (pt-BR) ---------- */", "\nroute();", keep_end=True)
    t = t.replace("\nroute();", "\nif($('#page-work'))readURL();\nobserveAll();")
    t = t.replace("history.replaceState(null,'','#work'+(q.toString()?'?'+q:''))",
                  "history.replaceState(null,'',location.pathname+(q.toString()?'?'+q:''))")
    t = t.replace("function readURL(){const h=location.hash;const i=h.indexOf('?');const q=new URLSearchParams(i>-1?h.slice(i+1):'');",
                  "function readURL(){const q=new URLSearchParams(location.search);")
    t = t.replace("slimIO.observe($('#filters'));", "if($('#filters'))slimIO.observe($('#filters'));")
    t = t.replace("if(!$('#page-quilted').hidden&&tl){", "if(tl){")
    t = t.replace("const secs=$$('[data-toc]');", "var secs=$$('[data-toc]');")
    # page-specific code only runs on its page
    t = t.replace("/* ---------- work v2 ---------- */", "if($('#page-work')){\n/* ---------- work v2 ---------- */")
    t = t.replace("/* ---------- quilted v2 ---------- */", "}\nif($('#page-quilted')){\n/* ---------- quilted v2 ---------- */")
    t = t.replace("/* ---------- motion observers ---------- */", "}\n/* ---------- motion observers ---------- */")
    # data-n review pins are not rendered without the notes script; drop the attributes
    t = re.sub(r' data-n="\d+"', "", t)
    return t


def page(t, key):
    p = PAGES[key]
    drop = p["drop"]
    start = t.index(f'<main id="{drop}"')
    end = t.index("</main>", start) + len("</main>")
    t = t[:start] + t[end:]
    t = t.replace('<main id="page-quilted" class="page" hidden>', '<main id="page-quilted" class="page">')
    canonical = f'{SITE}/{p["path"].replace("index.html", "")}'
    head = (f'<title>{p["title"]}</title>\n<meta name="description" content="{p["desc"]}">\n'
            f'<link rel="canonical" href="{canonical}">\n'
            f'<meta property="og:type" content="website">\n<meta property="og:title" content="{p["title"]}">\n'
            f'<meta property="og:description" content="{p["desc"]}">\n<meta property="og:url" content="{canonical}">\n'
            f'<meta name="theme-color" content="#0050FF">\n<link rel="icon" href="/assets/img/c8baf450d2.png">')
    t = re.sub(r"<title>.*?</title>", head, t, count=1)
    if key == "work":
        t = t.replace('<a href="/work/" data-nav="work">Clients</a>', '<a href="/work/" data-nav="work" aria-current="page">Clients</a>')
    return t


def main():
    t = common(SRC.read_text(encoding="utf-8"))
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(PUBLIC, DIST)
    for key, p in PAGES.items():
        out = DIST / p["path"]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(t, key), encoding="utf-8")
        print(f"built {out.relative_to(ROOT)} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
