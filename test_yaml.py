import yaml

md_content = """---
marp: true
theme: default
paginate: true
title: "AI Assisted Software Development"
subtitle: "From Code to Copilot"
style: |
  section {
    background-color: #0D7FA8;
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    padding: 60px;
  }
---
# Some heading
"""

lines = md_content.splitlines()

if lines and lines[0].strip() == "---":
    for end in range(1, len(lines)):
        if lines[end] != "---":
            continue
        front_matter = "\n".join(lines[1:end])
        print("Parsing:", repr(front_matter))
        try:
            parsed = yaml.safe_load(front_matter)
            print("Parsed:", parsed)
            print("Is dict?", isinstance(parsed, dict))
        except yaml.YAMLError as e:
            print("Parsing error:", e)
            continue
