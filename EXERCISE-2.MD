# Python Automation Framework

## Overview

This Python automation framework is designed to facilitate both UI and API testing. It utilizes `pytest` for test execution and generates comprehensive HTML reports for review.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **Virtual Environment**: Helps manage dependencies and isolate the project environment.

## Getting Started

Follow the steps below to set up the framework:

```bash
# Clone the repository
git clone https://github.com/your-repo/your-framework.git

# Navigate to the framework folder
cd AutomationFramework

# Remove any existing venv, Create and activate a virtual environment
rm -rf venv
python -m venv venv
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt

# To run all tests (UI and API), use the following command:
python -m pytest -v --html=Reports/report.html testCases/

# To run only API tests, use the following command:
python -m pytest -v -m api --html=Reports/report.html testCases/
```


