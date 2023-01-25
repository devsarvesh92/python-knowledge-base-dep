import logging
from time import perf_counter

logging.basicConfig(
    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s',
                    handlers=[logging.FileHandler("my_log.log", mode='w')]
)

logger = logging.getLogger()

def timer(fn):
    def wrapper(*args,**kwargs):
        t1_start = perf_counter()
        result = fn(*args,**kwargs)
        t1_stop = perf_counter()
        logger.info(f"Time taken to for {fn.__name__} execute in seconds is {t1_stop-t1_start}")
        return result
    return wrapper



@timer
def add(a,b):
    return a+b

print(add(2,3))
