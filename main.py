"""_ALL MODULES INTEGRATION_
"""

from config import BASE_URL , TIMEOUT , HEADERS
from scraper import fetch_html
from parser import parse_html


def main():
    
    """_RUNNING THE WHOLE WORKFLOW_
    """
    try:
        response = fetch_html(url=BASE_URL , headers=HEADERS , timeout=TIMEOUT)
        
        soup = parse_html(response.text)
        
        with open("Data/raw/books.html" , 'w' , encoding="utf-8") as f:
            f.write(response.text)
        
    except Exception as e:
        print(f"Scraper Failed : {e}")
        
        

if __name__ == "__main__":
    main()
    