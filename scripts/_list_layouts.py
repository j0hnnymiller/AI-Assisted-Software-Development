import zipfile, re, sys

path = sys.argv[1] if len(sys.argv) > 1 else "Slides/individual-slides/jMM-CODE-Training-Slide-Template-clean.pptx"
with zipfile.ZipFile(path) as z:
    names = sorted(n for n in z.namelist() if "slideLayout" in n and n.endswith(".xml") and "_rels" not in n)
    for n in names:
        x = z.read(n).decode("utf-8", errors="replace")
        m = re.search(r'<p:cSld[^>]*name="([^"]+)"', x)
        print(f"{n}: {m.group(1) if m else '(unnamed)'}")
