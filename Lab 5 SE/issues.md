# Lab 5: Static Code Analysis — Issues and Fixes

| Issue | Type | Description | Fix Approach |
|---|---|---|---|
| Long lines | Style | SQL statements exceeded the recommended line length | Split SQL statements across multiple lines |
| Missing docstrings | Code quality | Module and functions lacked documentation | Added module and function docstrings |
| Invalid naming conventions | Style | Function names used camelCase | Renamed functions using snake_case |
| Global statement | Code quality | Global variable was used to maintain the order total | Calculated the total from the database |
| SQL injection risk | Security | SQL query used string formatting | Replaced string formatting with parameterized queries |
| Unsafe shell execution | Security | `os.system()` executed a shell command | Replaced it with a direct print statement |
| Broad exception handling | Code quality | A generic exception was silently ignored | Removed unnecessary exception suppression |
| Unused argument | Code quality | The remarks argument was not used | Documented its limitation because the schema has no remarks column |

## Result

- Original Pylint score: 2.41/10
- Final Pylint score: 10.00/10
- The program was executed successfully after modification.