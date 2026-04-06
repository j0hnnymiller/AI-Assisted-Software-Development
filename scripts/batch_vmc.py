import os
import sys
import yaml
from pathlib import Path

manifests = [
    "slides/manifests/vmc/aiasd-311-monday.vmc.manifest.md",
    "slides/manifests/vmc/aiasd-311-tuesday.vmc.manifest.md",
    "slides/manifests/vmc/aiasd-311-wednesday.vmc.manifest.md",
    "slides/manifests/vmc/aiasd-311-thursday.vmc.manifest.md",
    "slides/manifests/vmc/aiasd-311-friday.vmc.manifest.md"
]

for manifest_path in manifests:
    # Derive output paths (strip .manifest.md, keep .vmc, add -draft)
    basename = Path(manifest_path).stem  # Gets 'aiasd-311-monday.vmc'
    merged_path = f"slides/merged/{basename}-draft.md"
    pptx_path = f"slides/output/{basename}-draft.pptx"
    
    print(f"\n{'='*60}")
    print(f"Processing: {manifest_path}")
    print(f"Merged:     {merged_path}")
    print(f"PPTX:       {pptx_path}")
    print(f"{'='*60}\n")
    
    # For now, just validate paths
    if not os.path.exists(manifest_path):
        print(f"ERROR: Manifest not found: {manifest_path}")
        continue
    
    print(f"✓ Manifest exists")
