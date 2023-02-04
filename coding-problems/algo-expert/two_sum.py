def twoSum(nums: list[int], target: int) -> list[int]:
    for id,num in enumerate(nums):
        if id < len(nums)-1:
            for nxt_num in enumerate(nums[id:]):
                if num+nxt_num==target:
                    return(id,nums.index(nxt_num))


print(twoSum(nums=[2,7,11,15],target=9))