##############################################################
# Pseudo code
# 1,2,1
# 
# include num or don't include
# dest =3
# 
# 1 -> sum = 2 -> 2 -> sum =0 -> 1 path
# 1 -> sum = 2 -> X -> sum = 2 -> 1 -> sum =1 -> not a path
# 1 -> sum = 2 -> X -> sum = 2 -> 1->X -> sum = 1 -> not a path
# 
# X -> sum = 3 -> 2 -> sum =1 -> 1 ->sum = 0 -> 2nd path
# X -> sum = 3 -> X -> sum=3 -> 1 -> sum = 2 -> not a path
# X -> sum = 3 -> X -> sum=3-> X -> sum = 3 -> not a path
##############################################################

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
