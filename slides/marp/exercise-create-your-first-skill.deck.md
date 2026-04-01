---
marp: true
theme: default
paginate: true
---

<!-- layout: two-column -->

## Exercise: Create Your First Skill

Objective
  - Author and commit a working Copilot skill to your repository.

Activities
  1. Create the folder structure

```bash
mkdir -p .github/skills/my-skill
```

  2. Create `SKILL.md` with required sections
  - Add the following to `.github/skills/my-skill/SKILL.md`:
    - YAML metadata (name, description, keywords)
    - Clear description of the skill's purpose
    - Numbered procedure steps (imperative, deterministic)
    - Optional examples or attached scripts

::: column

  3. Commit and test

```bash
git add .github/skills/my-skill/
git commit -m "Add my-skill"
```

Prompt Copilot with a task matching your skill's keywords. Verify it loads correctly.

Success Criteria
  - Skill folder exists in `.github/skills/`
  - `SKILL.md` contains all required sections
  - Changes are committed to your branch
  - Copilot recognizes and applies the skill in relevant conversations

::: notes
This is a hands-on exercise. Give participants 10–15 minutes to complete it. Walk around and help with questions. Emphasize that skills are version-controlled artifacts and should go through normal code review. The success criteria ensure they've met the baseline for a functional skill.
:::
