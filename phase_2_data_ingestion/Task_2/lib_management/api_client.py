import logging
import time
import requests

logging.basicConfig(level=logging.INFO)

class OpenApiClient:
    BASE_URL="https://openlibrary.org"

    def __init__(self,api_limit=1):
        self.api_limit=api_limit                    # seconds between requests

    def _get(self,endpoint,params=None):
        url=f"{self.BASE_URL}{endpoint}"
        try:
            response=requests.get(url,params=params,timeout=10)          # 10 seconds timeout for requests
            response.raise_for_status()
            time.sleep(self.api_limit)
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(e)
            raise e

    def author_search(self,author_name):
        data=self._get(f"/search/authors.json?q={author_name}")           #call private method _get
        if data or "docs" in data or data["docs"]:                        # checking docs is in data which is fetched
            return data["docs"][0]
        return None

    def author_work(self,author_key,limit=10):
        offset=0
        works=[]
        while len(works)<limit:                                           # fetch works until we reach the limit
            data=self._get(f"/authors/{author_key}/works.json?limit=50&offset={offset}")       # fetch 50 works at a time
            if not data or "entries" not in data:
                break
            works.extend(data["entries"])
            if len(works)<50:                                        # if less than 50 works are fetched then break
                break
            offset+=50
        return works[:limit]                                       # return only up to the limit

    def book_detail(self,work_key):
        data=self._get(f"/works/{work_key}/editions.json")
        if data:
            return data["entries"]
        return []