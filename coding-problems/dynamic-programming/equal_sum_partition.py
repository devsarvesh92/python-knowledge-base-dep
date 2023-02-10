


def equal_sum_partition(nums:list[int],sum:int,index:int):
    
    if index < 0:
        return False

    if sum == 0:
        return True

    if nums[index] > sum:
        return equal_sum_partition(nums,sum,index-1)
    else:
        return equal_sum_partition(nums,sum-nums[index-1],index-1) or equal_sum_partition(nums,sum,index-1)

if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    if sum(nums)%2==0:
        print(equal_sum_partition(nums=nums,sum=sum(nums)/2,index=len(nums)-1))
    else:
        print("Equal sum partiion not possible")