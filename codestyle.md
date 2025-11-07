# Backend Code Style Guide

This document is based on the following industry standards:
- PEP 8 -- Style Guide for Python Code: https://pep8.org/
- Flask Project Structure Best Practices

## Python Coding Standards
- Use 4 spaces per indentation level (no tabs)
- Maximum line length: 79 characters
- Use UTF-8 encoding (add `# -*- coding: utf-8 -*-` at file beginning)
- Use snake_case for variable and function names: `contact_list`, `get_contacts()`
- Use PascalCase for class names: `class ContactManager`
- Use UPPERCASE for constants: `MAX_CONTACTS = 100`
- Use single quotes for strings: `name = 'John'`
- Use double quotes for docstrings

## Imports Organization
- Group imports in the following order:
  1. Standard library imports
  2. Related third party imports
  3. Local application/library specific imports
- Put each import on a separate line
- Use absolute imports instead of relative imports

## Function and Class Standards
- Use descriptive names for functions and classes
- Limit functions to a single responsibility
- Keep functions small and focused
- Use docstrings for all public modules, functions, classes, and methods
- Separate top-level functions and classes with two blank lines
- Methods inside a class are separated by one blank line

## Flask-Specific Standards
- Use Blueprints to organize larger applications
- Keep route functions focused on HTTP logic
- Move business logic to separate modules
- Use configuration objects for different environments
- Handle errors with appropriate HTTP status codes

## File Structure
- Place all source code in the `src/` directory
- Use `controller/` directory for route handlers
- Use descriptive file names: `contact_routes.py` instead of `routes.py`
- Separate database models from route handlers