---
marp: true
paginate: false
---

# When to Use Each Copilot Instruction File Type

## **Repo‑level `.md` files**
- Apply **everywhere** in the repo
- Always included
- For **universal rules**: style, security, logging, architecture
- No `applyTo` / `exclude` support
- Best for **global, evergreen guidance**

---

## **Scoped `<name>.instructions.md` files**
- Apply **only** when `applyTo` matches
- Can **exclude** paths
- For **language-, framework-, or domain‑specific rules**
- Ideal for precision control
- Best for **targeted, contextual guidance**

---

## **Decision Rule**
- If it should apply **repo‑wide** → use `.md`
- If it should apply **only in certain paths** → use `.instructions.md`
- If you need **exclusions** → must use `.instructions.md`

::: notes
This slide summarizes the functional difference between the two instruction file types GitHub Copilot supports inside `.github/instructions/`.
Repo‑level `.md` files are unconditional and always included.
Scoped `.instructions.md` files are conditional, support `applyTo` and `exclude`, and only activate when relevant.
The decision rule gives teams a simple, auditable way to choose the correct mechanism.
:::
