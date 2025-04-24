# Create settings.py file
cat > config/__init__.py << 'EOL'
# Empty init file to make the directory a Python package
EOL

cat > config/settings.py << 'EOL'
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv() 

# API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEFAULT_MODEL = "gpt-4o"

# Agent Configuration
ENABLE_HUMAN_FEEDBACK = False
VERBOSE_MODE = True
EOL
