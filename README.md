
# Harden -- Automated Code Improvement

This project automates the process of updating a local GitHub repository, analyzing the source code using a Hugging Face model, applying suggested improvements, committing these changes, and then pushing them back to the remote repository.

## Features

- **Automatic Updates**: Pulls the latest changes from the remote repository.
- **Code Analysis**: Analyzes the source code using the Hugging Face `transformers` pipeline with a code review model.
- **Apply Improvements**: Applies suggested code improvements directly to the source files.
- **Git Operations**: Automatically commits the updated files with a message and pushes them to the remote repository.

## Prerequisites

Before you begin, ensure you meet the following requirements:
- Python 3.6 or higher installed.
- Git installed and configured on your machine.
- Access to a GitHub repository with appropriate permissions.

## Dependencies

Install all required dependencies by running:

```bash
pip install transformers
```

Ensure that your Python environment is set up with all necessary packages. The main dependency is the `transformers` library from Hugging Face.

## Setup

1. **Clone the Repository**: Make sure your repository is cloned to your local machine.
2. **Configure Path**: Modify the `REPO_PATH` in the script to the path of your local repository.
3. **Git Configuration**: Ensure that Git is configured to handle commits and pushes without manual authentication each time, either through credential caching or SSH keys.

## Usage

To run this script, execute:

```bash
python harden.py
```

This will start the process of pulling the latest changes, analyzing the code, applying improvements, committing the changes, and pushing them back to the repository.