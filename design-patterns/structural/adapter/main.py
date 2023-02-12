import json
import os
from functools import partial

from adapter.experiment import Experiment
from adapter.xml_adapter import get
from bs4 import BeautifulSoup

if __name__ == '__main__':
    print(os.path.dirname(__file__))
    with open(f'{os.path.dirname(__file__)}/config.xml','r') as f:
        soup = BeautifulSoup(f, 'xml')
        adapter = partial(get,soup)
        Experiment(config_adapter=adapter).run()