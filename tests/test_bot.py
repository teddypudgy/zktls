"""Tests for the zkTLS Twitter AI Agent"""

import pytest
from src.agent.bot import ZkTLSAgent
from unittest.mock import patch, MagicMock

@pytest.fixture
def agent():
    """Create a test instance of ZkTLSAgent"""
    return ZkTLSAgent()

def test_init(agent):
    """Test agent initialization"""
    assert agent.grok_api_url is not None
    assert hasattr(agent, 'prompts')

@patch('requests.post')
def test_generate_content(mock_post, agent):
    """Test content generation"""
    # Mock response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "choices": [{
            "message": {
                "content": "Test tweet content\nSecond line"
            }
        }]
    }
    mock_post.return_value = mock_response
    
    # Test content generation
    tweets = agent.generate_content(
        topic="Test topic",
        audience_type="technical"
    )
    
    assert isinstance(tweets, list)
    assert len(tweets) > 0
    assert all(len(tweet) <= 280 for tweet in tweets)

def test_split_into_tweets(agent):
    """Test tweet splitting functionality"""
    content = "Short tweet"
    tweets = agent._split_into_tweets(content)
    assert len(tweets) == 1
    assert tweets[0] == "Short tweet"
    
    # Test long content splitting
    long_content = "x" * 300
    tweets = agent._split_into_tweets(long_content)
    assert len(tweets) > 1
    assert all(len(tweet) <= 280 for tweet in tweets) 