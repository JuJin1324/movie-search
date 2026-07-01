#!/usr/bin/env python3
"""
PDF 빌드 스크립트 — Markdown → PDF 변환

사용법:
  python3 build_pdf.py \
    --sources file1.md file2.md \
    --output-dir ./pdf \
    --names file1.pdf file2.pdf \
    --combined combined.pdf \
    --css /path/to/portfolio-pdf.css

파이프라인: Mermaid PNG 렌더링(mmdc) → pandoc HTML → weasyprint PDF
"""

import argparse
import re
import subprocess
import shutil
from pathlib import Path


def resolve_relative_image_paths(md_text: str, src_dir: Path) -> str:
    def is_external(path: str) -> bool:
        return path.startswith(("http://", "https://", "/", "data:"))

    def resolve(path: str) -> str:
        if is_external(path):
            return path
        return str((src_dir / path).resolve())

    md_text = re.sub(
        r'(<img[^>]*\bsrc=")([^"]+)(")',
        lambda m: m.group(1) + resolve(m.group(2)) + m.group(3),
        md_text,
    )
    md_text = re.sub(
        r'(!\[[^\]]*\]\()([^)\s]+)(\s*(?:"[^"]*")?\))',
        lambda m: m.group(1) + resolve(m.group(2)) + m.group(3),
        md_text,
    )
    return md_text


def extract_and_render_mermaid(md_text: str, work_dir: Path) -> str:
    pattern = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)
    diagrams = pattern.findall(md_text)

    for i, diagram in enumerate(diagrams, start=1):
        mmd_path = work_dir / f"diagram-{i:02d}.mmd"
        png_path = work_dir / f"diagram-{i:02d}.png"
        mmd_path.write_text(diagram.strip(), encoding="utf-8")

        try:
            result = subprocess.run(
                ["npx", "-y", "@mermaid-js/mermaid-cli", "-i", str(mmd_path), "-o", str(png_path), "-s", "3"],
                capture_output=True, text=True, timeout=45
            )
            if result.returncode != 0:
                print(f"  [경고] diagram-{i:02d} 렌더링 실패: {result.stderr.strip()}")
        except subprocess.TimeoutExpired:
            print(f"  [경고] diagram-{i:02d} 렌더링 타임아웃")

    def replace_mermaid(match):
        idx = diagrams.index(match.group(1)) + 1
        png_path = work_dir / f"diagram-{idx:02d}.png"
        return (
            f'\n<figure class="mermaid-figure">\n\n'
            f"![]({png_path})\n\n"
            f"</figure>\n"
        )

    return pattern.sub(replace_mermaid, md_text)


def md_to_pdf(md_text: str, output_pdf: Path, work_dir: Path, css: Path):
    rendered_md = work_dir / "rendered.md"
    html_path = work_dir / "rendered.html"

    rendered_md.write_text(md_text, encoding="utf-8")

    subprocess.run(
        ["pandoc", str(rendered_md), "--standalone", f"--css={css}", "-o", str(html_path)],
        check=True, capture_output=True
    )

    subprocess.run(
        ["weasyprint", str(html_path), str(output_pdf)],
        check=True, capture_output=True
    )


def build(sources: list[Path], output_dir: Path, names: list[str], combined: str | None, css: Path, combined_sources: list[Path] | None = None):
    output_dir.mkdir(parents=True, exist_ok=True)
    work_base = output_dir / ".pdf-build"
    rendered_map: dict[Path, str] = {}

    for src, out_name in zip(sources, names):
        print(f"\n▶ {src.name}")
        work_dir = work_base / src.stem
        work_dir.mkdir(parents=True, exist_ok=True)

        md_text = src.read_text(encoding="utf-8")
        md_text = resolve_relative_image_paths(md_text, src.parent)
        print(f"  Mermaid 렌더링 중...")
        rendered = extract_and_render_mermaid(md_text, work_dir)
        rendered_map[src] = rendered

        output_pdf = output_dir / out_name
        print(f"  PDF 생성 중: {out_name}")
        md_to_pdf(rendered, output_pdf, work_dir, css)
        print(f"  완료: {output_pdf}")

    if combined:
        targets = combined_sources if combined_sources else sources
        rendered_texts = [rendered_map[t] for t in targets if t in rendered_map]
        if rendered_texts:
            print(f"\n▶ 합본 PDF 생성 중...")
            combined_work = work_base / "combined"
            combined_work.mkdir(parents=True, exist_ok=True)
            page_break = '\n\n<div class="page-break-before"></div>\n\n'
            combined_text = page_break.join(rendered_texts)
            combined_pdf = output_dir / combined
            md_to_pdf(combined_text, combined_pdf, combined_work, css)
            print(f"  완료: {combined_pdf}")

    shutil.rmtree(work_base, ignore_errors=True)
    print("\n✓ 모든 PDF 생성 완료")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sources", nargs="+", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--names", nargs="+", required=True)
    parser.add_argument("--combined", default=None)
    parser.add_argument("--combined-sources", nargs="+", default=None)
    parser.add_argument("--css", required=True)
    args = parser.parse_args()

    build(
        sources=[Path(s).resolve() for s in args.sources],
        output_dir=Path(args.output_dir).resolve(),
        names=args.names,
        combined=args.combined,
        css=Path(args.css).resolve(),
        combined_sources=[Path(s).resolve() for s in args.combined_sources] if args.combined_sources else None,
    )
