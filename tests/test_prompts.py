"""Tests for prompt management"""
import pytest
from src.agent.prompts import TECHNICAL_PROMPT, GENERAL_PROMPT

def test_technical_prompt_content():
    """Test technical prompt structure and content"""
    assert "zkTLS" in TECHNICAL_PROMPT
    assert "technical" in TECHNICAL_PROMPT.lower()
    assert "280 characters" in TECHNICAL_PROMPT

def test_general_prompt_content():
    """Test general prompt structure and content"""
    assert "zkTLS" in GENERAL_PROMPT
    assert "clear" in GENERAL_PROMPT.lower()
    assert "280 characters" in GENERAL_PROMPT

def test_prompt_differences():
    """Test that prompts are distinct"""
    assert TECHNICAL_PROMPT != GENERAL_PROMPT
    assert len(TECHNICAL_PROMPT) > 0
    assert len(GENERAL_PROMPT) > 0 