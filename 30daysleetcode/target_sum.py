def target_sum_three(*,nums:list[int],target_sum:int):
    """
    https://www.youtube.com/watch?v=6qgC-dqKElA&list=PLYAlGR1wWgUUyYZ3wX2GdnhiL-QVhAXfR&index=1
    3 Sum
    """
    result = []
    # sort numbers
    nums.sort()

    for i in range(len(nums)-2):
        current_num = nums[i]
        left_ptr = nums[i+1]
        right_ptr = len(nums)-1

        while left_ptr < right_ptr:
            current_sum = current_num + nums[left_ptr] + nums[right_ptr]
            if current_sum == target_sum:
                if len(set([current_num,nums[left_ptr],nums[right_ptr]]))==3:
                    result.append([current_num,nums[left_ptr],nums[right_ptr]])
                left_ptr+=1
                right_ptr-=1
            elif current_num < target_sum:
                left_ptr+=1
            else:
                right_ptr-=1
    return result

if __name__ == "__main__":
    print(target_sum_three(nums=[-4,-1,-1,0,1,2],target_sum=0))


