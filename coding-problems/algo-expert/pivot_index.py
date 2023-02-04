def find_pivot_index(nums):
    equality_check = lambda expected,actual : True if expected==actual else False
    for id,num in enumerate(nums):
        if id == 0:
            expected_sum = 0
            acutal_sum = sum(nums[id+1:])
            if equality_check(expected=expected_sum,actual=acutal_sum):
                return id
        elif id==len(nums)-1:
            expected_sum = 0
            acutal_sum = sum(nums[:id])
            if equality_check(expected=expected_sum,actual=acutal_sum):
                return id
        else:
            l_sum = sum(nums[:id])
            r_sum = sum(nums[id+1:])
            if equality_check(expected=l_sum,actual=r_sum):
                return id
    
    return -1





if __name__ == '__main__':
    print(find_pivot_index([2,1,-1]))