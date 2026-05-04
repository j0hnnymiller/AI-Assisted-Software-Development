# update-deck-titles-with-mof.ps1
# Rewrites each deck H1 from:
#   # Witty Title                   (newly-added)  →  # Matter of Fact Title || Witty Title
#   # Matter of Fact Title          (pre-existing) →  # Matter of Fact Title || Witty Title
#
# Run from repo root.

$basePath = "c:\git\AIASD\AI-Assisted-Software-Development-Course\slides\marp"

# Each entry:  filename = @("Matter of Fact Title", "Witty Title")
# For files that already had an H1 (their existing text becomes the MoF, and we add the witty suffix).
# For files updated by the previous script (their existing text IS the witty, we prepend the MoF).

$titles = [ordered]@{
    # --- files that previously had H1s (their existing H1 = MoF; add witty suffix) ---
    "ai-assisted-output.deck.md"                                     = @("AI-Assisted Output",
        "The Compiler That Covers Its Tracks")
    "business-rules-to-slices.deck.md"                               = @("Business Rules to Vertical Slices",
        "From Boardroom to Backlog in One Prompt")
    "copilot-instruction-file-types.deck.md"                         = @("When to Use Each Copilot Instruction File Type",
        "Right Tool, Right File, Right AI Behavior")
    "creating-custom-agents.deck.md"                                 = @("Creating Custom Agents",
        "Build the Robot That Does Your Bidding")
    "dependency-management-policy.deck.md"                           = @("Dependency Management Policy",
        "npm install chaos --save-never")
    "github-cli.deck.md"                                             = @("GitHub CLI",
        "The Terminal Never Lies")
    "vs2026-copilot-context-management.deck.md"                      = @("Managing Context with GitHub Copilot",
        "Your AI Has a Memory - Use It Wisely")

    # --- files updated by the previous script (their existing H1 = witty; prepend MoF) ---
    "20260323-aiasd-repos.deck.md"                                   = @("Forking and Cloning Course Repositories",
        "Three Repos Walk Into a GitHub...")
    "about-code.deck.md"                                             = @("About CODE Magazine",
        "Thirty Years and Still Compiling")
    "adding-ai-guardrails.deck.md"                                   = @("Adding AI Guardrails",
        "Teaching Your AI to Color Inside the Lines")
    "addressing-technical-debt.deck.md"                              = @("Addressing Technical Debt with Copilot",
        "Your Technical Debt Has an AI Payment Plan")
    "advanced-context-techniques.deck.md"                            = @("Advanced Context Techniques",
        "Garbage In, Hallucinations Out")
    "ai-assisted-cicd-pipelines.deck.md"                             = @("AI-Assisted CI/CD Pipelines",
        "YAML: Now With 50% Less Soul-Crushing Manual Edits")
    "ai-assisted-github-pull-requests.deck.md"                       = @("AI-Assisted Pull Request Workflows",
        "Pull Requests That Actually Get Reviewed")
    "ai-development-approaches-comparison.deck.md"                   = @("Comparing AI Development Approaches",
        "Know Thy Copilot: Context, Artifacts, and Agent Files")
    "ai-first-vs-prompt-first.deck.md"                               = @("AI-First vs. Prompt-First Development",
        "Philosophy vs. Practice: The AI Developer's Identity Crisis")
    "ai-implementation-workflow.deck.md"                             = @("AI Implementation Workflow",
        "Don't Let the AI Drive Before You Check the Mirrors")
    "ai-practitioner-resources.deck.md"                              = @("AI Practitioner Resources",
        "The AI Practitioner's Cheat Sheet")
    "basic-vertical-slice-workflow.deck.md"                          = @("Basic Vertical Slice Workflow",
        "Thin Slices, Big Results")
    "building-a-backlog.deck.md"                                     = @("Building a Technical Debt Backlog",
        "Finally, an Excuse to File All Those Issues")
    "code-explanation-and-analysis.deck.md"                          = @("Code Explanation and Analysis",
        'Ctrl+I: The "What Does This Even Do?" Button')
    "code-quality-analysis-exercise.deck.md"                         = @("Code Quality Analysis Exercise",
        "AI-Powered Code Shame Session")
    "code-translation-technical-hotspot-analysis.deck.md"            = @("Code Translation and Hotspot Analysis",
        "The Language School for Legacy Code")
    "conformance-and-gap-analysis.deck.md"                           = @("Conformance and Gap Analysis",
        "The Architectural Rules Lawyer Is In")
    "copilot-instruction-control.deck.md"                            = @("Controlling Copilot Instruction Files",
        "Who's Allowed at the AI Dinner Table?")
    "copilot-instruction-files-vs-prompt-files-vs-chatmodes.deck.md" = @("Instruction Files vs. Prompt Files vs. Chat Modes",
        "Three Flavors of Telling Your AI What to Do")
    "copilot-pricing-licensing.deck.md"                              = @("GitHub Copilot Pricing and Licensing",
        "How Much Does an AI Pair Programmer Cost?")
    "core-instruction-files.deck.md"                                 = @("Core Instruction Files",
        "The Constitution of Your AI Republic")
    "cqrs-architecture.deck.md"                                      = @("CQRS Architecture",
        "Reads and Writes: Better Apart, Like Most Couples")
    "creating-instruction-files-from-prompts.deck.md"                = @("Creating Instruction Files from Prompts",
        "The Prompt That Writes the Rules That Guide the Prompt")
    "creating-robust-testing-frameworks.deck.md"                     = @("Creating Robust Testing Frameworks",
        "Tests So Comprehensive Even You'd Be Impressed")
    "custom-agent-best-practices.deck.md"                            = @("Custom Agent Best Practices",
        "Your AI Agent Is Not a Swiss Army Knife")
    "custom-agents.deck.md"                                          = @("Custom Agents Overview",
        "The Org Chart Your AI Actually Respects")
    "daily-themes.deck.md"                                           = @("Course Daily Themes",
        "Five Days. One AI. Zero Excuses.")
    "dependency-analysis-planning.deck.md"                           = @("Dependency Analysis and Planning",
        "Everything Depends on This Slide (Literally)")
    "documentation-generation-code-analysis.deck.md"                 = @("Documentation Generation and Code Analysis",
        "The README That Writes Itself (Finally)")
    "effective-prompts-for-technical-debt.deck.md"                   = @("Effective Prompts for Technical Debt",
        "The Art of Complaining Productively to Your AI")
    "evergreen-software-core-principles.deck.md"                     = @("Evergreen Software Core Principles",
        "Code That Doesn't Rot: A Love Story")
    "exercise-addressing-technical-debt-with-copilot.deck.md"        = @("Exercise: Addressing Technical Debt with Copilot",
        "Exercise: Ask Copilot to Clean Your Room")
    "exercise-business-requirements-generation.deck.md"              = @("Exercise: Business Requirements Generation",
        "Exercise: Let the AI Write the Requirements for Once")
    "exercise-c4-diagrams-from-code.deck.md"                         = @("Exercise: C4 Diagrams from Code",
        "Exercise: Boxes, Arrows, and the Truth About Your Architecture")
    "exercise-calculator-project.deck.md"                            = @("Exercise: Calculator Project Setup",
        "Exercise: The Calculator That Launched a Thousand Prompts")
    "exercise-create-and-use-custom-agent.deck.md"                   = @("Exercise: Create and Use a Custom Agent",
        "Exercise: Build the AI That Does Your Job (Just This One Task)")
    "exercise-create-and-use-custom-skill.deck.md"                   = @("Exercise: Create and Use a Custom Skill",
        "Exercise: Teach Your AI a New Trick")
    "exercise-creating-prompt-files.deck.md"                         = @("Exercise: Creating Prompt Files",
        "Exercise: The Prompt Engineering Gauntlet")
    "exercise-evergreen-software-intro.deck.md"                      = @("Exercise: Evergreen Software Introduction",
        "Exercise: Stop Writing Code That Needs a Eulogy")
    "exercise-fork-and-clone-repositories.deck.md"                   = @("Exercise: Fork and Clone Repositories",
        "Exercise: Your First git clone of Many")
    "exercise-github-copilot-vscode-workflows.deck.md"               = @("Lab: Getting Started with GitHub Copilot in VS Code",
        "Lab: Your AI Copilot Reports for Duty")
    "exercise-mcp-server-create-test-use.deck.md"                    = @("Exercise: Create, Test, and Use an MCP Server",
        "Exercise: Build the Bridge Between Copilot and Everything Else")
    "exercise-technology-inventory-instructions.deck.md"             = @("Exercise: Technology Inventory and Instruction Generation",
        "Exercise: Take Stock Before You Start Spending Tokens")
    "exercise-template.deck.md"                                      = @("Exercise: Template",
        "Exercise: Insert Wit Here")
    "exercise-test-automation-quality.deck.md"                       = @("Exercise: Test Automation and Quality",
        "Exercise: The Tests You Always Meant to Write")
    "exercise-test-coverage-improvement.deck.md"                     = @("Exercise: Test Coverage Improvement",
        'Exercise: From "It Works on My Machine" to Actually Tested')
    "exercise-test-driven-development.deck.md"                       = @("Exercise: Test-Driven Development with Copilot",
        "Exercise: Write the Test First. Trust the Process.")
    "feature-flags-and-test-suites.deck.md"                          = @("Feature Flags and Test Suites",
        "Ship It Behind a Flag and Pretend It's Not There Yet")
    "getting-started-checklist.deck.md"                              = @("Getting Started Checklist",
        "The Recipe Before the Meal")
    "github-cli-pr-management.deck.md"                               = @("GitHub CLI and Pull Request Management",
        "gh pr merge --squash (and Mean It)")
    "github-code-review-with-copilot.deck.md"                        = @("GitHub Code Review with Copilot",
        'The AI Reviewer Who Never Says "Looks Good to Me"')
    "github-copilot-chat-mode-personas.deck.md"                      = @("GitHub Copilot Chat Mode Personas",
        "One Copilot, Many Hats")
    "github-copilot-for-teams.deck.md"                               = @("GitHub Copilot for Teams",
        "Deploying AI Without Deploying Chaos")
    "github-copilot-skills-practical-introduction.deck.md"           = @("GitHub Copilot Skills: A Practical Introduction",
        "Skills: The API for Telling Copilot How to Think")
    "hands-on-with-github-copilot-visual-studio.deck.md"             = @("Hands-On with GitHub Copilot in Visual Studio",
        "GitHub Copilot Meets the IDE That Never Left")
    "hands-on-with-github-copilot-vs-code.deck.md"                   = @("Hands-On with GitHub Copilot in VS Code",
        "Getting Your Pair Programmer to Stop Guessing")
    "implementation-plan-prioritization.deck.md"                     = @("Implementation Plan Prioritization",
        "Security First: The Only Priority With No Exceptions")
    "implementation-prompts-verification.deck.md"                    = @("Implementation Prompts and Verification",
        "The Prompt That Does the Implementation (With a Checklist)")
    "implementing-vertical-slices.deck.md"                           = @("Implementing Vertical Slices",
        "Stop Organizing Code by Type, Start by Intent")
    "instruction-file-applyto-patterns.deck.md"                      = @("Instruction File applyTo Patterns",
        "Glob Patterns: The Bouncer at Your AI's Door")
    "instruction-files.deck.md"                                      = @("Instruction Files",
        "The .editorconfig for Your AI's Soul")
    "introductions.deck.md"                                          = @("Course Introductions",
        "Hi, I'm a Developer Who Has Talked to a Robot")
    "john-michael-miller-intro.deck.md"                              = @("Instructor Introduction",
        "The Human Behind the AI Prompts")
    "large-language-models.deck.md"                                  = @("Large Language Models",
        "It's Not Magic. It's Calculus.")
    "legacy-code-evergreen.deck.md"                                  = @("Legacy Code and Evergreen Development",
        "The Code That Time Forgot (But Production Didn't)")
    "managing-github-copilot-effectively.deck.md"                    = @("Managing GitHub Copilot Effectively",
        "Fast, Eager, and Sometimes Confidently Wrong")
    "managing-instruction-files-context-windows.deck.md"             = @("Managing Instruction Files and Context Windows",
        "You Only Have So Many Tokens - Use Them Wisely")
    "markdown-formatting-regression.deck.md"                         = @("Markdown Formatting Regression Test",
        "Does This Bold Text Look Bold to You?")
    "mcp-model-context-protocol-servers.deck.md"                     = @("Model Context Protocol Servers",
        "Giving Your AI a USB Hub")
    "model-selection-and-comparison.deck.md"                         = @("Model Selection and Comparison",
        "So Many Models, So Few Context Windows")
    "multi-model-implementation-comparison.deck.md"                  = @("Multi-Model Implementation Comparison",
        "Ask Three AIs, Get Four Opinions")
    "organizational-vs-repository-instruction-files.deck.md"         = @("Organizational vs. Repository Instruction Files",
        "Corporate Rules vs. Your Team's Rules")
    "prompt-files.deck.md"                                           = @("Prompt Files",
        "Prompts That Run, Not Just Chat")
    "pull-request-code-review.deck.md"                               = @("Pull Request Code Review",
        "The Code Review That Doesn't Ghost You")
    "repository-and-tool-setup.deck.md"                              = @("Repository and Tool Setup",
        "Day One: Clone Something, Break Nothing")
    "safe-ai-assisted-coding.deck.md"                                = @("Safe AI-Assisted Coding",
        "AI Goes Faster. Tests Make Sure It Goes Somewhere Good.")
    "safe-brownfield-coding.deck.md"                                 = @("Safe Brownfield Coding",
        "Don't Break Production. Use a Flag.")
    "safety-measures-best-practices.deck.md"                         = @("Safety Measures and Best Practices",
        "Code Review: The Last Line of Defense Against AI Overconfidence")
    "starting-with-requirements.deck.md"                             = @("Starting with Requirements",
        "Build the Right Thing Before Building the Thing Right")
    "technology-stack-instruction-files.deck.md"                     = @("Technology Stack Instruction Files",
        "Teaching Your AI the House Rules for Every Room")
    "test-automation-and-code-quality.deck.md"                       = @("Test Automation and Code Quality",
        "The Test Suite You Deserved All Along")
    "testing-in-production.deck.md"                                  = @("Testing in Production",
        "Testing in Production: Bravery or Strategy?")
    "the-ai-revolution.deck.md"                                      = @("The AI Revolution in Software Development",
        "With Great Token Budget Comes Great Responsibility")
    "understanding-legacy-code.deck.md"                              = @("Understanding Legacy Code",
        "Legacy Code Deserves Respect, Not Fear")
    "vertical-slice-implementation-plans.deck.md"                    = @("Vertical Slice Implementation Plans",
        "The Blueprint Before the Blueprint")
    "vertical-slice-implementation-webcat.deck.md"                   = @("Implementing Your First Vertical Slice",
        "Slice One: Where Theory Meets git commit")
    "vertical-slicing-architecture-introduction.deck.md"             = @("Vertical Slicing Architecture Introduction",
        "Features Go Vertical. Layers Go Home.")
    "vibe-coding.deck.md"                                            = @("Vibe Coding: Collaborative AI Development",
        "One Keyboard, Many Opinions, One Calculator")
    "vscode-configuration-tips.deck.md"                              = @("VS Code Configuration Tips",
        "The 30 Seconds That Save Hours")
    "vscode-copilot-agents-overview.deck.md"                         = @("VS Code Copilot Agents Overview",
        "Agents: Copilot With a To-Do List")
    "welcome-back.deck.md"                                           = @("Welcome Back",
        "The Return of the Prompter")
    "welcome-to-aiasd.deck.md"                                       = @("Welcome to AI-Assisted Software Development",
        "Welcome to the Future of Writing Code (It Involves Chatting)")
    "whats-the-big-deal.deck.md"                                     = @("What's the Big Deal About AI?",
        "The More Things Change, the More They Still Compile")
}

$updated = 0
$failed = 0

foreach ($file in $titles.Keys) {
    $mof = $titles[$file][0]
    $witty = $titles[$file][1]
    $target = "# $mof || $witty"

    $filePath = Join-Path $basePath $file
    if (-not (Test-Path $filePath)) {
        Write-Warning "File not found: $filePath"
        $failed++
        continue
    }

    try {
        $content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)

        # Replace any existing H1 line (first occurrence after front matter) with the new composite title.
        # We match "# <anything>" that does NOT start with ## — the first such line in the body.
        # Strategy: split at front matter, replace first H1 in the body.
        if ($content -match '(?s)^(---\r?\n.*?\r?\n---\r?\n)(.*)$') {
            $frontMatter = $Matches[1]
            $rest = $Matches[2]

            # Replace the first H1 line in the body (only the first match)
            $newRest = [regex]::Replace($rest, '(?m)^# (?!#).*', $target, 1)

            if ($newRest -eq $rest) {
                Write-Warning "No H1 found to replace in: $file"
                $failed++
                continue
            }

            $newContent = $frontMatter + $newRest
            [System.IO.File]::WriteAllText($filePath, $newContent, [System.Text.Encoding]::UTF8)
            Write-Host "UPDATED: $file" -ForegroundColor Green
            $updated++
        }
        else {
            Write-Warning "Could not find front matter in: $file"
            $failed++
        }
    }
    catch {
        Write-Warning "Error processing ${file}: $_"
        $failed++
    }
}

Write-Host ""
Write-Host "Done. Updated: $updated  |  Failed: $failed" -ForegroundColor Cyan
