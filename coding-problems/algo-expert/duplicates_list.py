def get_duplicates(nums:list[int]):
    nums.sort()
    dup_numbers = {}
    for num in nums:
        if num in dup_numbers:
            dup_numbers[num]+=1
        else:
            dup_numbers[num] = 1
    return dup_numbers




if __name__ == '__main__':
    print([{num:val} for num,val in get_duplicates(nums=[1,1,1,2,3,4,5,5]).items() if val >1])
