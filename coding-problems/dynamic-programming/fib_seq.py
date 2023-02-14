
dp = {}
def fib(seq:int):
    if seq==0 or seq==1:
        return seq
    if seq in dp:
        print(f"{seq}:{dp[seq]}")
        return dp[seq]
    dp[seq]=fib(seq-1)+ fib(seq-2)
    return dp[seq] 

print(fib(5))