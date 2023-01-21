import json
import os

from bs4 import BeautifulSoup

from adapter.experiment import Experiment
from adapter.xml_adapter import XMLAdapter


if __name__ == '__main__':
    print(os.path.dirname(__file__))
    with open(f'{os.path.dirname(__file__)}/config.xml','r') as f:
        soup = BeautifulSoup(f, 'xml')
        adapter = XMLAdapter(bs=soup)
        Experiment(config=adapter).run()