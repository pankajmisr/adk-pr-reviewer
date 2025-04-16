# ADK PR Reviewer

A simple GitHub Pull Request review tool built with Google's Agent Development Kit (ADK).

## Overview

This tool uses the ADK CLI approach to create a PR review agent that can analyze GitHub pull requests and provide feedback on code quality, potential issues, and suggested improvements.

## Features

- Reviews GitHub pull requests using AI
- Analyzes code changes
- Provides constructive feedback
- Categorizes issues by severity

## Project Structure

```
adk-pr-reviewer/
├── README.md               # This file
├── requirements.txt        # Project dependencies
├── pr_reviewer/            # Agent package
│   ├── __init__.py         # Package marker
│   ├── agent.py            # Agent definition
│   └── github_tools.py     # GitHub integration tools
└── .env.example            # Template for environment variables
```

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/pankajmisr/adk-pr-reviewer.git
   cd adk-pr-reviewer
   ```

2. Set up a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure your environment:
   ```
   cp .env.example .env
   # Edit .env to add your GitHub token and Google API key
   ```

## Usage

1. Run the agent using the ADK CLI:
   ```
   adk run pr_reviewer
   ```

2. When prompted, enter your PR review request, for example:
   ```
   Please review pull request #4 from pankajmisr/stock-price-tracker.
   ```

3. The agent will fetch the PR details, analyze the code changes, and provide feedback.

## Requirements

- Python 3.9+
- GitHub personal access token
- Google API key for Gemini models

## License

MIT
