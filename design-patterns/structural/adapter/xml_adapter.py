

from typing import Any, Optional

import bs4


def get(bs:bs4,key:Any)->Optional[Any]:
    """
    Find key from xml
    """
    if re:= bs.find(key):
        return re