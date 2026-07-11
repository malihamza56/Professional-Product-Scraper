"""_ALL MODULES INTEGRATION_
"""

from config import BASE_URL , TIMEOUT , HEADERS
from scraper import fetch_html
from parser import parse_html,extract_products,extract_books_data
import json

def main():
    
    """_RUNNING THE WHOLE WORKFLOW_
    """
    try:
        response = fetch_html(url=BASE_URL , headers=HEADERS , timeout=TIMEOUT)
        
        with open("Data/raw/books.html" , 'w' , encoding="utf-8") as f:
            f.write(response.text)
        
        
        soup = parse_html(response.text)
        
        products = extract_products(soup=soup)

        books = extract_books_data(products)
        
        with open("Data/raw/raw_books.json" , 'w' , encoding="utf-8") as f:
            json.dump(books,f)
        
        
    except Exception as e:
        print(f"Scraper Failed : {e}")
        
        
if __name__ == "__main__":
    main()
    