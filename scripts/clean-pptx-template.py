#!/usr/bin/env python3
"""
clean-pptx-template.py

Removes customXml parts from a .pptx (or .potx) reference template so that
pandoc --reference-doc does not produce broken relationships.

Root cause: pandoc copies presentation.xml.rels from the reference doc (including
customXml relationship entries) but does NOT copy the actual customXml/ folder,
leaving dangling references that cause PowerPoint's repair dialog.

Usage:
    python clean-pptx-template.py <input.pptx> [output.pptx]

If output path is omitted, writes <input>-clean.pptx alongside the input file.
"""
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

RELS_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
CT_NS   = "http://schemas.openxmlformats.org/package/2006/content-types"

# Register namespaces so ElementTree re-serialises them cleanly
ET.register_namespace("",        RELS_NS)
ET.register_namespace("",        CT_NS)


def strip_customxml(src: Path, dst: Path) -> None:
    with zipfile.ZipFile(src, "r") as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        # Collect names of customXml entries to drop
        all_names = set(zin.namelist())
        drop = {n for n in all_names if n.startswith("customXml/")}

        for item in zin.infolist():
            name = item.filename
            data = zin.read(name)

            # ── Patch presentation.xml.rels ──────────────────────────────────
            if name == "ppt/_rels/presentation.xml.rels":
                data = patch_rels(data)

            # ── Patch [Content_Types].xml ────────────────────────────────────
            elif name == "[Content_Types].xml":
                data = patch_content_types(data)

            # ── Skip customXml files ─────────────────────────────────────────
            if name in drop:
                print(f"  removed: {name}")
                continue

            zout.writestr(item, data)

    print(f"\nWrote clean template: {dst}")


def patch_rels(data: bytes) -> bytes:
    """Remove all <Relationship> entries pointing into ../customXml/."""
    text = data.decode("utf-8")
    # Remove any Relationship whose Target contains customXml
    cleaned = re.sub(
        r'<Relationship[^>]+Target="[^"]*customXml[^"]*"[^/]*/>\s*',
        "",
        text,
    )
    if cleaned != text:
        removed = len(re.findall(r'<Relationship[^>]+Target="[^"]*customXml[^"]*"', text))
        print(f"  removed {removed} customXml relationship(s) from presentation.xml.rels")
    return cleaned.encode("utf-8")


def patch_content_types(data: bytes) -> bytes:
    """Remove <Override PartName="/customXml/..."> entries."""
    text = data.decode("utf-8")
    cleaned = re.sub(
        r'<Override\s+PartName="/customXml/[^"]*"[^/]*/>\s*',
        "",
        text,
    )
    if cleaned != text:
        removed = len(re.findall(r'<Override\s+PartName="/customXml/', text))
        print(f"  removed {removed} customXml entry/entries from [Content_Types].xml")
    return cleaned.encode("utf-8")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    src = Path(sys.argv[1]).resolve()
    if not src.exists():
        print(f"Error: {src} not found")
        sys.exit(1)

    if len(sys.argv) >= 3:
        dst = Path(sys.argv[2]).resolve()
    else:
        dst = src.with_stem(src.stem + "-clean")

    print(f"Input:  {src}")
    print(f"Output: {dst}")
    print()

    strip_customxml(src, dst)


if __name__ == "__main__":
    main()
