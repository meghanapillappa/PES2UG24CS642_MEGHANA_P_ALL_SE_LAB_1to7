# Lab 5: Reflection

### 1. What is static code analysis?

Static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities and style violations.

### 2. What is the difference between Pylint, Bandit and Flake8?

Pylint checks code quality and programming practices. Bandit checks for common security vulnerabilities. Flake8 checks Python formatting and style.

### 3. What issues did you identify and fix?

The original program had long lines, missing docstrings, inconsistent naming conventions, global-variable usage, unsafe SQL construction, shell command execution and overly broad exception handling. I improved the code and reran the analysis tools to verify the changes.

### 4. How does static analysis improve software quality?

Static analysis improves readability, maintainability and security by detecting potential problems early. It complements testing and code review.

### Results

The Pylint score improved from 2.41/10 to 10.00/10. The modified program executed successfully and printed the expected output.