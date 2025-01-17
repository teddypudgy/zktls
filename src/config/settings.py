"""Configuration settings for the zkTLS Twitter AI Agent"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
GROK_API_URL = "https://api.x.ai/v1/chat/completions"
GROK_API_KEY = os.getenv("GROK_API_KEY")

# Content Generation Settings
MAX_TOKENS = 800
TEMPERATURE = 0.7
TWEET_MAX_LENGTH = 280
MAX_TWEETS_PER_THREAD = 10

# Audience Types
AUDIENCE_TYPES = {
    "technical": "Technical audience with cryptography background",
    "general": "General audience interested in technology",
    "developer": "Software developers and system architects",
    "business": "Business decision makers and executives"
}

# Content Categories
CONTENT_CATEGORIES = {
    "technical": 0.4,  # 40% technical deep-dives
    "practical": 0.3,  # 30% practical applications
    "educational": 0.2,  # 20% educational content
    "news": 0.1  # 10% industry news
}

# Logging Configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s" 