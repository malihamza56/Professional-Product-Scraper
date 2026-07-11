"""
_EXPORTER WHERE ALL DATA (PROCESSED & RAW) EXPORT TO FILES_
"""

from logger import logger

import pandas as pd

"""
_RAW DATA TO JSON_
"""

def raw_json(raw_data):
    
    logger.info("Raw data moving...")
    
    try:
        
        df = pd.DataFrame(raw_data)
        
        df.to_json("Data/raw/raw_books.json" , orient="records" , index=False)
        logger.info("Raw Data moved successful")
        
    except Exception as e:
        logger.error(f"Raw data unsuccessfull | {e}")
        raise
"""
PROCESSED DATA TO JSON
"""

def processed_json(processed_data):
    
    logger.info("Processed data moving to json...")
    try:
        
        df = pd.DataFrame(processed_data)
        
        df.to_json("Data/processed/books.json" , orient="records" , index=False , force_ascii=False , indent=4)
        
        logger.info("Processed Data moved to json successfuly")
    
    except Exception as e:
       logger.error(f"Data processing unsuccessfull | {e}")
       raise

"""
PROCESSED DATA TO CSV
"""
def processed_csv(processed_data):
    
    logger.info("Processed data moving to csv...")
    
    try:
        
        df = pd.DataFrame(processed_data)
        df.to_csv("Data/processed/books.csv" ,index=False)
        
        logger.info("Processed Data moved to csv successfuly")
        
    except Exception as e:
       logger.error(f"Data processing unsuccessfull | {e}")
       raise
"""
PROCESSED DATA TO EXCEL
""" 
def processed_excel(processed_data):
    
    
    logger.info("Processed data moving to Excel...")
    
    try:
        
        df = pd.DataFrame(processed_data)
        df.to_excel("Data/processed/books.xlsx" ,index=False)
        
        logger.info("Processed Data moved to Excel successfuly")
    
    except Exception as e:
       logger.error(f"Data processing unsuccessfull | {e}")
       raise