import requests
import time
import logging
from typing import Optional, Dict, Any, List

logging.basicConfig(level=logging.INFO)

class OpenLibraryClient:
    BASE_URL = "https://openlibrary.org"

    def __init__(self, rate_limit= 1):
        self.rate_limit = rate_limit                                       # seconds between requests

    def _get(self, endpoint, params = None):
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            time.sleep(self.rate_limit)                                     # rate limiting
            return response.json()
        except requests.RequestException as e:
            logging.error(f"API request failed: {e}")
            return None

    def search_authors(self, author_name):
        data = self._get("/search/authors.json", params={"q": author_name})  # search the author name
        if data and "docs" in data and data["docs"]:
            return data["docs"][0]                                           # returning first match
        return None

    def fetch_works(self, author_key, limit=10):
        offset = 0
        works = []
        while len(works) < limit:
            data = self._get(f"/authors/{author_key}/works.json", {"limit": 50, "offset": offset})
            if not data or "entries" not in data:
                break
            works.extend(data["entries"])
            if len(data["entries"]) < 50:
                break
            offset += 50
        return works[:limit]

    def fetch_book_details(self, work_key):
        data=self._get(f"/works/{work_key}.json")                           # fetch detailed book information.
        return data