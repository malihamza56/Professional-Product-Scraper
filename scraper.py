
import requests
from urllib.parse import urljoin
from logger import logger
import time
from config import MAX_DELAY,MIN_DELAY
import random
from parser import parse_html,extract_products,extract_books_data,extract_next_page


"""
    FETCH HTML FROM A BASE URL
"""
def fetch_html(
    url : str ,
    headers : dict ,
    timeout : int
):
    """
    Fetch HTML content from the given URL.

    Args:
        url (str): Website URL.
        headers (dict): Request headers.
        timeout (int): Maximum waiting time in seconds.

    Returns:
        requests.Response: HTTP response object.
    """

    try :
        logger.info(f"Sending request to URL  {url}...")
        
        response = requests.get(
            url=url,
            headers=headers,
            timeout=timeout
        )
        response.encoding = "utf-8"
        
        response.raise_for_status()
        logger.info("HTML Fetched successfully....")
        
        return response
        
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP Error occured : {e}")
        raise
    
    except requests.exceptions.Timeout as e:
        logger.error(f"Timeout error : {e}")
        raise
    
    except requests.exceptions.ConnectionError as e:
        logger.error(f"Connection error :{e}")
        raise
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Unexpected Error occured : {e}")
        raise
          

def fetch_all_pages(
    url : str,
    headers : dict,
    timeout : int
):
    
    """
    _PAGINATION THROUGH WHOLE WEBSITE_
    """
    
    logger.info("Multi-Pages Fetching Started....")
    
    try:
        
        all_books = []
        current_url = url
        count = 0
        
        while current_url:
            
            logger.info(f"Fetching Page : {current_url}")
            response = fetch_html(url=current_url , headers=headers , timeout=timeout)

            soup = parse_html(response.text)
            
            products = extract_products(soup=soup)
            
            books = extract_books_data(products=products , page_url=response.url)
            
            all_books.extend(books)
            
            logger.info(f"Current URL :{current_url}" )
            
            print("Current URL :", current_url)
            next_page = extract_next_page(soup=soup)
            
            logger.info(f"Next Page :{next_page}" )
            print(f"Next Page :{next_page}")
            
            
            if next_page:
                current_url = urljoin(response.url,next_page)
                print("New URL :", current_url)
                time.sleep(random.uniform(MIN_DELAY,MAX_DELAY))
                count+=20
                print(f"Products : {count}")
                
            else:
                current_url = None
        
                
        logger.info(f"Total Books : {len(all_books)}")     
        logger.info("All Pages Scraped Successfully !")
        return all_books    
            
    except Exception as e:
        logger.error(f"Pagination Failed | {e}")
        raise
        
        