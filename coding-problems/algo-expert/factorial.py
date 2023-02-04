from functools import lru_cache

@lru_cache
def calc_factorial(number:int):
    if number == 0 or number ==1:
        return 1
    return number * calc_factorial(number - 1)


print(calc_factorial(3))