
def non_constructible_change(*,coins:list[int])->int:
    change=0
    sorted_coins = sorted(coins)
    for coin in sorted_coins:
        if (coin-change)>1:
            change+=1
            return change
        change=coin+change
    return change+1


print(non_constructible_change(coins = [5, 7, 1, 1, 2, 3, 22]))