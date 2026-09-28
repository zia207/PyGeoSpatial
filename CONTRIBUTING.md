# Contributing to Py-GeoSpatial

Thank you for your interest in contributing to Py-GeoSpatial! This document provides guidelines for contributing to the project.

## Development Setup

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/Py-GeoSpatial.git`
3. Navigate to the project directory: `cd Py-GeoSpatial`
4. Create a virtual environment: `python -m venv venv`
5. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/macOS: `source venv/bin/activate`
6. Install in development mode: `pip install -e .[dev]`

## Code Style

We use Black for code formatting and flake8 for linting:

```bash
# Format code
black pygeospatial tests examples

# Check linting
flake8 pygeospatial tests examples
```

## Type Checking

We use mypy for type checking:

```bash
mypy pygeospatial
```

## Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=pygeospatial --cov-report=html

# Run specific test file
pytest tests/test_core.py
```

## Documentation

Build the documentation:

```bash
cd docs
make html
```

The built documentation will be in `docs/build/html`.

## Submitting Changes

1. Create a new branch: `git checkout -b feature/your-feature-name`
2. Make your changes and commit them with descriptive messages
3. Run tests and ensure they pass
4. Push to your fork: `git push origin feature/your-feature-name`
5. Create a pull request to the main repository

## Pull Request Guidelines

- Describe your changes clearly in the PR description
- Include tests for new functionality
- Update documentation as needed
- Ensure all tests pass
- Follow the existing code style

## Issue Reporting

When reporting issues, please include:

- Python version
- Py-GeoSpatial version
- Operating system
- Minimal code example to reproduce the issue
- Expected vs actual behavior
- Any error messages or stack traces

## License

By contributing to Py-GeoSpatial, you agree that your contributions will be licensed under the MIT License.
