"""
Finds a number from infinitely large sequence

Approach:
1. MAX_SIZE = OS bits
2. derive_upper_and_lower_bounds -> determines the range where number lies
3. Once the bounds are finalized we will do binary search in that range
"""

import platform


MAX_SIZE = int(platform.architecture()[0][:2])

def guess_number(number)->bool:
    """
    This is esentially a api call
    """
    number_in_mind:int = 25
    if number <= number_in_mind:
        return True
    else:
        return False
    


def derive_upper_and_lower_bounds(*,lower,upper)->tuple[int,int]:
    """

    # if guess number True -> middle to upper
    # if guess number False -> lower to middle

    """
    middle = (lower + upper) //2
    number = pow(2,middle)

    if upper-lower==1:
        return (pow(2,lower),pow(2,upper))

    if guess_number(number):
        return derive_upper_and_lower_bounds(lower=middle,upper=upper)
    else:
        return derive_upper_and_lower_bounds(lower=lower,upper=middle)

    
def find_number_in_range(lower,upper):
    middle = (lower+upper)//2
    result = guess_number(middle)

    if result and (upper-lower==1):
        return middle

    if result:
         # number is greater than or equal to middle
         return find_number_in_range(middle,upper)
    else:
        # number is less than or equal to middle
        return find_number_in_range(lower,middle)

def find_number():
    # Time complexity -> log(n)
    # Space complexity ->  As using recurrsion -> O(n)
    bounds = derive_upper_and_lower_bounds(lower=0,upper=MAX_SIZE) 

    # Time complexity -> log(n)
    # Space complexity ->  As using recurrsion -> O(n)
    print(find_number_in_range(lower=bounds[0],upper=bounds[1]))

    ## Total complexity ->  
    # O(log n) + O(log n) = O(2 log n).
    # we can simplify this further by using the rule of logarithms that states that log a + log b = log(ab)
    # O(log n * log n) = O((log n)^2).
    # i.e total time complexity ->  O((log n)^2)


if __name__ == "__main__":
    find_number()





