"""
_RAW DATA CLEAN INTO PROCESSED DATA_
"""

from config import BASE_URL
from logger import logger


def clean_title(product):
    
    title = product['Book Title'] 
    logger.info("Title cleaner started...")
    
    try:
        
        logger.info("Title cleaned successfully")
        
        return title.strip()
        
    except Exception as e:
        logger.error(f"Title cleaner stopped | {e}")
        raise
        
def clean_price(product):
    clean_price = product['Price']
    logger.info("Price cleaner started...")
    
    try:
        
        logger.info("Price cleaned successfully")
        return float(clean_price.replace("Â", "").replace("£", "").strip())
    
    except Exception as e:
        logger.error(f"Cleaning Stopped | {e}")
        raise
    
        
def clean_rating(product):
    clean_rating = product['Rating']
    ratings = ['One' , 'Two' , 'Three' , 'Four' , 'Five']
    
    logger.info("Rating cleaner started...")
    
    try:
        
        if clean_rating.lower().strip() == 'one':
            clean_rating = 1
        elif clean_rating.lower().strip() == 'two':
            clean_rating = 2
        elif clean_rating.lower().strip() == 'three':
            clean_rating = 3
        elif clean_rating.lower().strip() == 'four':
            clean_rating = 4
        elif clean_rating.lower().strip() == 'five':
            clean_rating = 5
        
        logger.info("Rating cleaned successfully")
        return clean_rating

    except Exception as e:
        logger.error(f"Rating cleaner failed | {e}")
        raise
    
    
def clean_availability_status(product):
    clean_status = False
    
    logger.info("Status cleaner started...")
    
    try:
        
        if product["Availability Status"].lower().strip() == "in stock":
            clean_status = True
        
        logger.info("Status cleaned successfully")
        
        return clean_status
    
    except Exception as e:
        logger.error(f"Status cleaner failed | {e}")
        raise
        
def clean_book_link(product):
    
    product_url = product['Links']
    logger.info("product Url cleaner started...")
    
    try:
        logger.info("product Url cleaned successfully")
    
        return product["Links"]
    
    except Exception as e:
        
        logger.error(f"product Url cleaner stopped | {e}")
        raise
        

def clean_image_link(product):
    image_url = product['Images']
    logger.info("Image Url cleaner started...")
    
    try:
        logger.info("Url cleaned successfully")
    
        return BASE_URL+image_url
    
    except Exception as e:
        
        logger.error(f"Image Url cleaner stopped | {e}")
        raise



def clean_extracted_data(products):
    
    clean_data_list = []
    logger.info("Clean data extracting...")
    try: 
        
        for product in products:
        
            clean_data = {
                
            }
        
            clean_data['title'] = clean_title(product)
            clean_data['price'] = clean_price(product)
            clean_data['rating'] = clean_rating(product)
            clean_data['availability status'] = clean_availability_status(product)
            clean_data['book-links'] = clean_book_link(product)
            clean_data['image-link'] = clean_image_link(product)
            
            clean_data_list.append(clean_data)
        
        logger.info("Cleaned Data Extracted successfully !")
        return clean_data_list
    
    except Exception as e:
        logger.error(f"Cleaned Data extraction failed | {e}")
        raise