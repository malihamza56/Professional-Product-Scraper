"""_ALL MODULES INTEGRATION_
"""
from logger import logger
from config import BASE_URL , HEADERS , TIMEOUT
from scraper import fetch_all_pages
from cleaner import clean_extracted_data
from exporter import raw_json,processed_json,processed_csv,processed_excel,save_raw_html


def main():
    
    """_RUNNING THE WHOLE WORKFLOW_
    """
    logger.info("Scraper Started...")
    print("Scraper Started...")
    
    try:
        
        save_raw_html()
        #list of products

        books = fetch_all_pages(url=BASE_URL,headers=HEADERS,timeout=TIMEOUT)    #raw books data
        raw_json(books)  #raw json
        
        
        #---------ALL PROCESSED DATA FILES--------
        cleaned_books = clean_extracted_data(books)
        
        processed_json(cleaned_books)
        processed_csv(cleaned_books)
        processed_excel(cleaned_books)
        logger.info("Books Scraper Completed Successfully")
        
        
    except Exception as e:
        logger.error(f"Scraper Failed : {e}")
        print(f"Scraper Failed : {e}")
        
    
if __name__ == "__main__":
    main()


print("Books Scraper Completed Successfully")