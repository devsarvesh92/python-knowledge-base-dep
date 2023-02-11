#############
# Time complexity -> O(log n)
# Space complexity -> O(1)
############


def binary_iter(nums:list[int],number_to_search:int):
    """Binary search iterative"""

    low = 0
    high = len(nums) - 1

    nums.sort()

    while low<=high:

        middle = high+1//2
        
        if number_to_search == nums[middle]:
            return middle
        
        if number_to_search < nums[middle]:
            high = middle
        else:
            low = middle


def binary_recur(nums:list[int],number_to_search:int,high:int,low:int):
    if high>=low:
        middle = (high+low)//2

        if nums[middle]==number_to_search:
            return middle

        if number_to_search>nums[middle]:
            return binary_recur(nums,number_to_search,high=high,low=middle+1)
        else:
            return binary_recur(nums,number_to_search,high=middle-1,low=low)
            

print(binary_iter(nums=list(range(1,11)),number_to_search=10))
ls = sorted([i for i in range(1,11) if i % 2==0])
print(binary_recur(nums=ls,number_to_search=4,high=len(ls)-1,low=0))
