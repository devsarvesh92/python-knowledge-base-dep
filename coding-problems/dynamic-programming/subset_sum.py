

def subset_sum(nums:list[int],target_sum:int,index:int)->bool:
    """Check if number of arrays are combined to form a subset"""
    
    if index<0:
        return False

    if target_sum == 0:
        return True
    
    if nums[index] > target_sum:
        return subset_sum(nums,target_sum,index-1)
    else:
        return subset_sum(nums,target_sum-nums[index],index-1) or (subset_sum(nums,target_sum,index-1))



if __name__ == '__main__':
    print(subset_sum([3, 34, 4, 12, 5, 2],target_sum=40,index=len([3, 34, 4, 12, 5, 2])-1))
