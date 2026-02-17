# AI-Assisted Software Development with GitHub Copilot (Monday Afternoon)

## Overview

- **Total Duration**: 02:00:10 (120 minutes, 10 seconds)
- **Sections**: 14
- **Format**: VTT (WebVTT)
- **Instructor**: John Miller
- **Date**: February 9, 2026 (Monday Afternoon)
- **Session Type**: Interactive mob programming session building a calculator application

---

## Section 1: Introduction and Welcome Back (Duration: 00:00:28)

**Timestamp**: 00:01:49 - 00:02:17

### Key Topics

- Welcome back to afternoon session
- Introduction to mob programming as a collaborative tool
- Setting expectations for hands-on development work

### Notes

- Brief welcome and transition into main content
- Focus on collaborative development approach

---

## Section 2: Mob Programming Introduction (Duration: 00:04:13)

**Timestamp**: 00:02:17 - 00:06:30

### Key Topics

- What is mob programming?
- Traditional in-person vs. remote mob programming
- Role definitions: Driver, Navigator, Supporters
- Benefits of collaborative development approach

### Subsections

#### Mob Programming Roles

- **Driver**: Person at the keyboard executing commands
- **Navigator**: Person directing what needs to be done next
- **Supporters**: Team members providing research and support

#### Mob.sh Tool Benefits

- Smooth handoff during pair rotation
- Handles work-in-progress branches automatically
- Built-in timer for time management
- Automatic commit and merge cleanup
- Works with any Git provider

---

## Section 3: Installing Mob.sh Tools (Duration: 00:04:30)

**Timestamp**: 00:06:30 - 00:11:00

### Key Topics

- mob.sh installation instructions overview
- Platform-specific installation challenges
- Checking for successful installation
- Prerequisites and requirements

### Common Issues Discussed

- Windows installation problems with Scoop and Chocolatey
- Git Bash as alternative installation method
- WSL (Windows Subsystem for Linux) as backup option

---

## Section 4: Repository Cloning and Setup (Duration: 00:15:00)

**Timestamp**: 00:11:00 - 00:26:00

### Key Topics

- Cloning the course repository (AIASD-260209)
- GitHub access and authentication
- Handling GitHub service intermittent errors
- Ensuring all participants have repository access

### Subsections

#### Repository Information

- Repository: johnmillerATcodemag-com/AIASD-260209
- Purpose: Shared workspace for mob programming exercises
- Access: Collaborative permissions required

#### Technical Issues Encountered

- GitHub 500 errors (intermittent service issues)
- Clone authentication problems
- Network connectivity challenges
- Solutions: Retrying, using alternative methods

---

## Section 5: Mob Programming Tool Configuration (Duration: 00:16:00)

**Timestamp**: 00:26:00 - 00:42:00

### Key Topics

- mob start, mob next, mob done command overview
- Adding collaborators to repository
- Troubleshooting access denied errors
- Decision to abandon tool due to technical difficulties

### Subsections

#### Mob.sh Commands

- **mob start**: Begins a new mob session, creates WIP branch
- **mob next**: Commits changes and hands off to next driver
- **mob done**: Finalizes session, merges changes back

#### Collaboration Setup Challenges

- GitHub Enterprise vs. public GitHub differences
- Collaborator invitation issues
- Access permission problems
- Workaround: Instructor-driven approach with screen sharing

#### Alternative Approach Decided

- Instructor as sole driver
- Manual timer management
- Team provides navigation and direction
- Regular pushes for team synchronization

---

## Section 6: Working with GitHub Copilot - Creating .gitignore (Duration: 00:02:00)

**Timestamp**: 00:42:00 - 00:44:00

### Key Topics

- Using Copilot to generate .gitignore file
- Examining Copilot's output
- Understanding appropriate .gitignore patterns

### Example Prompt

- "Create a .gitignore file for [project type]"

---

## Section 7: Understanding Copilot's Keep/Undo Functionality (Duration: 00:06:00)

**Timestamp**: 00:44:00 - 00:50:00

### Key Topics

- Copilot change review interface
- Three levels of keeping/undoing changes
- Evaluating individual changes vs. bulk acceptance

### Subsections

#### Change Acceptance Options

- **Keep this**: Accept single specific change
- **Keep all in file**: Accept all changes in current file
- **Keep all from prompt**: Accept all changes from entire Copilot response

#### Best Practices

- Review changes incrementally for complex modifications
- Evaluate each change for correctness and intent
- Use granular control when uncertain
- Bulk acceptance for trusted, simple operations

---

## Section 8: Building a Calculator Application (Duration: 00:22:00)

**Timestamp**: 00:50:00 - 01:12:00

### Key Topics

- Creating console calculator application
- Using Copilot to build basic functionality
- Implementing arithmetic operations
- Adding input validation
- Testing the calculator

### Subsections

#### Calculator Features Implemented

- Basic arithmetic: addition, subtraction, multiplication, division
- Input parsing from console
- Error handling for invalid input
- Division by zero protection
- Exit functionality

#### Development Approach

- Iterative feature addition
- Copilot-assisted code generation
- Team collaboration on feature decisions
- Quick testing cycles

#### Key Observations

- Copilot inferred need for exit functionality without explicit request
- Automatic implementation of best practices
- Intelligent error handling suggestions

---

## Section 9: Creating Web Calculator Project with Copilot (Duration: 00:20:30)

**Timestamp**: 01:12:00 - 01:32:30

### Key Topics

- Transitioning from console to web application
- NuGet package issues encountered
- Decision to use .NET CLI for project scaffolding
- Creating Blazor/Razor web interface

### Subsections

#### Initial Challenges

- Copilot struggled with proper NuGet package installation
- Project structure confusion
- Multiple iterations required

#### Solution Approach

- Use standard .NET CLI to create boilerplate project
- Let Copilot enhance existing structure rather than create from scratch
- Focus AI on feature implementation, not infrastructure setup

#### Lessons Learned

- AI tools work better enhancing existing projects than creating infrastructure
- Combine traditional tooling with AI assistance
- Use CLI/IDE for scaffolding, AI for feature development

---

## Section 10: Continuing Web Calculator Development (Duration: 00:16:30)

**Timestamp**: 01:32:30 - 01:49:00

### Key Topics

- Running the web calculator application
- Adding digit buttons to web interface
- Implementing button click handlers
- Testing web interface functionality

### Features Added

- Digit buttons (0-9)
- Operation buttons (+, -, \*, /)
- Display panel for results
- Button styling and layout

---

## Section 11: Preview of Evergreen Code Concepts (Duration: 00:01:30)

**Timestamp**: 01:49:00 - 01:50:30

### Key Topics

- Introduction to "Evergreen" code philosophy
- Modern tooling and technologies
- Continuous code quality monitoring
- AI-assisted technical debt management

### Subsections

#### Evergreen Code Principles

- Keep code current with modern practices
- Use modern technologies and frameworks
- Continuously address technical debt
- Prevent drift from quality standards

#### AI Integration for Evergreen Code

- Automated monitoring for code quality deviations
- CI/CD integration for build-breaking checks
- Automatic issue creation for quality problems
- Integration with backlog grooming processes

#### Future Topics to Cover

- Implementing Evergreen principles
- Setting up automated monitoring
- Creating quality gates in CI/CD
- Managing technical debt systematically

---

## Section 12: Final Feature Development (Duration: 00:08:30)

**Timestamp**: 01:50:30 - 01:59:00

### Key Topics

- Adding percentage calculation button
- Final testing of web calculator
- Troubleshooting display issues
- Application refresh and verification

### Final Implementation Details

- Percentage button functionality
- UI refresh to show changes
- Complete calculator feature set
- Successful application demonstration

---

## Section 13: Wrap-up and Closing (Duration: 00:01:10)

**Timestamp**: 01:59:00 - 02:00:10

### Key Topics

- Session summary
- Preview of next day's content
- Q&A opportunity
- Closing remarks

### Looking Ahead

- Deeper dive into Evergreen code concepts
- Refactoring existing code bases
- Advanced AI collaboration techniques
- Safe code modification strategies

---

## Summary Statistics

- **Total sections**: 14
- **Average section length**: ~8 minutes 35 seconds
- **Longest section**: Tool Setup and Repository Configuration (~16 minutes 30 seconds)
- **Shortest section**: Final Feature Additions and Wrap-up (~1 minute 10 seconds)

## Participants Mentioned

- John Miller (Instructor)
- Dan Blanchard
- Matt Hoffman
- Alex Myachin
- Tom Bui
- Buddy Toups
- Peter Goostree
- Lyle Ubben
- Christopher Rockwell
- Chris Bishop
- Stephen Childs

## Key Technologies Covered

- mob.sh (collaborative programming tool)
- GitHub (version control and collaboration)
- GitHub Copilot (AI-assisted development)
- .NET / C# (application framework)
- Blazor/Razor (web UI framework)
- Git (version control)
- Visual Studio Code (implied IDE)

## Main Learning Outcomes

1. **Mob Programming Workflow**: Understanding collaborative development with defined roles (driver, navigator, supporters)
2. **GitHub Copilot Integration**: Hands-on experience generating code, tests, and UI components with AI assistance
3. **Evaluating AI Code**: Learning to review and accept/reject AI-generated changes at different granularity levels
4. **Practical Application Building**: Building a complete calculator from console to web interface using AI assistance
5. **Tool Selection Strategy**: Understanding when to use traditional tools vs. AI tools (CLI for scaffolding, AI for features)
6. **Evergreen Code Concepts**: Introduction to maintaining code quality and preventing technical debt accumulation
7. **Iterative Development**: Building features incrementally with quick testing cycles
8. **AI Inference**: Observing how AI can infer requirements and add functionality proactively

## Technologies and Tools Discussed

- **mob.sh**: Remote mob programming tool for branch management and rotation
- **GitHub Copilot**: AI-assisted code generation and completion
- **C#/.NET**: Primary programming language and framework
- **ASP.NET**: Web application framework
- **xUnit**: Testing framework for automated tests
- **Visual Studio Code**: Primary development environment
- **Git/GitHub**: Version control and collaboration platform
- **NuGet**: Package management for .NET dependencies
- **DataTable.Compute()**: Expression evaluation method

## Key Learning Outcomes from Session

1. **Mob programming enables effective team collaboration with AI tools** - coordinated approach prevents divergent AI responses
2. **AI can generate significant functionality quickly with proper prompting** - calculator built from scratch in ~2 hours
3. **Iterative development with AI assistance produces working software rapidly** - start simple, add features incrementally
4. **Test-driven development integrates naturally with AI code generation** - AI can generate tests alongside implementation
5. **Technical debt accumulates even with AI-generated code** - Evergreen concept addresses this proactively
6. **Cross-platform considerations influence technology choices** - web UI chosen for compatibility
7. **AI can infer requirements and add functionality proactively** - exit command added without explicit request
8. **Combine traditional and AI tooling strategically** - use CLI for scaffolding, AI for feature implementation

## Notable Challenges and Solutions

### Challenge 1: Mob.sh Tool Access Issues

- **Problem**: Collaborator access and GitHub synchronization problems
- **Solution**: Instructor-led approach with screen sharing

### Challenge 2: NuGet Package Installation

- **Problem**: Copilot struggled with proper package management
- **Solution**: Use .NET CLI for scaffolding, AI for features

### Challenge 3: Windows Installation Issues

- **Problem**: Scoop and Chocolatey package managers not working
- **Solution**: Git Bash or WSL as alternative installation methods

## Best Practices Demonstrated

1. **Incremental Development**: Build features iteratively with quick testing
2. **AI-Human Collaboration**: Use AI suggestions as starting point, not final solution
3. **Change Review**: Always review AI-generated code before acceptance
4. **Granular Control**: Use keep/undo options at appropriate levels
5. **Tool Selection**: Choose right tool for the task (CLI for scaffolding, AI for features)
6. **Team Collaboration**: Navigate collectively, even with single driver

## Follow-up Topics

- Advanced AI prompt engineering
- Refactoring legacy code with AI assistance
- Implementing Evergreen code monitoring
- CI/CD integration for quality gates
- Technical debt management strategies
