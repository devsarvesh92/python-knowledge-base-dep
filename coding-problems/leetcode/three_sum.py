#######################
# Find unique triplets where sum = 0
######################

def threeSum(nums:list[int],target_sum=0)->list[list[int]]:
    """
    1. Sort
    2. Two ptrs
    3. Increment or decrement ptrs
    """
    # Tim sort - > n log n
    nums.sort()
    result = []
    for id,num in enumerate(nums):

        left_ptr = id + 1
        right_ptr = len(nums)-1

        while (left_ptr < right_ptr):
            sum = num+nums[left_ptr]+nums[right_ptr]
            if target_sum == sum:
                res = [num,nums[left_ptr],nums[right_ptr]]
                if res not in result:
                    result.append(res)
                left_ptr+=1
            elif target_sum > sum:
                left_ptr+=1
            elif target_sum < sum:
                right_ptr-=1
    return result

if __name__ == "__main__":
    print(threeSum(nums=[-1,0,1,2,-1,-4]))








