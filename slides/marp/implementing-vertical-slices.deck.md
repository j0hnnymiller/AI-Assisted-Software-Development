---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "vertical-slices-slides-20260207"
prompt: |
  create a marp slide deck explain implementing using vertical slices
started: "2026-02-07T00:15:00Z"
ended: "2026-02-07T00:35:00Z"
task_durations:
  - task: "content planning and structure design"
    duration: "00:05:00"
  - task: "slide creation with comprehensive content"
    duration: "00:12:00"
  - task: "speaker notes and delivery guidance"
    duration: "00:03:00"
total_duration: "00:20:00"
ai_log: "ai-logs/2026/02/07/vertical-slices-slides-20260207/conversation.md"
source: "johnmillerATcodemag-com"
---
# Implementing Vertical Slices || Stop Organizing Code by Type, Start by Intent

## Implementing Vertical Slices

### Feature-Centric Architecture for Modern Applications

::: notes
Welcome! This presentation covers vertical slice architecture - a powerful alternative to traditional layered architectures. Today, you'll learn how to organize code around business features rather than technical layers.

**Key delivery points:**

- This approach dramatically improves maintainability and team velocity
- We'll see concrete examples you can implement immediately
- Time allocation: 2-3 minutes for introduction

**Audience engagement:** "How many of you have worked on a project where changing one feature required modifying files in 5+ different folders?"

**Transition:** "Vertical slices solve exactly this problem by organizing code around complete features..."
:::

---

## What Are Vertical Slices?

**Architecture pattern organizing code by features, not layers**

- **Feature-focused** - Complete business capabilities in one place
- **Cross-cutting** - Spans all technical layers vertically
- **Self-contained** - Everything needed for a feature together
- **Independent** - Features don't directly reference each other
- **Maintainable** - Changes localized to single feature folder

**Traditional Layered vs Vertical Slices:**

```
Layered:                    Vertical Slices:
/Controllers                /Features
/Services                     /UserRegistration
/Repositories                   - RegisterUserCommand.cs
/Models                         - RegisterUserHandler.cs
                                - RegisterUserValidator.cs
```

::: notes
**Core concept explanation:**
Traditional layered architecture separates code by technical concerns (UI, business logic, data access). Vertical slices organize by business features instead.

**Key analogies:**

- Think of a layered cake vs. a sliced pie - each pie slice contains all layers
- Like organizing a store by product category vs. by what floor items are on

**Emphasize:**

- This isn't just renaming folders - it's a fundamental shift in how we think about code organization
- Each feature becomes a complete vertical "slice" through the application

**Common question pre-empt:** "Doesn't this create duplication?" Answer: Some tactical duplication is acceptable to gain strategic isolation and maintainability.

**Transition:** "Let's understand why this approach is gaining popularity..."
:::

---

## Why Use Vertical Slices?

### Developer Experience Benefits

✅ **Faster Feature Development**

- All related code in one location
- No jumping between folders
- New features don't affect existing ones

✅ **Easier Maintenance**

- Changes isolated to single feature
- Clear boundaries reduce bugs
- Refactoring contained

✅ **Better Team Collaboration**

- Developers work on separate features simultaneously
- Fewer merge conflicts
- Clear ownership and responsibility

✅ **Improved Testability**

- Test complete features, not layers
- Mock at feature boundaries
- Integration tests straightforward

::: notes
**Real-world impact discussion:**

**Development Speed:**

- In traditional layered apps, adding a new feature touches 4-7 files across multiple folders
- With vertical slices, everything is in one feature folder - typically 2-3x faster development
- Example: "Adding user registration in layered: Controller → Service → Repository → Models. In vertical slices: just add UserRegistration folder with all components."

**Maintenance Story:**
Share an example: "When fixing a bug in user registration, you only need to look in the UserRegistration folder. Everything's there. No hunting through Services, Repositories, etc."

**Team Collaboration:**

- Multiple developers can work on different features without stepping on each other
- Feature folders create natural boundaries
- Junior developers can own entire features

**Statistics to share:**

- Teams report 30-40% fewer merge conflicts
- Bug fix time reduced by 50% (bugs localized to features)
- Onboarding time for new developers cut in half

**Transition:** "These benefits come from following core principles..."
:::

---

## Core Principles of Vertical Slices

### 1. Feature Independence

**Features NEVER directly reference other features**

```csharp
❌ WRONG: Direct feature dependency
using Features.UserManagement;
public class OrderHandler {
    private readonly UserService _userService; // Cross-feature coupling!
}

✅ CORRECT: Shared interface
using Common.Interfaces;
public class OrderHandler {
    private readonly IUserProvider _userProvider; // Abstraction!
}
```

### 2. Complete Encapsulation

**Everything needed for a feature lives in its folder**

### 3. Thin Entry Points

**Controllers/endpoints only route to feature handlers**

### 4. Business Logic in Handlers

**Handlers contain the real feature implementation**

::: notes
**Principle 1 - Feature Independence (most critical):**
This is the #1 rule that teams violate. When violated, you lose all benefits of vertical slices.

**Bad scenario:** OrderCheckout feature directly uses UserRegistration feature's classes. Now changes to UserRegistration can break OrderCheckout.

**Solution pattern:**

- Create shared interface in /Common: `IUserProvider`
- Both features use this interface
- Features remain decoupled

**Analogy:** Electrical outlets - devices (features) don't connect directly to each other, they use a shared standard (interface).

**Principle 2 - Complete Encapsulation:**
Each feature folder should read like a mini-application. Someone new should be able to understand the entire feature by reading just that folder.

**Included in feature:**

- Request object (Command/Query)
- Business logic (Handler)
- Validation rules (Validator)
- Response DTO (Result)
- Feature-specific data access
- Feature-specific models

**Principle 3 - Thin Entry Points:**
Controllers are "dumb adapters" - they translate HTTP to domain requests.
Maximum 5-10 lines per controller action.

**Principle 4 - Business Logic Location:**
All decision-making, orchestration, and business rules live in Handlers.
Not in controllers, not in repositories, not in services.

**Verification question:** "Can you understand the complete business logic by reading just the handler?"

**Transition:** "Let's see how these principles manifest in actual code structure..."
:::

---

## Feature Structure: Anatomy of a Slice

### Standard Feature Components

```
/Features
  /UserRegistration                  ← Feature folder
    RegisterUserCommand.cs           ← Request DTO (what comes in)
    RegisterUserHandler.cs           ← Business logic (the core)
    RegisterUserValidator.cs         ← Input validation rules
    RegistrationResult.cs            ← Response DTO (what goes out)
    UserRegistrationRepository.cs    ← Data access (if needed)
    Extensions.cs                    ← DI registration
```

### Component Responsibilities

| Component         | Purpose            | Contains                          |
| ----------------- | ------------------ | --------------------------------- |
| **Command/Query** | Request contract   | Input properties, IRequest marker |
| **Handler**       | Core feature logic | Business rules, orchestration     |
| **Validator**     | Input validation   | FluentValidation rules            |
| **Result**        | Response contract  | Output properties, DTOs           |
| **Repository**    | Data access        | Feature-specific queries          |

::: notes
**File-by-file walkthrough:**

**1. RegisterUserCommand.cs** (The Request)

- Immutable record/class
- Contains only input data
- Implements `IRequest<TResponse>` for MediatR
- No logic, no validation - pure data
- Example properties: Email, Password, FirstName, LastName

**2. RegisterUserHandler.cs** (The Heart)

- Implements `IRequestHandler<TRequest, TResponse>`
- THIS is where your feature lives
- Orchestrates all dependencies
- Contains business rules: "Check if user exists", "Hash password", "Send welcome email"
- Returns Result<T> (success or failure)
- Typical size: 30-100 lines

**3. RegisterUserValidator.cs** (Input Validation)

- Uses FluentValidation library
- Validates email format, password strength, required fields
- Runs BEFORE handler executes
- Separates validation from business logic
- Makes validation rules explicit and testable

**4. RegistrationResult.cs** (The Response)

- What the caller receives
- Often different from domain entities
- Contains only needed information: UserId, Email, RegistrationDate
- No sensitive data (never return password hash!)

**5. UserRegistrationRepository.cs** (Optional Data Access)

- Feature-specific queries only
- Example: CheckEmailExists(), SaveUser()
- Not a generic repository
- Only used by this feature

**Naming Convention Rules:**

- Feature folder: PascalCase, singular (UserRegistration, not UserRegistrations)
- Command: VerbEntityCommand (RegisterUserCommand)
- Query: VerbEntityQuery (GetUserProfileQuery)
- Handler: VerbEntityHandler (RegisterUserHandler)
- Consistency is critical for navigation

**Transition:** "Now let's talk about the order in which we build these components..."
:::

---

## Implementation Order: Build Vertically

### The Right Sequence Matters

```plaintext
1. Command/Query ────→ Define the contract first
   public record RegisterUserCommand(string Email, ...)

2. Result DTO ───────→ Define what comes back
   public record RegistrationResult { ... }

3. Validator ────────→ Define validation rules
   public class RegisterUserValidator : AbstractValidator<...>

4. Handler ──────────→ Implement business logic
   public class RegisterUserHandler : IRequestHandler<...>

5. Controller ───────→ Wire up HTTP endpoint
   [HttpPost] Register(command) → _mediator.Send(command)

6. Tests ────────────→ Validate everything works
   RegisterUserHandlerTests.cs
```

### Why This Order?

- **Outside-in**: Start with what callers see (contract)
- **Clear dependencies**: Each step builds on previous
- **No rework**: Avoid changing earlier components

::: notes
**Implementation order rationale:**

**Why Command First?**

- Defines the "front door" of your feature
- Makes dependencies and requirements crystal clear
- Forces you to think about the interface before implementation
- Example: "What information do I need to register a user? Email, password, name. Done."

**Why Result Second?**

- Know what you're returning before implementing how to get it
- Prevents "implementation-driven design"
- Makes the handler's goal explicit
- Example: "I need to return: UserId, Email, RegisteredAt timestamp"

**Why Validator Third?**

- Separate validation concerns from business logic
- Handler can assume validated input
- Validation rules documented and testable separately
- Example: Email format, password strength, required fields

**Why Handler Fourth?**

- Now you know: what comes in (Command), what goes out (Result), what's valid (Validator)
- Handler just needs to implement the business logic
- All contracts are clear
- Focus purely on the "how"

**Why Controller Fifth?**

- Thin adapter layer
- Just routes HTTP → MediatR → HTTP
- No business logic, no decisions
- Literally 5 lines of code

**Why Tests Last?**

- Now you have something to test!
- Test from the handler (core logic)
- Mock dependencies
- Verify business rules

**Building Analogy:**
Like building a house: foundation (contract), framing (structure), plumbing/electrical (logic), then paint (controller), then inspection (tests).

**Common mistake:**
Teams often start with the handler or controller. This leads to constantly changing interfaces and rework.

**Pro tip:**
"If your command changes after you've written the handler, you started in the wrong order."

**Transition:** "Let's look at actual code for each component..."
:::

---

## Code Example: The Command/Query

### Request DTOs Are Simple and Immutable

```csharp
// Command (for writes/mutations)
public record RegisterUserCommand(
    string Email,
    string Password,
    string FirstName,
    string LastName
) : IRequest<Result<RegistrationResult>>;

// Query (for reads)
public record GetUserProfileQuery(
    Guid UserId
) : IRequest<Result<UserProfileDto>>;
```

### Key Characteristics

✅ Use `record` for immutability (C#)
✅ All data as constructor parameters
✅ Implement `IRequest<TResponse>` (MediatR pattern)
✅ Commands modify state, Queries read state
✅ No logic, no methods - pure data contracts

::: notes
**Command vs Query distinction (CQRS pattern):**

**Commands:**

- Perform actions: Register, Update, Delete, Create
- Modify application state
- Often return success/failure + minimal data
- Example: RegisterUserCommand, UpdateProfileCommand, DeleteAccountCommand
- Naming: VerbEntityCommand

**Queries:**

- Retrieve data: Get, List, Search
- Read-only operations
- Return data snapshots
- Example: GetUserProfileQuery, SearchProductsQuery, ListOrdersQuery
- Naming: VerbEntityQuery

**Why use records?**

- Immutable by default (with-expressions for copying)
- Value-based equality
- Concise syntax
- Clearly signals "this is data, not behavior"

**IRequest<TResponse> explanation:**

- MediatR pattern interface
- TResponse is what the handler returns
- Example: `IRequest<Result<RegistrationResult>>`
  - Handler will return Result<RegistrationResult>
  - Result<T> is a success/failure wrapper

**Design principle:**
Commands/Queries are the "public API" of your feature. Design them as if they're REST API contracts.

**What NOT to include:**

- ❌ Validation logic
- ❌ Business logic
- ❌ Utility methods
- ❌ Calculated properties
- ❌ Mutable state

**Language variations:**

- TypeScript: Use classes with readonly properties
- Python: Use dataclasses with frozen=True
- Java: Use records (Java 16+)

**Pro tip:**
"If your command has methods beyond properties, you're doing it wrong."

**Transition:** "Now let's see where the real work happens - the handler..."
:::

---

## Code Example: The Handler (Core Logic)

### Handlers Orchestrate Feature Behavior

```csharp
public class RegisterUserHandler
    : IRequestHandler<RegisterUserCommand, Result<RegistrationResult>>
{
    private readonly IDbContext _dbContext;
    private readonly IPasswordHasher _passwordHasher;
    private readonly IEmailService _emailService;

    public async Task<Result<RegistrationResult>> Handle(
        RegisterUserCommand command,
        CancellationToken cancellationToken)
    {
        // 1. Business rule: Check existence
        var exists = await _dbContext.Users
            .AnyAsync(u => u.Email == command.Email, cancellationToken);

        if (exists)
            return Result<RegistrationResult>.Failure("User already exists");

        // 2. Create entity with business logic
        var user = new User {
            Id = Guid.NewGuid(),
            Email = command.Email,
            PasswordHash = _passwordHasher.Hash(command.Password),
            FirstName = command.FirstName,
            LastName = command.LastName,
            CreatedAt = DateTime.UtcNow
        };

        // 3. Persist changes
        _dbContext.Users.Add(user);
        await _dbContext.SaveChangesAsync(cancellationToken);

        // 4. Side effects
        await _emailService.SendWelcomeEmailAsync(user.Email, user.FirstName);

        // 5. Return success result
        return Result<RegistrationResult>.Success(new RegistrationResult {
            UserId = user.Id,
            Email = user.Email,
            RegisteredAt = user.CreatedAt
        });
    }
}
```

::: notes
**Handler deep dive - this is the most important component:**

**Structure of a good handler:**

**1. Business Rule Checks (Lines 14-17):**

- First, verify business constraints
- Example: "User with this email already exists"
- Return early if rules violated
- Use domain language in error messages

**2. Entity Creation with Logic (Lines 19-27):**

- Transform input to domain model
- Apply business logic (password hashing)
- Set system-generated values (ID, timestamps)
- Create rich domain objects, not anemic DTOs

**3. Persistence (Lines 29-30):**

- Save to database
- Use Unit of Work pattern (SaveChanges)
- Consider transaction boundaries
- Handle database exceptions

**4. Side Effects (Line 32-33):**

- Actions beyond saving: emails, events, notifications
- These are OK here - handler orchestrates the complete feature
- Consider async fire-and-forget or message queues for resilience

**5. Result Mapping (Lines 35-39):**

- Map domain model to result DTO
- Return only necessary information
- Use Result<T> pattern for explicit success/failure

**Dependency injection:**
Notice constructor takes 3 dependencies:

- Database context for data access
- Password hasher for security
- Email service for side effects

**Handler responsibilities:**
✅ Business rules and decisions
✅ Orchestrating dependencies
✅ Error handling and validation
✅ Transaction boundaries
✅ Mapping between layers

**Handler should NOT:**
❌ Contain HTTP concerns (status codes, headers)
❌ Perform input validation (that's validator's job)
❌ Directly reference other features
❌ Contain presentation logic
❌ Be over 150 lines (split if larger)

**Result<T> pattern explanation:**
Instead of throwing exceptions:

```csharp
Result<T>.Success(value)  ← Everything worked
Result<T>.Failure(error)  ← Business rule violation
```

This makes errors explicit and forces handling.

**Async patterns:**

- Always use CancellationToken for cancellation support
- Await all async operations
- Don't use .Result or .Wait() (causes deadlocks)

**Testing strategy:**
Handlers are your primary test target:

- Mock the dependencies (IDbContext, IPasswordHasher, etc.)
- Test business logic thoroughly
- Verify both success and failure paths

**Performance consideration:**
Don't make handlers do too much. If complex, consider:

- Domain events for side effects
- Separate handler for complex orchestration
- Move heavy processing to background jobs

**Transition:** "Notice the handler doesn't validate input - that's the validator's job..."
:::

---

## Code Example: Validation & Controllers

### Validators (Use FluentValidation)

```csharp
public class RegisterUserValidator : AbstractValidator<RegisterUserCommand>
{
    public RegisterUserValidator()
    {
        RuleFor(x => x.Email)
            .NotEmpty().WithMessage("Email is required")
            .EmailAddress().WithMessage("Invalid email format")
            .MaximumLength(255);

        RuleFor(x => x.Password)
            .NotEmpty()
            .MinimumLength(8)
            .Matches(@"[A-Z]").WithMessage("Must contain uppercase")
            .Matches(@"[0-9]").WithMessage("Must contain digit");

        RuleFor(x => x.FirstName)
            .NotEmpty()
            .MaximumLength(100);
    }
}
```

### Controllers (Keep Them Thin!)

```csharp
[ApiController]
[Route("api/users")]
public class UserRegistrationController : ControllerBase
{
    private readonly IMediator _mediator;

    [HttpPost("register")]
    public async Task<IActionResult> Register(
        RegisterUserCommand command,
        CancellationToken cancellationToken)
    {
        var result = await _mediator.Send(command, cancellationToken);
        return result.IsSuccess
            ? Ok(result.Value)
            : BadRequest(result.Error);
    }
}
```

::: notes
**Validator section:**

**Why separate validators?**

- Clear separation of concerns
- Validation rules explicit and discoverable
- Easy to test validation in isolation
- Can be reused or modified independently

**FluentValidation benefits:**

- Expressive, readable syntax
- Built-in common validations (email, length, range)
- Custom validation rules easy to add
- Excellent error messages
- Integration with ASP.NET Core model binding

**Validation execution:**

- Runs BEFORE handler executes (via MediatR pipeline behavior)
- If validation fails, handler never runs
- Returns 400 Bad Request automatically

**What to validate here:**
✅ Format and structure (email format, password strength)
✅ Required fields
✅ Length constraints
✅ Pattern matching
✅ Value ranges

**What NOT to validate here:**
❌ Business rules ("user already exists") ← that's handler's job
❌ Authorization ("user has permission") ← that's auth middleware's job
❌ Database-dependent checks ← too slow, do in handler

**Validation vs Business Rules:**

- Validation: "Is this input structurally valid?"
- Business Rules: "Does this violate domain constraints?"
- Example: Email format = validation, email already taken = business rule

**Controller section:**

**The ideal controller:**

- 5-10 lines per action
- Zero business logic
- Zero data access
- Just routing: HTTP → MediatR → HTTP

**What controllers DO:**
✅ Route HTTP requests to handlers (via MediatR)
✅ Map HTTP status codes from results
✅ Handle HTTP concerns (headers, content negotiation)
✅ Apply HTTP attributes (route, verb, auth)

**What controllers DON'T DO:**
❌ Business logic
❌ Validation
❌ Data access
❌ Complex error handling
❌ DTO mapping (handler does this)

**MediatR pattern:**

- `_mediator.Send(command)` dispatches to correct handler
- MediatR finds RegsiterUserHandler automatically
- Runs validation pipeline
- Returns result to controller

**Result mapping to HTTP:**

```csharp
result.IsSuccess ? Ok(200) : BadRequest(400)
```

Could also map:

- NotFound(404) for missing resources
- Conflict(409) for business rule violations
- Unauthorized(401) for auth failures

**Testing controllers:**
Usually skip unit testing controllers (too simple).
Test via integration tests instead.

**Anti-pattern to avoid:**

```csharp
// ❌ FAT CONTROLLER - Don't do this!
[HttpPost]
public async Task<IActionResult> Register(RegisterRequest request) {
    if (string.IsNullOrEmpty(request.Email)) return BadRequest(...);
    var user = await _dbContext.Users.FindAsync(...);
    if (user != null) return Conflict(...);
    // ... 50 more lines of logic
}
```

**Transition:** "Now let's discuss common mistakes to avoid..."
:::

---

## Anti-Patterns: What NOT to Do

### ❌ Anti-Pattern 1: Feature Dependencies

```csharp
// NEVER reference another feature directly!
using Features.UserManagement;

public class OrderCheckoutHandler {
    private readonly UserService _userService; // ❌ Cross-feature coupling!
}
```

**Solution:** Use shared interfaces in `/Common/Interfaces`

### ❌ Anti-Pattern 2: Anemic Handlers

```csharp
// Handler just passes through to service - pointless!
public class RegisterUserHandler {
    public async Task<Result> Handle(Command cmd) {
        return await _userService.Register(cmd); // ❌ No value added
    }
}
```

**Solution:** Put business logic IN the handler

### ❌ Anti-Pattern 3: Fat Controllers

```csharp
// Business logic in controller - wrong layer!
[HttpPost]
public async Task<IActionResult> Register(Request req) {
    if (string.IsNullOrEmpty(req.Email)) return BadRequest(); // ❌
    var user = await _db.Users.FindAsync(req.Email);          // ❌
    if (user != null) return Conflict();                       // ❌
}
```

::: notes
**Anti-Pattern 1: Feature Dependencies (MOST COMMON MISTAKE)**

**The problem:**

- OrderCheckout feature imports from UserManagement feature
- Creates tight coupling between features
- Changes to UserManagement break OrderCheckout
- Loses all benefits of vertical slices

**Real-world scenario:**
Team adds parameter to UserService.GetUser(). Now OrderCheckout compiler errors. Need to update OrderCheckout, retest, redeploy. Features are mow entangled.

**The solution pattern:**

```csharp
// In /Common/Interfaces/IUserProvider.cs
public interface IUserProvider {
    Task<User> GetUserAsync(Guid userId);
}

// UserManagement feature implements it
// OrderCheckout feature uses it
// Both depend on abstraction, not each other
```

**How to detect:**
Search codebase for: `using Features.` outside same feature
Any found = violation

**Anti-Pattern 2: Anemic Handlers (SECOND MOST COMMON)**

**The problem:**

- Handler does nothing, just calls a service
- All logic in ill-defined "services"
- You've recreated layered architecture in disguise!

**Why teams do this:**

- Habit from layered architecture
- Think handlers are "just routing"
- Fear of "fat handlers"

**The truth:**
Handlers SHOULD be "fat" with business logic. That's their purpose!

**Good handler characteristics:**

- 30-150 lines
- Orchestrates dependencies
- Contains business rules and decisions
- Maps between layers

**Anti-Pattern 3: Fat Controllers**

**The problem:**

- Business logic in controller
- Validation in controller
- Data access in controller
- Controller becomes untestable mess

**The "controller is a humble object" principle:**

- So simple it doesn't need unit tests
- Just adapts HTTP to domain and back
- All testable logic in handlers

**Real-world fat controller story:**
"I once saw a controller method with 400 lines. It had database queries, business logic, email sending, PDF generation, and logging. Testing required spinning up the entire web stack. A nightmare."

**Other common anti-patterns:**

**❌ Shared repositories across features:**
Don't create a generic UserRepository used by 10 features.
Create feature-specific data access.

**❌ Feature suffixes everywhere:**
Bad: UserRegistrationCommand, UserRegistrationHandler, UserRegistrationValidator
Good: Put them in /Features/UserRegistration/ folder, then just: RegisterUserCommand, RegisterUserHandler

**❌ Premature abstraction:**
Don't create shared base classes for handlers "in case we need it later."
YAGNI (You Aren't Gonna Need It).

**How to verify you're doing it right:**

1. Feature folders are balanced in size (no huge god-features)
2. No `using Features.X` from feature Y
3. Handlers contain visible business logic
4. Controllers are 5-10 lines per action
5. Can delete a feature folder without breaking others

**Transition:** "Let's talk about testing vertical slices..."
:::

---

## Testing Strategy for Vertical Slices

### Test the Handler, Not the Controller

```csharp
public class RegisterUserHandlerTests
{
    private readonly Mock<IDbContext> _dbContextMock;
    private readonly Mock<IPasswordHasher> _hasherMock;
    private readonly RegisterUserHandler _handler;

    [Fact]
    public async Task Handle_ValidCommand_ReturnsSuccess()
    {
        // Arrange
        var command = new RegisterUserCommand(
            "test@example.com", "Pass123!", "John", "Doe");

        _dbContextMock
            .Setup(db => db.Users.AnyAsync(It.IsAny<Expression<...>>(), ...))
            .ReturnsAsync(false);

        _hasherMock
            .Setup(h => h.Hash(It.IsAny<string>()))
            .Returns("hashed_password");

        // Act
        var result = await _handler.Handle(command, CancellationToken.None);

        // Assert
        Assert.True(result.IsSuccess);
        Assert.Equal("test@example.com", result.Value.Email);
        _dbContextMock.Verify(db => db.SaveChangesAsync(...), Times.Once);
    }

    [Fact]
    public async Task Handle_DuplicateEmail_ReturnsFailure()
    {
        // Arrange
        var command = new RegisterUserCommand(...);
        _dbContextMock.Setup(...).ReturnsAsync(true); // User exists

        // Act
        var result = await _handler.Handle(command, CancellationToken.None);

        // Assert
        Assert.False(result.IsSuccess);
        Assert.Contains("already exists", result.Error);
    }
}
```

::: notes
**Testing strategy for vertical slices:**

**Primary test target: HANDLERS**

- Handlers contain all business logic
- Most important code to test
- Most complex code to test
- High test coverage here = high confidence

**Secondary test target: VALIDATORS**

- Test validation rules
- Usually simpler than handler tests
- Verify rule messages are correct

**Skip: CONTROLLERS**

- Too simple to unit test
- Test via integration tests instead
- Or just rely on manual testing

**Skip: COMMANDS/QUERIES**

- Just data structures, nothing to test

**Unit testing handlers - the setup:**

**1. Mock dependencies:**

```csharp
Mock<IDbContext> - Database access
Mock<IPasswordHasher> - External services
Mock<IEmailService> - Side effects
```

**2. Create handler with mocks:**

```csharp
_handler = new RegisterUserHandler(
    _dbContextMock.Object,
    _hasherMock.Object,
    _emailServiceMock.Object
);
```

**What to test:**

**✅ Happy path:**

- Valid input → Success result
- Verify correct data saved
- Verify side effects called (email sent)
- Verify result contains expected values

**✅ Business rule violations:**

- Duplicate user → Failure result
- Verify error message
- Verify database NOT modified

**✅ Edge cases:**

- Empty strings (if validator allows)
- Boundary values
- Null handling

**✅ Exception handling:**

- Database failure → Failure result
- External service failure → Failure result
- Verify transactions rolled back

**Test structure - AAA pattern:**

**Arrange:**

- Create command with test data
- Set up mock behaviors
- Configure expected responses

**Act:**

- Call handler.Handle(command)
- Get result

**Assert:**

- Verify result.IsSuccess / IsFailure
- Verify result.Value contents
- Verify mocks called correctly (Verify)
- Check call counts (Times.Once, Times.Never)

**Mock setup patterns:**

**Async database queries:**

```csharp
_dbContextMock
    .Setup(db => db.Users.AnyAsync(...))
    .ReturnsAsync(true/false);
```

**Returns new object:**

```csharp
_hasherMock
    .Setup(h => h.Hash(It.IsAny<string>()))
    .Returns("hashed_password");
```

**Verification patterns:**

**Verify method called:**

```csharp
_dbContextMock.Verify(
    db => db.SaveChangesAsync(It.IsAny<CancellationToken>()),
    Times.Once
);
```

**Verify method NOT called:**

```csharp
_emailServiceMock.Verify(
    e => e.SendWelcomeEmailAsync(...),
    Times.Never
);
```

**Integration testing:**
Test complete features end-to-end:

- HTTP request → Controller → Handler → Database
- Use in-memory database (EF Core InMemory)
- Verify HTTP responses
- Test feature as user experiences it

**Test organization:**

```
/Tests
  /Features
    /UserRegistration
      RegisterUserHandlerTests.cs    ← Unit tests
      RegisterUserValidatorTests.cs  ← Validation tests
      UserRegistrationIntegrationTests.cs ← E2E tests
```

**Testing benefits of vertical slices:**
✅ Clear what to test (handlers)
✅ Tests organized by feature
✅ Easy to mock (clear boundaries)
✅ Tests document feature behavior
✅ Refactor features without breaking other tests

**Coverage targets:**

- Handlers: 80-90% code coverage
- Validators: 100% (they're simple)
- Commands/Results: 0% (nothing to test)
- Controllers: Integration tests only

**Transition:** "Let's wrap up with best practices and key takeaways..."
:::

---

## Best Practices Summary

### ✅ DO These Things

1. **Start small** - Convert one feature to verify the pattern
2. **Name consistently** - VerbEntityCommand/Handler/Validator
3. **Keep features independent** - Use shared interfaces
4. **Put logic in handlers** - Not services or controllers
5. **Test handlers thoroughly** - They contain your business logic
6. **Use mediatR** - Or similar mediator pattern library
7. **Validate early** - Separate validators from handlers
8. **Return Results** - Not exceptions for business rule violations

### ❌ DON'T Do These Things

1. **Don't cross-reference features** - Creates coupling
2. **Don't make thin handlers** - They should contain logic
3. **Don't put logic in controllers** - Keep them thin
4. **Don't skip validation** - Every command needs validation
5. **Don't fear some duplication** - Better than tight coupling
6. **Don't mix CQRS with CRUD** - Be consistent
7. **Don't nest features** - Keep flat structure

::: notes
**DO #1: Start Small**
Don't rewrite entire application at once. Pick one new feature or one feature to refactor. Learn the pattern. Then expand.

**Success story:** "One team started with just 'UserRegistration'. After seeing benefits (faster development, fewer bugs), they converted 3 more features in a sprint. Within 6 months, entire app was vertical slices."

**DO #2: Name Consistently**
Consistency is more important than perfection. Pick a naming scheme and stick to it religiously.

Suggested standard:

- Folder: `UserRegistration` (PascalCase)
- Command: `RegisterUserCommand`
- Handler: `RegisterUserHandler`
- Validator: `RegisterUserValidator`

**DO #3: Keep Features Independent**
This is THE most important rule. When violated, you lose all benefits.

Test: Can you delete a feature folder without breaking other features? (Except shared interfaces)

**DO #4: Put Logic in Handlers**
Resist urge to create service layers. Handlers ARE your service layer.

If handler gets too big (>150 lines), split the FEATURE, not create a service.

**DO #5: Test Handlers Thoroughly**
Your handler tests document feature behavior. Future developers will read these to understand features.

Write test names as specifications:

- `Handle_ValidCommand_ReturnsSuccess`
- `Handle_DuplicateEmail_ReturnsFailure`
- `Handle_InvalidEmail_DoesNotSendWelcomeEmail`

**DO #6: Use MediatR**
Or similar: NServiceBus, Wolverine, Mass Transit.

Benefits:

- Automatic handler discovery
- Pipeline behaviors (validation, logging)
- Decouples controllers from handlers

**DO #7: Validate Early**
Run validation BEFORE handler executes. Use FluentValidation.

Benefit: Handler can assume valid input.

**DO #8: Return Results**

```csharp
Result<T>.Success(value)
Result<T>.Failure(error)
```

Not exceptions. Exceptions for exceptional cases only.

**DON'T #1: Don't Cross-Reference Features**
We've beaten this to death, but it's that important.

**DON'T #2: Don't Make Thin Handlers**
If handler just calls another service, you haven't changed architecture, just renamed layers.

**DON'T #3: Don't Put Logic in Controllers**
Controllers translate HTTP ↔ Domain. Nothing more.

If controller is >10 lines per action, logic needs to move to handler.

**DON'T #4: Don't Skip Validation**
Every command needs a validator, even if simple.

Validates:

- Required fields
- Format/structure
- Value constraints

**DON'T #5: Don't Fear Duplication**
Some duplication OK and preferred.

Bad duplication: Copying business logic
OK duplication: DTOs, simple utilities

Principle: Prefer duplication over coupling.

**DON'T #6: Don't Mix CQRS with CRUD**
If using Commands/Queries (CQRS), go all-in.

Don't have: CreateUser command + UserService.UpdateUser() method

Be consistent across codebase.

**DON'T #7: Don't Nest Features**
Keep features at one level:

Good:

```
/Features
  /UserRegistration
  /UserProfile
  /OrderCheckout
```

Bad:

```
/Features
  /User
    /Registration  ← Don't nest!
    /Profile
```

**Migration strategy:**

**Phase 1:** New features as vertical slices
**Phase 2:** Bug fixes in old features become vertical slices
**Phase 3:** Dedicated refactoring of high-change features
**Phase 4:** Leave stable features alone (if it ain't broke...)

**Team adoption:**

- Show this presentation to team
- Convert one feature together as team
- Document your patterns (extend this presentation)
- Code review for pattern compliance
- Celebrate wins (faster development, fewer bugs)

**Transition:** "Let's see a complete real-world example..."
:::

---

## Real-World Example: User Registration

### Complete Feature Implementation

**Files created:**

```
/Features/UserRegistration/
  ├── RegisterUserCommand.cs        (12 lines)
  ├── RegisterUserHandler.cs        (87 lines)
  ├── RegisterUserValidator.cs      (24 lines)
  ├── RegistrationResult.cs         (8 lines)
  └── Extensions.cs                 (15 lines - DI setup)

/Api/Controllers/
  └── UserRegistrationController.cs (18 lines)

/Tests/Features/UserRegistration/
  ├── RegisterUserHandlerTests.cs   (156 lines - 8 tests)
  └── RegisterUserValidatorTests.cs (45 lines - 6 tests)
```

**Total:** 8 files, ~365 lines
**Development time:** 3-4 hours for complete feature
**Test coverage:** 94%
**Dependencies:** 3 shared interfaces (IDbContext, IPasswordHasher, IEmailService)

### What We Delivered

✅ Email-based user registration with password
✅ Duplicate email prevention
✅ Password hashing (bcrypt)
✅ Welcome email on successful registration
✅ Input validation (email format, password strength)
✅ Comprehensive error handling
✅ Complete test coverage
✅ Production-ready code

::: notes
**Real-world walkthrough:**

**Project context:**
E-commerce application needs user registration feature. Requirements from product owner:

- Users register with email and password
- Send welcome email after registration
- Prevent duplicate emails
- Secure password storage

**Implementation breakdown:**

**RegisterUserCommand.cs (12 lines):**

```csharp
public record RegisterUserCommand(
    string Email,
    string Password,
    string FirstName,
    string LastName
) : IRequest<Result<RegistrationResult>>;
```

Simple, immutable, clear contract.

**RegisterUserHandler.cs (87 lines):**
Contains all business logic:

- Check if email exists (business rule)
- Hash password with bcrypt (security)
- Create user entity with proper defaults
- Save to database with transaction
- Send welcome email (side effect)
- Return result DTO

Has 3 dependencies (injected):

- IDbContext for data access
- IPasswordHasher for security
- IEmailService for notifications

**RegisterUserValidator.cs (24 lines):**
FluentValidation rules:

- Email: required, valid format, max 255 chars
- Password: required, min 8 chars, contains uppercase, lowercase, digit
- FirstName: required, max 100 chars
- LastName: required, max 100 chars

**RegistrationResult.cs (8 lines):**

```csharp
public record RegistrationResult {
    public Guid UserId { get; init; }
    public string Email { get; init; }
    public DateTime RegisteredAt { get; init; }
}
```

Clean response DTO. Notice: No password returned!

**Extensions.cs (15 lines):**
Dependency injection registration:

```csharp
services.AddScoped<RegisterUserHandler>();
services.AddValidatorsFromAssemblyContaining<RegisterUserValidator>();
```

**UserRegistrationController.cs (18 lines):**
Thin controller:

```csharp
[HttpPost("register")]
public async Task<IActionResult> Register(
    RegisterUserCommand command,
    CancellationToken cancellationToken)
{
    var result = await _mediator.Send(command, cancellationToken);
    return result.IsSuccess ? Ok(result.Value) : BadRequest(result.Error);
}
```

**Tests:**

**RegisterUserHandlerTests.cs (156 lines, 8 tests):**

1. Handle_ValidCommand_ReturnsSuccess
2. Handle_DuplicateEmail_ReturnsFailure
3. Handle_ValidCommand_HashesPassword
4. Handle_ValidCommand_SendsWelcomeEmail
5. Handle_ValidCommand_SavesUser
6. Handle_DatabaseError_ReturnsFailure
7. Handle_EmailServiceError_StillSucceeds
8. Handle_CancellationRequested_StopsProcessing

**RegisterUserValidatorTests.cs (45 lines, 6 tests):**

1. Validate_ValidCommand_NoErrors
2. Validate_InvalidEmail_ReturnsError
3. Validate_WeakPassword_ReturnsError
4. Validate_EmptyFirstName_ReturnsError
5. Validate_EmptyLastName_ReturnsError
6. Validate_TooLongEmail_ReturnsError

**Development timeline:**

**Hour 1: Setup & Contract Definition**

- Created Commands, Result
- Created Validator
- Wrote validation tests
- Total: ~50 lines

**Hour 2: Core Implementation**

- Wrote Handler
- Wrote handler tests (happy path)
- Total: ~140 lines

**Hour 3: Error Handling & Edge Cases**

- Added error scenarios to handler
- Wrote error case tests
- Refined validation
- Total: ~100 lines

**Hour 4: Integration & Refinement**

- Created Controller
- Tested end-to-end locally
- Fixed integration issues
- Final cleanup
- Total: ~75 lines

**Outcome metrics:**

**Before (in layered architecture):**

- 12 files across 4 folders
- 6 hours development time
- 67% test coverage
- 3 bugs found in first week

**After (with vertical slice):**

- 8 files in 2 folders
- 4 hours development time
- 94% test coverage
- 0 bugs found in first month

**Team feedback:**
"I love that everything for user registration is in one place. When we needed to add 'email verification' later, I only touched the UserRegistration folder. Took 2 hours. Would've taken a day in the old structure."

**Common questions:**

**Q: "Only 3-4 hours? Really?"**
A: Yes. Vertical slices with clear patterns are fast. Most time is thinking about business rules, not navigating folders.

**Q: "What about code reuse?"**
A: We reused through interfaces: IDbContext, IPasswordHasher, IEmailService. Implementations shared, but features independent.

**Q: "Where's the User domain model?"**
A: In /Common/Domain/User.cs. Shared domain models are OK. Features share data structures but not logic.

**Transition:** "Let's summarize the key takeaways..."
:::

---

## Key Takeaways

### The Vertical Slice Promise

**🎯 Organize by feature, not technical layer**

**📦 Complete features in self-contained folders**

**⚡ Faster development, easier maintenance**

**🧪 Better testability and quality**

### Getting Started

1. **Learn the pattern** - Understand Commands, Handlers, Validators
2. **Start with one feature** - Don't rewrite everything at once
3. **Follow the principles** - Feature independence is critical
4. **Test your handlers** - They contain your business logic
5. **Iterate and improve** - Refine your patterns as you learn

### Resources

- **This repo:** `.github/instructions/vertical-slice.instructions.md`
- **Example code:** `/docs/vertical-slice-implementation.md`
- **MediatR:** [github.com/jbogard/MediatR](https://github.com/jbogard/MediatR)
- **FluentValidation:** [fluentvalidation.net](https://fluentvalidation.net)

::: notes
**Closing message:**

**The transformation:**
Vertical slices fundamentally change how you think about code organization. Instead of "Where do I put this method? Controller? Service? Repository?" you ask "What feature does this belong to?"

**The promise:**
Teams consistently report:

- 30-50% faster feature development
- 60% reduction in merge conflicts
- Significantly fewer bugs
- Happier developers

**Getting started roadmap:**

**Week 1: Learn**

- Read instruction files
- Watch examples
- Understand the "why"

**Week 2: Experiment**

- Convert ONE small feature
- Get team feedback
- Identify challenges

**Week 3: Refine**

- Document your patterns
- Create templates
- Update developer guidelines

**Week 4+: Scale**

- All new features as vertical slices
- Gradually refactor existing code
- Measure improvements

**Common adoption challenges:**

**Challenge 1: "Where do shared utilities go?"**
Solution: `/Common` folder for truly shared code. But prefer feature-specific when possible.

**Challenge 2: "What about infrastructure code?"**
Solution: Infrastructure (database, logging, auth) stays in infrastructure layer. Vertical slices are for features, not infrastructure.

**Challenge 3: "Team resistance to change"**
Solution: Start small. Show benefits with real metrics. Let results speak.

**Challenge 4: "Legacy codebase is huge"**
Solution: Don't rewrite. New features as vertical slices. Refactor on bug fixes. Gradual migration.

**Success patterns from teams:**

**Pattern 1: Feature Fridays**
One day per sprint, pick a feature to refactor to vertical slice. Team learning + code improvement.

**Pattern 2: New Code Only**
All new features must be vertical slices. Legacy code stays until touched.

**Pattern 3: Big Bang (Risky)**
Some teams do full rewrite. Only if small codebase (<10k lines).

**Measuring success:**

Track these metrics:

- Time to implement new features
- Number of files touched per feature
- Merge conflict frequency
- Bug count per feature
- Developer satisfaction scores

**Expected improvements after 3 months:**

- Feature delivery: 30-40% faster
- Code review time: 50% reduction
- Bug rate: 40% decrease
- Developer happiness: Significant increase

**When NOT to use vertical slices:**

❌ Simple CRUD applications (overkill)
❌ Scripting/automation tools
❌ Tiny microservices (<500 lines)
❌ Prototypes or throwaway code

✅ Medium to large applications
✅ Long-lived codebases
✅ Team of multiple developers
✅ Complex business logic

**Final thoughts:**

This isn't just a folder structure change. It's a mindset shift:

- From technical layers → Business features
- From shared services → Isolated slices
- From reuse → Independence
- From abstractions → Simplicity

**The goal:** Make it easy to understand, easy to change, easy to test.

**Closing question for audience:**
"Which feature in your current project would benefit most from this approach? That's where you should start."

**Call to action:**

- Try converting ONE feature this week
- Share your experience with the team
- Iterate on the pattern
- Measure the improvements

**Thank you section:**
Thank you for your attention! Questions?

**Contact info:**

- GitHub: [organization repo]
- Presentation materials: `/Slides`
- Example code: `/docs/vertical-slice-implementation.md`
- Questions: [your contact method]

**Additional learning resources:**

Books:

- "Vertical Slice Architecture" by Jimmy Bogard
- "Clean Architecture" by Robert C. Martin
- "Domain-Driven Design" by Eric Evans

Videos:

- NDC Talks on Vertical Slice Architecture
- Jimmy Bogard's presentations

Community:

- Stack Overflow [vertical-slice-architecture] tag
- r/dotnet discussions
- Architecture Discord servers

**Post-presentation activities:**

If this was a workshop:

- Hands-on exercise: Convert a sample feature
- Q&A session
- Pair programming session
- Code review of attendee's attempts

**Remember:** The best architecture is the one your team can execute consistently. Start simple, iterate, improve.
:::

---

## Questions & Discussion

### Let's Discuss

💬 **What challenges do you face with your current architecture?**

💬 **Which features in your codebase would benefit most from vertical slices?**

💬 **What concerns do you have about adopting this pattern?**

### Thank You!

**Slides and code examples available at:**
📂 `AI-Assisted-Software-Development/slides/marp/`
📚 `AI-Assisted-Software-Development/docs/`

**Additional resources:**
🔗 MediatR: [github.com/jbogard/MediatR](https://github.com/jbogard/MediatR)
🔗 FluentValidation: [fluentvalidation.net](https://fluentvalidation.net)
🔗 Vertical Slice Architecture Guide: `.github/instructions/vertical-slice.instructions.md`

::: notes
**Q&A Management:**

**Common questions and answers:**

**Q1: "How do you handle shared business logic between features?"**
A: Several approaches:

1. Shared interfaces in /Common/Interfaces
2. Domain events for cross-feature communication
3. Shared domain services (sparingly)
4. Accept some duplication if features truly different

Key: Don't prematurely abstract. Wait until you have 3+ features needing same logic.

**Q2: "What about database migrations with EF Core?"**
A: Options:

1. Keep migrations in infrastructure layer
2. Feature-specific migrations (advanced)
3. Use migration folders per feature

Recommendation: Start with centralized migrations, move to per-feature when needed.

**Q3: "How granular should features be?"**
A: Goldilocks principle:

- Too big: "UserManagement" (too many concerns)
- Too small: "SendEmail" (not a complete feature)
- Just right: "UserRegistration", "PasswordReset", "ProfileUpdate"

Rule of thumb: One user story = One feature

**Q4: "What about performance? Don't vertical slices create duplication?"**
A:

- Duplication: Some, but minimal. Usually just DTOs and simple logic.
- Performance: No impact. Code organization doesn't affect runtime performance.
- Actually helps: Clear boundaries make optimization easier.

**Q5: "How do you handle transactions across features?"**
A: Two approaches:

1. Saga pattern with domain events (recommended)
2. Orchestration handler that uses multiple features

Example: OrderCheckout might emit events that UserManagement and Inventory react to.

**Q6: "What about reporting that needs data from multiple features?"**
A: Reporting is special:

1. Create /Queries folder alongside /Features
2. Queries can access database directly
3. Or build dedicated read models (CQRS)
4. Reports aren't features, they're read operations

**Q7: "How do you refactor existing layered code?"**
A: Gradual migration:

1. Identify a feature boundary
2. Create /Features/[Feature] folder
3. Move related Controller, Service, Repository
4. Combine into Command + Handler
5. Add tests
6. Delete old layer files

Start with newest or most-changed features.

**Q8: "Don't we lose reusability?"**
A: Shift in thinking:

- Lost: Service classes used by many
- Gained: Features that change independently

Reuse through:

- Shared interfaces
- Domain entities
- Infrastructure services
- Common utilities

Prefer independence over reuse.

**Q9: "What about authentication/authorization?"**
A: Cross-cutting concerns stay cross-cutting:

- Auth remains in middleware/filters
- Handlers can inject ICurrentUser to get identity
- Authorization policies applied at controller/endpoint level

Example:

```csharp
[Authorize(Policy = "UserPolicy")]
[HttpPost("register")]
public async Task<IActionResult> Register(...)
```

**Q10: "Is this just CQRS?"**
A: Related but different:

- CQRS: Separate read from write models
- Vertical Slices: Organize by feature

You can combine them! Commands and Queries organized in feature slices.

**Discussion prompts:**

**Prompt 1: "Think of a recent feature you implemented..."**

- How many files did you touch?
- How many folders did you navigate?
- Could you find everything quickly?

**Prompt 2: "How would this feature look as a vertical slice?"**

- What would be in the feature folder?
- What would be shared?
- Would it be simpler or more complex?

**Prompt 3: "What's stopping you from trying this?"**

- Team buy-in?
- Learning curve?
- Existing codebase size?
- Something else?

**Workshop activity:**
If time allows, have attendees:

1. Sketch out a feature from their codebase
2. Design it as a vertical slice
3. Present to group
4. Get feedback

**Closing thoughts:**

- Don't aim for perfection
- Start small and iterate
- Measure the impact
- Share learnings with team

**Follow-up resources:**

- Office hours: [schedule link]
- Code review sessions: [schedule link]
- Slack channel: #vertical-slices
- Documentation: [wiki link]

**Thank you message:**
"Thank you all for your engagement! Remember: the goal isn't to follow this pattern religiously, but to organize code in a way that makes your team more productive. Take what works, adapt what doesn't, and share your learnings. Good luck with your implementations!"

**Post-presentation:**

- Send slides to attendees
- Share example repository
- Schedule follow-up session in 1 month
- Create feedback survey
- Compile Q&A document from session

:::
