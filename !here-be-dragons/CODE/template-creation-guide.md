# PowerPoint Template Creation Guide

## Steps to Create a .potx Template

1. **Open PowerPoint and create a new presentation**
2. **Go to View > Slide Master**
3. **Customize the master layouts:**

   - Title Slide Master
   - Title and Content Master
   - Section Header Master
   - Blank Master
   - **Comparison Layout** (for side-by-side content)
   - **Content with Caption Layout** (for images with captions)

4. **Set your branding:**

   - Company colors
   - Fonts (title and body)
   - Logo placement
   - Background styles

5. **Save as template:**
   - File > Save As
   - Choose "PowerPoint Template (.potx)" format
   - Save in your slides directory

## Layout Mapping

- `# Title` → Title Slide Layout
- `## Slide Title` → Title and Content Layout
- `# Section` → Section Header Layout

## Adding a Subtitle Placeholder to Section Header Layout

1. **Create a new slide layout for Section Header:**

   - In Slide Master view, right-click on an existing layout → "Duplicate Layout"
   - Select the duplicated layout

2. **Customize the new layout:**
   - Right-click the new layout → "Rename Layout" → "Section Header"
   - Delete unnecessary placeholders
   - Keep only title placeholder (or add a large title placeholder)
   - **To add subtitle placeholder:**
     - Go to Insert tab → Text → Text Box
     - Draw a text box below the title area
     - Right-click the text box → "Set as Default for New Objects"
     - In the text box, type placeholder text like "Section Description"
     - Format the subtitle text (smaller font, different color/style)
     - Right-click text box → "Format Shape" → set as placeholder if available
     - Or use Insert → Placeholder → Text for a proper placeholder

## Required Layout Names for Pandoc Compatibility

To avoid warnings, ensure your template includes these exact layout names:

- **"Title Slide"** - Main title slide
- **"Title and Content"** - Standard bullet point slides
- **"Section Header"** - Section divider slides
- **"Two Content"** (or custom **"Two Column"**) - Two-column content
- **"Content with Caption"** - Image with caption layout
- **"Blank"** - Empty slide for custom content

### Adding Missing Layouts

1. **In Slide Master view**
2. **Right-click master slide → Insert Layout**
3. **Rename layouts to match exact names above**
4. **For Two Content / Two Column layout:**
   - Add two content placeholders side by side
   - Include title placeholder at top
5. **For Content with Caption layout:**
   - Add image placeholder on one side
   - Add text placeholder for caption
   - Include title placeholder at top

## Creating Content with Caption Layout (Detailed Steps)

1. **In Slide Master view**
2. **Right-click master slide → Insert Layout**
3. **Rename the new layout to "Content with Caption" (exact name)**
4. **Add placeholders:**
   - **Title placeholder at top:**
     - Slide Master tab → Insert Placeholder → Title
     - Draw title area across top of slide
   - **Image/Content placeholder:**
     - Slide Master tab → Insert Placeholder → Content
     - Draw on left side or main area (typically takes up 60-70% of slide width)
   - **Caption text placeholder:**
     - Slide Master tab → Insert Placeholder → Text
     - Draw below or to the right of content area
     - Format with smaller font size for caption text
5. **Format the layout:**
   - Adjust placeholder sizes and positions
   - Set caption text formatting (smaller font, italic, etc.)
   - Ensure consistent spacing and alignment
6. **Test the layout:**
   - Exit Slide Master view
   - Create new slide → select "Content with Caption" layout
   - Verify placeholders work correctly

## Creating Business-Specific Templates

When you have multiple business groups requiring different branding:

1. **Create separate template files:**
   - Open your multi-master template
   - Delete all masters except the one for the target business group
   - Save as "template-[business-group].potx"
   - Repeat for each business group

2. **Set the default master:**
   - In Slide Master view, right-click the desired master
   - Select "Preserve Master" to ensure it's the primary one
   - Delete or hide unused masters
   - Save the template

3. **Use descriptive naming:**
   - `template-engineering.potx`
   - `template-sales.potx` 
   - `template-marketing.potx`
