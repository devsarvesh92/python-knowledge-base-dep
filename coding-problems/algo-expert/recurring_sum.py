def running_sum(nums:list[int]):
    run_sum = []
    for id,num in enumerate(nums):
        if run_sum:
            run_sum.append(run_sum[id-1]+num)
        else:
            run_sum.append(num)
    return run_sum


print(running_sum([1,2,3,4]))