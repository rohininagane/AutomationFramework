# Python Automation Framework

## Overview

This POM design pattern automation framework is designed to facilitate both UI and API testing. It utilizes below tools and technologies. 
- Programming language - `python`
- Test Framework - `pytest`
- Automation tool for UI - `selenium`
- Library for logs - `logging`
- Reports - `pytest supported html report`
- For API automation - `Request module`


### Directory and File Descriptions

- pageObject: Contains page object classes that encapsulate the UI elements and interactions for UI testing.
- testCases: Contains the test cases for both UI and API testing.
- utilities: Contains utility modules, custom loggers, and helper functions used across the framework.
- Reports: Directory where test execution reports are generated and stored. Typically, these include HTML reports and other formats as needed.
- Logs: Contains log files created during test execution, useful for debugging and tracking test execution.
- Screenshots: Stores screenshots taken during test execution, useful for visual verification and debugging.
- Configurations: Contains configuration files, such as environment settings and API endpoints.
- RequestTemplates: Contains templates for API requests that can be used for testing.
- TestData: Stores JSON format files containing test data used in test cases.
- EXERCISE-2.MD: README for API test cases.
- UIREADME.MD: README file with specific instructions or details about UI testing.
- requirements.txt: Lists all the Python packages required for the project, which can be installed using `pip`.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **Virtual Environment**: Helps manage dependencies and isolate the project environment.

## Getting Started

To get started, Follow below commands to setup framework:

```bash
#Clone the repository using below command
git clone https://github.com/your-repo/your-framework.git

#Navigate to framework folder
cd AutomationFramework

#Remvoe any existing venv, Create new virtual env and activate it
rm -rf venv
python -m venv venv
source venv/bin/activate 

# Install requirements with below command
pip install -r requirements.txt

# To run all test cases UI and API. Run below command
python -m pytest -v --html=Reports/report.html testCases/

# To run only UI tests execute below command
python -m pytest -v -m ui --html=Reports/report.html testCases/
```

Once execution is completed check html report in report folder

# AutomationFramework
