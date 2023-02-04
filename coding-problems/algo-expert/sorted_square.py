def sortedSquaredArray(array):
    # Write your code here.
    return sorted([num * num for num in array])


def sorted_squared_array_opt(array):
    start = 0
    end = len(array) - 1
    result = [0 for i in array]
    # [-7,-5,-4,3,6,8,9]
    currpos = len(array) - 1
    while end >= start:
        if abs(array[end]) > abs(array[start]):
            result[currpos] = array[end] * array[end]
            end -= 1
        else:
            result[currpos] = array[start] * array[start]
            start += 1
        currpos -= 1
    return result


def sorted_squared_arry_opt_alt(array):
    start = 0
    end = len(array) - 1
    result = [0 for _ in array]

    for i in reversed(range(len(array))):
        if abs(array[start]) > abs(array[end]):
            result[i] = array[start] * array[start]
            start += 1
        else:
            result[i] = array[end] * array[end]
            end -= 1
    return result


print(sorted_squared_arry_opt_alt([-2, -1]))
