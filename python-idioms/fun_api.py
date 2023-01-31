

import asyncio
import time
import requests as re
from typing import Any



def send_request(url:str):
    resp = re.get(url)
    return resp.json()

async def send_request_async(url:str):
    return await asyncio.to_thread(send_request,url)

async def get_pokemon_details():
    start = time.perf_counter()
    results = await asyncio.gather(*[send_request_async(f"https://pokeapi.co/api/v2/pokemon/1") for _ in range(100)])
    end = time.perf_counter()
    print(f"Time taken to make 100 api calls {end-start} seconds")
    
asyncio.run(get_pokemon_details())

    

    