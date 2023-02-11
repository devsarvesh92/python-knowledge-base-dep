##################
# Time complexity -> O(n)
# Space -> O(1)
##################

def linear(nums:list[int],number_to_search:int):
    for index,num in enumerate(nums):
        if num == number_to_search:
            return index
    return -1



print(linear(nums=list(range(1,11)),number_to_search=10))

