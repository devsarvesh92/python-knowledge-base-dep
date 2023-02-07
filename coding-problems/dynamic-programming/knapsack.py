#####################
# 1. DP -> Recurssion -> Memoization -> Top down
# 2. Max profit
# 3. Item -> dataclass
# 4. Base cond -> smallest valid input
# 5. Choice dig
#####################

from dataclasses import dataclass
from functools import lru_cache

@dataclass
class Item:
    val: int
    wt:int


memoize_store = [[-1 for r in range(11)]for r in range(3)]

def zero_one_knapsack(items:list[Item],knapsack_weight:int,index:int)-> int:
    if knapsack_weight == 0 or index < 0:
        return 0

    if memoize_store[index][knapsack_weight] > 0:
        return memoize_store[index][knapsack_weight]
    
    current_item = items[index] 
    if items[index].wt > knapsack_weight:
        memoize_store[index][knapsack_weight] = zero_one_knapsack(items,knapsack_weight,index-1)
        return memoize_store[index][knapsack_weight]
    else:
        memoize_store[index][knapsack_weight] = max(current_item.val+zero_one_knapsack(items,knapsack_weight-current_item.wt,index-1),
        zero_one_knapsack(items,knapsack_weight,index-1)
        )
        return memoize_store[index][knapsack_weight]

        

print(zero_one_knapsack([Item(100,8),Item(100,2),Item(200,8)],10,2))