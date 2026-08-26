#!/usr/bin/env python3
"""Render structured resume JSON into the bundled one-page HTML template."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path
from typing import Any


UNRESOLVED = re.compile(
    r"待确认|needs confirmation|TBD|TODO|\[\[[^\]]+\]\]|<[^>]+>|YYYY\.MM",
    re.IGNORECASE,
)


def esc(value: Any) -> str:
    return html.escape(str(value or ""), quote=True)


def list_html(items: list[Any], css_class: str) -> str:
    clean = [esc(item) for item in items if str(item or "").strip()]
    if not clean:
        return ""
    return f'<ul class="{css_class}">' + "".join(f"<li>{item}</li>" for item in clean) + "</ul>"


def entries_html(entries: list[dict[str, Any]]) -> str:
    blocks: list[str] = []
    for entry in entries:
        title = esc(entry.get("title"))
        dates = esc(entry.get("dates"))
        subtitle = esc(entry.get("subtitle"))
        bullets = list_html(entry.get("bullets") or entry.get("details") or [], "bullets")
        subtitle_html = f'<div class="entry-subtitle">{subtitle}</div>' if subtitle else ""
        blocks.append(
            '<article class="entry">'
            '<div class="entry-head">'
            f'<div class="entry-title">{title}</div>'
            f'<div class="entry-date">{dates}</div>'
            "</div>"
            f"{subtitle_html}{bullets}"
            "</article>"
        )
    return "".join(blocks)


def section(title: str, body: str) -> str:
    if not body:
        return ""
    return f"<section><h2>{esc(title)}</h2>{body}</section>"


def skill_lines(items: list[dict[str, Any]]) -> str:
    lines = []
    for item in items:
        label = esc(item.get("label"))
        value = esc(item.get("items"))
        if label or value:
            lines.append(f'<div class="skill-line"><strong>{label}：</strong>{value}</div>')
    return '<div class="skills">' + "".join(lines) + "</div>" if lines else ""


def validate(data: dict[str, Any], strict: bool) -> list[str]:
    errors: list[str] = []
    warnings: list[str] = []
    if not str(data.get("name", "")).strip():
        errors.append("Missing name")
    if not data.get("education"):
        warnings.append("Education section is empty")
    if not data.get("experience") and not data.get("projects"):
        errors.append("At least one experience or project is required")
    for idx, item in enumerate(data.get("experience") or [], start=1):
        count = len(item.get("bullets") or [])
        if count > 5:
            errors.append(f"Experience {idx} has {count} bullets; maximum is 5")
    for idx, item in enumerate(data.get("projects") or [], start=1):
        count = len(item.get("bullets") or [])
        if count > 3:
            errors.append(f"Project {idx} has {count} bullets; maximum is 3")
    text_blob = json.dumps(data, ensure_ascii=False)
    if strict and UNRESOLVED.search(text_blob):
        errors.append("Strict-final check found unresolved placeholders or confirmation markers")
    visible_chars = len(re.sub(r"\s+", "", text_blob))
    if visible_chars > 2600:
        warnings.append("Content is dense and may exceed one A4 page; render and inspect")
    if errors:
        raise ValueError("; ".join(errors))
    return warnings


def render(data: dict[str, Any], template_text: str) -> str:
    contact_items = [esc(item) for item in data.get("contact") or [] if str(item or "").strip()]
    contact = '<span class="sep">｜</span>'.join(f"<span>{item}</span>" for item in contact_items)
    summary_body = list_html(data.get("summary") or [], "summary-list")
    education_body = entries_html(data.get("education") or [])
    experience_body = entries_html(data.get("experience") or [])
    project_body = entries_html(data.get("projects") or [])
    skills_body = skill_lines(data.get("skills") or [])
    certificates_body = list_html(data.get("certificates") or [], "bullets")
    replacements = {
        "{{TITLE}}": esc(f"{data.get('name', '')} - {data.get('target_role', '')}"),
        "{{NAME}}": esc(data.get("name")),
        "{{TARGET_ROLE}}": esc(data.get("target_role")),
        "{{CONTACT}}": contact,
        "{{SUMMARY_SECTION}}": section("个人简介", summary_body),
        "{{EDUCATION_SECTION}}": section("教育背景", education_body),
        "{{EXPERIENCE_SECTION}}": section("实习经历", experience_body),
        "{{PROJECTS_SECTION}}": section("项目经历", project_body),
        "{{SKILLS_SECTION}}": section("技能", skills_body),
        "{{CERTIFICATES_SECTION}}": section("证书与荣誉", certificates_body),
    }
    output = template_text
    for marker, value in replacements.items():
        output = output.replace(marker, value)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("data", type=Path, help="Structured resume JSON")
    parser.add_argument("--output", type=Path, required=True, help="Output HTML file")
    parser.add_argument("--template", type=Path, help="Optional HTML template")
    parser.add_argument("--strict-final", action="store_true", help="Reject unresolved markers")
    args = parser.parse_args()

    skill_root = Path(__file__).resolve().parent.parent
    template_path = args.template or skill_root / "assets" / "one-page-product-resume.html"
    data = json.loads(args.data.read_text(encoding="utf-8"))
    warnings = validate(data, args.strict_final)
    output = render(data, template_path.read_text(encoding="utf-8"))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")
    print(f"Wrote {args.output}")
    for warning in warnings:
        print(f"Warning: {warning}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
