---
ai_generated: true
model: "anthropic/claude-sonnet-4.6"
operator: "johnmillerATcodemag-com"
chat_id: "aiasd-three-repos-setup-20260318"
prompt: |
  Add instructions for:
  1. Forking the AIASD-Brownfield-Example repository (j0hnnymiller/AIASD-Brownfield-Example)
  2. Forking the course materials repository (johnmillerATcodemag-com/AI-Assisted-Software-Development)
  3. Cloning the session repository (j0hnnymiller/20260323-aiasd.git) and creating personal branches
  4. Add detailed descriptions elaborating on repository purposes and contents

  Show all three repository workflows with proper distinctions between fork and clone strategies.
started: "2026-03-18T00:00:00Z"
ended: "2026-03-18T01:10:00Z"
task_durations:
  - task: "initial brownfield forking instructions"
    duration: "00:07:00"
  - task: "formatting and review"
    duration: "00:03:00"
  - task: "adding session repo clone and branch instructions"
    duration: "00:15:00"
  - task: "integration and verification"
    duration: "00:05:00"
  - task: "adding course materials fork instructions"
    duration: "00:20:00"
  - task: "updating all references from two to three repos"
    duration: "00:10:00"
  - task: "adding detailed repository descriptions"
    duration: "00:10:00"
total_duration: "01:10:00"
ai_log: "ai-logs/2026/03/18/aiasd-three-repos-setup-20260318/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---
## Forking the AIASD Brownfield Repository ### Getting Your Own Copy to Work With ::: notes
Duration ~00:01 This slide introduces the concept of forking the AIASD Brownfield Example repository. Forking creates a personal copy of the repository under your GitHub account, allowing you to experiment and make changes without affecting the original. **Key Points**: - Forking is essential for hands-on practice
- Creates an independent copy you can modify
- Maintains connection to the original repository for updates **Delivery**: Emphasize that forking is a one-time setup step that enables all subsequent exercises. **Transition**: "Let's understand why we fork instead of just cloning."
::: --- ## Why Fork Instead of Clone? **Forking Benefits**: - ✅ Your own GitHub repository
- ✅ Safe to experiment and break things
- ✅ Can create pull requests back to original
- ✅ Easy to sync updates from upstream
- ✅ Visible in your GitHub profile **Direct Cloning**: - ❌ No push permissions to original repo
- ❌ Changes stay local only
- ❌ No practice with PR workflow ::: notes
Duration ~00:02 **Key Points**: - Forking creates a full copy on GitHub under your account
- You have full control over your fork
- Can sync changes from the original (upstream) repository
- Essential for contributing back via pull requests **Demo Notes**: If showing live, navigate to GitHub and show the fork button. **Common Questions**: - "Can I just clone directly?" - Yes, but you can't push changes
- "What if the original updates?" - We'll cover syncing forks later **Transition**: "Now let's walk through the forking process."
::: --- ## Forking Via GitHub UI ### Method 1: Web Interface 1. **Navigate** to https://github.com/j0hnnymiller/AIASD-Brownfield-Example
2. **Click** the Fork button (top-right corner)
3. **Select** your GitHub account as the destination
4. **Optionally** rename your fork
5. **Choose** to copy the main branch only (recommended)
6. **Click** "Create Fork" ✨ **Result**: Repository now exists at `https://github.com/YOUR_USERNAME/AIASD-Brownfield-Example` ::: notes
Duration ~00:03 **Key Points**: - Most intuitive method for beginners
- Visual confirmation of each step
- Immediate feedback in the UI **Demo Instructions**: 1. Open the repository URL in a browser
2. Point out the Fork button location
3. Show the fork creation dialog
4. Explain the options (copy all branches vs main only)
5. Show the resulting forked repository **Common Issues**: - "I don't see the Fork button" - Check if you're logged into GitHub
- "It says 'already forked'" - You already have a fork; use that one **Best Practice**: Recommend copying main branch only for cleaner starting point. **Transition**: "For those comfortable with the command line, here's the CLI approach."
::: --- ## Forking Via GitHub CLI ### Method 2: Command Line (gh CLI) ```bash
# Fork the repository
gh repo fork j0hnnymiller/AIASD-Brownfield-Example # Fork and clone in one step
gh repo fork j0hnnymiller/AIASD-Brownfield-Example --clone # Fork with a custom name
gh repo fork j0hnnymiller/AIASD-Brownfield-Example \ --fork-name my-brownfield-example
``` **Prerequisites**: GitHub CLI installed and authenticated - Install: `winget install GitHub.cli` (Windows)
- Auth: `gh auth login` ::: notes
Duration ~00:03 **Key Points**: - Faster for developers comfortable with CLI
- Can combine fork and clone in single command
- Automatically sets up upstream remote **Demo Instructions**: 1. Show `gh auth status` to verify authentication
2. Run `gh repo fork j0hnnymiller/AIASD-Brownfield-Example --clone`
3. Show the resulting local directory
4. Run `git remote -v` to show origin and upstream **Prerequisites Check**: - Verify students have GitHub CLI installed
- If not, direct them to the UI method **CLI Benefits**: - Scriptable and repeatable
- Easier to integrate into workflows
- Automatically configures remotes properly **Common Issues**: - "gh command not found" - Need to install GitHub CLI
- "Authentication failed" - Run `gh auth login` **Transition**: "After forking, you need to clone your fork locally."
::: --- ## Cloning Your Fork ### Getting the Code on Your Machine ```bash
# Clone your fork (if you didn't use --clone)
git clone https://github.com/YOUR_USERNAME/AIASD-Brownfield-Example.git # Or use SSH
git clone git@github.com:YOUR_USERNAME/AIASD-Brownfield-Example.git # Navigate into the directory
cd AIASD-Brownfield-Example
``` **Verify your setup**: ```bash
# Check remote configuration
git remote -v # Should show:
# origin https://github.com/YOUR_USERNAME/AIASD-Brownfield-Example.git (fetch)
# origin https://github.com/YOUR_USERNAME/AIASD-Brownfield-Example.git (push)
``` ::: notes
Duration ~00:02 **Key Points**: - Clone creates a local working copy
- Origin points to YOUR fork
- SSH vs HTTPS depends on authentication preference **Demo Instructions**: 1. Copy the clone URL from GitHub
2. Run git clone command
3. Show `git remote -v` output
4. Show directory structure with `ls` or `dir` **HTTPS vs SSH**: - HTTPS: Works everywhere, may require token auth
- SSH: Requires SSH key setup but more convenient long-term **Verification Steps**: - Check that origin points to YOUR fork, not the original
- Verify you can see the files locally **Common Issues**: - "Permission denied" - Authentication problem
- "Repository not found" - Check the URL has YOUR username **Transition**: "Next, let's set up the connection to the original repository."
::: --- ## Setting Up Upstream Remote ### Staying Connected to the Original ```bash
# Add the original repository as 'upstream'
git remote add upstream https://github.com/j0hnnymiller/AIASD-Brownfield-Example.git # Verify both remotes are configured
git remote -v # Should show:
# origin https://github.com/YOUR_USERNAME/AIASD-Brownfield-Example.git
# upstream https://github.com/j0hnnymiller/AIASD-Brownfield-Example.git
``` **Why?** This lets you pull updates from the original repository while working in your fork. ::: notes
Duration ~00:02 **Key Points**: - Upstream tracks the original repository
- Origin tracks your fork
- Standard naming convention in Git workflows **Demo Instructions**: 1. Run `git remote add upstream` command
2. Show `git remote -v` showing both remotes
3. Explain origin vs upstream terminology **Conceptual Model**: ```
[Original Repo] ← upstream ← [Your Local Copy] → origin → [Your Fork]
``` **When to Use Each**: - `git push origin` - Save your work to your fork
- `git pull upstream main` - Get updates from original
- `git push upstream` - Usually disabled (no permission) **Common Issues**: - "Upstream already exists" - Already configured, skip this step
- Name confusion - Remind that these are just labels **Best Practice**: Always fetch from upstream before starting new work. **Transition**: "Now you're ready to work with the repository."
::: --- ## Your Fork Workflow ### Making Changes and Staying Updated ```bash
# 1. Fetch latest changes from original
git fetch upstream # 2. Merge upstream changes into your main
git checkout main
git merge upstream/main # 3. Create a feature branch for your work
git checkout -b feature/my-changes # 4. Make changes, commit, and push to YOUR fork
git add .
git commit -m "Your changes"
git push origin feature/my-changes # 5. Create a Pull Request on GitHub (optional)
``` ::: notes
Duration ~00:03 **Key Points**: - Always start from updated main branch
- Work in feature branches, not main
- Push to origin (your fork)
- Can create PRs to practice **Demo Instructions**: 1. Show the complete workflow sequence
2. Emphasize the fetch → merge → branch pattern
3. Demonstrate creating a feature branch
4. Show a sample commit and push **Best Practices**: - Keep main branch clean and in sync with upstream
- Use descriptive branch names
- Commit frequently with clear messages **Fork Workflow Diagram**: ```
upstream/main → your/main → feature-branch → commit → push → PR
``` **Syncing Frequency**: - Beginning of each work session
- Before creating new branches
- After major updates announced **Common Issues**: - "Diverged branches" - Resolve conflicts carefully
- "Push failed" - Might be pushing to wrong remote **Transition**: "Let's look at what to do when the original repository updates."
::: --- ## Syncing Your Fork with Updates ### Keeping Your Fork Current **When the original repository gets updates:** ```bash
# Fetch all changes from upstream
git fetch upstream # Switch to your main branch
git checkout main # Merge upstream changes
git merge upstream/main # Push updates to your fork on GitHub
git push origin main
``` **Alternative: GitHub UI Method** - Click "Sync fork" button on your fork's GitHub page
- Click "Update branch" to sync ::: notes
Duration ~00:02 **Key Points**: - Original repository may receive updates during the course
- Your fork doesn't auto-sync
- Manual sync keeps you current
- Two methods: CLI or GitHub UI **Demo Instructions**: 1. Show the command sequence
2. Navigate to fork on GitHub and show "Sync fork" button
3. Explain when this button appears (when behind upstream) **When to Sync**: - Before starting new exercises
- When instructor announces updates
- If you see "This branch is X commits behind" **Conflict Resolution**: - If you modified main: conflicts possible
- Best practice: never modify main directly
- If conflicts occur, may need to reset or resolve **UI Sync Benefits**: - Visual confirmation
- No CLI needed
- Safe for simple cases **CLI Sync Benefits**: - More control
- Can see exactly what's updating
- Better for complex scenarios **Transition**: "Now you have everything you need to work with the repository."
::: --- ## Verification Checklist ### Confirm Your Setup - [ ] Repository forked to your GitHub account
- [ ] Fork cloned to your local machine
- [ ] `origin` remote points to YOUR fork
- [ ] `upstream` remote points to original repository
- [ ] Can successfully run `git fetch upstream`
- [ ] Repository builds/runs locally (we'll test this next) **Quick Test**: ```bash
git remote -v | grep -E '(origin|upstream)'
``` **Expected Output**: - `origin`: your username
- `upstream`: j0hnnymiller ::: notes
Duration ~00:02 **Key Points**: - Use this checklist to verify correct setup
- All students should complete this before moving on
- Quick command to verify remotes **Interactive Activity**: - Have students raise hands when each item is completed
- Walk around to help anyone stuck
- Address common issues as they arise **Troubleshooting Common Issues**: 1. **Wrong origin**: ```bash
git remote set-url origin https://github.com/YOUR_USERNAME/AIASD-Brownfield-Example.git
``` 2. **Missing upstream**: ```bash
git remote add upstream https://github.com/j0hnnymiller/AIASD-Brownfield-Example.git
``` 3. **Fork not created**:
- Return to fork instructions
- Verify GitHub login **Success Criteria**: - All remotes configured correctly
- Can fetch from upstream without errors
- Local directory contains expected files **Transition**: "With your brownfield fork ready, let's set up the course materials repository."
::: --- ## Forking the Course Materials Repository ### Getting Your Own Copy of AI-Assisted-Software-Development **Now let's fork the course materials repository:** Repository: `https://github.com/johnmillerATcodemag-com/AI-Assisted-Software-Development.git` **This repository contains:** - Complete curriculum and slides
- Course labs and exercises
- Reference documentation
- AI-assisted development instructions
- Workshop materials and examples **Why fork this one too?** You can customize content, add notes, and keep your version even after the course. ::: notes
Duration ~00:02 **Key Points**: - Second repository to fork
- Contains all course curriculum materials
- Your personal reference copy
- Can customize and annotate freely **Repository Purpose**: - Master course content repository
- Slides, labs, and documentation
- Instruction files for AI assistants
- Templates and examples **Benefits of Forking**: - Personalize the content with your notes
- Keep access to materials long-term
- Practice forking workflow again
- Can contribute improvements back **Differentiation**: - Brownfield Example = Practice codebase
- AI-Assisted-Software-Development = Course materials
- Both are forked for full control **Transition**: "Let's fork this repository using the same methods we learned."
::: --- ## Forking AI-Assisted-Software-Development ### Method 1: GitHub UI 1. **Navigate** to https://github.com/johnmillerATcodemag-com/AI-Assisted-Software-Development
2. **Click** the Fork button (top-right corner)
3. **Select** your GitHub account as destination
4. **Optionally** rename (e.g., `my-aiasd-course`)
5. **Choose** to copy the main branch only (recommended)
6. **Click** "Create Fork" ✨ **Result**: Repository at `https://github.com/YOUR_USERNAME/AI-Assisted-Software-Development` **Or via GitHub CLI:** ```bash
# Fork the repository
gh repo fork johnmillerATcodemag-com/AI-Assisted-Software-Development # Fork and clone in one step
gh repo fork johnmillerATcodemag-com/AI-Assisted-Software-Development --clone
``` ::: notes
Duration ~00:02 **Key Points**: - Same forking process as brownfield
- Students should be familiar with steps now
- Can go faster since it's the second fork **Demo Instructions**: 1. Open repository URL
2. Quick demonstration of fork button
3. Show CLI alternative for speed
4. Emphasize this is repetition for practice **Name Considerations**: - Can keep default name
- Or rename to something memorable
- Example: `my-aiasd-course-2026-03` **CLI Advantage**: - If you did brownfield via CLI, this is even faster
- One command to fork and clone
- Automatic remote configuration **Common Questions**: - "Do I need both forks?" - Yes, different purposes
- "Can I just use one?" - Each serves different role
- "Why not just share access?" - Forking gives you control **Transition**: "Now let's clone and set up this repository."
::: --- ## Cloning and Setting Up Course Materials ### Getting the Repository Locally ```bash
# Clone your fork (if you didn't use --clone)
git clone https://github.com/YOUR_USERNAME/AI-Assisted-Software-Development.git # Or use SSH
git clone git@github.com:YOUR_USERNAME/AI-Assisted-Software-Development.git # Navigate into the directory
cd AI-Assisted-Software-Development # Add upstream remote
git remote add upstream https://github.com/johnmillerATcodemag-com/AI-Assisted-Software-Development.git # Verify remotes
git remote -v
``` **Expected output:** ```
origin https://github.com/YOUR_USERNAME/AI-Assisted-Software-Development.git
upstream https://github.com/johnmillerATcodemag-com/AI-Assisted-Software-Development.git
``` ::: notes
Duration ~00:02 **Key Points**: - Standard fork workflow
- Same steps as brownfield repository
- Students should be comfortable with this now **Demo Instructions**: 1. Run clone command
2. Navigate into directory
3. Add upstream remote
4. Verify with `git remote -v` **Directory Structure**: - Show key folders: slides/, Labs/, CODE/
- Point out .github/instructions/ folder
- Mention ai-logs/ for provenance tracking **Remote Configuration**: - Origin = Your fork (for your changes)
- Upstream = Original (for course updates)
- Same pattern as brownfield repo **Syncing Strategy**: - Pull updates from upstream when instructor announces
- Push your notes/changes to origin
- Keep your fork current with course **Common Issues**: - "Authentication failed" - Check GitHub credentials
- "Directory exists" - Already cloned, just cd into it
- "Permission denied" - Verify fork was created **Transition**: "Now you have access to all course materials in your own fork."
::: --- ## Exploring the Course Materials Repository ### What's Inside ```
AI-Assisted-Software-Development/
├── .github/
│ └── instructions/ # AI assistant instructions
├── slides/
│ └── marp/ # Course slide decks
├── Labs/ # Hands-on lab exercises
├── CODE/ # Code examples and templates
├── ai-logs/ # AI conversation logs
└── README.md # Repository overview
``` **Key Directories:** - **slides/**: All presentation materials
- **Labs/**: Daily lab exercises with solutions
- **CODE/**: Example code and templates
- **.github/instructions/**: Rules for AI assistants ::: notes
Duration ~00:02 **Key Points**: - Overview of repository structure
- Where to find specific materials
- Understanding organization system **Directory Details**: 1. **.github/instructions/**:
- Instructions for GitHub Copilot
- Coding standards and conventions
- AI-assisted development rules 2. **slides/marp/**:
- Marp-formatted slide decks
- Speaker notes included
- Can be compiled to presentations 3. **Labs/**:
- Day-by-day lab exercises
- Multiple language options (C#, Python, TypeScript)
- Progressive difficulty 4. **CODE/**:
- Reference implementations
- Templates for new projects
- Best practice examples 5. **ai-logs/**:
- Conversation history
- Provenance tracking
- Example AI interactions **Customization Ideas**: - Add your own notes in a `notes/` folder
- Annotate slides with insights
- Track your progress in a journal
- Document questions and answers **Best Practices**: - Don't modify original content directly
- Create a `custom/` or `my-notes/` folder
- Use branches for experiments
- Keep main branch clean for syncing **Transition**: "Let's move on to setting up the collaborative session repository."
::: --- ## Cloning the Course Repository ### Working with the 20260323-AIASD Repository **For this session, we'll also use a dedicated course repository:** Repository: `https://github.com/j0hnnymiller/20260323-aiasd.git` **This repository contains:** - Course-specific examples
- Hands-on exercises
- Session materials
- Starting templates **Note:** Unlike the brownfield example, we'll clone this directly and work on personal branches. ::: notes
Duration ~00:02 **Key Points**: - This is a different workflow from forking
- Direct clone with personal branches
- Used for collaborative course work
- Each student works on their own branch **Differentiation**: - Brownfield Example = Your fork (full control)
- 20260323-AIASD = Shared repo (personal branches) **When to Use Each**: - Fork: Long-term projects, portfolio work
- Clone + Branch: Team environments, courses, shared projects **Transition**: "Let's clone this repository and set up your personal workspace."
::: --- ## Cloning the 20260323-AIASD Repository ### Getting Started ```bash
# Clone the repository
git clone https://github.com/j0hnnymiller/20260323-aiasd.git # Navigate into the directory
cd 20260323-aiasd # Check current branch
git branch
``` **Or using SSH:** ```bash
git clone git@github.com:j0hnnymiller/20260323-aiasd.git
cd 20260323-aiasd
``` **Verify the clone:** ```bash
# Check remote configuration
git remote -v # Should show:
# origin https://github.com/j0hnnymiller/20260323-aiasd.git (fetch)
# origin https://github.com/j0hnnymiller/20260323-aiasd.git (push)
``` ::: notes
Duration ~00:02 **Key Points**: - Standard git clone operation
- No forking needed for this repository
- Origin points directly to the shared repository
- All students clone the same repository **Demo Instructions**: 1. Copy repository URL from GitHub
2. Run git clone command in your workspace directory
3. Navigate into the cloned directory
4. Verify with `git remote -v` **Directory Organization**: - Suggest cloning in a dedicated course workspace
- Example: `C:\git\courses\aiasd\` or `~/courses/aiasd/` **HTTPS vs SSH**: - HTTPS: Works immediately, may prompt for credentials
- SSH: Requires SSH key setup but smoother for multiple operations **Common Issues**: - "Authentication failed": Need GitHub credentials or token
- "Already exists": Directory name conflict, clone elsewhere or rename **Transition**: "Now let's create your personal branch."
::: --- ## Creating Your Personal Branch ### Setting Up Your Workspace **Create a branch with your name or identifier:** ```bash
# Create and switch to your personal branch
git checkout -b yourname-workspace # Example with actual name:
git checkout -b john-miller-workspace # Or use a convention like firstname-lastname:
git checkout -b jane-doe-workspace
``` **Verify your branch:** ```bash
# Check current branch (should show your new branch with *)
git branch # Or see current branch in prompt
git status
``` ::: notes
Duration ~00:02 **Key Points**: - Each student creates their own named branch
- Branch names should be unique and identifiable
- This prevents conflicts between students
- All work happens in personal branches **Naming Convention**: - Use lowercase with hyphens
- Include "workspace" or "dev" suffix
- Examples: `john-smith-workspace`, `jane-doe-dev`
- Avoid special characters except hyphens **Demo Instructions**: 1. Show creating a branch with example name
2. Show `git branch` output highlighting active branch
3. Explain the asterisk (\*) indicates current branch **Why Personal Branches?**: - Isolates your work from others
- Safe to experiment
- Easy to reset if needed
- Can be pushed for instructor review **Branch Strategy**: - One main personal branch for the session
- Can create feature branches off your personal branch if needed **Transition**: "Let's push your branch and verify the setup."
::: --- ## Pushing Your Personal Branch ### Making Your Branch Available ```bash
# Push your branch to the remote repository
git push -u origin yourname-workspace # The -u flag sets up tracking
# Future pushes can just be: git push
``` **After pushing:** ```bash
# Verify tracking is set up
git branch -vv # Should show your branch tracking origin/yourname-workspace
``` **Create a test commit to verify access:** ```bash
# Create a test file
echo "# My Workspace" > README-yourname.md
git add README-yourname.md
git commit -m "Initial workspace setup"
git push
``` ::: notes
Duration ~00:02 **Key Points**: - Push creates your branch on the remote
- `-u` flag sets up tracking for easier future pushes
- Verify with a test commit
- Confirms you have push access **Demo Instructions**: 1. Push the branch with `-u` flag
2. Show the tracking information with `git branch -vv`
3. Create a test commit and push
4. Show the branch on GitHub **Upstream Tracking Benefits**: - Can use `git push` without specifying branch name
- `git pull` automatically knows where to pull from
- `git status` shows ahead/behind information **Permissions Check**: - If push fails, may not have repository access
- Instructor needs to add you as collaborator
- Provide your GitHub username **Best Practice**: - Push your branch early to claim the name
- Commit and push regularly during exercises
- Allows instructor to review your progress **Common Issues**: - "Permission denied": Need to be added as collaborator
- "Branch already exists": Someone else used that name, choose another **Transition**: "Now you have all three repositories set up - let's review the workflow."
::: --- ## Three-Repository Workflow ### Understanding Your Setup **AIASD-Brownfield-Example (Forked):** This is a real-world codebase from GitHub - not a toy example! It contains actual production-style code with technical debt, legacy patterns, and opportunities for improvement. Perfect for practicing AI-assisted refactoring and modernization techniques. - ✅ Your own copy on GitHub
- ✅ Full control and experimentation
- ✅ Practice ground for techniques
- ✅ Realistic brownfield codebase with typical challenges
- ✅ Can create PRs to original **AI-Assisted-Software-Development (Forked):** This repository is your complete AI development toolkit! It contains example `.instructions.md` files for configuring AI assistants, `.prompt.md` files for reusable workflows, `.agent.md` configurations, and code samples demonstrating best practices. You can copy these patterns directly into your own projects. - ✅ Your personal course materials copy
- ✅ Example instruction files for GitHub Copilot
- ✅ Reusable prompt templates and agent configurations
- ✅ Reference code samples and implementations
- ✅ Add notes and customizations
- ✅ Reference materials and curriculum
- ✅ Keep access after course ends **20260323-AIASD (Cloned with Personal Branch):** This is our collaborative workspace for the course session. All the code, documentation, and artifacts you create during class exercises will be pushed here on your personal branch. The instructor can review your work, and you can see the collective progress of the class. - ✅ Shared course repository
- ✅ Work on your named branch
- ✅ Push all exercise solutions and practice code here
- ✅ Files created during live coding sessions
- ✅ Session-specific exercises
- ✅ Instructor can review and provide feedback
- ✅ Collaborative environment ```bash
# Quick way to see which repo you're in:
git remote get-url origin
``` ::: notes
Duration ~00:02 **Key Points**: - Three different repositories, three different workflows
- Each serves a distinct purpose
- Know which repository you're working in
- Different push/pull strategies for each **Repository Purposes**: 1. **Brownfield Example**:
- Real-world codebase from GitHub (not a toy example)
- Contains authentic technical debt and legacy code
- Practice ground for AI-assisted refactoring
- Long-term reference
- Your portfolio piece
- Experimentation sandbox
- Can keep after course 2. **AI-Assisted-Software-Development**:
- Complete AI development toolkit
- Example .instructions.md files for AI configuration
- Reusable .prompt.md templates
- .agent.md configurations
- Reference code samples
- Course curriculum materials
- Long-term reference documentation
- Your annotated study guide
- Copy patterns into your projects
- Keep indefinitely 3. **20260323-AIASD**:
- Collaborative workspace for course session
- All exercise solutions pushed here
- Live coding and practice artifacts
- Session-specific work
- Shared exercises
- Instructor can review your branch
- Course coordination
- Immediate feedback on your work **Workflow Comparison**: | Action | Brownfield (Fork) | Course Materials (Fork) | 20260323-AIASD (Branch) |
| --------- | ----------------------- | ----------------------- | ----------------------- |
| Updates | Sync from upstream | Sync from upstream | Pull from origin/main |
| Your work | Any branch in your fork | Any branch in your fork | Your personal branch |
| Share | Create PR to upstream | Create PR to upstream | Push to your branch |
| Access | Full control | Full control | Shared collaboration | **Directory Organization**: ```
workspace/
├── AIASD-Brownfield-Example/ (your fork - practice code)
├── AI-Assisted-Software-Development/ (your fork - course materials)
└── 20260323-aiasd/ (shared repo - session work)
``` **Common Confusion**: - "Which repo should I use?" - Instructor will specify per exercise
- "Can I push to main?" - No, always work in branches
- "Do I need all three?" - Yes, each serves a specific purpose **Transition**: "Let's create a checklist to verify all three repositories are ready."
::: --- ## Complete Setup Verification ### Confirm All Three Repositories **AIASD-Brownfield-Example Checklist:** - [ ] Forked to your GitHub account
- [ ] Cloned locally
- [ ] `origin` points to YOUR fork
- [ ] `upstream` points to j0hnnymiller/AIASD-Brownfield-Example
- [ ] Can run `git fetch upstream` **AI-Assisted-Software-Development Checklist:** - [ ] Forked to your GitHub account
- [ ] Cloned locally
- [ ] `origin` points to YOUR fork
- [ ] `upstream` points to johnmillerATcodemag-com/AI-Assisted-Software-Development
- [ ] Can run `git fetch upstream` **20260323-AIASD Checklist:** - [ ] Cloned locally
- [ ] Created personal branch (`yourname-workspace`)
- [ ] Pushed personal branch to origin
- [ ] Can run `git push` successfully
- [ ] `origin` points to j0hnnymiller/20260323-aiasd ::: notes
Duration ~00:02 **Key Points**: - Use these checklists to verify complete setup
- All three repositories should be ready
- Troubleshoot any issues before proceeding
- Get instructor help if stuck **Interactive Activity**: - Have students verify each item
- Show of hands when all three repositories ready
- Pair up students to help each other
- Instructor circulates to help **Quick Verification Commands**: ```bash
# For Brownfield:
cd AIASD-Brownfield-Example
git remote -v
git fetch upstream # For Course Materials:
cd ../AI-Assisted-Software-Development
git remote -v
git fetch upstream # For 20260323-AIASD:
cd ../20260323-aiasd
git remote -v
git branch
git push
``` **Troubleshooting Resources**: - Review previous slides for setup steps
- Check Git configuration: `git config --list`
- Verify GitHub authentication: `gh auth status` **Success Criteria**: - All three repositories cloned
- Correct remotes configured
- Can push/pull without errors
- Ready for hands-on exercises **Transition**: "With all three repositories ready, you're fully set for the entire course."
::: --- ## Next Steps ### Ready to Develop! **You're now prepared to:** 1. ✅ Experiment freely in your brownfield fork
2. ✅ Reference course materials in your curriculum fork
3. ✅ Work collaboratively in the session repository
4. ✅ Follow along with all course exercises
5. ✅ Practice pull request workflows
6. ✅ Sync updates as the course progresses
7. ✅ Create branches for different features **Resources:** - Brownfield Repository: https://github.com/j0hnnymiller/AIASD-Brownfield-Example
- Your Brownfield Fork: `https://github.com/YOUR_USERNAME/AIASD-Brownfield-Example`
- Course Materials: https://github.com/johnmillerATcodemag-com/AI-Assisted-Software-Development
- Your Course Fork: `https://github.com/YOUR_USERNAME/AI-Assisted-Software-Development`
- Session Repository: https://github.com/j0hnnymiller/20260323-aiasd
- Your Branch: `yourname-workspace`
- GitHub Docs: https://docs.github.com/en/get-started/quickstart/fork-a-repo ::: notes
Duration ~00:01 **Key Points**: - Setup is complete for all three repositories
- Two forks for independent work and reference
- Personal branch for collaborative session work
- Safe environment to learn and practice
- Foundation for all future exercises **Three Repository Summary**: - **Brownfield fork**: Your independent practice workspace
- **Course Materials fork**: Your personal curriculum reference
- **20260323-AIASD**: Collaborative session workspace **Encouragement**: - Setup is a one-time effort
- Worth it for comprehensive hands-on practice
- Mistakes are learning opportunities
- You have both independent and collaborative spaces **Preview Next Content**: - Next we'll explore the repository structures
- Then dive into the codebases
- Start making AI-assisted improvements
- Apply techniques in all three contexts **Resources Note**: - Bookmark all three repository URLs
- Reference when needed throughout course
- Forking applies to any open-source contribution
- Branching applies to team development **Final Check**: - "Any questions about repository setup?"
- Address any remaining concerns
- Ensure everyone has all three repos ready
- Verify everyone can push/pull **Transition**: "Let's explore what's inside these repositories."
::: --- ## Quick Reference: Repository Commands ### Command Cheat Sheet **Brownfield Fork Workflow:** ```bash
# Fork via CLI
gh repo fork j0hnnymiller/AIASD-Brownfield-Example --clone # Or fork via web + clone manually
git clone https://github.com/YOUR_USERNAME/AIASD-Brownfield-Example.git
cd AIASD-Brownfield-Example # Add upstream remote
git remote add upstream https://github.com/j0hnnymiller/AIASD-Brownfield-Example.git # Sync workflow
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
``` **Course Materials Fork Workflow:** ```bash
# Fork via CLI
gh repo fork johnmillerATcodemag-com/AI-Assisted-Software-Development --clone # Or fork via web + clone manually
git clone https://github.com/YOUR_USERNAME/AI-Assisted-Software-Development.git
cd AI-Assisted-Software-Development # Add upstream remote
git remote add upstream https://github.com/johnmillerATcodemag-com/AI-Assisted-Software-Development.git # Sync workflow
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
``` **20260323-AIASD Clone and Branch Workflow:** ```bash
# Clone the repository
git clone https://github.com/j0hnnymiller/20260323-aiasd.git
cd 20260323-aiasd # Create and push your personal branch
git checkout -b yourname-workspace
git push -u origin yourname-workspace # Regular workflow
git add .
git commit -m "Your changes"
git push
``` **Save this slide for reference!** ::: notes
**Optional Reference Slide** **Purpose**: - Quick reference for students
- Screenshot-worthy slide
- Can be shared independently
- Covers all three repository workflows **Usage**: - Keep this slide visible during exercises
- Students can refer back when needed
- Include in handout materials
- Helps students remember which commands for which repo **Three Workflow Summary**: - First section: Brownfield fork workflow (practice code)
- Second section: Course Materials fork workflow (curriculum)
- Third section: Clone + branch workflow (session work)
- Different strategies for different purposes **No Need to Read**: - This is a pure reference slide
- Mention it's available but don't read through it
- Suggest students bookmark or screenshot
- Available in slide deck for later reference **Transition**: End of repository setup module. Proceed to repository exploration or hands-on exercises.
:::
