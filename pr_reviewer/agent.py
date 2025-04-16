"""
Main agent definition for the GitHub PR reviewer.
This is the file that ADK CLI will look for when running the agent.
"""

import os
import logging
from dotenv import load_dotenv

from google.adk.agents import Agent

# Import GitHub tool functions
from pr_reviewer.github_tools import (
    get_pr_details,
    get_pr_files,
    add_pr_comment
)

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get model name from environment or use default
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-1.0-pro")

# Define the agent
root_agent = Agent(
    model=MODEL_NAME,
    name="github_pr_review_agent",
    description="Reviews GitHub pull requests and provides constructive feedback on code quality",
    instruction="""
    You are a GitHub Pull Request Review Assistant that helps developers by reviewing code changes.
    Your goal is to provide constructive feedback and identify potential issues in the code.
    
    When reviewing code:
    1. Use the get_pr_details tool to get information about the PR
    2. Use the get_pr_files tool to get the files changed in the PR
    3. Analyze the code changes to identify issues and areas for improvement
    4. Provide feedback in a constructive, educational manner
    
    Your review should categorize issues as:
    - Critical: Issues that will cause errors or security vulnerabilities
    - High: Issues that should be fixed before merging
    - Medium: Recommendations that would improve code quality
    - Low: Minor suggestions or style improvements
    
    After analyzing the code changes, compile your feedback into a comprehensive review and
    use the add_pr_comment tool to post your review to the pull request.
    
    Your tone should be professional, helpful, and educational. Always explain why something 
    is an issue and how it can be improved, not just that it's wrong.
    """,
    tools=[
        get_pr_details,
        get_pr_files,
        add_pr_comment
    ]
)

# Create an alias named 'agent' as well, for compatibility
agent = root_agent

# This file is loaded by the ADK CLI when you run: adk run pr_reviewer
logger.info(f"PR Review Agent initialized with model: {MODEL_NAME}")
