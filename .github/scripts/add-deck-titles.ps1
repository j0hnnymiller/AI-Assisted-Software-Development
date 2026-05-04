# add-deck-titles.ps1
# Inserts a witty H1 title as the first line of the first slide in each .deck.md file
# (i.e., right after the closing --- of the YAML front matter)

$basePath = "c:\git\AIASD\AI-Assisted-Software-Development-Course\slides\marp"

$titles = [ordered]@{
    "20260323-aiasd-repos.deck.md"                                  = "Three Repos Walk Into a GitHub..."
    "about-code.deck.md"                                            = "Thirty Years and Still Compiling"
    "adding-ai-guardrails.deck.md"                                  = "Teaching Your AI to Color Inside the Lines"
    "addressing-technical-debt.deck.md"                             = "Your Technical Debt Has an AI Payment Plan"
    "advanced-context-techniques.deck.md"                           = "Garbage In, Hallucinations Out"
    "ai-assisted-cicd-pipelines.deck.md"                            = "YAML: Now With 50% Less Soul-Crushing Manual Edits"
    "ai-assisted-github-pull-requests.deck.md"                      = "Pull Requests That Actually Get Reviewed"
    "ai-development-approaches-comparison.deck.md"                  = 'Know Thy Copilot: Context, Artifacts, and Agent Files'
    "ai-first-vs-prompt-first.deck.md"                              = "Philosophy vs. Practice: The AI Developer's Identity Crisis"
    "ai-implementation-workflow.deck.md"                            = "Don't Let the AI Drive Before You Check the Mirrors"
    "ai-practitioner-resources.deck.md"                             = "The AI Practitioner's Cheat Sheet"
    "basic-vertical-slice-workflow.deck.md"                         = "Thin Slices, Big Results"
    "building-a-backlog.deck.md"                                    = "Finally, an Excuse to File All Those Issues"
    "code-explanation-and-analysis.deck.md"                         = 'Ctrl+I: The "What Does This Even Do?" Button'
    "code-quality-analysis-exercise.deck.md"                        = "AI-Powered Code Shame Session"
    "code-translation-technical-hotspot-analysis.deck.md"           = "The Language School for Legacy Code"
    "conformance-and-gap-analysis.deck.md"                          = "The Architectural Rules Lawyer Is In"
    "copilot-instruction-control.deck.md"                           = "Who's Allowed at the AI Dinner Table?"
    "copilot-instruction-files-vs-prompt-files-vs-chatmodes.deck.md" = "Three Flavors of Telling Your AI What to Do"
    "copilot-pricing-licensing.deck.md"                             = "How Much Does an AI Pair Programmer Cost?"
    "core-instruction-files.deck.md"                                = "The Constitution of Your AI Republic"
    "cqrs-architecture.deck.md"                                     = "Reads and Writes: Better Apart, Like Most Couples"
    "creating-instruction-files-from-prompts.deck.md"               = "The Prompt That Writes the Rules That Guide the Prompt"
    "creating-robust-testing-frameworks.deck.md"                    = "Tests So Comprehensive Even You'd Be Impressed"
    "custom-agent-best-practices.deck.md"                           = "Your AI Agent Is Not a Swiss Army Knife"
    "custom-agents.deck.md"                                         = "The Org Chart Your AI Actually Respects"
    "daily-themes.deck.md"                                          = "Five Days. One AI. Zero Excuses."
    "dependency-analysis-planning.deck.md"                          = "Everything Depends on This Slide (Literally)"
    "documentation-generation-code-analysis.deck.md"                = "The README That Writes Itself (Finally)"
    "effective-prompts-for-technical-debt.deck.md"                  = "The Art of Complaining Productively to Your AI"
    "evergreen-software-core-principles.deck.md"                    = "Code That Doesn't Rot: A Love Story"
    "exercise-addressing-technical-debt-with-copilot.deck.md"       = "Exercise: Ask Copilot to Clean Your Room"
    "exercise-business-requirements-generation.deck.md"             = "Exercise: Let the AI Write the Requirements for Once"
    "exercise-c4-diagrams-from-code.deck.md"                        = "Exercise: Boxes, Arrows, and the Truth About Your Architecture"
    "exercise-calculator-project.deck.md"                           = "Exercise: The Calculator That Launched a Thousand Prompts"
    "exercise-create-and-use-custom-agent.deck.md"                  = "Exercise: Build the AI That Does Your Job (Just This One Task)"
    "exercise-create-and-use-custom-skill.deck.md"                  = "Exercise: Teach Your AI a New Trick"
    "exercise-creating-prompt-files.deck.md"                        = "Exercise: The Prompt Engineering Gauntlet"
    "exercise-evergreen-software-intro.deck.md"                     = "Exercise: Stop Writing Code That Needs a Eulogy"
    "exercise-fork-and-clone-repositories.deck.md"                  = "Exercise: Your First git clone of Many"
    "exercise-github-copilot-vscode-workflows.deck.md"              = "Lab: Your AI Copilot Reports for Duty"
    "exercise-mcp-server-create-test-use.deck.md"                   = "Exercise: Build the Bridge Between Copilot and Everything Else"
    "exercise-technology-inventory-instructions.deck.md"            = "Exercise: Take Stock Before You Start Spending Tokens"
    "exercise-template.deck.md"                                     = "Exercise: Insert Wit Here"
    "exercise-test-automation-quality.deck.md"                      = "Exercise: The Tests You Always Meant to Write"
    "exercise-test-coverage-improvement.deck.md"                    = 'Exercise: From "It Works on My Machine" to Actually Tested'
    "exercise-test-driven-development.deck.md"                      = "Exercise: Write the Test First. Trust the Process."
    "feature-flags-and-test-suites.deck.md"                         = "Ship It Behind a Flag and Pretend It's Not There Yet"
    "getting-started-checklist.deck.md"                             = "The Recipe Before the Meal"
    "github-cli-pr-management.deck.md"                              = "gh pr merge --squash (and Mean It)"
    "github-code-review-with-copilot.deck.md"                       = 'The AI Reviewer Who Never Says "Looks Good to Me"'
    "github-copilot-chat-mode-personas.deck.md"                     = "One Copilot, Many Hats"
    "github-copilot-for-teams.deck.md"                              = "Deploying AI Without Deploying Chaos"
    "github-copilot-skills-practical-introduction.deck.md"          = "Skills: The API for Telling Copilot How to Think"
    "hands-on-with-github-copilot-visual-studio.deck.md"            = "GitHub Copilot Meets the IDE That Never Left"
    "hands-on-with-github-copilot-vs-code.deck.md"                  = "Getting Your Pair Programmer to Stop Guessing"
    "implementation-plan-prioritization.deck.md"                    = "Security First: The Only Priority With No Exceptions"
    "implementation-prompts-verification.deck.md"                   = "The Prompt That Does the Implementation (With a Checklist)"
    "implementing-vertical-slices.deck.md"                          = "Stop Organizing Code by Type, Start by Intent"
    "instruction-file-applyto-patterns.deck.md"                     = "Glob Patterns: The Bouncer at Your AI's Door"
    "instruction-files.deck.md"                                     = "The .editorconfig for Your AI's Soul"
    "introductions.deck.md"                                         = "Hi, I'm a Developer Who Has Talked to a Robot"
    "john-michael-miller-intro.deck.md"                             = "The Human Behind the AI Prompts"
    "large-language-models.deck.md"                                 = "It's Not Magic. It's Calculus."
    "legacy-code-evergreen.deck.md"                                 = "The Code That Time Forgot (But Production Didn't)"
    "managing-github-copilot-effectively.deck.md"                   = "Fast, Eager, and Sometimes Confidently Wrong"
    "managing-instruction-files-context-windows.deck.md"            = "You Only Have So Many Tokens - Use Them Wisely"
    "markdown-formatting-regression.deck.md"                        = "Does This Bold Text Look Bold to You?"
    "mcp-model-context-protocol-servers.deck.md"                    = "Giving Your AI a USB Hub"
    "model-selection-and-comparison.deck.md"                        = "So Many Models, So Few Context Windows"
    "multi-model-implementation-comparison.deck.md"                 = "Ask Three AIs, Get Four Opinions"
    "organizational-vs-repository-instruction-files.deck.md"        = "Corporate Rules vs. Your Team's Rules"
    "prompt-files.deck.md"                                          = "Prompts That Run, Not Just Chat"
    "pull-request-code-review.deck.md"                              = "The Code Review That Doesn't Ghost You"
    "repository-and-tool-setup.deck.md"                             = "Day One: Clone Something, Break Nothing"
    "safe-ai-assisted-coding.deck.md"                               = "AI Goes Faster. Tests Make Sure It Goes Somewhere Good."
    "safe-brownfield-coding.deck.md"                                = "Don't Break Production. Use a Flag."
    "safety-measures-best-practices.deck.md"                        = "Code Review: The Last Line of Defense Against AI Overconfidence"
    "starting-with-requirements.deck.md"                            = "Build the Right Thing Before Building the Thing Right"
    "technology-stack-instruction-files.deck.md"                    = "Teaching Your AI the House Rules for Every Room"
    "test-automation-and-code-quality.deck.md"                      = "The Test Suite You Deserved All Along"
    "testing-in-production.deck.md"                                 = "Testing in Production: Bravery or Strategy?"
    "the-ai-revolution.deck.md"                                     = "With Great Token Budget Comes Great Responsibility"
    "understanding-legacy-code.deck.md"                             = "Legacy Code Deserves Respect, Not Fear"
    "vertical-slice-implementation-plans.deck.md"                   = "The Blueprint Before the Blueprint"
    "vertical-slice-implementation-webcat.deck.md"                  = "Slice One: Where Theory Meets git commit"
    "vertical-slicing-architecture-introduction.deck.md"            = "Features Go Vertical. Layers Go Home."
    "vibe-coding.deck.md"                                           = "One Keyboard, Many Opinions, One Calculator"
    "vscode-configuration-tips.deck.md"                             = "The 30 Seconds That Save Hours"
    "vscode-copilot-agents-overview.deck.md"                        = "Agents: Copilot With a To-Do List"
    "welcome-back.deck.md"                                          = "The Return of the Prompter"
    "welcome-to-aiasd.deck.md"                                      = "Welcome to the Future of Writing Code (It Involves Chatting)"
    "whats-the-big-deal.deck.md"                                    = "The More Things Change, the More They Still Compile"
}

$updated = 0
$skipped = 0
$failed  = 0

foreach ($file in $titles.Keys) {
    $title    = $titles[$file]
    $filePath = Join-Path $basePath $file

    if (-not (Test-Path $filePath)) {
        Write-Warning "File not found: $filePath"
        $failed++
        continue
    }

    try {
        $content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)

        # Match the YAML front matter: opening ---, any content, closing ---
        # (?s) makes . match newlines; .*? is lazy so stops at the first closing ---
        if ($content -match '(?s)^(---\r?\n.*?\r?\n---\r?\n)(.*)$') {
            $frontMatter = $Matches[1]
            $rest        = $Matches[2]

            # Skip if first slide already opens with an H1
            if ($rest -match '^#\s') {
                Write-Host "SKIP (has H1): $file" -ForegroundColor Yellow
                $skipped++
                continue
            }

            # Strip any leading blank lines from the slide content so spacing is clean
            $trimmedRest = $rest -replace '^[\r\n]+', ''

            $newContent = $frontMatter + "# $title`n`n" + $trimmedRest

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
Write-Host "Done. Updated: $updated  |  Skipped (had H1): $skipped  |  Failed: $failed" -ForegroundColor Cyan
