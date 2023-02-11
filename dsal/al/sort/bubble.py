"""Bubble sort"""


import decimal
from typing import Any


def bubble_sort(*,elements:list[dict[str,Any]],key:str,reverse:bool=False):
    for i in range(len(elements)):
        for j in range(len(elements)-1-i):
            if decimal.Decimal(elements[j][key]) > decimal.Decimal(elements [j+1][key]):
                elements[j],elements[j+1] = elements[j+1],elements[j]
    return elements if not reverse else elements[::-1]
        

print(bubble_sort(elements=[
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ],reverse=True,key='transaction_amount'))
