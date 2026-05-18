# TestGuard AI

AI-powered code review agent for test automation projects.

## Overview

TestGuard AI analyzes automated test codebases and detects quality issues that commonly make test suites fragile, flaky, hard to maintain, or difficult to scale.

This project focuses on QA automation engineering best practices enhanced with AI-powered review capabilities.

## Initial Features

- Detect flaky test patterns
- Review locator quality
- Analyze naming conventions
- Detect duplicated test logic
- Review assertion quality
- Detect Page Object violations
- Identify hardcoded test data
- Generate AI-powered recommendations

## Supported Stack (initial)

- Java
- Selenium WebDriver
- TestNG

Future support:

- Playwright
- Cypress
- JUnit
- Pytest

## Example Findings

### Flaky Pattern

```java
Thread.sleep(5000);
```

Finding:

```txt
High Risk: Fixed wait detected.
Recommendation: Replace with explicit waits.
```

### Poor Locator

```java
driver.findElement(By.xpath("//*[@id='main']/div[2]/div[5]/button"));
```

Finding:

```txt
Warning: Fragile absolute XPath detected.
Recommendation: Prefer stable IDs, data-test attributes, or semantic selectors.
```

## Roadmap

### MVP
- Java parser
- Static rule engine
- Flaky pattern detection
- Locator quality analysis
- Naming convention review

### Phase 2
- AI explanation layer
- Refactor suggestions
- Automation quality score
- HTML reporting

### Phase 3
- Multi-framework support
- CLI interface
- CI integration
- Pull request review mode

## Goal

Help QA engineers build cleaner, more reliable, and more scalable automation frameworks.
