
import requests
from logger import logger

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
          
    