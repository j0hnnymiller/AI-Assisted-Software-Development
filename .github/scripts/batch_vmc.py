import os

from phase1_merge_marp_decks import derive_manifest_output_path

manifests = [
    "slides/manifests/vmc/aiasd-311-monday.vmc.manifest.md",
    "slides/manifests/vmc/aiasd-311-tuesday.vmc.manifest.md",
    "slides/manifests/vmc/aiasd-311-wednesday.vmc.manifest.md",
    "slides/manifests/vmc/aiasd-311-thursday.vmc.manifest.md",
    "slides/manifests/vmc/aiasd-311-friday.vmc.manifest.md"
]

for manifest_path in manifests:
    merged_path = str(derive_manifest_output_path(manifest_path, "slides/merged", ".md"))
    pptx_path = str(derive_manifest_output_path(manifest_path, "slides/output", ".pptx"))

    print(f"\n{'='*60}")
    print(f"Processing: {manifest_path}")
    print(f"Merged:     {merged_path}")
    print(f"PPTX:       {pptx_path}")
    print(f"{'='*60}\n")

    # For now, just validate paths
    if not os.path.exists(manifest_path):
        print(f"ERROR: Manifest not found: {manifest_path}")
        continue

    print("✓ Manifest exists")
