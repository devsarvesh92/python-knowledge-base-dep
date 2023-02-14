


def min_subset_sum(nums:list[int],current_sum:int,index:int,total_sum:int):
    if index==0:
        return abs((total_sum-current_sum)-current_sum)
    
    return min(min_subset_sum(nums,current_sum+nums[index-1],index-1,total_sum),min_subset_sum(nums,current_sum,index-1,total_sum))


if __name__ == '__main__':
    nums = [1,6,11,5]
    total = sum(nums)
    print(min_subset_sum(nums,0,len(nums),total))
