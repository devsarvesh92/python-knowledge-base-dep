

def count_subset_sum(nums:list[int],sum:int,index:int,count:int):
    """
    Count subset sum
    """
    
    if sum==0:
        count+=1
        return count
    
    if index==0:
        return count
    
    if nums[index-1]>sum:
        return count_subset_sum(nums,sum,index-1,count)
    else:
        count = count_subset_sum(nums,sum-nums[index-1],index-1,count)
        count = count_subset_sum(nums,sum,index-1,count)
        return count




print(count_subset_sum([3, 34, 4, 12, 5, 2],sum=7,index=len([3, 34, 4, 12, 5, 2]),count=0))
