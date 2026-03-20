Absolutely — here's a complete, presentation-ready **slide deck** you can drop straight into Marp or any Markdown-based slide system. It's structured for a clean, instructor-friendly flow: install → configure → use → advanced patterns → troubleshooting.

You can paste this directly into a `.md` file and render with Marp.

---

# 📘 **Mob.sh: Install, Configure, and Use**

_A practical slide deck for teams adopting mob programming_

---

````markdown
---
marp: true
theme: default
paginate: true
---

# 🧰 Mob Programming with mob.sh

### Installing, Configuring, and Using mob.sh

A practical guide for high-flow collaboration

---

# 🎯 What mob.sh Solves

- Smooth handoffs during mob/pair rotations
- Automatic WIP branches
- Zero-conf timers
- Clean commits and merges
- Works with any Git provider (GitHub, GitLab, Bitbucket)

---

# 📦 Installing mob.sh

## Requirements

- Git installed
- macOS, Linux, or WSL
- Optional: Homebrew

---

# 📥 Install Options

### **Homebrew (recommended)**

```bash
brew install mob
```
````

### **Curl installer**

```bash
curl -sL https://install.mob.sh | sh
```

### **Manual**

- Download from [https://mob.sh](https://mob.sh)
- Add to PATH
- Verify with:

```bash
mob version
```

---

# 🔧 First-Time Configuration

### Set your preferred editor

```bash
mob config editor "code"
```

### Set your default WIP branch name

```bash
mob config wip-branch "mob-session"
```

### Optional: Set timer duration

```bash
mob config timer 5
```

---

# 🏁 Starting a Mob Session

### Begin a session

```bash
mob start
```

What happens:

- Creates/updates a WIP branch
- Stashes local changes
- Opens your editor
- Starts optional timer

---

# 🔄 Handoff to the Next Driver

### When your rotation ends

```bash
mob next
```

This:

- Commits WIP
- Pushes to remote
- Prepares the next driver's environment

---

# 🧪 Running Tests During the Mob

- Use watch mode (Jest, Vitest, pytest-watch)
- Keep terminal visible to the whole mob
- Encourage “test first” flow during rotations

---

# 🚀 Finishing the Mob Session

### When the feature is ready

```bash
mob done
```

This:

- Squashes WIP commits
- Merges into your main branch
- Cleans up the WIP branch

---

# 🧱 Branching Model Best Practices

### Recommended

- Feature branch per story
- mob.sh manages the WIP branch
- PR created after `mob done`

### Avoid

- Multiple mobs on the same feature branch
- Manual commits on the WIP branch

---

# 🧭 Role Rotation Tips

- Driver rotates every 5–7 minutes
- Navigator(s) guide the next steps
- Researchers support without interrupting flow
- Use a shared timer (mob.sh or external)

---

# 🛠️ Advanced Features

### **mob start --include-uncommitted**

Keep local changes when starting a session.

### **mob start --branch <name>**

Use a custom WIP branch.

### **mob timer**

Start a standalone rotation timer.

### **mob status**

Check current mob state.

---

# 🧹 Troubleshooting

### “Uncommitted changes” error

→ Run:

```bash
git stash
```

### Conflicts on `mob done`

→ Resolve locally, then:

```bash
mob done --continue
```

### Someone forgot `mob next`

→ Use:

```bash
mob start --continue
```

---

# 🧩 Integrations

### Works great with:

- VS Code Live Share
- GitHub Codespaces
- JetBrains remote collaboration
- Zoom/Teams/Meet screen sharing
- Miro/FigJam for design phases

---

# 📚 Resources

- Official site: [https://mob.sh](https://mob.sh)
- ThoughtWorks Tech Radar (Technique): Mob Programming
- GitHub repo: `https://github.com/remotemobprogramming/mob` [(github.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fgithub.com%2Fremotemobprogramming%2Fmob")

---

# 🎉 Thank You

### Ready to mob with confidence

Let's build high-flow teams together.

```

---

If you want, I can also generate:

- A **speaker-notes version**
- A **facilitator script** for running a mob programming workshop
- A **hands-on exercise deck** for teaching mob.sh to new teams
- A **dual-layer infographic** showing the mob.sh workflow

Just tell me what direction you want to take this.
```
