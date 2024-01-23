# app/config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Application settings
APP_TITLE = "Qigong Assistant"

# OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY in your environment.")

# Embedding model name
EMBEDDING_MODEL_NAME = "text-embedding-ada-002"

# Chatbot settings
MAX_TOKENS = 150
MODEL_NAME = "text-davinci-003"

# Other global settings
# You can add more configurations here, such as database connection settings, external service URLs, etc.

# Example of a configuration that might be environment-specific
DEBUG_MODE = os.getenv('DEBUG_MODE', 'False').lower() in ['true', '1', 't']
