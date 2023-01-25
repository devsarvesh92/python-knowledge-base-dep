##
# generator 
##
def even_number_gen():
    number = 1
    while True:
        if number % 2 ==0:
            yield number
        number+=1

##
# generator expression
##
even_number_gen_exp = (x for x in range(1,100) if x % 2==0)

##
# generator pipelines
##
def even_filter(nums):
    for num in nums:
        if num%2==0:
            yield num

def multiply_by_three(nums):
    for num in nums:
        yield num * 3

def print_num(nums):
    for num in nums:
        yield f"Welcome to number gen {num}"

nums = [i for i in range(1,11)]
pipeline = print_num(multiply_by_three(even_filter(nums)))

print(type(pipeline))

while True:
    try:
        print(next(pipeline))
    except StopIteration:
        break


###
# Will write something more practical soon :P
###


