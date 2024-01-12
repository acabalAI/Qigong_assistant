import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Application Title
APP_TITLE = "Qigong Assistant"

# OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY in your environment.")

#openai.proxy = {
           # "http": "http://127.0.0.1:7890",
           # "https": "http://127.0.0.1:7890"
       # }
# Other configurations can be added here
# For example, database configuration, external service URLs, etc.

# Additional settings (if any)

