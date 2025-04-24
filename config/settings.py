import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
OPENAI_API_KEY = os.getenv("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")
DEFAULT_MODEL = "gpt-4o"

# Agent Configuration
ENABLE_HUMAN_FEEDBACK = False
VERBOSE_MODE = True
