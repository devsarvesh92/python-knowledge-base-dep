from typing import Any
from bs4 import BeautifulSoup

class XMLAdapter:

    def __init__(self,bs:BeautifulSoup) -> None:
        self.bs = bs
    
    def get(self,key:Any)->Any:
        """
        Find key from xml
        """
        if re:= self.bs.find(key):
            return re
        