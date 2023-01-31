def seq(end:int):
    for num in range(1,end):
        yield num

def square(nums:list[int]):
     for num in nums:
        yield num*num
    
def pipeline(nums):
    yield from nums

for num in pipeline(square(seq(100))):
    print(num)

