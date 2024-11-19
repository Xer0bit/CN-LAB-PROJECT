import logging
import sys
from datetime import datetime
import os

def setup_logger(name):
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create handlers with proper encoding for Windows
    c_handler = logging.StreamHandler(sys.stdout)
    
    # Ensure logs directory exists
    os.makedirs('logs', exist_ok=True)
    
    # Use utf-8 encoding for file handler
    f_handler = logging.FileHandler(
        f'logs/{name}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log',
        encoding='utf-8'
    )
    
    # Different formatters for console (with emoji) and file (without emoji)
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Custom filter to remove emojis from file logs
    class EmojiFilter(logging.Filter):
        def filter(self, record):
            # Remove emoji characters from log messages for file handler
            record.msg = record.msg.encode('ascii', 'ignore').decode('ascii')
            return True

    # Add filter to file handler
    f_handler.addFilter(EmojiFilter())
    
    # Add formatters to handlers
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger