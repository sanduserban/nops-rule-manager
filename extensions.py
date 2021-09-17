import atexit
import os
import re
from collections import defaultdict
from copy import deepcopy

import markdown2
from plim import lexer, preprocessor_factory
from plim.util import u

from stylus import Stylus

# icon#id.cls-[1rem]: filename
PARSE_SVG_PATH_RE = re.compile(
    r"icon(?:#(?P<id>[A-Za-z\-0-9]+))?(?P<cls>(?:\.[A-Za-z\-/0-9\[\]:]+)+)? : (?P<path>[A-Za-z\-0-9/_]+)"
)


def parse_svg_path(indent_level, current_line, matched, source, syntax):
    path = matched.group("path")
    svg_id = matched.group("id") or ""
    svg_class = (matched.group("cls") or "").replace(".", " ")
    svg_file = f"public/static/svg/{path}.svg"

    if not os.path.exists(svg_file):
        return "", indent_level, "", source

    with open(svg_file) as f:
        rt = f.read()
    return (
        rt.replace("<svg ", f'<svg id="{svg_id}" class="{svg_class}"'),
        indent_level,
        "",
        source,
    )


def stylus_to_css(source):
    compiler = Stylus(compress=True, plugins={"rupture": {}})
    css = compiler.compile(source).strip()
    return u("<style>{css}</style>").format(css=css)


def md_to_html(source):
    return markdown2.markdown(source, use_file_vars=True, extras=["header-ids"])


CUSTOM_PARSERS = [
    (PARSE_SVG_PATH_RE, parse_svg_path),
]
lexer.MARKUP_LANGUAGES["stylus"] = stylus_to_css
lexer.MARKUP_LANGUAGES["md"] = md_to_html
lexer.MARKUP_LANGUAGES["markdown"] = md_to_html

svg = preprocessor_factory(custom_parsers=CUSTOM_PARSERS, syntax="mako")
