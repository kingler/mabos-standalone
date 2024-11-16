# Contributing to MABOS

We welcome contributions to the Multi-Agent Business Optimization System (MABOS)! This document provides guidelines for contributing to the project.

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct, which can be found in the `CODE_OF_CONDUCT.md` file.

## How to Contribute

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes
4. Write or update tests for your changes
5. Ensure all tests pass
6. Submit a pull request

## Development Setup

Please refer to the README.md file for detailed instructions on setting up the development environment.

## Coding Standards

- Follow PEP 8 style guide for Python code
- Use ESLint and Prettier for JavaScript/React code
- Write meaningful commit messages
- Keep functions small and focused
- Comment your code where necessary

## Testing

- Write unit tests for new features or bug fixes
- Ensure all existing tests pass before submitting a pull request
- Run the full test suite locally before pushing your changes

## Security Considerations

Security is a top priority for MABOS. We have implemented several security measures, including automated security scanning using OWASP ZAP. Here's what you need to know:

1. Automated Security Scans: 
   - Every pull request to the main branch triggers an automated security scan.
   - Nightly scans are also performed on the main branch.

2. Before submitting a pull request:
   - Run the local security scan script: `python scripts/run_zap_scan.py`
   - Review the generated report in the `security_reports` directory
   - Address any high or medium severity issues found

3. Handling Security Issues:
   - If you discover a security vulnerability, please do NOT open an issue.
   - Instead, email security@mabos.com with details about the vulnerability.

4. Best Practices:
   - Always validate and sanitize user inputs
   - Use parameterized queries to prevent SQL injection
   - Avoid storing sensitive information in code or commit messages
   - Keep dependencies up to date

5. Code Review:
   - Security-related changes will undergo additional scrutiny during code review
   - Be prepared to explain and justify security-related decisions

By following these guidelines, you help maintain the security and integrity of MABOS.

## Pull Request Process

1. Ensure your code adheres to the coding standards outlined above
2. Update the README.md with details of changes to the interface, if applicable
3. Increase the version numbers in any examples files and the README.md to the new version that this Pull Request would represent
4. You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you

## Reporting Bugs

1. Check if the bug has already been reported in the Issues section
2. If not, create a new issue with a clear title and description
3. Include as much relevant information as possible
4. Add steps to reproduce the bug

## Suggesting Enhancements

1. Check if the enhancement has already been suggested in the Issues section
2. If not, create a new issue with a clear title and description
3. Provide a clear and detailed explanation of the feature you want to see
4. Explain why this enhancement would be useful to most MABOS users

Thank you for contributing to MABOS!