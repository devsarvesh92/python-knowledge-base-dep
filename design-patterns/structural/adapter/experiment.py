"""
Defines experiment
"""

from typing import Any, Callable, Optional
from adapter.config_adpater import Config


ConfigCallable = Callable[[str],Optional[Any]]
class Experiment:
    """
    Simulates the experiment
    """

    def __init__(self,config_adapter:ConfigCallable) -> None:
        """
        Defines the initialization
        """
        self.config_adapter = config_adapter
    
    def run(self):
        """
        Performs an experiment
        """

        path:str = self.config_adapter('path')
        log:str = self.config_adapter('log')
        space:str = self.config_adapter('space')

        print("[START] Performing experiment")
        print(f"{path=} and {log=} and {space=}")
        print("[END] Performing experiment")
    