---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "test-driven-development-20260520"
prompt: |
  Create a comprehensive instruction file for test-driven development (TDD) that covers
  the TDD workflow, best practices, patterns, anti-patterns, and practical examples.
  Include guidance for AI-assisted test authoring and integration with vertical slices.
started: "2026-05-20T00:00:00Z"
ended: "2026-05-20T00:15:00Z"
task_durations:
  - task: "framework and structure design"
    duration: "00:05:00"
  - task: "content creation and examples"
    duration: "00:08:00"
  - task: "review and refinement"
    duration: "00:02:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/05/20/test-driven-development-20260520/conversation.md"
source: "johnmillerATcodemag-com"
applyTo: "**/*.{cs,ts,js,py,java,go,rb}"
---

# Test-Driven Development Instructions

## Overview

This document provides comprehensive guidance for implementing test-driven development (TDD) across this repository. TDD is a development methodology where tests are written before implementation, ensuring code quality, design clarity, and confidence in refactoring.

**Target Audience**: Developers, QA engineers, and AI assistants authoring code
**Scope**: TDD workflow, patterns, best practices, anti-patterns, and AI-assisted test authoring

**Related Documentation**:

- [Vertical Slice Implementation](vertical-slice-implementation.instructions.md)
- [AI-Assisted Output Instructions](ai-assisted-output.instructions.md)
- [Business Rules to Vertical Slices](business-rules-to-vertical-slices.instructions.md)

## Table of Contents

- [TDD Workflow](#tdd-workflow)
- [The Red-Green-Refactor Cycle](#the-red-green-refactor-cycle)
- [Test Anatomy](#test-anatomy)
- [Test Categories](#test-categories)
- [Testing Patterns](#testing-patterns)
- [Mocking and Test Doubles](#mocking-and-test-doubles)
- [Test Naming Conventions](#test-naming-conventions)
- [AI-Assisted Test Authoring](#ai-assisted-test-authoring)
- [Integration with Vertical Slices](#integration-with-vertical-slices)
- [Common Anti-Patterns](#common-anti-patterns)
- [Performance and Optimization](#performance-and-optimization)
- [Quality Checklist](#quality-checklist)
- [Examples](#examples)

## TDD Workflow

### Core Principles

1. **Write Tests First**: Define expected behavior before implementation
2. **Minimize Scope**: Write the smallest test to drive one piece of code
3. **Refactor Safely**: Improve code with confidence because tests catch regressions
4. **Iterate Rapidly**: Cycle through red-green-refactor continuously
5. **Maintain Clarity**: Tests document intent and expected behavior

### Workflow Steps

```
1. Write a Failing Test (RED)
   ↓
2. Write Minimal Code to Pass (GREEN)
   ↓
3. Refactor to Improve Quality (REFACTOR)
   ↓
4. Repeat for Next Behavior
```

### Time Allocation

- **Writing test**: 40% of implementation time
- **Writing code**: 30% of implementation time
- **Refactoring**: 20% of implementation time
- **Debugging**: 10% of implementation time

---

## The Red-Green-Refactor Cycle

### Phase 1: RED — Write a Failing Test

**Goal**: Define the next piece of behavior

**Steps**:

1. Write a test that describes the desired behavior
2. Test should fail (because feature doesn't exist yet)
3. Failure must be clear and specific
4. Should not depend on other unimplemented features

**Example (Python)**:

```python
# Test file: test_user_registration.py

def test_register_user_with_valid_email():
    """User can register with valid email and password."""
    user = User.register(
        email="john@example.com",
        password="SecurePass123"
    )

    assert user.email == "john@example.com"
    assert user.is_active is True
```

**Running the test**: It fails because `User.register()` doesn't exist yet.

### Phase 2: GREEN — Write Minimal Code

**Goal**: Make the test pass with minimal code

**Steps**:

1. Write only enough code to pass the test
2. Don't implement features that aren't being tested yet
3. Accept imperfect or hardcoded solutions
4. Focus on making the test pass, not on design
5. Run tests frequently (after every small change)

**Example (Python)**:

```python
# Implementation: user.py

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.is_active = True

    @classmethod
    def register(cls, email, password):
        """Register a new user."""
        return cls(email, password)
```

**Running the test**: It passes.

### Phase 3: REFACTOR — Improve Quality

**Goal**: Clean up code without changing behavior

**Steps**:

1. Tests must continue to pass
2. Improve readability, eliminate duplication
3. Extract methods, simplify logic
4. Apply design patterns where appropriate
5. Run tests after every change to catch regressions

**Example (Python)**:

```python
# Refactored: user.py

class User:
    """Represents a registered user in the system."""

    def __init__(self, email, password):
        self.email = self._validate_email(email)
        self.password = self._hash_password(password)
        self.is_active = True

    @classmethod
    def register(cls, email, password):
        """Register a new user with email and password."""
        return cls(email, password)

    @staticmethod
    def _validate_email(email):
        """Validate email format."""
        if not email or "@" not in email:
            raise ValueError("Invalid email format")
        return email

    @staticmethod
    def _hash_password(password):
        """Hash password for security."""
        if len(password) < 8:
            raise ValueError("Password too short")
        return password  # Use real hashing in production
```

**Running the test**: It still passes, but code is now cleaner and more maintainable.

---

## Test Anatomy

### Structure: Arrange-Act-Assert

```python
def test_calculate_discount():
    """Test discount calculation for bulk orders."""

    # ARRANGE: Set up test data and context
    cart_value = 1000.00
    bulk_threshold = 500.00
    discount_rate = 0.10

    # ACT: Perform the action being tested
    discount = calculate_discount(cart_value, bulk_threshold, discount_rate)

    # ASSERT: Verify the result matches expectations
    expected_discount = 100.00
    assert discount == expected_discount
```

### Structure: Given-When-Then

```python
def test_user_cannot_login_with_inactive_account():
    """Test that inactive users cannot log in."""

    # GIVEN: An inactive user account
    user = User(email="john@example.com", password="SecurePass123")
    user.is_active = False

    # WHEN: Attempting to log in
    result = user.login(password="SecurePass123")

    # THEN: Login fails
    assert result.is_success is False
    assert result.error == "Account is inactive"
```

### Key Components

| Component     | Purpose                         | Example                                        |
| ------------- | ------------------------------- | ---------------------------------------------- |
| Test name     | Describes behavior being tested | `test_user_cannot_login_with_inactive_account` |
| Setup/Arrange | Create test data and context    | `user = User(...); user.is_active = False`     |
| Act           | Execute the code being tested   | `result = user.login(...)`                     |
| Assert        | Verify expected outcome         | `assert result.is_success is False`            |
| Cleanup       | Restore state (if needed)       | Database cleanup, file deletion                |

---

## Test Categories

### 1. Unit Tests

**What to test**: Individual functions, methods, or classes in isolation

**Characteristics**:

- Fast (< 100ms each)
- Isolated (no external dependencies)
- Deterministic (same input = same output)
- Use mocks/stubs for external dependencies

**Example**:

```python
def test_email_validator_rejects_invalid_format():
    """Unit test: Email validation."""
    validator = EmailValidator()

    assert validator.is_valid("john@example.com") is True
    assert validator.is_valid("invalid-email") is False
    assert validator.is_valid("") is False
```

### 2. Integration Tests

**What to test**: Multiple components working together (e.g., service + database)

**Characteristics**:

- Slower than unit tests (100ms - 1s)
- Use real or test databases
- Test actual interactions between components
- Limited mocking (mock external services only)

**Example**:

```python
def test_user_registration_stores_in_database():
    """Integration test: User registration with database."""
    db = TestDatabase()
    user_service = UserService(db)

    user = user_service.register(
        email="john@example.com",
        password="SecurePass123"
    )

    stored_user = db.query_user_by_email("john@example.com")
    assert stored_user.id == user.id
    assert stored_user.email == user.email
```

### 3. End-to-End (E2E) Tests

**What to test**: Complete user workflows from UI to backend

**Characteristics**:

- Slowest (1s - 30s+)
- Use entire real system
- Test actual user scenarios
- Run on staging environment

**Example**:

```python
def test_user_registration_workflow_end_to_end():
    """E2E test: Complete registration workflow."""
    browser = Browser()

    # User visits registration page
    browser.navigate("https://app.example.com/register")

    # User fills form and submits
    browser.fill_field("email", "john@example.com")
    browser.fill_field("password", "SecurePass123")
    browser.click("Register")

    # User is redirected to dashboard
    assert browser.current_url.contains("/dashboard")
    assert browser.find_element("Welcome, john").is_displayed()
```

### Test Pyramid

```
         /\
        /E2E\         (Few, slow, end-to-end tests)
       /------\       ~10% of tests
      /        \
     /Integration\   (Moderate, medium speed)
    /----------\     ~30% of tests
   /            \
  /    Unit      \   (Many, fast, isolated)
 /________________\ ~60% of tests
```

---

## Testing Patterns

### 1. Assertion Patterns

**Single Assertion (Preferred)**:

```python
def test_calculate_total_with_tax():
    """Test total calculation including tax."""
    subtotal = 100.00
    tax_rate = 0.10

    result = calculate_total(subtotal, tax_rate)

    assert result == 110.00
```

**Multiple Related Assertions (Acceptable)**:

```python
def test_user_registration_response():
    """Test successful registration response."""
    result = User.register(
        email="john@example.com",
        password="SecurePass123"
    )

    assert result.user_id is not None
    assert result.email == "john@example.com"
    assert result.status == "active"
```

**Parameterized Tests (Data-Driven)**:

```python
import pytest

@pytest.mark.parametrize("email,is_valid", [
    ("john@example.com", True),
    ("invalid-email", False),
    ("", False),
    ("test@domain.co.uk", True),
])
def test_email_validation(email, is_valid):
    """Parameterized test for email validation."""
    validator = EmailValidator()
    assert validator.is_valid(email) == is_valid
```

### 2. Test Fixtures

**Setup and Teardown**:

```python
import pytest

@pytest.fixture
def test_user():
    """Create a test user."""
    user = User.create(
        email="john@example.com",
        password="SecurePass123"
    )
    yield user
    # Cleanup
    user.delete()

def test_user_can_update_email(test_user):
    """Test email update."""
    test_user.email = "newemail@example.com"
    test_user.save()

    assert test_user.email == "newemail@example.com"
```

### 3. Exception Testing

```python
import pytest

def test_register_with_duplicate_email_raises_error():
    """Test that duplicate emails are rejected."""
    User.register("john@example.com", "Pass123")

    with pytest.raises(DuplicateEmailError):
        User.register("john@example.com", "Pass456")
```

---

## Mocking and Test Doubles

### 1. Stub (Fake Behavior)

```python
class EmailServiceStub:
    """Stub email service for testing (doesn't send real emails)."""

    def __init__(self):
        self.sent_emails = []

    def send_email(self, to, subject, body):
        """Record email instead of sending."""
        self.sent_emails.append({
            "to": to,
            "subject": subject,
            "body": body
        })
```

### 2. Mock (Verify Interactions)

```python
from unittest.mock import Mock, call

def test_user_registration_sends_welcome_email():
    """Test that registration triggers welcome email."""
    email_service = Mock()
    user_service = UserService(email_service)

    user_service.register("john@example.com", "Pass123")

    # Verify email was sent
    email_service.send_email.assert_called_once_with(
        to="john@example.com",
        subject="Welcome!",
        body=Mock()  # Don't check exact body
    )
```

### 3. Spy (Partial Mock)

```python
from unittest.mock import patch

def test_logging_on_user_registration():
    """Test that registration is logged."""
    with patch('logging.info') as mock_log:
        user = User.register("john@example.com", "Pass123")

        mock_log.assert_called()
        assert "registered" in str(mock_log.call_args).lower()
```

---

## Test Naming Conventions

### Naming Pattern

```
test_<unit_under_test>_<condition>_<expected_result>
```

**Examples**:

| Test Name                                           | What It Tests                                  |
| --------------------------------------------------- | ---------------------------------------------- |
| `test_email_validator_rejects_invalid_format`       | EmailValidator rejects invalid email formats   |
| `test_user_registration_fails_with_duplicate_email` | Registration fails when email already exists   |
| `test_discount_calculation_applies_bulk_rate`       | Discount calculator applies bulk pricing rules |
| `test_login_redirects_inactive_users_to_upgrade`    | Login redirects inactive users appropriately   |

### Naming Best Practices

✅ **Clear intent**:

```python
def test_cart_applies_10_percent_discount_for_orders_over_1000():
    """Specific about discount rate and threshold."""
```

❌ **Vague intent**:

```python
def test_discount():
    """What discount? What conditions?"""
```

✅ **Describes failure case**:

```python
def test_password_validation_fails_if_less_than_8_characters():
    """Clear about what makes it fail."""
```

❌ **Generic**:

```python
def test_password_validation():
    """Could mean anything."""
```

---

## AI-Assisted Test Authoring

### Best Practices for AI Prompts

**Good Prompt**:

```
Write unit tests for the EmailValidator class.

Requirements:
- Valid: user@domain.com, test@example.co.uk
- Invalid: invalid-email, empty string, no @symbol
- Use pytest
- Each test should verify one scenario
- Follow test_<function>_<condition>_<result> naming
```

**Better Prompt**:

```
Create unit tests for UserService.register() method:

Business rules:
- Email must be unique (reject if duplicate)
- Password must be 8+ characters
- Password must contain uppercase, lowercase, digit
- On success, return User with ID and status="active"
- On failure, raise appropriate exception

Test structure:
- Use pytest fixtures for test data
- Mock the database layer
- Each test verifies one rule
- Follow AAA (Arrange-Act-Assert) pattern

Expected test cases:
1. Successful registration with valid data
2. Duplicate email rejected
3. Weak password rejected
4. Missing uppercase in password rejected
```

### AI Model Instructions

When asking AI to generate tests, specify:

1. **Testing framework**: pytest, unittest, Jest, xUnit, etc.
2. **Scope**: unit / integration / E2E
3. **What to mock**: external dependencies, databases, APIs
4. **Business rules**: constraints and validation logic
5. **Naming conventions**: pattern from this repository
6. **Examples of edge cases**: what to test
7. **Assertion style**: single assertions vs multiple related

---

## Integration with Vertical Slices

### TDD in Vertical Slice Development

Each vertical slice should have complete test coverage:

```
Vertical Slice: User Registration

├── Unit Tests (test_user.py)
│   ├── test_user_creation_with_valid_data
│   ├── test_user_email_validation
│   ├── test_password_strength_validation
│   └── test_duplicate_email_rejected
│
├── Integration Tests (test_user_service.py)
│   ├── test_user_registration_stores_in_database
│   ├── test_registration_sends_welcome_email
│   └── test_registration_creates_auth_session
│
└── E2E Tests (test_registration_flow.py)
    ├── test_complete_registration_workflow
    └── test_registration_error_handling
```

### Acceptance Criteria → Tests

From business rules to test cases:

```
Business Rule:
"Users must verify their email within 24 hours"

Acceptance Criteria:
- Verification email sent on registration
- Link expires after 24 hours
- Unverified accounts deleted after 7 days
- Resend link available if expired

Test Cases:
1. test_registration_sends_verification_email
2. test_verification_link_expires_after_24_hours
3. test_expired_link_rejected
4. test_unverified_account_deleted_after_7_days
5. test_resend_verification_email_resets_timer
```

---

## Common Anti-Patterns

### ❌ Anti-Pattern 1: Testing Implementation, Not Behavior

**Bad**:

```python
def test_user():
    """Tests implementation details instead of behavior."""
    user = User("john@example.com", "Pass123")

    # Tests internal implementation
    assert user._email_validated is True
    assert user._password_hash is not None
    assert len(user._password_hash) == 60
```

**Good**:

```python
def test_user_registration():
    """Tests observable behavior."""
    user = User.register("john@example.com", "Pass123")

    # Tests behavior
    assert user.email == "john@example.com"
    assert user.is_active is True
    assert user.can_login() is True
```

### ❌ Anti-Pattern 2: Test Interdependence

**Bad**:

```python
def test_1_create_user():
    """Test depends on database state from test_0."""
    global test_user
    test_user = User.register("john@example.com", "Pass123")
    assert test_user is not None

def test_2_login_user():
    """Test depends on test_1 running first."""
    result = test_user.login("Pass123")
    assert result is True
```

**Good**:

```python
@pytest.fixture
def user():
    """Fresh user for each test."""
    return User.register("john@example.com", "Pass123")

def test_user_can_be_created(user):
    """Independent test."""
    assert user is not None

def test_user_can_login(user):
    """Independent test, uses fresh fixture."""
    result = user.login("Pass123")
    assert result is True
```

### ❌ Anti-Pattern 3: Brittle Tests (Too Many Assertions)

**Bad**:

```python
def test_user_complete_flow():
    """Too many things tested in one test."""
    user = User.register("john@example.com", "Pass123")
    assert user.email == "john@example.com"
    assert user.is_active is True
    assert user.created_at is not None
    assert user.updated_at is not None
    assert user.login("Pass123") is True
    user.email = "new@example.com"
    user.save()
    assert user.email == "new@example.com"
    # ... many more assertions
```

**Good**:

```python
def test_user_registration_sets_email(user):
    """One behavior per test."""
    assert user.email == "john@example.com"

def test_user_registration_activates_account(user):
    """One behavior per test."""
    assert user.is_active is True

def test_user_can_login_after_registration(user):
    """One behavior per test."""
    assert user.login("Pass123") is True
```

### ❌ Anti-Pattern 4: Insufficient Test Coverage

**Bad**:

```python
def calculate_discount(cart_value, discount_rate):
    """Function with multiple paths."""
    if cart_value > 1000:
        return cart_value * discount_rate
    return 0

# Only tests happy path
def test_discount():
    assert calculate_discount(1500, 0.10) == 150
```

**Good**:

```python
# Tests all paths
def test_discount_applied_for_large_cart():
    assert calculate_discount(1500, 0.10) == 150

def test_no_discount_for_small_cart():
    assert calculate_discount(500, 0.10) == 0

def test_discount_with_edge_case_amount():
    assert calculate_discount(1000, 0.10) == 0  # or == 100 if > vs >=
```

---

## Performance and Optimization

### Test Execution Speed

**Recommended targets**:

| Test Type   | Target Speed | Total Suite  |
| ----------- | ------------ | ------------ |
| Unit        | < 100ms      | < 5 seconds  |
| Integration | < 1s         | < 30 seconds |
| E2E         | 1-30s        | < 5 minutes  |

### Optimization Techniques

**1. Use Test Doubles (Mocks/Stubs)**:

```python
# Slow: Real database call
def test_slow():
    user = User.register("john@example.com", "Pass123")  # Hits DB
    assert user.id is not None

# Fast: Mock database
def test_fast(mock_db):
    user_service = UserService(mock_db)
    user = user_service.register("john@example.com", "Pass123")
    assert user.id is not None
```

**2. Shared Fixtures (reuse setup)**:

```python
@pytest.fixture(scope="session")
def app():
    """App initialized once per test session."""
    app = create_app()
    yield app
    # Cleanup once at end

def test_one(app):
    """Reuses same app instance."""
    pass

def test_two(app):
    """Reuses same app instance."""
    pass
```

**3. Parallel Test Execution**:

```bash
# Run tests in parallel (pytest-xdist)
pytest -n auto

# Or specify number of workers
pytest -n 4
```

---

## Quality Checklist

### Before Committing Tests

**Test Quality**:

- [ ] Each test verifies one behavior
- [ ] Test names clearly describe what is tested
- [ ] Follows Arrange-Act-Assert structure
- [ ] No test interdependencies
- [ ] Tests are deterministic (same result every run)
- [ ] No hardcoded sleep/wait statements (use mocks)
- [ ] All edge cases covered
- [ ] Tests fail when code is broken
- [ ] Tests pass when code is fixed

**Code Quality**:

- [ ] Implementation is readable and simple
- [ ] No duplication between implementation and tests
- [ ] Appropriate use of mocks/stubs
- [ ] Proper error handling tested
- [ ] Business rules all have corresponding tests
- [ ] Performance meets requirements

**Coverage**:

- [ ] All public methods have tests
- [ ] All branches covered (happy path + error cases)
- [ ] Code coverage > 80% for new code
- [ ] All business rules verified
- [ ] Integration points tested

---

## Examples

### Example 1: User Registration Feature

**Vertical Slice: Basic User Registration**

```python
# tests/test_user_registration.py

import pytest
from user import User, DuplicateEmailError, WeakPasswordError


class TestUserRegistration:
    """Test suite for user registration."""

    def test_register_user_with_valid_credentials(self):
        """User can register with valid email and password."""
        user = User.register(
            email="john@example.com",
            password="SecurePass123"
        )

        assert user.email == "john@example.com"
        assert user.is_active is True
        assert user.can_login() is True

    def test_register_rejects_duplicate_email(self):
        """Registration fails if email already registered."""
        User.register("john@example.com", "SecurePass123")

        with pytest.raises(DuplicateEmailError):
            User.register("john@example.com", "OtherPass456")

    def test_register_rejects_weak_password(self):
        """Registration fails if password too weak."""
        with pytest.raises(WeakPasswordError):
            User.register("john@example.com", "weak")

    def test_register_requires_uppercase_in_password(self):
        """Password must contain uppercase letter."""
        with pytest.raises(WeakPasswordError):
            User.register("john@example.com", "secureppass123")

    def test_register_requires_digit_in_password(self):
        """Password must contain digit."""
        with pytest.raises(WeakPasswordError):
            User.register("john@example.com", "SecurePass")


# Implementation driven by tests

class User:
    """User domain model."""

    def __init__(self, email, password):
        self.email = self._validate_email(email)
        self.password = self._validate_and_hash_password(password)
        self.is_active = True

    @classmethod
    def register(cls, email, password):
        """Register a new user."""
        if User._email_exists(email):
            raise DuplicateEmailError(f"Email {email} already registered")
        return cls(email, password)

    @staticmethod
    def _validate_email(email):
        """Validate email format and existence."""
        if not email or "@" not in email:
            raise ValueError("Invalid email format")
        return email.lower()

    @staticmethod
    def _validate_and_hash_password(password):
        """Validate password strength and hash."""
        if len(password) < 8:
            raise WeakPasswordError("Password must be 8+ characters")
        if not any(c.isupper() for c in password):
            raise WeakPasswordError("Password must contain uppercase letter")
        if not any(c.isdigit() for c in password):
            raise WeakPasswordError("Password must contain digit")
        return hash(password)  # Use real hashing in production

    def can_login(self):
        """Check if user can log in."""
        return self.is_active

    @staticmethod
    def _email_exists(email):
        """Check if email already registered."""
        # Implementation would check database
        return False
```

### Example 2: Payment Processing Feature

**Vertical Slice: Calculate Order Total with Tax and Discount**

```python
# tests/test_order_calculation.py

import pytest
from decimal import Decimal
from order import Order, OrderItem


class TestOrderCalculation:
    """Test suite for order total calculation."""

    @pytest.fixture
    def order(self):
        """Create a test order."""
        order = Order()
        order.add_item(OrderItem("Widget", Decimal("100.00"), 2))
        return order

    def test_calculate_subtotal(self, order):
        """Test subtotal calculation."""
        assert order.subtotal == Decimal("200.00")

    def test_calculate_tax(self, order):
        """Test tax calculation (10%)."""
        assert order.tax == Decimal("20.00")

    def test_calculate_total_without_discount(self, order):
        """Test total calculation without discount."""
        assert order.total == Decimal("220.00")

    def test_apply_fixed_discount(self, order):
        """Test fixed discount application."""
        order.apply_discount_fixed(Decimal("10.00"))
        assert order.total == Decimal("210.00")

    def test_apply_percentage_discount(self, order):
        """Test percentage discount application."""
        order.apply_discount_percentage(Decimal("10"))  # 10%
        # Discount applied before tax: $200 * 0.10 = $20
        # New subtotal: $180, Tax: $18, Total: $198
        assert order.total == Decimal("198.00")

    @pytest.mark.parametrize("cart_value,expected_discount", [
        (Decimal("500.00"), Decimal("0.00")),   # Below threshold
        (Decimal("1000.00"), Decimal("50.00")), # At threshold
        (Decimal("1500.00"), Decimal("75.00")), # Above threshold
    ])
    def test_automatic_bulk_discount(self, expected_discount, cart_value):
        """Test automatic bulk discount for orders >= $1000."""
        order = Order()
        order.add_item(OrderItem("Product", cart_value, 1))

        assert order.applied_discount == expected_discount
```

---

## Summary

### Key Principles

1. **Write tests first** to define behavior before implementation
2. **Keep tests focused** — one behavior per test
3. **Use descriptive names** that explain what is being tested
4. **Maintain test independence** — tests should not depend on each other
5. **Refactor safely** — tests protect against regressions
6. **Optimize test speed** — use mocks and fixtures appropriately
7. **Integrate with vertical slices** — each slice has complete test coverage

### Success Criteria

You've implemented TDD effectively if:

- ✅ Tests drive development (written before implementation)
- ✅ Tests are fast and run frequently
- ✅ Test failures are meaningful and specific
- ✅ Code quality is high and refactoring is safe
- ✅ Developers confidently ship code with test coverage
- ✅ New features don't break existing functionality
- ✅ Onboarding new developers is faster (tests document intent)

---

**Document Version**: 1.0.0
**Last Updated**: 2026-05-20
**Maintainer**: Development Team
**Related Practices**: Vertical slice development, AI-assisted code generation, continuous integration
