
# Software Design Principles (Based on *A Philosophy of Software Design, 2nd Edition*)

This document provides a detailed overview of foundational software design principles based on John Ousterhout’s *A Philosophy of Software Design (2nd Edition)*. These principles are meant to guide AI agents or human developers in writing clean, maintainable, and robust software.

---

## Table of Contents

1. [Complexity is the Root of All Evil](#1-complexity-is-the-root-of-all-evil)
2. [Modules Should Be Deep](#2-modules-should-be-deep)
3. [Information Hiding](#3-information-hiding)
4. [Define Errors Out of Existence](#4-define-errors-out-of-existence)
5. [Design It Twice](#5-design-it-twice)
6. [Pull Complexity Downwards](#6-pull-complexity-downwards)
7. [The End Justifies the Means](#7-the-end-justifies-the-means)
8. [Comments Should Describe the *Why*](#8-comments-should-describe-the-why)
9. [Choose Simplicity over Generality](#9-choose-simplicity-over-generality)
10. [Design for Change](#10-design-for-change)
11. [Write Less Code](#11-write-less-code)

---

## 1. Complexity is the Root of All Evil

**Summary**: The primary enemy of good design is complexity. Complex systems are hard to understand, change, and debug.

**Explanation**: Every line of code adds to the cognitive load of anyone maintaining the software. Complexity tends to accumulate unless deliberately managed.

**Example**:

Bad:

```go
// Updates cache only if multiple conditions are met
if isAuthenticated && user.Role == "admin" && time.Now().Before(sessionExpiry) {
    if cache.IsStale(user.ID) {
        cache.Refresh(user.ID)
    }
}
```

Better:

```go
if shouldRefreshCache(user) {
    cache.Refresh(user.ID)
}

func shouldRefreshCache(user User) bool {
    return isAuthenticatedUser(user) && cache.IsStale(user.ID)
}
```

---

## 2. Modules Should Be Deep

**Summary**: A good module provides a lot of functionality (deep) through a simple interface (narrow).

**Explanation**: Modules that are "shallow" (i.e., provide a thin wrapper over another system without hiding complexity) offer little benefit. A deep module hides complexity and offers significant abstraction.

**Example**:

Shallow Module:

```go
func OpenSocket(address string, port int) error {
    return net.Dial("tcp", fmt.Sprintf("%s:%d", address, port))
}
```

Deep Module:

```go
type Connection struct {
    conn net.Conn
}

func NewConnection(config Config) (*Connection, error) {
    address := fmt.Sprintf("%s:%d", config.Host, config.Port)
    conn, err := net.Dial("tcp", address)
    if err != nil {
        return nil, fmt.Errorf("connection failed: %w", err)
    }
    return &Connection{conn: conn}, nil
}
```

---

## 3. Information Hiding

**Summary**: Modules should hide as much information as possible. Only expose what is necessary.

**Explanation**: Encapsulation limits the impact of changes and reduces cognitive load. If a module changes its internal behavior, other parts of the code should not need to change.

**Example**:

Bad:

```go
type User struct {
    ID        string
    IsPremium bool
}
```

Better:

```go
type User struct {
    id        string
    isPremium bool
}

func (u *User) CanAccessFeatureX() bool {
    return u.isPremium
}
```

---

## 4. Define Errors Out of Existence

**Summary**: Design interfaces so that common errors cannot occur.

**Explanation**: The best way to deal with errors is to design them away. Make invalid states unrepresentable.

**Example**:

Bad:

```go
func SetUsername(username string) {
    if username == "" {
        log.Fatal("Username cannot be empty")
    }
    ...
}
```

Better:

```go
type Username string

func NewUsername(input string) (Username, error) {
    if input == "" {
        return "", errors.New("username cannot be empty")
    }
    return Username(input), nil
}
```

---

## 5. Design It Twice

**Summary**: The first design is rarely the best. Always iterate and refine.

**Explanation**: Initial designs are often suboptimal. By revisiting the design, you can spot flaws, unnecessary complexity, or better abstractions.

**Example**:

Initial Design:

```go
func SendNotification(userID string, message string, sms bool, email bool) {
    // Sends either SMS or email
}
```

Refined Design:

```go
type Channel interface {
    Send(userID, message string) error
}

type SMSChannel struct{}
type EmailChannel struct{}

func (s SMSChannel) Send(userID, message string) error {
    // send SMS
}

func (e EmailChannel) Send(userID, message string) error {
    // send email
}
```

---

## 6. Pull Complexity Downwards

**Summary**: Handle complexity at lower levels, not at the interface or caller level.

**Explanation**: If every caller needs to handle complex logic, move that logic into the module itself.

**Example**:

Bad:

```go
if file.Exists() {
    file.Delete()
}
```

Better:

```go
file.SafeDelete()
```

---

## 7. The End Justifies the Means

**Summary**: The most important thing is the overall design quality, not adherence to arbitrary rules.

**Explanation**: Don’t follow principles or best practices blindly. If breaking a rule reduces complexity or improves clarity, it's acceptable.

**Example**:

Breaking DRY for clarity:

```go
log.Println("Starting backup")
backupData()
log.Println("Backup completed successfully")
```

Versus:

```go
func logAndRun(msg string, f func()) {
    log.Println("Starting " + msg)
    f()
    log.Println(msg + " completed successfully")
}

logAndRun("backup", backupData)
```

---

## 8. Comments Should Describe the *Why*

**Summary**: Don’t comment on what the code does. Comment on why it does it.

**Explanation**: Good code is often self-explanatory in *what* it does. Comments should clarify *intent* or *rationale*.

**Example**:

Bad Comment:

```go
// Set x to 5
x := 5
```

Good Comment:

```go
// Use a buffer size of 5 for low-latency processing
x := 5
```

---

## 9. Choose Simplicity over Generality

**Summary**: Don’t generalize code prematurely. Handle specific use cases simply.

**Explanation**: Premature generalization increases complexity and maintenance burden.

**Example**:

Over-abstracted:

```go
func filter[T any](items []T, predicate func(T) bool) []T
```

Simple and effective:

```go
func filterStrings(items []string, predicate func(string) bool) []string
```

---

## 10. Design for Change

**Summary**: Anticipate how your code might evolve. Structure it so future changes are easy to make.

**Explanation**: Designing for change doesn't mean guessing the future, but creating loose coupling and high cohesion.

**Example**:

Instead of hardcoding behavior:

```go
func ValidateUser(u User) bool {
    return strings.Contains(u.Email, "@")
}
```

Abstract it:

```go
type Validator interface {
    Validate(u User) bool
}
```

---

## 11. Write Less Code

**Summary**: The less code you write, the less code you have to understand and maintain.

**Explanation**: Every line of code is a liability. Remove duplication, avoid unnecessary layers, and use libraries when appropriate.

**Example**:

Don't reinvent the wheel:

Bad:

```go
func reverse(s string) string {
    result := ""
    for i := len(s) - 1; i >= 0; i-- {
        result += string(s[i])
    }
    return result
}
```

Better:

Use built-in or standard library functions when available, or justify the custom logic.

---

## Final Notes for AI Agent Integration

When designing software or generating code:

- Favor clarity over cleverness.
- Bias toward deeper modules that encapsulate complexity.
- Prioritize design that reduces the need for comments or explanations.
- Revisit and iterate on your designs.
- Strive for high-level simplicity, even if the implementation is sophisticated.
