from typing import List, Dict
import logging
import os
import requests
from datetime import datetime

class ZkTLSAgent:
    """
    An autonomous AI agent for zkTLS technology education and promotion
    """
    def __init__(self):
        """Initialize the zkTLS Agent"""
        # Set up API configuration
        self.grok_api_key = os.getenv("GROK_API_KEY")
        self.grok_api_url = "https://api.x.ai/v1/chat/completions"
        
        # Set up logging
        self.logger = logging.getLogger(__name__)
        
        # Load prompts
        self.prompts = self._load_prompts()
        
    def generate_content(self, topic: str, audience_type: str = "technical") -> List[str]:
        """
        Generate content about zkTLS
        
        Args:
            topic: The specific topic to discuss
            audience_type: Target audience type ("technical" or "general")
            
        Returns:
            List of tweets forming a thread
        """
        try:
            # Select appropriate prompt based on audience
            system_prompt = self.prompts[audience_type]
            
            # Prepare API request
            headers = {
                "Authorization": f"Bearer {self.grok_api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": "grok-2",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": topic}
                ],
                "temperature": 0.7,
                "max_tokens": 800
            }
            
            # Make API call
            response = requests.post(
                self.grok_api_url,
                headers=headers,
                json=data,
                timeout=30
            )
            
            response.raise_for_status()
            
            # Process response
            content = response.json()["choices"][0]["message"]["content"]
            return self._split_into_tweets(content)
            
        except Exception as e:
            self.logger.error(f"Error generating content: {str(e)}")
            raise
            
    def _load_prompts(self) -> Dict[str, str]:
        """Load system prompts for different audience types"""
        from .prompts import TECHNICAL_PROMPT, GENERAL_PROMPT
        return {
            "technical": TECHNICAL_PROMPT,
            "general": GENERAL_PROMPT
        }
        
    def _split_into_tweets(self, content: str) -> List[str]:
        """Split content into tweet-sized chunks"""
        tweets = []
        current_tweet = ""
        
        for line in content.split('\n'):
            if len(current_tweet + line) <= 280:
                current_tweet += line + '\n'
            else:
                tweets.append(current_tweet.strip())
                current_tweet = line + '\n'
        
        if current_tweet:
            tweets.append(current_tweet.strip())
            
        return tweets 