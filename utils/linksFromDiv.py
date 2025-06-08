import requests
from typing import List
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_urls_within_el(url: str, selector: str) -> List[str]:
    """Fetches a webpage and extracts URLs from a specific div by selector.

    Args:
        url: The URL of the website
        selector: The CSS selector to extract links from
    
    Returns:
        List of URLs found in the specified element. If no element is found, returns an empty list.
    
    Raises:
        ValueError: If there's an error fetching the page or parsing the HTML
    
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        el = soup.select_one(selector)

        if not el:
            return []

        links = el.find_all('a', href=True)

        # loop over links and parse each using urllib.parse
        # this ensures that relative URLs are converted to absolute URLs
        # and that the URLs are properly encoded
        # also, we ensure that the URLs are unique by using a set
        if not links:
            return []   
        urls = set()
        for link in links:
            href = link['href']
            url = urlparse(href)
            # If the URL is relative, convert it to absolute using the base URL
            if not url.scheme:
                url = urljoin(response.url, href)
            urls.add(url)

        return urls

    except requests.RequestException as e:
        raise ValueError(f"Failed to fetch page: {str(e)}")
    except Exception as e:
        raise ValueError(f"Unexpected error processing page: {str(e)}")