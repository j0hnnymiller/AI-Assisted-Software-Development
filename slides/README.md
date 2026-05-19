---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "slide-pipeline-workflow-20260331"
prompt: |
  Create a README.md that documents the slide pipeline workflow including:
  - Pre-class review steps for slide manifest and Marp source
  - Pre-day tasks to copy draft PPTX to OneDrive and finalize formatting
  - Post-day tasks to copy PPTX from OneDrive, delete hidden slides, and commit
started: "2026-03-31T14:00:00Z"
ended: "2026-03-31T14:15:00Z"
task_durations:
  - task: "pipeline documentation review"
    duration: "00:10:00"
  - task: "workflow guide creation"
    duration: "00:05:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/03/31/slide-pipeline-workflow-20260331/conversation.md"
source: "johnmillerATcodemag-com"
applyTo: "slides/**"
---

# Slide Pipeline Workflow

This document provides a comprehensive guide for managing the complete slide lifecycle for AI-Assisted Software Development (AIASD) courses, from pre-class review through post-day archival and version control.

**Table of Contents**

- [Overview](#overview)
- [Directory Structure](#directory-structure)
- [Pre-Class Review](#pre-class-review)
- [Pre-Day Production](#pre-day-production)
- [Post-Day Archival](#post-day-archival)
- [Quick Reference](#quick-reference)
- [Troubleshooting](#troubleshooting)

---

## Overview

The slide pipeline consists of three main phases:

1. **Pre-Class Review** (1-2 weeks before class)
   - Review slide manifest and content
   - Refine Marp source files for accuracy and delivery
   - Merge Marp decks and generate draft PPTX

2. **Pre-Day Production** (morning of class)
   - Copy draft PPTX from the AI Assisted Software Development Course repository to CODE staffing OneDrive
   - Finalize formatting and hide slides not being presented
   - Prepare for live delivery

3. **Post-Day Archival** (end of class day)
   - Copy finalized PPTX from OneDrive to the class repository
   - Remove hidden slides to create final version
   - Commit updated slides to version control

---

## Directory Structure

```
slides/
├── marp/                           # Individual topic slide files (EDITABLE)
│   ├── *.deck.md                   # One topic per file
│   └── images/                     # Images referenced by individual slides
├── images/                         # Images referenced by merged deck
├── merged/                         # GENERATED — Do not edit manually
│   └── <course>-<day>-draft.md     # Merged deck from manifest
├── output/                         # GENERATED — Do not edit manually
│   └── <course>-<day>-draft.pptx   # Draft PPTX from python-pptx
└── manifests/                      # Course day manifests (EDITABLE)
    └── <course>-<day>.manifest.md  # Defines section order and deck inclusions

.github/copilot/Promptfiles/
└── merge-marp-decks.prompt.md      # Pipeline entry point — Copilot agent prompt
```

---

## Pre-Class Review

### 1. Review the Slide Manifest (1-2 weeks before)

The manifest defines the complete slide structure for the course day.

**Location:**

```
slides/manifests/<course>-<day>.manifest.md
```

**Example manifest structure:**

```yaml
template: slides\jMM-CODE-Training-Slide-Template-clean.pptx
title: "AI-Assisted Software Development"
subtitle: "From Code to Copilot"

sections:
  - name: Intro
    decks:
      - slides\marp\welcome-to-aiasd.deck.md
      - slides\marp\instructors\john-michael-miller-intro.deck.md

  - name: AI Assisted Software Development
    decks:
      - slides\marp\whats-the-big-deal-short.deck.md
      - slides\marp\the-ai-revolution.deck.md
```

**Review Checklist:**

- [ ] All sections are present and in correct order
- [ ] Section names are current and descriptive
- [ ] Deck file paths are correct and files exist
- [ ] Template path points to the correct CODE template
- [ ] Title and subtitle are accurate
- [ ] No duplicate decks across sections
- [ ] Timing: verify approximate slide count matches available time

**To verify slide count:**

```powershell
# From repository root
python scripts/merge_marp_decks.py slides\manifests\aiasd-311-monday.manifest.md | wc -l
```

### 2. Review and Refine Marp Source Files

Examine individual deck files for accuracy and presentation quality.

**Location:**

```
slides/marp/*.deck.md
```

**Review Checklist per Deck:**

- [ ] Front matter is valid YAML with `marp: true` and theme specified
- [ ] Exactly one `# H1` heading at the start (deck title)
- [ ] All slide titles are `## H2` headings (not `#` or `###`)
- [ ] Content is current and technically accurate
- [ ] Speaker notes (`::: notes` blocks) provide delivery guidance
- [ ] Image paths use `images/` (not `marp/images/`)
- [ ] Layout directives match template layout names (e.g., `<!-- layout: Two Content -->`)
- [ ] No trailing `---` separator (no orphaned slide markers)

**Example high-quality deck structure:**

```markdown
---
marp: true
theme: default
paginate: true
---

# Welcome to AI-Assisted Software Development

::: notes
This is the opening slide for the day. Set the tone enthusiastically.
Connect to attendees' backgrounds. Estimate 2-3 minutes.
:::

---

## Learning Objectives

- Understand foundational AI concepts
- Apply GitHub Copilot workflows
- Build production-ready AI-assisted solutions

::: notes
Walk through each objective. These set expectations for the day.
Reinforce that participants will have hands-on experience with all three.
:::
```

**If you identify issues:**

1. **Content errors:** Edit the `.deck.md` file directly
2. **Formatting issues:** Update layout directives or front matter
3. **Missing speaker notes:** Add or expand `::: notes` blocks

**Commit changes:**

```bash
git add slides/marp/*.deck.md
git commit -m "refactor: update slide content for [course]-[day]"
```

### 3. Merge Decks and Generate Draft PPTX

Once content is finalized, merge the individual deck files and generate the draft PPTX.

**Run the Copilot agent prompt (recommended):**

In VS Code, open the command palette:

```
Cmd+Shift+P (macOS) / Ctrl+Shift+P (Windows)
```

Search for and select:

```
GitHub Copilot: Slash Commands
/merge-marp-decks
```

Follow the prompts to select your manifest file.

**Output files generated:**

- `slides/merged/<course>-<day>-draft.md` — Merged Marp source (do not edit manually)
- `slides/output/<course>-<day>-draft.pptx` — Draft PPTX ready for finalization

**Verify the output:**

- [ ] PPTX opens without errors in PowerPoint
- [ ] All sections appear as named groups in PowerPoint (right-click → Slide Groups → Show All)
- [ ] Module list slides appear after the first section (not before): `Course Modules` with check arrows
- [ ] Speaker notes present on all slides (View → Notes)
- [ ] Slide count matches expected total
- [ ] Images render correctly (especially diagrams and screenshots)
- [ ] Text formatting is preserved (bold, italics, code blocks)

---

## Pre-Day Production

### 1. Copy Draft PPTX to OneDrive (morning of class)

**OneDrive folder structure:**

```
OneDrive://CODE Staffing/
└── training/
    └── aiasd-courses/
        └── [class-id] [start-date]/
            └── slides/
                └── [course]-[day]. pptx          ← Final after editing
```

**Copy the draft PPTX:**

```powershell
# Example for AIASD-311 Monday class
$sourceFile = "c:\git\AIASD\AI-Assisted-Software-Development-Course\slides\output\aiasd-311-monday-draft.pptx"
$destFile = "C:\Users\$env:USERNAME\OneDrive - Microsoft\CODE Staffing\AIASD\aiasd-311-monday.pptx"

# Create destination folder if needed
New-Item -ItemType Directory -Path (Split-Path $destFile) -Force | Out-Null

# Copy file
Copy-Item -Path $sourceFile -Destination $destFile -Force
Write-Host "Copied to: $destFile"
```

**Verify the copy:**

- [ ] File appears in OneDrive folder
- [ ] File size matches original (no truncation)
- [ ] File opens successfully in PowerPoint on your system
- [ ] OneDrive sync status shows "up to date" (green check mark)

### 2. Finalize Formatting and Hide Slides

With the draft PPTX copied to OneDrive, open PowerPoint and prepare for delivery.

**Open the file:**

```
OneDrive:/CODE Staffing/training/aiasd-courses/[class-id]/slides/[course]-[day].pptx
```

**Formatting refinements:**

| Issue                           | Solution                                                                           |
| ------------------------------- | ---------------------------------------------------------------------------------- |
| Text overflows or misaligns     | Use AutoFit to Placeholders (Home → Arrange → AutoFit)                             |
| Images are distorted or cropped | Use the Design Suggestions to adjust layout and alignment                          |
| Bullet points don't fit         | Reduce font size or split across slides (regenerate with updated source if needed) |
| Header/footer spacing is off    | Check master slide formatting (View → Slide Master)                                |
| Color contrast is poor          | Update theme or text colors (if template allows custom modifications)              |

**Hide slides not being presented:**

In PowerPoint, for slides you will not present during class:

1. Right-click the slide thumbnail (left panel)
2. Select **Hide Slide**
3. The slide number will appear with strikethrough (e.g., ~~5~~)

**Examples of slides to hide:**

- Advanced/optional content slides
- Backup slides for Q&A
- Slides for alternative explanations (if you're taking a different tempo)
- Accessibility alternatives (if presenting the main version instead)

**Verify before saving:**

- [ ] All formatting corrections are complete
- [ ] Speaker notes are accurate and up-to-date
- [ ] Hidden slides are clearly marked (strikethrough numbers in thumbnail panel)
- [ ] Slide sorter view shows the intended flow (hidden slides visible but dimmed)

**Save the finalized PPTX:**

```
File → Save (or Ctrl+S)
```

Save it with a clear filename in the same OneDrive folder:

```
[course]-[day].pptx   ← Final version ready for delivery
```

**OneDrive sync:**

- Wait for sync to complete (OneDrive icon shows "up to date")
- Verify file appears in cloud (onedrive.live.com) with current timestamp

---

## Post-Day Archival

### 1. Copy Finalized PPTX from OneDrive to the class Repository (end of day)

After class, copy the finalized and corrected PPTX to the class repository.

**Copy from OneDrive:**

```powershell
# Example for AIASD-311 Monday class
$sourceFile = "C:\Users\$env:USERNAME\OneDrive - Microsoft\CODE Staffing\AIASD\aiasd-311-monday.pptx"
$destFolder = "c:\git\AIASD\<course repository folder>\slides"
$destFile = Join-Path $destFolder "aiasd-311-monday.pptx"

Copy-Item -Path $sourceFile -Destination $destFile
Write-Host "Copied to: $destFile"
```

**Verify the copy:**

- [ ] File appears in `slides/`
- [ ] File size and modification time match the OneDrive version
- [ ] File opens successfully in PowerPoint
- [ ] Speaker notes and all formatting are preserved

### 2. Delete Hidden Slides

Remove slides that were marked as hidden to create the final clean version.

**Using PowerPoint COM automation (PowerShell):**

```powershell
param(
    [Parameter(Mandatory = $true)]
    [string]$PptxPath
)

$pptx = [System.IO.Path]::GetFullPath($PptxPath)

$application = New-Object -ComObject PowerPoint.Application
$application.Visible = [Microsoft.Office.Core.MsoTriState]::msoTrue

try {
    $presentation = $application.Presentations.Open($pptx, [Microsoft.Office.Core.MsoTriState]::msoFalse)

    # Delete hidden slides (iterate backwards to avoid index shifting)
    for ($i = $presentation.Slides.Count; $i -ge 1; $i--) {
        $slide = $presentation.Slides.Item($i)
        if ($slide.SlideShowTransition.Hidden -eq [Microsoft.Office.Core.MsoTriState]::msoTrue) {
            Write-Host "Deleting hidden slide $i"
            $slide.Delete()
        }
    }

    # Save the cleaned presentation
    $cleanFile = $pptx -replace '\.pptx$', '-final.pptx'
    $presentation.SaveAs($cleanFile, [Microsoft.Office.Interop.PowerPoint.PpSaveAsFileType]::ppSaveAsDefault)
    Write-Host "Saved clean version: $cleanFile"

    $presentation.Close()
}
finally {
    $application.Quit()
}
```

**Or manually in PowerPoint:**

1. Select all slides in Slide Sorter view (`View → Slide Sorter`)
2. Right-click any hidden slide (strikethrough number)
3. Select **Delete Slide**
4. Repeat for all hidden slides
5. Save the presentation (`Ctrl+S`)
6. Rename to indicate it's the final version (e.g., `aiasd-311-monday-final.pptx`)

**Verify all hidden slides are removed:**

- [ ] Slide Sorter view shows no strikethrough slide numbers
- [ ] Total slide count is correct (all hidden slides removed)
- [ ] Speaker notes still present on remaining slides

### 3. Commit to Repository

Update version control with the finalized presentation.

**Create session log (optional but recommended):**

Create a session summary to document the class delivery:

```markdown
# Session: AIASD-311 Monday [2026-03-31]

## Deliverables

- **Final Slides**: `slides/output/aiasd-311-monday-final.pptx`
  - Hidden slides removed
  - Formatting verified
  - Speaker notes updated

## Changes Made

- Updated slide content for technical accuracy
- Reformatted 3 slides for better text fitting
- Hidden 2 optional deep-dive slides (kept as reference)

## Statistics

- Total slides delivered: 145
- Duration: 8 hours with breaks
- Attendance: 25 participants
- Feedback: Generally positive (avg 4.2/5)

## Next Steps

- Incorporate feedback into content review (Q2)
- Update module progression slides for next cohort
- Archive OneDrive copy for historical reference
```

**Stage and commit:**

```bash
cd c:\git\AIASD\AI-Assisted-Software-Development-Course

# Stage the finalized PPTX
git add slides/output/aiasd-311-monday-final.pptx

# Add session notes (if you created them)
git add ai-logs/2026/03/31/aiasd-311-monday-delivery/session-notes.md

# Commit with descriptive message
git commit -m "docs: archive finalized slides for AIASD-311 Monday class (2026-03-31)

- Removed 2 hidden slides
- Updated speaker notes based on delivery
- Cleaned formatting for 3 slides with text overflow
- All 145 slides verified and synced"

# Push to repository
git push origin main
```

**Verify commit:**

```bash
git log --oneline -5
git show --stat
```

---

## Quick Reference

### Command Checklist

**Pre-Class Review (1-2 weeks before):**

```bash
# Review manifest
cat slides/manifests/aiasd-311-monday.manifest.md

# Generate draft PPTX (from VS Code: /merge-marp-decks or use command line)
python scripts/generate_pptx.py slides\manifests\aiasd-311-monday.manifest.md slides\output\aiasd-311-monday-draft.pptx

# Commit updated source slides
git add slides/marp/*.deck.md
git commit -m "refactor: update slide content for AIASD-311 Monday"
```

**Pre-Day Production (morning of class):**

```powershell
# Copy draft to OneDrive
Copy-Item "slides\output\aiasd-311-monday-draft.pptx" `
  "C:\Users\$env:USERNAME\OneDrive - Microsoft\CODE Staffing\training\aiasd-courses\AIASD-311 [2026-03-31]\slides\"

# Finalize in PowerPoint:
# 1. Open slides/output/aiasd-311-monday-draft.pptx from OneDrive
# 2. Fix formatting issues
# 3. Hide slides not being presented (right-click → Hide Slide)
# 4. Save as aiasd-311-monday.pptx
```

**Post-Day Archival (end of class):**

```powershell
# Copy finalized PPTX back to repository
Copy-Item "C:\Users\$env:USERNAME\OneDrive - Microsoft\CODE Staffing\training\aiasd-courses\AIASD-311 [2026-03-31]\slides\aiasd-311-monday.pptx" `
  "slides\output\"

# Delete hidden slides (use script above or PowerPoint manually)
# Save as aiasd-311-monday-final.pptx

# Commit to repository
git add slides/output/aiasd-311-monday-final.pptx
git commit -m "docs: archive finalized slides for AIASD-311 Monday"
git push
```

---

## Troubleshooting

### Issue: Draft PPTX has missing images

**Cause:** Image paths in Marp source are incorrect or images were not copied to `slides/marp/images/`

**Solution:**

1. Verify image files exist in `slides/marp/images/`
2. Check Marp source files use `images/filename.png` (not `marp/images/` or full paths)
3. Regenerate PPTX after fixing paths
4. Commit updated source files

### Issue: Slide text overflows or misaligns in PPTX

**Cause:** Content was too large for placeholder or formatting didn't apply correctly

**Solution:**

1. Note which slides have issues (slide numbers)
2. Edit `.deck.md` source files to reduce content or split across slides
3. Regenerate PPTX
4. If issue persists, check template layout placeholders (View → Slide Master in PowerPoint)

### Issue: Speaker notes are missing from PPTX

**Cause:** Marp source files lack `::: notes` blocks or notes weren't generated

**Solution:**

1. Add comprehensive `::: notes` blocks to `.deck.md` files with delivery guidance
2. Include in notes: timing, key points, audience engagement tips, transitions
3. Regenerate PPTX
4. Verify in PowerPoint (View → Notes)

### Issue: OneDrive file won't sync or shows "pending upload"

**Cause:** File is locked by PowerPoint or network connectivity issue

**Solution:**

1. Close PowerPoint and wait 30 seconds
2. Check OneDrive sync status (notification area → OneDrive icon)
3. If still pending, manually refresh (OneDrive icon → click to open)
4. Verify network connectivity
5. Force sync: `OneDrive /resetsyncengine` (Windows PowerShell)

### Issue: Cannot connect to OneDrive folder from PowerShell

**Cause:** OneDrive path not yet synced or special characters in folder name

**Solution:**

1. Verify folder exists in OneDrive (open File Explorer → OneDrive folder manually)
2. Use UNC path if available: `\\server\share\training\...`
3. Or mount OneDrive as a network drive and use drive letter
4. Copy file manually using File Explorer if script fails

### Issue: Merged deck has duplicate sections or missing decks

**Cause:** Manifest YAML syntax error or deck file paths are incorrect

**Solution:**

1. Validate manifest YAML: open in VS Code, check for red squiggles
2. Verify all deck file paths exist: `ls slides/marp/[filename].deck.md`
3. Check for typos in section names or deck paths
4. Re-run merge after fixing manifest
5. Commit corrected manifest

---

## Related Documentation

- **Slide Pipeline Specification**: [`.github/instructions/slide-pipeline.instructions.md`](../.github/instructions/slide-pipeline.instructions.md)
- **Scripts README**: [`scripts/README.md`](../scripts/README.md)
- **AI-Assisted Output Instructions**: [`.github/instructions/ai-assisted-output.instructions.md`](../.github/instructions/ai-assisted-output.instructions.md)

---

**Document Version:** 1.0.0
**Last Updated:** 2026-03-31
**Owner:** John Michael Miller
**Chat Log:** [ai-logs/2026/03/31/slide-pipeline-workflow-20260331](../ai-logs/2026/03/31/slide-pipeline-workflow-20260331/)
