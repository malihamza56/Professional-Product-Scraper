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
    
    
def extract_products(soup):
    
    """
    Extract all product containers from the parsed HTML.

    Args:
        soup (BeautifulSoup): Parsed HTML object.

    Returns:
        list: List of product container tags.
    """
    
    logger.info("Products Extraction started...")
    
    try:
        products = soup.select(".product_pod")

        logger.info("Products Container Extracted Succefully")
        
        return products
    
    except Exception as e:
        logger.error(f"Oops ! Extraction Failed | {e}")
        raise

   

def extract_title(product):
    
    """_TITLE EXCTRACTION OF PRODUCT_

    Returns:
        _TITLE TAG_: _GIVES TITLE_
    """

    logger.info("Title Exctracting...")
    try:
        title_tag = product.select_one("a[title]")
        
        logger.info("Title Extracted")
        
        return title_tag.get("title")

    except Exception as e:
        logger.error(f"Title Extraction Failed | {e}")
        raise
   

def extract_price(product):
    
    """_PRICE EXCTRACTION OF PRODUCT_

    Returns:
        _PRICE TAG_: _GIVES PRICE_
    """

    logger.info("Price Exctracting...")
    try:
        price_tag = product.select_one(".price_color")
        
        logger.info("Price Extracted")
        
        return price_tag.text.strip()

    except Exception as e:
        logger.error(f"Price Extraction Failed | {e}")
        raise
   

def extract_rating(product):
    
    """_RATING EXCTRACTION OF PRODUCT_

    Returns:
        _RATING TAG_: _GIVES RATING_
    """

    logger.info("Rating Exctracting...")
    
    try:
        rating_tag = product.select_one(".star-rating")
        
        logger.info("Rating Extracted")
        
        ratings = ("One" , "Two" , "Three" , "Four" , "Five")
        classes = rating_tag.get("class")
        for cls in classes:
            if cls in ratings:
                return  cls

    except Exception as e:
        logger.error(f"Title Extraction Failed | {e}")
        raise
   

def availabilty_status(product):
    
    """_AVAILIBILITY STATUS CHECKING OF PRODUCT_

    Returns:
        _STATUS TAG_: _GIVES STATUS_
    """

    logger.info("Availabilty Status Checking ...")
    
    try:
        availabilty_status_tag = product.select_one(".instock.availability")
        
        logger.info("Availability Status Checked ")
        
        return availabilty_status_tag.text.strip()

    except Exception as e:
        logger.error(f"Availabilty Status Checking Failed | {e}")
        raise
   

def extract_product_links(product):
    
    """_LINK EXCTRACTION OF PRODUCT_

    Returns:
        _LINK TAG_: _GIVES LINK_
    """

    logger.info("Product Link Exctracting...")
    
    try:
        link_tag = product.select_one("a[href]")
        
        logger.info("Product Link Extracted")
        
        return link_tag.get("href")

    except Exception as e:
        logger.error(f"Link Extraction Failed | {e}")
        raise
   

def extract_image_links(product):
    
    """_IMAGE EXCTRACTION OF PRODUCT_

    Returns:
        _IMAGE TAG_: _GIVES IMAGE_
    """

    logger.info("Product Image Exctracting...")
    
    try:
        image_tag = product.select_one("img[src]")
        
        logger.info("Image Extracted")
        
        return image_tag.get("src")

    except Exception as e:
        logger.error(f"Image Extraction Failed | {e}")
        raise


def extract_books_data(products):
    
    """_ALL PRODUCTS DATA EXCTRATION_

    Args:
        products (_LIST_): _A LIST OF ALL THE PRODUCTS_
    """
    
    data_list = []
    
    logger.info("Data extracting...")
    
    try:
        for product in products:
            
            data = {}
            
            data['Book Title'] = extract_title(product) 
            data['Price'] = extract_price(product)
            data['Rating'] = extract_rating(product)
            data['Availability Status'] = availabilty_status(product)
            data['Links'] = extract_product_links(product)
            data['Images'] = extract_image_links(product)
            
            data_list.append(data)
        
        logger.info("Whole Data extracted Successfully")
        
        return data_list
    
    except Exception as e:
        logger.error(f"Error Occured | {e}")
        raise