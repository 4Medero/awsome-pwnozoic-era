## Format String

These vulnerabilities arise when format strings are user-controlled and not properly validated.
### Vulnerable functions:

`printf`, `fprintf`, `sprintf`, `snprintf`: Use of format strings not controlled by the developer.

`vprintf`, `vfprintf`, `vsprintf`, `vsnprintf`: Similar to the above, but with variable argument lists.

`scanf`, `sscanf`, `fscanf`: If used without specifying specific buffer sizes.
