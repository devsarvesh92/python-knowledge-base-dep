

def fib_gen(count:int):

    a,b = 1,0
    for _ in range(count):
        a,b = b,a+b
        yield b


for i in fib_gen(10):
    print(i)