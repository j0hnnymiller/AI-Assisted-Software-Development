import re, yaml
from pathlib import Path

text = Path("slides/merged/aia-compliance-draft.md").read_text(encoding="utf-8")
lines = text.split("\n")
errors = []

# 1. Single front matter at top
in_fm = False
fm_closes = 0
for i, ln in enumerate(lines):
    s = ln.strip()
    if i == 0 and s == "---":
        in_fm = True
    elif in_fm and s == "---":
        fm_closes += 1; in_fm = False
if fm_closes != 1:
    errors.append(f"FAIL 1: {fm_closes} front matter close(s)")
else:
    print("1. Single front matter block at top: OK")

# 2. YAML parse
fm_end = text.find("\n---\n", 3)
if fm_end == -1:
    errors.append("FAIL 2: cannot locate front matter end")
else:
    try:
        yaml.safe_load(text[3:fm_end])
        print("2. Front matter YAML parse: OK")
    except Exception as e:
        errors.append(f"FAIL 2: {e}")

# body after front matter
body_start = (fm_end + 4) if fm_end != -1 else 0
body = text[body_start:]
body_lines = body.split("\n")

# 3. No consecutive ---
prev_sep = False
cons = 0
for ln in body_lines:
    s = ln.strip()
    if s == "---":
        if prev_sep: cons += 1
        prev_sep = True
    elif s:
        prev_sep = False
if cons:
    errors.append(f"FAIL 3: {cons} consecutive separator pair(s)")
else:
    print("3. Separator integrity: OK")

# 4. Fence balance
TICK = chr(96)*3
TILDE = "~~~"
in_fence = False
fc = None
depth = 0
for ln in body_lines:
    s = ln.strip()
    if not in_fence:
        if s.startswith(TICK) or s.startswith(TILDE):
            in_fence = True
            fc = TICK if s.startswith(TICK) else TILDE
            depth += 1
    else:
        if fc == TICK and s.startswith(TICK):
            in_fence = False; depth -= 1
        elif fc == TILDE and s.startswith(TILDE):
            in_fence = False; depth -= 1
if depth != 0:
    errors.append(f"FAIL 4: fence imbalance depth={depth}")
else:
    print("4. Fence balance: OK")

# 5. Notes block balance
notes_open = len(re.findall(r"^::: notes", body, re.MULTILINE))
notes_close = len(re.findall(r"^:::", body, re.MULTILINE))
if notes_open != notes_close:
    errors.append(f"FAIL 5: ::: notes={notes_open} opens vs {notes_close} closes")
else:
    print(f"5. Notes blocks balanced ({notes_open}): OK")

# 10. No H1 in body
h1_lines = [ln for ln in body_lines if re.match(r"^# ", ln)]
if h1_lines:
    errors.append(f"FAIL 10: {len(h1_lines)} H1 heading(s) remain in body: {h1_lines[:2]}")
else:
    print("10. No H1 headings in body: OK")

# Count separators outside fences
in_f = False; fc2 = None; seps = 0
TICK = chr(96)*3
for ln in body_lines:
    s = ln.strip()
    if not in_f:
        if s.startswith(TICK) or s.startswith("~~~"):
            in_f = True; fc2 = TICK if s.startswith(TICK) else "~~~"
        elif s == "---":
            seps += 1
    else:
        if fc2 == TICK and s.startswith(TICK): in_f = False
        elif fc2 == "~~~" and s.startswith("~~~"): in_f = False
print(f"V7. Slide count: 1 + {seps} = {1+seps}")

# 7. Module slide count — should be 4 (one per non-first section)
module_slides = len(re.findall(r"## Course Modules", body))
print(f"7. Module list slides injected: {module_slides} (expect 4)")

if errors:
    print("\nVALIDATION ERRORS:")
    for e in errors:
        print(" ", e)
else:
    print("\nPhase 1.5: all checks passed.")