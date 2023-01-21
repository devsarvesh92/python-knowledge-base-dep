"""
Defines experiment
"""

from typing import Any
from adapter.config_adpater import Config

class Experiment:
    """
    Simulates the experiment
    """

    def __init__(self,config:Config) -> None:
        """
        Defines the initialization
        """
        self.config = config
    
    def run(self):
        """
        Performs an experiment
        """

        path:str = self.config.get('path')
        log:str = self.config.get('log')
        space:str = self.config.get('space')

        print("[START] Performing experiment")
        print(f"{path=} and {log=} and {space=}")
        print("[END] Performing experiment")
    