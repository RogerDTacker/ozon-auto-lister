"""
Configuration module for Ozon Auto Lister
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent

# Pinduoduo Configuration
PINDUODUO_CONFIG = {
    'base_url': os.getenv('PINDUODUO_BASE_URL', 'https://www.pinduoduo.com'),
    'timeout': int(os.getenv('PINDUODUO_TIMEOUT', 30)),
}

# Ozon Configuration
OZON_CONFIG = {
    'api_key': os.getenv('OZON_API_KEY'),
    'client_id': os.getenv('OZON_CLIENT_ID'),
    'base_url': os.getenv('OZON_BASE_URL', 'https://api.ozon.ru'),
}

# Database Configuration
DATABASE_CONFIG = {
    'type': os.getenv('DATABASE_TYPE', 'sqlite'),
    'path': os.getenv('DATABASE_PATH', './data/products.db'),
}

# Logging Configuration
LOGGING_CONFIG = {
    'level': os.getenv('LOG_LEVEL', 'INFO'),
    'file': os.getenv('LOG_FILE', './logs/app.log'),
}

# Scraper Configuration
SCRAPER_CONFIG = {
    'delay': float(os.getenv('SCRAPER_DELAY', 2)),
    'max_retries': int(os.getenv('SCRAPER_MAX_RETRIES', 3)),
    'headless': os.getenv('SCRAPER_HEADLESS', 'true').lower() == 'true',
}

# Upload Configuration
UPLOAD_CONFIG = {
    'batch_size': int(os.getenv('BATCH_SIZE', 10)),
    'auto_upload': os.getenv('AUTO_UPLOAD', 'false').lower() == 'true',
}

# Ensure required directories exist
LOGS_DIR = PROJECT_ROOT / 'logs'
DATA_DIR = PROJECT_ROOT / 'data'

LOGS_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)
