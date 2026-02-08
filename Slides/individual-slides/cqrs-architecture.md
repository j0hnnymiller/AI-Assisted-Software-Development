---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "cqrs-architecture-slides-20260207"
prompt: |
  create slides that explain the CQRS architecture pattern
started: "2026-02-07T18:30:00Z"
ended: "2026-02-07T19:15:00Z"
task_durations:
  - task: "content planning and structure design"
    duration: "00:10:00"
  - task: "slide creation with comprehensive content"
    duration: "00:30:00"
  - task: "speaker notes and delivery guidance"
    duration: "00:05:00"
total_duration: "00:45:00"
ai_log: "ai-logs/2026/02/07/cqrs-architecture-slides-20260207/conversation.md"
source: "johnmillerATcodemag-com"
---

# CQRS Architecture

### Command Query Responsibility Segregation for Scalable Systems

::: notes
Welcome! This presentation covers CQRS (Command Query Responsibility Segregation) - a powerful architectural pattern that separates read and write operations for improved scalability, performance, and maintainability.

**Key delivery points:**

- CQRS solves real scalability and performance problems in complex applications
- We'll explore when to use it and when to avoid it
- Concrete examples and implementation patterns you can apply immediately
- Time allocation: 2-3 minutes for introduction

**Audience engagement:** "How many of you have struggled with complex queries that slow down your application's write operations? Or database schemas that try to serve both analytical reports and transactional updates?"

**Transition:** "CQRS addresses these exact challenges by recognizing that reads and writes often have fundamentally different requirements..."
:::

---

## What is CQRS?

**Architectural pattern that separates command (write) and query (read) responsibilities**

- 📝 **Commands** - Modify application state, enforce business rules
- 📖 **Queries** - Retrieve data, optimized for specific use cases
- 🏗️ **Separate Models** - Different data structures for reads vs writes
- ⚡ **Independent Scaling** - Scale read and write sides independently
- 🎯 **Optimized for Purpose** - Each side optimized for its specific concerns

**Traditional vs CQRS:**

```
Traditional (single model):          CQRS (separate models):
User ←→ Service ←→ Database          Commands → Write Model → Write DB
                                    Queries  ← Read Models  ← Read DB
```

::: notes
**Core concept explanation:**
CQRS is based on the simple principle that reads and writes often have very different requirements:

**Write operations need:**

- Strong consistency and validation
- Complex business rule enforcement
- Transactional integrity
- Normalized data structures

**Read operations need:**

- Fast response times
- Denormalized data for efficiency
- Complex aggregations and filtering
- High availability

**Key insight:** Trying to use the same model for both creates compromises that hurt both.

**Analogies:**

- Like having separate entrances for depositing vs. withdrawing money at a bank
- Or different interfaces for writing vs. reading a book
- Specialized tools for specialized jobs

**Important clarification:**
CQRS doesn't require separate databases (though it often leads there). You can start with separate models using the same database.

**Address common misconceptions:**

- This isn't just about database separation
- It's not the same as Event Sourcing (though they work well together)
- It doesn't mean every operation needs to be async

**Transition:** "Let's explore when CQRS adds value vs when it adds unnecessary complexity..."
:::

---

## When to Use CQRS

### ✅ Good Candidates for CQRS

**Performance & Scalability Issues:**

- Read/write workloads scale differently
- Complex queries slowing down transactional operations
- Need for high read throughput vs. consistent writes

**Domain Complexity:**

- Rich business rules that don't map well to query needs
- Different stakeholders need different views of the same data
- Audit trails and event-driven workflows required

**Team & System Boundaries:**

- Separate teams managing read vs. write operations
- Integration with multiple external systems
- Need for multiple read models (web, mobile, reports)

### ❌ When to Avoid CQRS

- Simple CRUD applications with balanced read/write patterns
- Small teams without operational expertise
- Low-complexity domains with straightforward data access needs

::: notes
**When CQRS Adds Value:**

**Performance scenarios:**

- E-commerce: Product catalog queries vs. order processing
- Financial systems: Account balance queries vs. transaction processing
- Social media: Feed generation vs. posting content
- Analytics: Reporting queries vs. operational data entry

**Domain complexity scenarios:**

- Order management: Complex aggregation rules for writes, denormalized views for dashboards
- Inventory: Stock level enforcement vs. availability queries across channels
- Customer service: Ticket workflow management vs. reporting and analytics

**Real-world example:**
"A client had order processing where a single order update touched 15+ database tables but their dashboard queries needed denormalized data across those same tables. Read queries were taking 3-5 seconds and blocking write operations. CQRS allowed them to optimize writes for speed and consistency while pre-building read models for instant query response."

**Warning signs you need CQRS:**

- Queries requiring 5+ table joins for simple UI displays
- Write operations waiting for read-heavy queries to complete
- Different parts of your application fighting for database resources
- Difficulty optimizing for both read and write performance

**Warning signs you DON'T need CQRS:**

- Todo list applications
- Simple content management
- Internal business tools with <100 users
- Startups validating product-market fit

**Risk assessment:**
CQRS adds operational complexity. Only use when the benefits clearly outweigh the costs.

**Team capability assessment:**

- Do you have monitoring and observability tools?
- Can your team handle eventual consistency?
- Do you have experience with message queues/event systems?

**Transition:** "For teams ready for CQRS, let's explore the core principles that make it work..."
:::

---

## Core CQRS Principles

### 1. Command-Query Separation

**Commands (Write Side):**

- Modify application state
- Enforce business rules and invariants
- Return success/failure (minimal data)
- Can fail and should be validated

**Queries (Read Side):**

- Retrieve data for presentation
- Never modify state
- Optimized for specific use cases
- Should always succeed (read-only)

### 2. Optimized Models

**Write Model:**

- Normalized for consistency
- Rich domain logic
- Transaction boundaries
- Aggregate roots

**Read Model:**

- Denormalized for performance
- Shaped for UI/consumer needs
- Pre-computed values
- Multiple specialized views

::: notes
**Principle #1: Command-Query Separation**

This goes beyond just method naming - it's about fundamentally different responsibilities:

**Command characteristics:**

```csharp
// Commands are task-based, not CRUD-based
public class ProcessOrderCommand
{
    public Guid OrderId { get; set; }
    public PaymentInfo PaymentInfo { get; set; }
    // Business intent is clear from the name
}

// Never this:
public class UpdateOrderCommand // Too generic!
```

**Query characteristics:**

```csharp
// Queries are shaped for specific needs
public class OrderSummaryQuery
{
    public DateTime DateRange { get; set; }
    public string CustomerId { get; set; }
    // Returns exactly what the UI needs
}
```

**Principle #2: Model Optimization**

**Write model example:**

```csharp
public class Order  // Rich aggregate with business logic
{
    public void ProcessPayment(PaymentInfo info)
    {
        if (Status != OrderStatus.Pending)
            throw new InvalidOperationException("Cannot process non-pending order");

        // Complex business rules here
        ValidatePayment(info);
        ApplyDiscounts();
        UpdateInventory();
        // etc.
    }
}
```

**Read model example:**

```csharp
public class OrderSummaryView  // Flat, denormalized for queries
{
    public string OrderId { get; set; }
    public string CustomerName { get; set; }  // Denormalized from Customer table
    public string ProductNames { get; set; }  // Concatenated from OrderItems
    public decimal TotalWithTax { get; set; } // Pre-calculated
    public string StatusDisplay { get; set; } // Formatted for UI
}
```

**Why separate models matter:**

- Write model can enforce complex business rules without worrying about query performance
- Read model can be optimized for specific UI scenarios without compromising write logic
- Each model evolves independently based on its concerns

**Common beginner mistake:**
Trying to use the same model for both reads and writes. This creates a "god model" that's optimized for nothing.

**Transition:** "Now let's see how these models work together in a complete architecture..."
:::

---

## CQRS Architecture Components

### Essential Components

```
┌─────────────────┐    ┌─────────────────┐
│   Command API   │    │    Query API    │
│  (Write Side)   │    │   (Read Side)   │
└─────────┬───────┘    └─────────┬───────┘
          │                      │
          ▼                      ▼
┌─────────────────┐    ┌─────────────────┐
│ Command Handler │    │ Query Handler   │
└─────────┬───────┘    └─────────┬───────┘
          │                      │
          ▼                      ▼
┌─────────────────┐    ┌─────────────────┐
│   Write Store   │◄───┤  Read Models    │
│  (Source of     │    │  (Projections)  │
│   Truth)        │    │                 │
└─────────────────┘    └─────────────────┘
          │
          ▼
┌─────────────────┐
│ Event Publisher │
└─────────────────┘
```

**Data Flow:**

1. Commands → Validation → Business Logic → Write Store
2. Events → Projection Updates → Read Models
3. Queries → Read Models → Formatted Results

::: notes
**Component Deep Dive:**

**Command API:**

- Accepts commands from clients (web, mobile, API consumers)
- First line of validation (basic structure, authentication)
- Routes to appropriate command handlers
- Returns success/failure responses

**Command Handlers:**

- Contain business logic and domain rules
- Load aggregates from write store
- Execute business operations
- Persist changes and publish events
- Example: `ProcessOrderHandler`, `UpdateInventoryHandler`

**Write Store:**

- Source of truth for all data
- Optimized for transactions and consistency
- Usually a traditional relational database
- Stores normalized data with enforced constraints

**Event Publisher:**

- Publishes domain events after successful writes
- Ensures reliable event delivery (outbox pattern)
- Enables decoupling between write and read sides
- Examples: "OrderProcessed", "InventoryUpdated", "CustomerRegistered"

**Query Handlers:**

- Execute read-only operations
- Access pre-built read models
- Apply filtering, paging, sorting
- Format data for specific consumers

**Read Models (Projections):**

- Denormalized views built from events
- Optimized for query performance
- Can be stored in different databases (SQL, NoSQL, search engines)
- Multiple read models for different use cases

**Event Flow Example:**

1. `ProcessOrderCommand` → `ProcessOrderHandler`
2. Handler validates business rules and updates write store
3. `OrderProcessedEvent` published
4. `OrderSummaryProjection` handler updates read model
5. `GetOrderSummaryQuery` reads from optimized read model

**Storage Options:**

- **Write Store**: PostgreSQL, SQL Server (ACID transactions)
- **Read Store**: MongoDB (documents), Redis (caching), Elasticsearch (search)

**Scalability Benefits:**

- Write side scales for transaction throughput
- Read side scales for query volume
- Different databases can be optimized for their specific workloads

**Transition:** "Let's dive deeper into designing effective commands..."
:::

---

## Command Model Design

### Task-Based Commands

```csharp
// ✅ GOOD: Task-based, intention-revealing
public class ProcessOrderCommand
{
    public Guid OrderId { get; set; }
    public PaymentDetails Payment { get; set; }
    public ShippingAddress Address { get; set; }
}

public class ApproveRefundCommand
{
    public Guid RefundId { get; set; }
    public string ApprovalReason { get; set; }
    public Guid ApprovedBy { get; set; }
}

// ❌ BAD: CRUD-based, generic
public class UpdateOrderCommand  // What kind of update?
{
    public Guid OrderId { get; set; }
    public Dictionary<string, object> Changes { get; set; }
}
```

### Command Handler Pattern

```csharp
public class ProcessOrderHandler : ICommandHandler<ProcessOrderCommand>
{
    public async Task<Result> Handle(ProcessOrderCommand command)
    {
        // 1. Load aggregate
        var order = await _orderRepository.GetById(command.OrderId);

        // 2. Execute business logic
        order.ProcessPayment(command.Payment);
        order.SetShippingAddress(command.Address);

        // 3. Persist changes
        await _orderRepository.SaveAsync(order);

        // 4. Publish events
        await _eventPublisher.PublishAsync(new OrderProcessedEvent(order.Id));

        return Result.Success();
    }
}
```

::: notes
**Task-Based Command Design:**

**Why task-based vs. CRUD:**

- Task-based commands express business intent clearly
- Easier to implement business rules and validations
- Better alignment with user workflows
- Clearer API contracts

**Command naming patterns:**

- Use verbs that match business language: `ProcessOrder`, `ApproveLeave`, `ScheduleMeeting`
- Avoid generic terms: `UpdateX`, `ModifyX`, `ChangeX`
- Include context when needed: `ProcessOrderPayment` vs. just `ProcessPayment`

**Command structure:**

- Include only data needed for the operation
- No behavior or logic in command objects
- Immutable data contracts
- Use value objects for complex data (Address, Money, etc.)

**Command validation strategy:**

1. **Structural validation**: Basic data type/format validation at API level
2. **Business validation**: Complex rules in the handler that require domain knowledge
3. **Cross-aggregate validation**: Use domain services when needed

**Handler responsibilities:**

1. **Load**: Get necessary aggregates from the write store
2. **Execute**: Call domain methods that contain business logic
3. **Persist**: Save changes to the write store
4. **Publish**: Emit events for interested parties

**Error handling patterns:**

```csharp
// Return success/failure, don't throw exceptions for business rule violations
if (!order.CanBeProcessed())
    return Result.Failure("Order cannot be processed in current state");

// Throw exceptions only for technical errors
if (paymentService == null)
    throw new InvalidOperationException("Payment service not configured");
```

**Aggregate design:**

- Keep aggregates small and focused
- One command should typically affect one aggregate
- Use domain events for cross-aggregate communication

**Idempotency:**
Commands should be idempotent when possible:

```csharp
// Check if already processed
if (order.Status == OrderStatus.Processed)
    return Result.Success(); // Already done, that's fine
```

**Testing strategy:**

- Test command handlers, not just commands
- Use mocks for repositories and external services
- Focus on business logic scenarios
- Test both success and failure cases

**Transition:** "Now let's see how the query side is designed for optimal reading..."
:::

---

## Query Model Design

### Shaped for Consumers

```csharp
// ✅ GOOD: UI-specific query models
public class CustomerOrderHistoryQuery
{
    public Guid CustomerId { get; set; }
    public DateTime? FromDate { get; set; }
    public int PageSize { get; set; } = 20;
    public int Page { get; set; } = 1;
}

public class CustomerOrderHistoryView
{
    public string OrderId { get; set; }
    public DateTime OrderDate { get; set; }
    public string StatusDisplay { get; set; }      // "Shipped on March 5th"
    public decimal TotalAmount { get; set; }
    public string ProductSummary { get; set; }     // "3 items: Book, Pen, +"
    public bool CanCancel { get; set; }           // Pre-computed business rule
}
```

### Read Model Patterns

```csharp
// Projection handler updates read models from events
public class OrderSummaryProjectionHandler : IEventHandler<OrderProcessedEvent>
{
    public async Task Handle(OrderProcessedEvent @event)
    {
        var orderSummary = new OrderSummaryView
        {
            OrderId = @event.OrderId.ToString(),
            CustomerName = @event.CustomerName,
            OrderDate = @event.ProcessedAt,
            StatusDisplay = FormatStatus(@event.Status),
            TotalAmount = @event.Total,
            ProductSummary = CreateProductSummary(@event.Items)
        };

        await _readDatabase.UpsertAsync(orderSummary);
    }
}
```

::: notes
**Query Model Design Philosophy:**

**Shape for specific consumers:**
Each query model should be designed for a specific use case, not generic data access.

**UI-driven design:**

- Start with the UI mockup or wireframe
- Design the query response to exactly match what the UI needs
- Include computed/formatted values to minimize client-side logic

**Example scenarios:**

**Dashboard queries:**

```csharp
public class SalesDashboardQuery
{
    public DateTime DateRange { get; set; }
    public string Region { get; set; }
}

public class SalesDashboardView
{
    public decimal TotalRevenue { get; set; }
    public int OrderCount { get; set; }
    public decimal AverageOrderValue { get; set; }  // Pre-calculated
    public List<TopProduct> TopSellingProducts { get; set; }
    public Dictionary<string, decimal> RevenueByCategory { get; set; }
}
```

**Mobile vs. Web:**
Different clients may need different representations:

```csharp
// Mobile - minimal data
public class OrderSummaryMobileView
{
    public string OrderNumber { get; set; }
    public string StatusIcon { get; set; }  // "✓", "🚚", "⏳"
    public decimal Total { get; set; }
}

// Web - detailed data
public class OrderSummaryWebView
{
    public string OrderNumber { get; set; }
    public string DetailedStatus { get; set; }
    public DateTime OrderDate { get; set; }
    public List<OrderLineItem> Items { get; set; }
    public ShippingInfo Shipping { get; set; }
    // ... much more detail
}
```

**Projection patterns:**

**1. Real-time projections:**

- Updated immediately when events occur
- Good for critical business data
- Requires reliable event processing

**2. Batch projections:**

- Updated on schedule (hourly, daily)
- Good for analytical data
- More efficient for large datasets

**3. On-demand projections:**

- Built when requested (with caching)
- Good for rarely-used or expensive queries
- Balances performance vs. storage

**Read model storage strategies:**

**Single database approach:**

- Use views or materialized views
- Simpler to manage
- Still get query optimization benefits

**Separate database approach:**

- Use different database technologies (MongoDB, Redis, Elasticsearch)
- Better performance and scalability
- More operational complexity

**Query handler responsibilities:**

```csharp
public class OrderHistoryQueryHandler : IQueryHandler<OrderHistoryQuery, OrderHistoryView>
{
    public async Task<OrderHistoryView> Handle(OrderHistoryQuery query)
    {
        // 1. Apply filtering
        var baseQuery = _readDatabase.Orders.Where(o => o.CustomerId == query.CustomerId);

        if (query.FromDate.HasValue)
            baseQuery = baseQuery.Where(o => o.OrderDate >= query.FromDate);

        // 2. Apply paging
        var orders = await baseQuery
            .Skip((query.Page - 1) * query.PageSize)
            .Take(query.PageSize)
            .ToListAsync();

        // 3. Shape response
        return new OrderHistoryView
        {
            Orders = orders,
            TotalCount = await baseQuery.CountAsync(),
            Page = query.Page,
            PageSize = query.PageSize
        };
    }
}
```

**Performance considerations:**

- Use indexes optimized for query patterns
- Consider caching for frequently accessed data
- Monitor and optimize slow queries
- Use database-specific features (SQL Server columnstore, PostgreSQL partial indexes)

**Transition:** "Now let's address one of the biggest concerns with CQRS - data consistency..."
:::

---

## Consistency Patterns

### Eventual Consistency

**Default CQRS Pattern:**

```
Command → Write Store → Event → Read Model Update
   ↓           ↓          ↓           ↓
  1ms        5ms       10ms        15ms
```

**User Experience:**

- Write operation completes immediately
- Read models updated shortly after
- UI shows "processing" or optimistic updates

### Consistency Decision Matrix

| Use Case                 | Consistency Level | Pattern                    |
| ------------------------ | ----------------- | -------------------------- |
| **Banking transactions** | Strong            | Query write store directly |
| **User profile display** | Eventual          | Standard CQRS              |
| **Order status**         | Bounded staleness | TTL-based refresh          |
| **Analytics dashboard**  | Eventual          | Batch projections          |

### Implementation Patterns

```csharp
// Pattern 1: Eventual consistency (standard)
public async Task<Result> ProcessOrder(ProcessOrderCommand command)
{
    await _writeModel.ProcessOrder(command);
    await _eventPublisher.Publish(new OrderProcessedEvent(...));
    // Read model will be updated asynchronously
    return Result.Success();
}

// Pattern 2: Strong consistency (when needed)
public async Task<OrderView> GetCriticalOrderData(Guid orderId)
{
    // For critical data, query the write store directly
    var order = await _writeStore.GetOrder(orderId);
    return MapToView(order);
}
```

::: notes
**Understanding Eventual Consistency:**

**What it means:**

- Write operations complete immediately
- Read models are updated shortly after (usually milliseconds to seconds)
- There's a brief window where reads might not reflect the latest writes

**Why it's usually acceptable:**

- Most business operations can tolerate slight delays
- Users often expect some processing time for complex operations
- Massive scalability benefits outweigh minor consistency delays

**Common scenarios:**

**E-commerce example:**

1. User places order → Write model updated (order saved)
2. User redirected to "Thank you" page
3. Background: Order details projected to read models
4. User can view order in "My Orders" (updated within seconds)

**Social media example:**

1. User posts content → Write model stores post
2. User sees confirmation message
3. Background: Post projected to feeds, search indexes
4. Post appears in followers' feeds (seconds later)

**Managing user expectations:**

**UI patterns for eventual consistency:**

```javascript
// Optimistic UI - show expected result immediately
function processOrder(order) {
    // 1. Update UI optimistically
    showOrderProcessing(order);

    // 2. Send command
    await api.processOrder(order);

    // 3. Poll for read model updates or use websockets
    pollForOrderStatus(order.id);
}
```

**Consistency requirement analysis:**

**Questions to ask:**

1. What happens if the user sees stale data?
   2 Is this a safety-critical operation?
2. Can we use optimistic UI patterns?
3. What's the business impact of delays?

**Strong consistency scenarios:**

- Financial transactions (bank balances)
- Inventory checks during purchase
- Security/authorization decisions
- Regulatory compliance data

**Eventual consistency scenarios:**

- User profile information
- Product recommendations
- Activity feeds and notifications
- Analytics and reporting

**Implementation strategies:**

**Outbox pattern for reliability:**

```csharp
public async Task ProcessOrder(ProcessOrderCommand command)
{
    using var transaction = await _database.BeginTransactionAsync();

    // 1. Write to business tables
    await _orderRepository.SaveAsync(order);

    // 2. Write to outbox table (same transaction)
    await _outboxRepository.SaveAsync(new OutboxEvent
    {
        EventType = nameof(OrderProcessedEvent),
        EventData = JsonSerializer.Serialize(orderEvent),
        CreatedAt = DateTime.UtcNow
    });

    await transaction.CommitAsync();

    // 3. Background service publishes from outbox
}
```

**Monitoring consistency lag:**

- Track time between write and read model updates
- Alert on unusual delays
- Provide user feedback for slow operations

**Bounded staleness:**
Some applications need a middle ground:

```csharp
public class ReadModelWithFreshness<T>
{
    public T Data { get; set; }
    public DateTime LastUpdated { get; set; }
    public TimeSpan MaxStaleness { get; set; }

    public bool IsStale => DateTime.UtcNow - LastUpdated > MaxStaleness;
}
```

**Transition:** "Let's look at practical implementation examples..."
:::

---

## Implementation Example

### E-Commerce Order Processing

**Command Side:**

```csharp
// Order aggregate enforces business rules
public class Order
{
    public Guid Id { get; private set; }
    public CustomerId CustomerId { get; private set; }
    public OrderStatus Status { get; private set; }
    public List<OrderItem> Items { get; private set; }

    public void ProcessPayment(PaymentInfo payment)
    {
        if (Status != OrderStatus.Pending)
            throw new InvalidOperationException("Order not in correct state");

        if (Items.Sum(i => i.Price) != payment.Amount)
            throw new InvalidOperationException("Payment amount mismatch");

        Status = OrderStatus.Paid;

        // Emit domain event
        AddDomainEvent(new OrderProcessedEvent(Id, CustomerId, payment.Amount));
    }
}

// Command handler orchestrates the workflow
public class ProcessOrderHandler
{
    public async Task<Result> Handle(ProcessOrderCommand command)
    {
        var order = await _orderRepository.GetByIdAsync(command.OrderId);

        order.ProcessPayment(command.Payment);

        await _orderRepository.SaveAsync(order);
        await _eventPublisher.PublishAsync(order.DomainEvents);

        return Result.Success();
    }
}
```

**Query Side:**

```csharp
// Projection creates optimized read models
public class OrderSummaryProjection : IEventHandler<OrderProcessedEvent>
{
    public async Task Handle(OrderProcessedEvent @event)
    {
        // Build denormalized view
        var customer = await _customerService.GetAsync(@event.CustomerId);
        var orderItems = await _orderItemService.GetAsync(@event.OrderId);

        var summary = new OrderSummaryView
        {
            OrderId = @event.OrderId,
            CustomerName = $"{customer.FirstName} {customer.LastName}",
            CustomerEmail = customer.Email,
            TotalAmount = @event.Amount,
            ItemCount = orderItems.Count,
            ItemSummary = CreateItemSummary(orderItems),
            ProcessedDate = @event.ProcessedAt,
            CanBeCancelled = CanCancelOrder(@event.ProcessedAt)
        };

        await _readDatabase.UpsertAsync(summary);
    }

    private bool CanCancelOrder(DateTime processedAt)
    {
        return DateTime.UtcNow - processedAt < TimeSpan.FromHours(24);
    }
}
```

::: notes
**Complete CQRS Implementation Walkthrough:**

**Write Side Deep Dive:**

**Domain modeling:**
The Order aggregate encapsulates all business rules about order processing:

- State validation (can't process a non-pending order)
- Business rule enforcement (payment must match order total)
- Domain event emission (for projection updates)

**Why aggregates matter in CQRS:**

- Commands target single aggregates for consistency
- Aggregates maintain business invariants
- Clear boundaries for transaction scope

**Event design:**

```csharp
public class OrderProcessedEvent : IDomainEvent
{
    public Guid OrderId { get; }
    public Guid CustomerId { get; }
    public decimal Amount { get; }
    public DateTime ProcessedAt { get; }
    public List<OrderItemData> Items { get; }

    // Include all data needed by projections
    // Avoid requiring additional queries in projection handlers
}
```

**Read Side Deep Dive:**

**Projection strategy:**
The projection handler builds a denormalized view that combines data from multiple sources:

- Order details from the event
- Customer information from customer service
- Computed values (can be cancelled, item summary)

**Why denormalization helps:**

- Single query returns all data needed by UI
- No complex joins at query time
- Pre-computed business rules (CanBeCancelled)
- Formatted display values (ItemSummary)

**Real-world considerations:**

**Error handling in projections:**

```csharp
public async Task Handle(OrderProcessedEvent @event)
{
    try
    {
        // Projection logic here
    }
    catch (Exception ex)
    {
        // Log error and decide: retry, dead letter, or skip
        _logger.LogError(ex, "Failed to project OrderProcessedEvent for order {OrderId}", @event.OrderId);

        // For critical projections, throw to retry
        // For non-critical projections, log and continue
        throw;
    }
}
```

**Projection idempotency:**
Projections should be idempotent since events might be replayed:

```csharp
public async Task Handle(OrderProcessedEvent @event)
{
    var existing = await _readDatabase.GetOrderSummaryAsync(@event.OrderId);

    if (existing?.ProcessedDate == @event.ProcessedAt)
    {
        // Already processed this exact event, skip
        return;
    }

    // Process the event...
}
```

**Multiple read models:**
Different consumers need different views:

```csharp
// Admin dashboard view
public class OrderAdminView
{
    public string OrderId { get; set; }
    public string PaymentStatus { get; set; }
    public decimal RefundAmount { get; set; }
    public List<string> Notes { get; set; }
    // Internal details not needed by customers
}

// Customer view
public class OrderCustomerView
{
    public string OrderNumber { get; set; }  // Friendly display
    public string TrackingNumber { get; set; }
    public DateTime EstimatedDelivery { get; set; }
    // Customer-focused information
}
```

**Performance optimization:**

```csharp
// Batch processing for efficiency
public class OrderSummaryBatchProjection
{
    public async Task HandleBatch(List<OrderProcessedEvent> events)
    {
        // Process multiple events in single database operation
        var summaries = events.Select(CreateOrderSummary);
        await _readDatabase.BulkUpsertAsync(summaries);
    }
}
```

**Query optimization:**

```csharp
public class OrderQueryHandler
{
    public async Task<PagedResult<OrderSummaryView>> GetCustomerOrders(CustomerOrderQuery query)
    {
        // Use database-specific optimizations
        return await _readDatabase.Orders
            .Where(o => o.CustomerId == query.CustomerId)
            .Where(o => o.ProcessedDate >= query.FromDate) // Use indexed columns
            .OrderByDescending(o => o.ProcessedDate)
            .Select(o => new OrderSummaryView {  // Project only needed fields
                OrderId = o.OrderId,
                TotalAmount = o.TotalAmount,
                // etc.
            })
            .ToPagedResultAsync(query.Page, query.PageSize);
    }
}
```

**Transition:** "Now let's look at best practices and common pitfalls..."
:::

---

## Best Practices & Anti-Patterns

### ✅ CQRS Best Practices

**1. Start Simple**

- Begin with shared database, separate models
- Add read store when performance requires it
- Don't over-engineer early

**2. Design for Specific Use Cases**

- Shape queries for UI requirements
- Create multiple read models for different consumers
- Avoid generic "get everything" queries

**3. Event-Driven Projections**

- Use events to update read models
- Make projections idempotent
- Handle projection failures gracefully

**4. Monitor Everything**

- Track command latency
- Monitor projection lag
- Alert on consistency delays

### ❌ Common Anti-Patterns

**1. Shared Models**

```csharp
// ❌ DON'T: Use same model for reads and writes
public class Order // Used for both!
{
    // Write concern: business logic
    public void ProcessPayment(PaymentInfo info) { }

    // Read concern: UI display
    public string DisplayStatus => FormatStatus(Status);
}
```

**2. CRUD-based Commands**

```csharp
// ❌ DON'T: Generic update commands
public class UpdateOrderCommand
{
    public Dictionary<string, object> Changes { get; set; }
}

// ✅ DO: Task-based commands
public class ProcessOrderPaymentCommand
{
    public PaymentInfo Payment { get; set; }
}
```

**3. Query Logic in Command Handlers**

```csharp
// ❌ DON'T: Mix query logic with commands
public async Task<OrderDto> ProcessOrder(ProcessOrderCommand command)
{
    // Process the order (good)
    await ProcessOrderLogic(command);

    // Return formatted data (bad - this is a query concern!)
    return await FormatOrderForDisplay(command.OrderId);
}
```

::: notes
**Best Practices Deep Dive:**

**Start Simple Philosophy:**

Many teams rush to implement full CQRS with separate databases, message queues, and event sourcing all at once. This leads to complexity overload.

**Progressive CQRS adoption:**

1. **Phase 1**: Separate command/query handlers, same database
2. **Phase 2**: Add read-optimized views/tables
3. **Phase 3**: Separate read database when performance demands it
4. **Phase 4**: Add event sourcing if audit/replay is needed

**Example of starting simple:**

```csharp
// Phase 1: Same database, different models
public class OrderWriteModel { /* Rich domain model */ }
public class OrderReadModel { /* Flat, denormalized */ }

// Both use same database, but different tables/views
```

**Use Case-Driven Design:**

Instead of thinking "How do I expose my data?", think "What does this UI/feature need?"

**Example - Product search:**

```csharp
// Generic (anti-pattern)
public class GetProductQuery
{
    public Guid ProductId { get; set; }
}

// Specific (good pattern)
public class ProductSearchQuery
{
    public string SearchTerm { get; set; }
    public List<string> Categories { get; set; }
    public PriceRange PriceRange { get; set; }
    public SortOption SortBy { get; set; }
}

public class ProductSearchResult
{
    public string ProductId { get; set; }
    public string Title { get; set; }
    public decimal Price { get; set; }
    public string ImageUrl { get; set; }
    public decimal Rating { get; set; }
    public int ReviewCount { get; set; }
    public bool InStock { get; set; }
    // Exactly what the product search UI needs
}
```

**Anti-Pattern Deep Dive:**

**Shared Models Problem:**
When you use the same model for reads and writes, you get:

- Complex models that serve multiple masters
- Brittle code that breaks when read or write requirements change
- Poor performance (over-fetching for reads, complex updates for writes)

**CRUD Commands Problem:**
Generic update commands are maintainability nightmares:

- Unclear business intent
- Difficult to implement business rules
- Hard to test all possible combinations
- Security issues (what if someone updates fields they shouldn't?)

**Mixed Concerns Problem:**
When command handlers return query data:

- Violates single responsibility principle
- Makes commands harder to test
- Couples write and read logic
- User gets inconsistent data (command succeeded but query shows old data)

**Additional Anti-Patterns:**

**Chatty Commands:**

```csharp
// ❌ DON'T: Multiple commands for single business operation
await _mediator.Send(new CreateOrderCommand(customerId));
await _mediator.Send(new AddOrderItemCommand(orderId, item1));
await _mediator.Send(new AddOrderItemCommand(orderId, item2));
await _mediator.Send(new ProcessOrderCommand(orderId));

// ✅ DO: Single command for complete operation
await _mediator.Send(new PlaceOrderCommand(customerId, items));
```

**Anemic Read Models:**

```csharp
// ❌ DON'T: Read models that require additional logic
public class OrderView
{
    public decimal Price { get; set; }
    public decimal Tax { get; set; }
    // Client has to calculate total
}

// ✅ DO: Read models with all computed values
public class OrderView
{
    public decimal Subtotal { get; set; }
    public decimal Tax { get; set; }
    public decimal Total { get; set; }  // Pre-calculated
    public string TotalDisplay { get; set; }  // "$123.45"
}
```

**Synchronous Projections:**

```csharp
// ❌ DON'T: Update read models synchronously
public async Task Handle(OrderProcessedEvent @event)
{
    await _writeRepository.SaveOrder(@event.Order);
    await _readRepository.UpdateOrderSummary(@event.Order);  // Blocks writes
}

// ✅ DO: Async projection updates
public async Task Handle(OrderProcessedEvent @event)
{
    await _writeRepository.SaveOrder(@event.Order);
    _eventPublisher.PublishAsync(@event);  // Async read model updates
}
```

**Monitoring and Operations:**

**Key metrics to track:**

- Command processing time (95th percentile)
- Event processing lag (time from event to projection update)
- Read model freshness (how stale are the read models?)
- Error rates (commands failing, projection failures)

**Alerting thresholds:**

- Command latency > 200ms (for most operations)
- Projection lag > 5 seconds (for real-time projections)
- Error rate > 1% (for production systems)

**Transition:** "Let's discuss migration strategies for existing systems..."
:::

---

## Migration to CQRS

### Gradual Migration Strategy

**Phase 1: Introduce Command/Query Separation**

```csharp
// Start with existing model, separate handlers
public class OrderService
{
    // Write operations
    public async Task<Result> ProcessOrder(ProcessOrderCommand command) { }
    public async Task<Result> CancelOrder(CancelOrderCommand command) { }

    // Read operations
    public async Task<OrderView> GetOrder(GetOrderQuery query) { }
    public async Task<List<OrderView>> GetCustomerOrders(CustomerOrdersQuery query) { }
}
```

**Phase 2: Optimize Read Models**

```csharp
// Add read-optimized tables/views
CREATE VIEW order_summary_view AS
SELECT
    o.order_id,
    c.first_name + ' ' + c.last_name as customer_name,
    o.total_amount,
    COUNT(oi.item_id) as item_count,
    o.created_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY o.order_id, c.first_name, c.last_name, o.total_amount, o.created_date;
```

**Phase 3: Event-Driven Projections**

```csharp
// Add event publishing and projection handlers
public class ProcessOrderHandler
{
    public async Task Handle(ProcessOrderCommand command)
    {
        // Existing business logic
        await ProcessOrderLogic(command);

        // Add event publishing
        await _eventPublisher.PublishAsync(new OrderProcessedEvent(command.OrderId));
    }
}
```

**Phase 4: Separate Read Store (if needed)**

### Migration Checklist

- [ ] Identify high-value use case to convert first
- [ ] Establish monitoring for current performance baseline
- [ ] Implement command/query separation with existing data store
- [ ] Add event publishing infrastructure
- [ ] Create first projection with monitoring
- [ ] Validate read model consistency
- [ ] Gradually migrate other use cases
- [ ] Consider separate read store only when performance requires it

::: notes
**Migration Strategy Details:**

**Why gradual migration:**

- Reduces risk of breaking existing functionality
- Allows team to learn patterns incrementally
- Provides early wins to build confidence
- Enables rollback at each phase

**Choosing the first use case:**

**Good first candidates:**

- Features with performance problems
- New features being developed
- Features with complex read requirements
- Features that don't affect critical business operations

**Bad first candidates:**

- Core business operations (billing, payments)
- Features with tight coupling to other systems
- Features without clear read/write boundaries

**Phase-by-Phase Details:**

**Phase 1 Implementation:**

```csharp
// Before: Fat service with mixed concerns
public class OrderService
{
    public async Task<OrderDto> ProcessAndGetOrder(ProcessOrderRequest request)
    {
        // Mixed write and read logic
        var order = await ProcessOrder(request);
        return await FormatOrderForDisplay(order.Id);
    }
}

// After: Separated concerns
public class ProcessOrderHandler
{
    public async Task<Result> Handle(ProcessOrderCommand command)
    {
        // Pure write logic
        return await ProcessOrderLogic(command);
    }
}

public class GetOrderHandler
{
    public async Task<OrderView> Handle(GetOrderQuery query)
    {
        // Pure read logic
        return await GetOrderLogic(query);
    }
}
```

**Phase 2 Benefits:**

- Immediate query performance improvements
- No changes to application logic
- Safe to implement and test
- Measurable benefits

**Phase 2 Example:**

```sql
-- Instead of complex runtime joins
SELECT o.*, c.*, oi.*
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id

-- Use pre-built view
SELECT * FROM order_summary_view WHERE order_id = ?
```

**Phase 3 Challenges:**

- Event publishing infrastructure
- Message delivery guarantees
- Projection error handling
- Event schema evolution

**Projection deployment strategy:**

```csharp
// Deploy projection handler first (consuming events)
// Then deploy command handler (publishing events)
// This prevents event loss during deployment
```

**Phase 4 Considerations:**

- Only when single database becomes bottleneck
- Requires separate infrastructure
- Operational complexity increases significantly
- Consider alternatives first (read replicas, caching)

**Migration Safety Nets:**

**Dual writes during transition:**

```csharp
public async Task Handle(OrderProcessedEvent @event)
{
    // Update new read model
    await _newProjection.UpdateAsync(@event);

    // Temporarily also update old model for safety
    await _legacyService.UpdateOrderSummary(@event);

    // Remove legacy update after validation period
}
```

**Shadow mode testing:**

```csharp
public async Task<OrderView> GetOrder(GetOrderQuery query)
{
    // Primary: Use legacy system
    var legacyResult = await _legacyService.GetOrder(query);

    // Shadow: Test new system (don't return result)
    _ = Task.Run(async () =>
    {
        try
        {
            var newResult = await _newQueryHandler.Handle(query);
            _metrics.CompareResults(legacyResult, newResult);
        }
        catch (Exception ex)
        {
            _logger.LogWarning(ex, "New query handler failed");
        }
    });

    return legacyResult;
}
```

**Rollback strategies:**

- Feature flags to switch between old and new implementations
- Keep legacy code until new system proves stable
- Database rollback scripts for schema changes
- Event replay capabilities for projection rebuilds

**Success metrics:**

- Query response time improvements
- Write throughput improvements
- Developer velocity (time to add new features)
- System reliability (error rates, uptime)

**Common migration mistakes:**

- Trying to migrate everything at once
- Not establishing monitoring before changes
- Underestimating operational complexity
- Not having rollback plans

**Transition:** "Let's wrap up with key takeaways and Q&A..."
:::

---

## Key Takeaways

### The CQRS Promise

**🎯 Separate read and write concerns for optimal performance**

**⚡ Scale reads and writes independently**

**🔧 Optimize each side for its specific requirements**

**📊 Build powerful read models for complex queries**

### When CQRS Adds Value

✅ **Performance problems** with complex queries slowing writes
✅ **Scalability needs** with different read/write patterns
✅ **Domain complexity** requiring rich business logic
✅ **Multiple consumers** needing different data views

### Remember

- **Start simple** - Don't over-engineer early
- **Embrace eventual consistency** - It's usually acceptable
- **Design for use cases** - Shape queries for specific needs
- **Monitor everything** - Track latency and consistency

### Resources

📖 **CQRS Guide**: `.github/instructions/cqrs-architecture.instructions.md`
🔗 **Event Store**: [eventstore.com](https://eventstore.com)
🔗 **MediatR**: [github.com/jbogard/MediatR](https://github.com/jbogard/MediatR)
📚 **Further Reading**: "Implementing Domain-Driven Design" by Vaughn Vernon

::: notes
**Final Inspiration and Practical Advice:**

**The Core Value Proposition:**
CQRS isn't just about architecture - it's about recognizing that reads and writes have fundamentally different requirements and optimizing for both.

**Real-world impact stories:**

- "A client reduced dashboard load times from 30 seconds to under 1 second by moving to CQRS read models"
- "Order processing throughput increased 5x when complex reporting queries were moved to separate read models"
- "Development velocity improved because developers could optimize writes and reads independently"

**Action plan for attendees:**

**Week 1: Assessment**

- Identify performance bottlenecks in your current system
- Look for places where complex queries affect write performance
- Assess your team's operational capabilities

**Week 2: Experiment**

- Choose one feature with clear read/write separation
- Implement separate handlers using existing database
- Measure performance improvements

**Month 1: Expand**

- Add read-optimized views or tables
- Implement event publishing for projection updates
- Monitor consistency and performance

**Month 3: Evaluate**

- Assess whether separate read store is needed
- Plan broader CQRS adoption if beneficial
- Share learnings with team

**When NOT to pursue CQRS:**

- Simple applications without performance problems
- Small teams without operational expertise
- Domains without clear read/write boundaries
- Startups focusing on product-market fit

**Success indicators:**

- Improved query performance
- Better write throughput
- Easier feature development
- Reduced database contention

**Warning signs:**

- Increased operational complexity without clear benefits
- Team struggling with eventual consistency concepts
- Over-engineering simple operations

**Final thoughts:**

- CQRS is a tool for specific problems, not a universal solution
- Start with the simplest implementation that solves your problem
- Focus on measurable improvements, not architectural purity
- Remember: the best architecture is the one your team can execute effectively

**Questions to consider:**

- "What are your specific performance pain points?"
- "How comfortable is your team with eventual consistency?"
- "Do you have monitoring and observability in place?"

**Transition to Q&A:** "Now let's discuss your specific challenges and how CQRS might help address them..."
:::

---

## Questions & Discussion

### Let's Discuss

💬 **What performance challenges do you face with your current data access patterns?**

💬 **Where do you see complex queries affecting write operations?**

💬 **What concerns do you have about eventual consistency?**

💬 **How do you currently handle scalability for reads vs. writes?**

### Thank You!

**Slides and documentation available at:**
📂 `AI-Assisted-Software-Development/Slides/individual-slides/`
📚 `AI-Assisted-Software-Development/.github/instructions/`

**Additional resources:**
🔗 **Martin Fowler's CQRS**: [martinfowler.com/bliki/CQRS.html](https://martinfowler.com/bliki/CQRS.html)
🔗 **Greg Young's Event Store**: [eventstore.com](https://eventstore.com)
🔗 **MediatR for .NET**: [github.com/jbogard/MediatR](https://github.com/jbogard/MediatR)
🔗 **CQRS Architecture Guide**: `.github/instructions/cqrs-architecture.instructions.md`

::: notes
**Q&A Management:**

**Common questions and prepared answers:**

**Q1: "Isn't CQRS just overcomplicating simple CRUD operations?"**
A: Yes, for simple CRUD! CQRS adds value when:

- You have performance bottlenecks
- Complex business rules affect simple reads
- Different consumers need different data shapes
- Read and write scalability needs differ significantly

Don't use CQRS for todo lists or simple content management.

**Q2: "How do you handle transactions that span multiple aggregates?"**
A: Two approaches:

1. **Saga pattern**: Orchestrate through events and compensating actions
2. **Process managers**: Coordinate multiple commands based on business workflow

Example: Order processing might emit events that inventory and billing services react to.

**Q3: "What about reporting queries that need data from multiple bounded contexts?"**
A: Several strategies:

1. **Dedicated reporting database**: ETL from multiple sources
2. **Event-driven reporting**: Build reporting projections from events across contexts
3. **API composition**: Aggregate data from multiple services at query time
4. **Data lake approach**: Stream events to analytics platform

**Q4: "How do you test eventual consistency?"**
A: Testing strategies:

```csharp
[Test]
public async Task OrderProcessing_EventuallyUpdatesReadModel()
{
    // Arrange
    var order = CreateTestOrder();

    // Act
    await _commandHandler.Handle(new ProcessOrderCommand(order.Id));

    // Assert - poll until read model updated
    await Eventually.AssertAsync(async () =>
    {
        var readModel = await _queryHandler.Handle(new GetOrderQuery(order.Id));
        Assert.That(readModel.Status, Is.EqualTo("Processed"));
    }, timeout: TimeSpan.FromSeconds(5));
}
```

**Q5: "What's the difference between CQRS and Event Sourcing?"**
A: Often confused, but different patterns:

- **CQRS**: Separate read and write models
- **Event Sourcing**: Store events instead of current state

They work well together but solve different problems:

- CQRS solves performance and scalability
- Event Sourcing solves auditability and temporal queries

**Q6: "How do you handle schema evolution in read models?"**
A: Versioning strategies:

```csharp
// Version your read models
public class OrderSummaryViewV2
{
    public string OrderId { get; set; }
    public decimal TotalAmount { get; set; }
    public string NewField { get; set; }  // Added in V2

    public static OrderSummaryViewV2 FromV1(OrderSummaryView v1)
    {
        return new OrderSummaryViewV2
        {
            OrderId = v1.OrderId,
            TotalAmount = v1.TotalAmount,
            NewField = DeriveFromExisting(v1)
        };
    }
}
```

**Q7: "What about GDPR and data deletion with CQRS?"**
A: Design considerations:

- Include deletion events that cascade to read models
- Use encryption with key deletion for "right to be forgotten"
- Design aggregates with GDPR in mind from the start

**Engagement techniques:**

- Ask for specific scenarios from audience
- Draw architecture diagrams on whiteboard based on their challenges
- Role-play consistency scenarios to make concepts concrete

**Follow-up opportunities:**

- Workshop on CQRS implementation patterns
- Architecture review sessions for specific applications
- Performance optimization consulting
  :::
