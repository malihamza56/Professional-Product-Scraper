"""_ALL MODULES INTEGRATION_
"""
from logger import logger
from config import BASE_URL , TIMEOUT , HEADERS
from scraper import fetch_html
from parser import parse_html,extract_products,extract_books_data
from cleaner import clean_extracted_data
from exporter import raw_json,processed_json,processed_csv,processed_excel
import time


def main():
    
    """_RUNNING THE WHOLE WORKFLOW_
    """
    logger.info("Scraper Started...")
    print("Scraper Started...")
    
    try:
        response = fetch_html(url=BASE_URL , headers=HEADERS , timeout=TIMEOUT)
        
        with open("Data/raw/books.html" , 'w' , encoding="utf-8") as f:
            f.write(response.text)
        
        
        soup = parse_html(response.text)         
        
        products = extract_products(soup=soup)   #list of products

        books = extract_books_data(products)    #raw books data
        raw_json(books)    #raw json
        
        
        #---------ALL PROCESSED DATA FILES--------
        cleaned_books = clean_extracted_data(books)
        
        processed_json(cleaned_books)
        processed_csv(cleaned_books)
        processed_excel(cleaned_books)
        
    except Exception as e:
        logger.error(f"Scraper Failed : {e}")
        print(f"Scraper Failed : {e}")
        
    
if __name__ == "__main__":
    main()

logger.info("Books Scraper Completed Successfully")
print("Books Scraper Completed Successfully")