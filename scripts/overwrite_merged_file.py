"""
Temporary script to overwrite the merged markdown file with complete new content.
This script will be deleted after use.
"""
import sys

target_file = r"c:\git\AIASD\AI-Assisted-Software-Development-Course\slides\merged\aiasd-311-monday.ge-draft.md"

# Get the new content from argument or stdin
if len(sys.argv) > 1:
    new_content_file = sys.argv[1]
    with open(new_content_file, 'r', encoding='utf-8') as f:
        new_content = f.read()
else:
    print("Reading new content from stdin...")
    new_content = sys.stdin.read()

# Write the new content
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Successfully wrote {len(new_content)} characters to {target_file}")
