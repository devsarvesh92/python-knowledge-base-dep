
from typing import Any, Protocol


class Config(Protocol):
    """
    Defines configuration protocol
    """

    def get(self,key:Any)->Any|None:
        """
        defines protocol
        """

