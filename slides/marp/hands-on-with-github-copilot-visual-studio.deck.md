---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "vs2026-copilot-deck-20260327"
prompt: |
  Using slides\marp\hands-on-with-github-copilot-vs-code.deck.md as a guide, and
  "docs\research-GitHub Copilot in Visual Studio Code vs Visual Studio 2026 Community Edition.docx"
  as a source, create a marp deck that describes the GitHub Copilot features in Visual Studio 2026.
started: "2026-03-27T00:00:00Z"
ended: "2026-03-27T00:30:00Z"
task_durations:
  - task: "requirements analysis"
    duration: "00:05:00"
  - task: "content creation"
    duration: "00:20:00"
  - task: "review and refinement"
    duration: "00:05:00"
total_duration: "00:30:00"
ai_log: "ai-logs/2026/03/27/vs2026-copilot-deck-20260327/conversation.md"
source: "johnmillerATcodemag-com"
---

# Hands-On with GitHub Copilot in Visual Studio || GitHub Copilot Meets the IDE That Never Left

---

## Hands-On with GitHub Copilot in Visual Studio 2026

Enterprise-grade AI assistance for .NET developers

- Installing and configuring Copilot
- Deep .NET/C# productivity features
- Debugging and profiler integration
- Agent mode and MCP support
- Microsoft Learn integration

::: notes
Welcome .NET developers to GitHub Copilot in Visual Studio 2026. This session covers the unique, deeply integrated AI features designed for enterprise-scale development. Visual Studio offers features that go beyond VS Code, including doc comment generation, QuickInfo enhancements, profiler agent, and Microsoft Learn integration.

**Target Audience**: .NET, C#, C++, and enterprise Windows developers
**Prerequisites**: Visual Studio 2026 Community, Professional, or Enterprise edition
**Duration**: 90 minutes hands-on
:::

---

## Installation and Setup

Getting started with Copilot in Visual Studio 2026

- **Install GitHub Copilot extension** from Extensions > Manage Extensions
- **Sign in with GitHub account** via Tools > Options > GitHub
- **Configure settings** via Tools > Options > GitHub > Copilot
- **Verify activation** by opening a code file and observing inline suggestions

**Subscription Plans:**

- Free: 2,000 completions + 50 chat requests/month
- Pro/Pro+: Unlimited completions, premium models
- Business/Enterprise: Centralized management, BYOK

::: notes
**Installation Demo (5 minutes):**

1. Open Visual Studio 2026
2. Go to Extensions > Manage Extensions
3. Search for "GitHub Copilot" and install
4. Restart Visual Studio when prompted
5. Tools > Options > GitHub > Sign in with GitHub account
6. Accept authorization in browser
7. Return to Visual Studio and verify connection

**Key Points:**

- Copilot is an **optional** extension; VS works fully without it
- Subscription managed via GitHub, not Visual Studio licenses
- Free tier is sufficient for learning and small projects
- Enterprise customers get centralized policy controls

**Common Issues:**

- Authentication failures: Clear browser cache or try different browser
- Extension not appearing: Ensure Visual Studio 2026 or later
- No suggestions: Check Tools > Options > GitHub > Copilot > Enable completions

**Reference**: https://docs.github.com/copilot/using-github-copilot/getting-started-with-github-copilot-in-visual-studio
:::

---

## Core Features: Inline Completions

Ghost text suggestions as you type

- **Automatic suggestions** appear as gray ghost text
- **Tab to accept** entire suggestion
- **Ctrl+Right Arrow** to accept next word
- **Next Edit Suggestions (NES)** predict follow-up edits anywhere in the file
- **Navigation arrows** in gutter indicate suggested changes

::: column

**Use Cases:**

- Completing method implementations
- Generating boilerplate code
- Writing LINQ queries
- Creating unit tests

::: notes
**Demo: Inline Completions (8 minutes)**

1. **Basic Completion:**
   - Create new C# class: `public class OrderProcessor`
   - Start typing method signature: `public decimal Calculate`
   - Observe ghost text suggestion completing the method
   - Press Tab to accept

2. **Multi-line Completion:**
   - Type method comment: `// Calculate order total with discounts`
   - Press Enter, start method: `public decimal CalculateTotal(`
   - Copilot suggests full method with parameters, logic, return

3. **Next Edit Suggestions (NES):**
   - Rename a variable (e.g., `price` to `unitPrice`)
   - Look for gutter arrows indicating related changes
   - Press Tab to navigate and accept suggestions
   - Demonstrate how NES updates all related references

**Key Teaching Points:**

- Ghost text is **predictions**, not guaranteed correct—always review
- NES uses recent changes to predict logical follow-up edits
- Multi-line suggestions can scaffold entire methods, reducing boilerplate
- Accept word-by-word (Ctrl+Right Arrow) for fine-grained control

**Troubleshooting:**

- No suggestions appearing: Check enabled in Tools > Options
- Wrong suggestions: Improve context with better comments or method names
- Performance issues: Close unused files, update Visual Studio

**Best Practices:**

- Write descriptive method names and comments to guide suggestions
- Use NES for refactoring—faster than Find/Replace
- Review generated code for logic errors, security issues
  :::

---

## Copilot Chat: Natural Language Assistance

Multi-surface conversational AI

**Chat Surfaces:**

- **Chat Pane** (View > Chat): Dedicated window for Q&A and research
- **Inline Chat** (Alt+/): In-editor modifications and queries
- **Context Menus**: Right-click code > Ask Copilot

::: column

**Key Capabilities:**

- Code explanations and documentation
- Refactoring suggestions
- Bug fixing and error analysis
- Generating tests and documentation
- Answering .NET/C# questions

::: notes
**Demo: Copilot Chat Modes (10 minutes)**

1. **Chat Pane (Q&A):**
   - Open View > Chat (or Ctrl+Q, type "Copilot Chat")
   - Ask: "What's the difference between IEnumerable and IQueryable?"
   - Ask: "Show me how to use async/await with HttpClient"
   - Ask: "Generate a repository pattern for Entity Framework Core"
   - Observe detailed, context-aware responses

2. **Inline Chat (Code Modifications):**
   - Select a method in the editor
   - Press Alt+/ to open inline chat
   - Type: "Add error handling with try-catch and logging"
   - Press Enter—Copilot modifies the code inline
   - Review changes before accepting

3. **Context Menu Integration:**
   - Right-click a complex LINQ query
   - Select "Ask Copilot" > "Explain this code"
   - Observe detailed explanation in chat pane
   - Try "Optimize this query" or "Add comments"

**Key Teaching Points:**

- Chat pane is best for **research, planning, architecture questions**
- Inline chat is best for **direct code modifications, refactoring**
- Context menu provides **quick access** to common AI actions
- Copilot maintains conversation history for follow-up questions

**Advanced Usage:**

- Use `/explain`, `/fix`, `/tests` slash commands for quick actions
- Reference files with `@file:` (coming soon to Visual Studio)
- Include solution context: Copilot sees open files and project structure

**Transition:** "Now let's explore Visual Studio's exclusive productivity features..."
:::

---

## Visual Studio Exclusive: Doc Comment Generation

Automatic XML documentation

**/// Magic:**

- Type `///` above any method, class, or property
- Copilot generates complete XML documentation
- Includes `<summary>`, `<param>`, `<returns>`, `<exception>`
- Learns from your existing documentation style

::: column

**Example:**

```csharp
/// <summary>
/// Calculates the total price with applicable discounts and tax.
/// </summary>
/// <param name="items">List of order items</param>
/// <param name="discountCode">Optional discount code</param>
/// <returns>Total price including tax and discounts</returns>
/// <exception cref="ArgumentNullException">items is null</exception>
public decimal CalculateTotal(List<OrderItem> items, string discountCode = null)
```

::: notes
**Demo: Doc Comment Generation (5 minutes)**

1. **Basic Method Documentation:**
   - Create method without comments:
     ```csharp
     public async Task<User> GetUserByIdAsync(int userId)
     {
         // implementation
     }
     ```
   - Type `///` on line above method
   - Press Enter—Copilot generates full XML doc
   - Review parameter descriptions, return type, exceptions

2. **Complex Method with Multiple Parameters:**
   - Create method with many parameters:
     ```csharp
     public Order CreateOrder(int customerId, List<OrderItem> items,
         string shippingAddress, PaymentMethod payment,
         string discountCode = null, bool expressShipping = false)
     ```
   - Type `///` above method
   - Observe comprehensive documentation for all parameters
   - Edit any descriptions that need refinement

3. **Class-Level Documentation:**
   - Type `///` above a class definition
   - Copilot generates class summary based on members and purpose
   - Demonstrate how it learns from existing style

**Key Teaching Points:**

- This feature is **exclusive to Visual Studio** (not in VS Code)
- Saves significant time on documentation requirements
- Especially valuable for public APIs and libraries
- Generated docs follow XML documentation standard
- IntelliSense immediately shows generated docs to other developers

**Best Practices:**

- Always review generated documentation for accuracy
- Edit domain-specific terminology or business logic descriptions
- Use consistent terminology—Copilot learns from existing docs
- Generate docs **before** code reviews—reviewers see context

**Productivity Impact:**

- Reduces documentation time by 70-80%
- Improves API discoverability
- Ensures consistent documentation style across team
  :::

---

## Visual Studio Exclusive: QuickInfo "Describe with Copilot"

AI-powered IntelliSense enhancements

**Hover Intelligence:**

- Hover over any method, class, or property
- Click "Describe with Copilot" link in QuickInfo tooltip
- Copilot generates contextual summary and usage guidance
- Temporary AI-generated help—not saved to code

::: column

**Use Cases:**

- Understanding unfamiliar APIs
- Learning third-party library methods
- Exploring legacy code
- Onboarding new team members

::: notes
**Demo: QuickInfo Enhancements (7 minutes)**

1. **Exploring Unfamiliar API:**
   - Open code with unfamiliar NuGet package (e.g., Polly, Dapper)
   - Hover over a method from the library
   - Click "Describe with Copilot" in tooltip
   - Observe AI-generated explanation with usage examples
   - Ask follow-up: "Show me common patterns with this method"

2. **Understanding Complex LINQ:**
   - Hover over complex LINQ query or method chain
   - Click "Describe with Copilot"
   - Review step-by-step breakdown of query logic
   - Ask: "How can I optimize this query?"

3. **Legacy Code Exploration:**
   - Navigate to poorly documented legacy method
   - Hover, click "Describe with Copilot"
   - Get instant understanding without reading full implementation
   - Ask: "What design pattern is this using?"

**Key Teaching Points:**

- **Visual Studio exclusive** feature—not available in VS Code
- Summaries are **temporary** (not saved as code comments)
- Useful for rapid exploration and learning
- Reduces time spent reading documentation
- Complements traditional IntelliSense

**Productivity Benefits:**

- **Faster onboarding**: New developers understand code faster
- **API discovery**: Learn unfamiliar libraries without leaving IDE
- **Legacy modernization**: Understand old code before refactoring
- **Knowledge sharing**: AI bridges knowledge gaps on teams

**Limitations:**

- Summaries are generated on-demand (requires API call)
- May not have latest library updates (see Microsoft Learn integration)
- Not a replacement for proper code documentation

**Transition:** "Speaking of documentation, let's see how Visual Studio integrates with Microsoft Learn..."
:::

---

## Microsoft Learn Integration

Access authoritative documentation when AI needs help

**How It Works:**

- Copilot detects when its training data is outdated
- Automatically retrieves latest docs from Microsoft Learn
- Provides authoritative, up-to-date answers
- Cites sources for verification

::: column

**Covered Topics:**

- .NET APIs and framework changes
- Azure service updates
- Visual Studio features
- C# language updates
- Latest best practices

::: notes
**Demo: Microsoft Learn Integration (6 minutes)**

1. **Recent .NET Feature:**
   - Ask Copilot Chat: "How do I use required properties in C# 11?"
   - Observe Copilot retrieving latest documentation
   - See inline citation links to Microsoft Learn
   - Click citation to verify in browser

2. **Azure Service Update:**
   - Ask: "What's new in Azure Functions v4?"
   - Copilot pulls latest release notes and features
   - Provides code examples from official documentation
   - Citations link directly to relevant Learn articles

3. **Framework Migration:**
   - Ask: "How do I migrate from .NET 6 to .NET 8?"
   - Copilot retrieves migration guide from Learn
   - Provides step-by-step breaking changes
   - Links to detailed migration documentation

**Key Teaching Points:**

- **Visual Studio exclusive**—not in VS Code (yet)
- Solves the "outdated LLM training data" problem
- Ensures recommendations follow Microsoft best practices
- Particularly valuable for:
  - New framework releases
  - Azure service updates
  - Breaking changes and migrations
  - Latest C# language features

**When It Activates:**

- Copilot detects knowledge gap (post-training cutoff date)
- User asks about recent features or updates
- Question involves Microsoft technologies with recent changes
- Automatically falls back to Learn when needed

**Productivity Benefits:**

- No need to leave IDE to verify information
- Confidence in accuracy of recommendations
- Direct links to deep-dive documentation
- Reduced risk of using deprecated patterns

**Enterprise Value:**

- Ensures team follows official guidance
- Reduces security risks from outdated practices
- Accelerates adoption of new features
- Supports compliance and audit requirements
  :::

---

## Deep .NET Productivity: "Implement with Copilot"

AI-powered refactoring integration

**Workflow:**

1. Generate interface or abstract class
2. Right-click > Quick Actions (Ctrl+.)
3. Select "Implement Interface" or "Implement Abstract Class"
4. Copilot generates complete, context-aware implementation

::: column

**Advanced Features:**

- **Contextual implementations** based on interface semantics
- **Pattern recognition** (repository, service, factory patterns)
- **Error handling** and logging included
- **Async/await** patterns when appropriate

::: notes
**Demo: Implement with Copilot (8 minutes)**

1. **Basic Interface Implementation:**
   - Define interface:
     ```csharp
     public interface IOrderRepository
     {
         Task<Order> GetByIdAsync(int orderId);
         Task<IEnumerable<Order>> GetAllAsync();
         Task<Order> CreateAsync(Order order);
         Task UpdateAsync(Order order);
         Task DeleteAsync(int orderId);
     }
     ```
   - Create class implementing interface:
     ```csharp
     public class OrderRepository : IOrderRepository
     {
     }
     ```
   - Ctrl+. on `IOrderRepository` > "Implement Interface with Copilot"
   - Observe Copilot generates full CRUD implementation with Entity Framework

2. **Service Layer Implementation:**
   - Define service interface:
     ```csharp
     public interface IPaymentService
     {
         Task<PaymentResult> ProcessPaymentAsync(PaymentRequest request);
         Task<RefundResult> RefundPaymentAsync(string transactionId);
         Task<bool> ValidatePaymentMethodAsync(PaymentMethod method);
     }
     ```
   - Implement with Copilot
   - Show generated error handling, validation, and logging

3. **Pattern-Aware Implementation:**
   - Create factory interface:
     ```csharp
     public interface INotificationFactory
     {
         INotification CreateNotification(NotificationType type);
     }
     ```
   - Implement with Copilot
   - Observe factory pattern with switch/case for notification types

**Key Teaching Points:**

- **Visual Studio exclusive** deep integration with refactoring system
- VS Code has basic interface implementation, but not AI-powered
- Copilot understands common patterns (repository, service, factory)
- Generated code includes:
  - Appropriate async/await patterns
  - Basic error handling
  - Null checks and validation
  - Logging placeholders (if detected in project)

**Best Practices:**

- Review generated implementations for business logic accuracy
- Add domain-specific validation
- Customize error handling to match project standards
- Rename generic variable names to meaningful domain terms

**Productivity Impact:**

- Reduces boilerplate implementation time by 80%
- Ensures consistent patterns across codebase
- Faster prototyping and scaffolding
- Less context switching to search for patterns

**Next:** "Let's see how Copilot supercharges debugging..."
:::

---

## Debugging Integration: AI-Aware Debugger

Copilot understands your debugging context

**Debugging Features:**

- **Exception analysis** with AI-powered suggestions
- **Variable inspection** with explanations
- **Call stack analysis** and troubleshooting
- **Conditional breakpoint** expression suggestions
- **LINQ query evaluation** and optimization

::: column

**Access Points:**

- Ask Copilot button in exception helpers
- Right-click variables in Autos/Locals windows
- Hover over variables with data tips
- Breakpoint context menus

::: notes
**Demo: AI-Powered Debugging (10 minutes)**

1. **Exception Analysis:**
   - Trigger NullReferenceException in code
   - Start debugging, observe exception helper
   - Click "Ask Copilot" in exception dialog
   - Copilot analyzes call stack and suggests fixes
   - Show suggested code changes inline

   **Example Exception:**

   ```csharp
   var user = await _userRepository.GetByIdAsync(userId);
   var fullName = user.FirstName + " " + user.LastName; // NullReferenceException
   ```

   Copilot suggests: "Add null check before accessing properties"

2. **Variable Inspection:**
   - Set breakpoint in complex method
   - Hover over variable in Autos/Locals window
   - Right-click > Ask Copilot > "Explain this value"
   - Copilot explains current state and potential issues

3. **LINQ Query Debugging:**
   - Set breakpoint on LINQ query:
     ```csharp
     var orders = customers
         .SelectMany(c => c.Orders)
         .Where(o => o.Total > 1000)
         .OrderByDescending(o => o.OrderDate)
         .Take(10);
     ```
   - Hover over query in debugger
   - Copilot shows evaluated results and explains query logic
   - Ask: "Is this query efficient?"
   - Get optimization suggestions

4. **Conditional Breakpoint Suggestions:**
   - Right-click breakpoint > Conditions
   - Type partial condition: "when order"
   - Copilot suggests: `order.Total > 1000 && order.Status == OrderStatus.Pending`
   - Accept and test breakpoint

**Key Teaching Points:**

- **Visual Studio exclusive** debugger-aware AI
- Copilot sees full debugging context:
  - Current call stack
  - Local variable values
  - Exception details
  - Breakpoint locations
- Dramatically faster root cause analysis
- Suggestions are **context-specific** to current execution state

**Debugging Workflow:**

1. Hit exception or unexpected behavior
2. Use "Ask Copilot" in exception helper
3. Review suggested fixes
4. Apply fix or ask follow-up questions
5. Continue debugging with AI assistance

**Advanced Scenarios:**

- Multi-threaded debugging: "Why is this variable changed unexpectedly?"
- Memory leaks: "What objects are keeping this in memory?"
- Performance issues: "Why is this method slow?"

**Productivity Impact:**

- 50-60% faster debugging sessions
- Reduced time searching Stack Overflow
- Faster onboarding to unfamiliar codebases
- Fewer wild-goose-chase debugging sessions
  :::

---

## Profiler Agent: Performance Optimization

AI-guided performance analysis and optimization

**Profiler Integration:**

- Launch profiler, collect performance data
- Copilot analyzes profiling results
- Identifies bottlenecks and hot paths
- Suggests optimization strategies
- Generates benchmark code (BenchmarkDotNet)

::: column

**Optimization Workflow:**

1. Profile application (CPU, memory, allocations)
2. Ask Copilot to analyze profiler results
3. Review suggested optimizations
4. Generate benchmarks to validate improvements
5. Apply changes and re-profile

::: notes
**Demo: Profiler Agent (12 minutes)**

1. **Profiling Setup:**
   - Open project with performance issues
   - Debug > Performance Profiler (Alt+F2)
   - Select tools: CPU Usage, Memory Usage, .NET Object Allocation
   - Start profiling session
   - Exercise slow code paths
   - Stop profiling

2. **AI Analysis:**
   - Review profiler results (hot paths, allocations)
   - Click "Ask Copilot" in profiler window
   - Ask: "What are the main bottlenecks?"
   - Copilot identifies:
     - Method with excessive allocations (e.g., string concatenation in loop)
     - Synchronous I/O blocking threads
     - Expensive LINQ queries running repeatedly

3. **Optimization Suggestions:**
   - Ask: "How can I optimize this string concatenation?"
   - Copilot suggests: Use `StringBuilder` or `string.Join`
   - Shows before/after code comparison
   - Explains performance impact

4. **Benchmark Generation:**
   - Ask: "Generate BenchmarkDotNet code to compare these approaches"
   - Copilot generates:

     ```csharp
     [MemoryDiagnoser]
     public class StringConcatBenchmark
     {
         private readonly List<string> _items = Enumerable.Range(1, 1000)
             .Select(i => $"Item {i}").ToList();

         [Benchmark]
         public string StringConcat()
         {
             string result = "";
             foreach (var item in _items)
                 result += item + ", ";
             return result;
         }

         [Benchmark]
         public string StringBuilder()
         {
             var sb = new StringBuilder();
             foreach (var item in _items)
                 sb.Append(item).Append(", ");
             return sb.ToString();
         }
     }
     ```

   - Run benchmark, review results
   - Apply optimal solution

**Key Teaching Points:**

- **Visual Studio exclusive** profiler integration
- Copilot understands profiling data:
  - CPU hot paths
  - Memory allocations
  - Garbage collection pressure
  - Lock contention
- Provides **actionable optimization strategies**, not just "make it faster"
- Benchmark generation ensures changes actually improve performance

**Common Optimizations Suggested:**

- Replace synchronous I/O with async
- Use `StringBuilder` for string concatenation in loops
- Cache expensive computations
- Use `Span<T>` and `Memory<T>` to reduce allocations
- Optimize LINQ queries (use `AsParallel`, avoid multiple enumerations)
- Pool objects to reduce GC pressure

**Advanced Scenarios:**

- Ask: "Should I use parallel processing here?"
- Ask: "How can I reduce memory allocations in this method?"
- Ask: "What's causing garbage collection pauses?"

**Workflow Integration:**

- Iterative optimization: profile → analyze → optimize → validate → repeat
- CI/CD integration: profile performance tests, track regressions
- Enterprise scenarios: optimize high-throughput services, reduce cloud costs

**Productivity Impact:**

- Faster identification of bottlenecks (from hours to minutes)
- Evidence-based optimization (benchmarks validate changes)
- Reduced guesswork and premature optimization
- Knowledge transfer: Learn best practices through AI suggestions
  :::

---

## Agent Mode: Autonomous Coding Workflows

Let Copilot work on your behalf

**What is Agent Mode?**

- Autonomous, goal-driven coding workflows
- Copilot plans, edits, tests, and iterates
- Manual approval and steering available
- Cross-file changes and refactoring

::: column

**Example Tasks:**

- "Implement user authentication with JWT"
- "Add logging to all service classes"
- "Refactor to use repository pattern"
- "Fix all compiler warnings"
- "Generate unit tests for OrderService"

::: notes
**Demo: Agent Mode (10 minutes)**

1. **Simple Autonomous Task:**
   - Open Copilot Chat
   - Enable Agent Mode (toggle at top of chat pane)
   - Prompt: "Add input validation to all public methods in OrderService"
   - Observe Copilot:
     - Analyzes OrderService class
     - Plans validation additions
     - Generates validation code for each method
     - Previews changes (diff view)
   - Review changes, approve or request modifications
   - Copilot applies changes across file

2. **Multi-File Refactoring:**
   - Prompt: "Refactor direct database access in controllers to use repository pattern"
   - Copilot plans:
     - Create `IOrderRepository` interface
     - Implement `OrderRepository` class
     - Update `OrderController` to use repository
     - Register repository in dependency injection
   - Shows file tree with planned changes
   - Apply changes incrementally or all at once

3. **Test Generation:**
   - Prompt: "Generate comprehensive unit tests for PaymentService"
   - Copilot:
     - Creates test class with xUnit/NUnit/MSTest
     - Generates tests for each public method
     - Includes edge cases, error handling, async tests
     - Uses mocking framework (Moq, NSubstitute)
   - Review tests, run, iterate on failures

4. **Manual Steering:**
   - During any agent task, intervene with follow-up prompts:
     - "Use FluentValidation instead"
     - "Add XML documentation to all generated methods"
     - "Apply these changes only to OrderService, not CustomerService"
   - Copilot adjusts plan and continues

**Key Teaching Points:**

- Agent mode is **generally available** in both VS and VS Code
- Best for **repetitive, well-defined tasks**
- Requires review: Agent mode is not 100% accurate
- More powerful than simple chat: can edit multiple files, run tests
- Manual approval gates prevent unintended changes

**Best Use Cases:**

- Adding cross-cutting concerns (logging, validation, error handling)
- Scaffolding new features (controllers, services, repositories)
- Refactoring patterns across codebase
- Generating tests and documentation
- Fixing compiler warnings or code analysis issues

**Limitations and Considerations:**

- Requires clear, specific prompts for best results
- May need iteration and correction
- Always review changes before committing
- Not suitable for complex business logic without human oversight
- Enterprise policies control agent mode availability

**Agent Mode vs. Regular Chat:**

- Regular chat: Q&A, explanations, suggestions (read-only)
- Agent mode: Autonomous code changes (write mode)

**Security and Controls:**

- Tool approval required for file changes
- Organization policies can disable agent mode
- Audit logs track agent actions
- Rollback via source control if needed

**Transition:** "Now let's explore how agent mode integrates with external tools via MCP..."
:::

---

## Model Context Protocol (MCP) Integration

Extend Copilot with external tools and services

**What is MCP?**

- Open standard for AI tool integration
- Connect Copilot to databases, APIs, file systems, cloud services
- Define custom tools for domain-specific workflows
- Invoke tools automatically during agent mode

::: column

**MCP in Visual Studio:**

- Add servers via `.mcp.json` configuration
- Tools appear in Copilot tool palette
- Authenticate via CodeLens or chat
- Manual approval for tool invocations

::: notes
**Demo: MCP Server Integration (8 minutes)**

1. **Configure MCP Server:**
   - Create `.mcp.json` in solution root or user profile:
     ```json
     {
       "mcpServers": {
         "azure-resources": {
           "command": "python",
           "args": ["-m", "mcp_azure"],
           "env": {
             "AZURE_SUBSCRIPTION_ID": "${env:AZURE_SUBSCRIPTION_ID}"
           }
         },
         "database-tools": {
           "command": "npx",
           "args": ["-y", "@modelcontextprotocol/server-postgres"],
           "env": {
             "POSTGRES_CONNECTION": "${env:DB_CONNECTION}"
           }
         }
       }
     }
     ```
   - Save and restart Visual Studio
   - Copilot detects and loads MCP servers

2. **Authenticate MCP Server:**
   - Open file with MCP configuration
   - Click CodeLens "Authenticate" above server definition
   - Complete OAuth flow or enter credentials
   - Server status shows "Connected" in chat pane

3. **Using MCP Tools:**
   - Open Copilot Chat in agent mode
   - Prompt: "List all Azure App Services in my subscription"
   - Copilot invokes `azure-resources` MCP server
   - Displays results in chat
   - Follow-up: "Show me the app settings for the production app"

4. **Database Query Tool:**
   - Prompt: "Show me the schema for the Orders table"
   - Copilot uses `database-tools` MCP server
   - Executes safe schema query, displays result
   - Ask: "Generate a repository class for this table"
   - Copilot uses schema information to generate code

**Key Teaching Points:**

- MCP support is **available in both VS and VS Code**
- Visual Studio manages MCP via `.mcp.json` configuration
- Tools require **explicit approval** before invocation (security gate)
- MCP enables domain-specific workflows:
  - DevOps automation
  - Database schema exploration
  - Cloud resource management
  - Custom business logic integration

**MCP Capabilities:**

- **Tools**: Functions Copilot can invoke (e.g., query database, call API)
- **Prompts**: Reusable prompt templates
- **Resources**: External data sources (files, APIs, databases)
- **Sampling**: LLM-driven tool selection and invocation

**Security Controls:**

- Tools disabled by default—manual enablement required
- Authentication managed per-server
- Audit logs track tool invocations
- Organization policies control which MCP servers are allowed

**Example MCP Servers:**

- `@modelcontextprotocol/server-postgres`: PostgreSQL database tools
- `@modelcontextprotocol/server-filesystem`: File system operations
- `@modelcontextprotocol/server-github`: GitHub API access
- Custom servers for internal APIs, cloud platforms, business systems

**Custom MCP Server Development:**

- Implement MCP specification (JSON-RPC 2.0)
- Expose tools, prompts, resources
- Deploy as standalone service or CLI
- Distribute to team via configuration

**Enterprise Use Cases:**

- Integrate with internal ticketing systems (JIRA, ServiceNow)
- Connect to proprietary databases and schemas
- Expose company-specific APIs and services
- Automate deployment and infrastructure tasks

**Transition:** "Let's compare Visual Studio and VS Code Copilot features..."
:::

---

<!-- layout: Comparison -->

## Visual Studio vs. VS Code: Feature Comparison

Choosing the right IDE for your workflow

**Visual Studio Strengths:**

- Deep .NET/C# productivity (doc comments, QuickInfo, Learn integration)
- Advanced debugger integration with AI awareness
- Profiler agent for performance optimization
- Enterprise project and solution management
- Unified experience for .NET developers

::: column

**VS Code Strengths:**

- Custom agents and chat modes (personas, handoffs)
- Custom prompt files for reusable workflows
- Extensible tool sets and third-party agents
- Cross-platform and lightweight
- Broader language ecosystem (250+ languages)

::: notes
**Discussion: Choosing the Right IDE (5 minutes)**

**Visual Studio is Best For:**

- **Enterprise .NET development**:
  - Large solutions with 100+ projects
  - Windows desktop (WPF, WinForms, UWP, MAUI)
  - ASP.NET, Blazor, and .NET web services
- **Deep debugging and profiling**:
  - Complex multi-threaded applications
  - Memory leak investigation
  - Performance optimization
- **Team standardization**:
  - Shared refactoring tools
  - Built-in code analysis and StyleCop
  - Enterprise security and compliance

**VS Code is Best For:**

- **Cross-platform development**:
  - Linux, macOS, Windows
  - Docker and Kubernetes workflows
  - Cloud-native microservices
- **Polyglot projects**:
  - Multiple languages in one project
  - JavaScript/TypeScript frontend + Python/Go backend
  - Experimental languages and frameworks
- **Custom AI workflows**:
  - Build custom agents for planning, review, security analysis
  - Create reusable prompt files for team workflows
  - Integrate third-party AI models (Claude, Gemini, etc.)
- **Lightweight and fast**:
  - Quick startup, low resource usage
  - Remote development (SSH, WSL, Codespaces)
  - Minimal installations on constrained environments

**Feature Parity Summary:**
| Feature | VS Code | Visual Studio |
|---------|---------|---------------|
| Inline completions | ✓ | ✓ |
| Copilot Chat | ✓ | ✓ |
| Agent mode | ✓ | ✓ |
| MCP support | ✓ | ✓ |
| Next Edit Suggestions | ✓ | ✓ |
| Custom agents | ✓ | ✗ |
| Doc comment generation | ✗ | ✓ |
| QuickInfo AI | ✗ | ✓ |
| Microsoft Learn integration | ✗ | ✓ |
| Profiler agent | ✗ | ✓ |
| Deep debugger AI | ✗ | ✓ |

**Real-World Scenarios:**

1. **Startup Building SaaS (Multi-Language):**
   - **Choose VS Code**: React frontend, Node.js backend, Python ML services
   - Custom agents for code review and deployment
   - Cloud-native development with Docker

2. **Enterprise .NET Team (Financial Services):**
   - **Choose Visual Studio**: Large WPF application, ASP.NET Core APIs
   - Profiler agent for performance requirements
   - Deep debugging for complex business logic
   - Microsoft Learn for compliance with latest .NET standards

3. **Full-Stack Developer (Personal Projects):**
   - **Choose VS Code**: Quick startup, lightweight, cross-platform
   - Custom prompt files for rapid prototyping
   - Integration with multiple AI providers (OpenAI, Claude, local models)

4. **Consultant (Multiple Clients, Various Stacks):**
   - **Use Both**:
     - VS Code for initial exploration, scripts, lightweight projects
     - Visual Studio for deep .NET work, debugging, optimization
     - Share Copilot subscription across both IDEs

**Key Takeaway:**
"Visual Studio offers **deep, enterprise-grade integration** for .NET developers. VS Code offers **flexibility, extensibility, and cross-platform reach**. Both are excellent—choose based on your tech stack, team size, and workflow needs."

**Audience Question:** "Can I use both IDEs with one Copilot subscription?"
**Answer:** "Yes! Your GitHub Copilot subscription works across all supported IDEs (VS, VS Code, JetBrains, Neovim, etc.)."
:::

---

## Best Practices for Visual Studio Copilot

Maximizing productivity and code quality

**Prompt Engineering:**

- Write descriptive method names and comments
- Reference specific requirements and constraints
- Use domain-specific terminology
- Include context via comments above code

**Code Review:**

- Always review generated code for correctness
- Check security implications (input validation, auth, sensitive data)

::: column

- Verify performance characteristics
- Test edge cases and error paths

**Team Integration:**

- Share Copilot best practices across team
- Document domain-specific prompt patterns
- Review AI-generated code in pull requests
- Establish guidelines for agent mode usage

::: notes
**Best Practices Discussion (5 minutes)**

**1. Prompt Engineering for Better Results:**

✅ **Good Prompts:**

- "Add error handling to SaveOrderAsync method. Handle DbUpdateException, SqlException, and network timeouts. Log errors with ILogger. Return Result<T> with error details."
- "Generate repository pattern for User entity. Include async CRUD operations, paging support (PagedResult<T>), and filtering by email/username/status."

❌ **Bad Prompts:**

- "Add error handling" (too vague)
- "Make this better" (no actionable guidance)
- "Fix" (doesn't specify what's wrong)

**Improved Context:**

- Add comments above code: `// This method processes refunds for failed payments`
- Use descriptive variable names: `customerOrderTotal` instead of `total`
- Reference patterns: `// Use factory pattern to create notification types`

**2. Security and Code Review:**

Always review for:

- **Input validation**: SQL injection, XSS, command injection
- **Authentication/Authorization**: Ensure proper access controls
- **Sensitive data**: Don't log passwords, tokens, PII
- **Error handling**: Don't leak stack traces to users
- **Dependencies**: Verify NuGet packages are from trusted sources

**Example: Security Review**

```csharp
// ❌ AI-generated code (needs review):
public User GetUserById(string id)
{
    var query = $"SELECT * FROM Users WHERE Id = '{id}'"; // SQL INJECTION!
    return _db.ExecuteQuery<User>(query);
}

// ✅ After review and correction:
public async Task<User> GetUserByIdAsync(int id)
{
    return await _context.Users
        .AsNoTracking()
        .FirstOrDefaultAsync(u => u.Id == id);
}
```

**3. Performance Considerations:**

Review generated code for:

- Synchronous I/O (use async/await)
- N+1 queries (eager loading with Include())
- Excessive allocations (use `Span<T>`, `ArrayPool<T>`)
- Missing caching opportunities

**4. Team Guidelines:**

Establish team standards:

- **Pull Request Reviews**: Require human review of all AI-generated code
- **Testing Requirements**: Generate tests for AI-generated methods
- **Documentation**: Ensure generated code includes doc comments
- **Prompt Libraries**: Share effective prompts for common tasks
- **Agent Mode Policies**: Define when agent mode is appropriate

**5. Continuous Learning:**

- Experiment with different prompt styles
- Learn from Copilot's suggestions (teaches patterns and idioms)
- Share discoveries with team
- Stay updated on new features (Copilot evolves rapidly)

**6. Balancing AI and Human Expertise:**

**Use Copilot for:**

- Boilerplate and scaffolding
- Common patterns and idioms
- Documentation and tests
- Refactoring and code modernization

**Use Human Judgment for:**

- Business logic and domain rules
- Architecture and design decisions
- Security-critical code paths
- Complex algorithms and optimizations

**Key Principle:** "Copilot is a **powerful assistant, not a replacement** for developer expertise. Think of it as a junior developer who generates first drafts—you're the senior developer who reviews, corrects, and approves."

**Transition:** "Let's wrap up with hands-on labs and Q&A..."
:::

---

## Hands-On Labs

Practice exercises for Visual Studio Copilot

**Lab 1: Core Features (20 minutes)**

- Install and configure Copilot
- Generate doc comments with `///`
- Use QuickInfo "Describe with Copilot"
- Create method implementation from interface

**Lab 2: Debugging and Profiling (25 minutes)**

- Debug exception with AI assistance
- Analyze LINQ query during debugging
- Profile application and ask Copilot for optimization
- Generate and run BenchmarkDotNet code

**Lab 3: Agent Mode and MCP (25 minutes)**

- Use agent mode to add validation across service layer
- Configure local MCP server
- Use MCP tools to explore database schema
- Generate repository from schema using agent mode

::: notes
**Lab Setup and Instructions (5 minutes intro)**

**Prerequisites:**

- Visual Studio 2026 (Community, Professional, or Enterprise)
- GitHub Copilot subscription (free tier acceptable)
- Sample application codebase (provided in course materials)
- Internet connection for Copilot API

**Lab Environment:**

- Sample e-commerce application (C# / .NET 8)
- Entity Framework Core with SQL Server LocalDB
- ASP.NET Core Web API
- xUnit test project

**Lab 1: Core Features (20 minutes)**

**Objective**: Get comfortable with Visual Studio's exclusive Copilot features

**Tasks:**

1. **Doc Comment Generation:**
   - Open `OrderService.cs`
   - Type `///` above `CreateOrderAsync` method
   - Review generated documentation
   - Edit parameter descriptions for domain accuracy
   - Repeat for 3 more methods

2. **QuickInfo Enhancement:**
   - Open `PaymentController.cs`
   - Hover over `_paymentService.ProcessPaymentAsync()`
   - Click "Describe with Copilot"
   - Read AI-generated explanation
   - Ask follow-up: "What happens if this method fails?"

3. **Implement with Copilot:**
   - Open `IOrderRepository.cs`
   - Create new class `OrderRepository : IOrderRepository`
   - Ctrl+. (Quick Action) > "Implement Interface with Copilot"
   - Review generated Entity Framework implementation
   - Add to `Program.cs` DI container

**Expected Results:**

- Complete method documentation
- Understanding of unfamiliar methods via QuickInfo
- Fully implemented repository with CRUD operations

**Common Issues:**

- Copilot not generating docs: Ensure enabled in Tools > Options
- Generic implementations: Add more context via comments
- Missing NuGet packages: Install Entity Framework Core

Lab transition: Lab 1 complete, move into debugging and profiling.

**Lab 2: Debugging and Profiling (25 minutes)**

**Objective**: Use AI-powered debugging and performance analysis

**Tasks:**

1. **AI-Assisted Exception Debugging:**
   - Open `OrderService.cs` > `CalculateDiscountAsync`
   - Introduce a bug (comment out null check)
   - Run application, trigger discount calculation
   - Observe NullReferenceException
   - Click "Ask Copilot" in exception helper
   - Review suggested fix
   - Apply fix and verify

2. **LINQ Query Debugging:**
   - Set breakpoint on complex LINQ query in `ReportService.cs`
   - Start debugging with Ctrl+F5, trigger report generation
   - Hover over LINQ query variable
   - Right-click > Ask Copilot > "Explain this query"
   - Ask: "Is this query efficient?"
   - Review optimization suggestions

3. **Performance Profiling:**
   - Debug > Performance Profiler (Alt+F2)
   - Select CPU Usage, .NET Object Allocation
   - Start profiling
   - Exercise slow report generation feature
   - Stop profiling, review hot paths
   - Click "Ask Copilot" in profiler results
   - Ask: "What's causing the slowdown in GenerateSalesReportAsync?"
   - Review suggestions (likely: N+1 query, missing indexes)

4. **Benchmark Generation:**
   - Ask Copilot: "Generate BenchmarkDotNet code to compare LINQ query approaches"
   - Review generated benchmark class
   - Add NuGet package: `BenchmarkDotNet`
   - Run benchmark: `dotnet run -c Release`
   - Review results, apply fastest approach

**Expected Results:**

- Faster exception root-cause identification
- Understanding of complex queries
- Identified performance bottlenecks
- Evidence-based optimization via benchmarks

Lab transition: Lab 2 complete, move into agent mode and MCP.

**Lab 3: Agent Mode and MCP (25 minutes)**

**Objective**: Use autonomous agents and external tool integration

**Tasks:**

1. **Add Validation with Agent Mode:**
   - Open Copilot Chat
   - Enable Agent Mode (toggle at top)
   - Prompt: "Add FluentValidation to all DTOs in the Models folder. Validate required fields, string lengths, and email formats."
   - Review Copilot's plan:
     - Install FluentValidation package
     - Create validator classes for each DTO
     - Register validators in DI container
   - Approve changes
   - Run tests to verify validation works

2. **Configure Local MCP Server:**
   - Create `.mcp.json` in solution root:
     ```json
     {
       "mcpServers": {
         "database": {
           "command": "npx",
           "args": ["-y", "@modelcontextprotocol/server-postgres"],
           "env": {
             "POSTGRES_CONNECTION": "Server=localhost;Database=EcommerceDb;..."
           }
         }
       }
     }
     ```
   - Restart Visual Studio
   - Authenticate MCP server via CodeLens

3. **Explore Schema with MCP:**
   - In Copilot Chat (agent mode):
   - "Show me the schema for the Products table"
   - Review column definitions
   - "What indexes exist on this table?"
   - "Generate a repository class for this table with full CRUD operations"
   - Review generated code, add to project

4. **Agent Mode Refactoring:**
   - Prompt: "Refactor ProductService to use the new ProductRepository. Update dependency injection and all method calls."
   - Review planned changes across files
   - Approve and apply
   - Run tests, fix any compilation errors

**Expected Results:**

- Validation rules automatically added to all DTOs
- Database schema explored without leaving IDE
- Generated repository code based on actual schema
- Refactored service layer using new repositories

**Troubleshooting:**

- Agent mode not available: Check GitHub Copilot plan (requires Pro or higher)
- MCP server won't connect: Verify connection string, check firewall
- Generated code has errors: Iterate with follow-up prompts ("Fix compilation errors")

Lab transition: Lab 3 complete, proceed to wrap-up and Q&A.

**Wrap-Up and Q&A (10 minutes)**

**Key Takeaways:**

1. Visual Studio offers **unique, deep integrations** for .NET developers
2. Doc comments, QuickInfo, Learn integration, and profiler agent are **exclusive to VS**
3. Agent mode and MCP work in **both VS and VS Code**
4. Always **review AI-generated code** for security and correctness
5. Copilot is a **powerful productivity multiplier**, not a replacement for expertise

**Discussion Questions:**

- "Which feature do you think will save you the most time?"
- "What concerns do you have about using AI in your workflow?"
- "How will you introduce Copilot to your team?"

**Resources:**

- Visual Studio Copilot Docs: https://learn.microsoft.com/visualstudio/ide/visual-studio-github-copilot
- GitHub Copilot in VS: https://docs.github.com/copilot/using-github-copilot/using-github-copilot-in-visual-studio
- MCP Specification: https://spec.modelcontextprotocol.io/
- Course materials: [Provide repository link]

**Next Steps:**

- Practice with real projects (start small, gradually increase Copilot usage)
- Share findings with team (demonstrate productivity gains)
- Establish team guidelines (code review, security, testing)
- Explore advanced features (custom MCP servers, agent mode workflows)
- Stay updated (Copilot evolves monthly—new features coming)
  :::

---

## Resources and Next Steps

Continue your GitHub Copilot journey

**Official Documentation:**

- [Visual Studio Copilot Reference](https://learn.microsoft.com/visualstudio/ide/visual-studio-github-copilot)
- [GitHub Copilot Documentation](https://docs.github.com/copilot)
- [Model Context Protocol Specification](https://spec.modelcontextprotocol.io/)
- [.NET Performance Best Practices](https://learn.microsoft.com/dotnet/core/performance/)

**Community and Support:**

- Visual Studio Developer Community
- GitHub Copilot Feedback Forum
- Stack Overflow (#github-copilot)
- Microsoft Learn Training Modules

**What's Next:**

- Explore advanced agent mode scenarios
- Build custom MCP servers for your domain
- Share best practices with your team
- Measure productivity gains

::: notes
**Closing Remarks (3 minutes)**

**Summary:**
Today we explored GitHub Copilot in Visual Studio 2026—a powerful, deeply integrated AI assistant for .NET developers. We covered:

✅ **Installation and setup** across subscription tiers
✅ **Core features**: inline completions, chat, agent mode
✅ **Visual Studio exclusives**: doc comments, QuickInfo AI, Learn integration
✅ **Deep .NET productivity**: implement with Copilot, debugger integration
✅ **Performance optimization**: profiler agent, benchmark generation
✅ **Extensibility**: MCP tool integration

**Key Differentiators:**
Visual Studio Copilot is **not just VS Code in a bigger IDE**. It offers:

- Tighter integration with .NET tools and debugger
- Enterprise-grade features for large-scale projects
- Performance optimization assistance
- Authoritative documentation via Microsoft Learn

**Productivity Impact:**
Teams report:

- 40-55% faster feature development
- 60-70% reduction in documentation time
- 50% faster debugging sessions
- Significant reduction in routine coding tasks

**Getting Started:**

1. **Start small**: Enable Copilot, use inline completions for a week
2. **Graduate to chat**: Use Copilot Chat for questions and explanations
3. **Adopt agent mode**: Let Copilot handle refactoring and test generation
4. **Customize**: Add MCP servers and custom tools for your domain
5. **Measure**: Track time saved on specific tasks to justify investment

**Common Concerns Addressed:**

**"Will AI replace developers?"**
No. Copilot is a tool that amplifies developer productivity, much like IDEs, version control, and unit testing frameworks did before it. It handles routine tasks, freeing developers for higher-level problem-solving, architecture, and business logic.

**"What about code quality?"**
AI-generated code requires review, just like junior developer code. Treat Copilot suggestions as first drafts. Your expertise ensures correctness, security, and performance.

**"Is my code secure?"**
GitHub Copilot does not store your code. Code snippets are sent to Copilot API for inference, but not retained. Enterprise customers have additional controls (BYOK, policy management, audit logs). See GitHub's privacy documentation for details.

**"What about licensing and costs?"**

- Free tier: Sufficient for learning and personal projects
- Pro/Pro+: ~$10-19/month, worth the productivity gain for professionals
- Business/Enterprise: Organization-wide licensing with centralized management
- ROI: Most teams recoup costs in saved developer hours within first month

**Final Thought:**
"GitHub Copilot in Visual Studio 2026 transforms how .NET developers work—reducing tedium, accelerating learning, and enabling faster delivery. The question isn't whether to adopt AI assistance, but how quickly you can integrate it into your workflow."

**Thank you for attending! Questions?**
:::
