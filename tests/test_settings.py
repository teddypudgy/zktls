"""Tests for configuration settings"""
import pytest
from src.config import settings

def test_api_configuration():
    """Test API configuration settings"""
    assert hasattr(settings, "GROK_API_URL")
    assert hasattr(settings, "GROK_API_KEY")

def test_content_settings():
    """Test content generation settings"""
    assert settings.MAX_TOKENS > 0
    assert 0 < settings.TEMPERATURE < 1
    assert settings.TWEET_MAX_LENGTH == 280

def test_audience_types():
    """Test audience type configurations"""
    assert "technical" in settings.AUDIENCE_TYPES
    assert "general" in settings.AUDIENCE_TYPES

def test_content_categories():
    """Test content category distributions"""
    categories = settings.CONTENT_CATEGORIES
    assert sum(categories.values()) == 1.0 