"""
LOGGING CONFIGURATION
"""

import logging

logging.basicConfig(
    filename= "logs/scraper.log",
    level= logging.INFO,
    format= "%(asctime)s - %(filename)s -  %(levelname)s - %(message)s ",
    filemode='a'
)


logger = logging.getLogger(__name__)

