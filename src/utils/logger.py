"""Logging configuration for the zkTLS Twitter AI Agent"""

import logging
import sys
from typing import Optional
from ..config.settings import LOG_LEVEL, LOG_FORMAT

def setup_logger(name: str, level: Optional[str] = None) -> logging.Logger:
    """
    Set up a logger with the specified configuration
    
    Args:
        name: Logger name
        level: Optional logging level override
        
    Returns:
        Configured logger instance
    """
    # Create logger
    logger = logging.getLogger(name)
    
    # Set level
    logger.setLevel(level or LOG_LEVEL)
    
    # Create console handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    
    # Create formatter
    formatter = logging.Formatter(LOG_FORMAT)
    handler.setFormatter(formatter)
    
    # Add handler to logger
    logger.addHandler(handler)
    
    return logger 