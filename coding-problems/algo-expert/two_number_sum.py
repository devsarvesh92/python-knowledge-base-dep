def two_number_sum(*, input: list[int], target: int) -> list[int]:
    result = []
    for index, num in enumerate(input):
        for sub in input[index + 1 :]:
            if num + sub == target:
                result.extend([num, sub])
    return result


def two_number_sum_with_ht(input, target):
    result = []
    ht = {i: i for i in input}
    for i in input:
        diff = target - i
        if (pair := ht.get(diff)) and pair != i:
            result.extend([i, pair])
            break
    return result


def two_number_sum_with_ptrs(input, target):
    input.sort()
    left_ptr, right_ptr = 0, len(input) - 1

    while left_ptr != right_ptr:
        tg = input[left_ptr] + input[right_ptr]

        if target == tg:
            return [input[left_ptr], input[right_ptr]]
        elif target > tg:
            left_ptr += 1
        elif target < tg:
            right_ptr += 1


# result = two_number_sum_with_ht(input=[3, 5, -4, 8, 11, 1, -1, 6], target=10)
result = two_number_sum_with_ptrs(input=[3, 5, -4, 8, 11, 1, -1, 6], target=10)
print(result)
