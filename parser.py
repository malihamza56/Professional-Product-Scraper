"""
_PARSED HTML AND SCRAP THE PRODUCTS DATA_ 
"""

from logger import logger
from bs4 import BeautifulSoup


def parse_html(html : str):
    
    """_PARSE RESPONSE CONTENT AND RETURNS A BEAUTIFUL SOUP
    OBJECT DONE WITH EXCEPTION HANDLING_

    Returns:
        _OBJECT_: _BEAUTIFUL SOUP_
    """
    
    logger.info("Parsing Start...")
    
    try:
        soup = BeautifulSoup(html , "html.parser")
        logger.info("Parsing Completed !")
        
        return soup
    
    except Exception as e :
        logger.error(f"An Error Occured : {e}")
        raise
    
    