#####################
# 1. DP -> Topdown
# 2. Without recurssion
# 2. Max profit
# 3. Item -> dataclass
# 4. Base cond -> smallest valid input
# 5. Choice dig
#####################


from dataclasses import dataclass


@dataclass
class Item:
    val: int
    wt:int


def max_profit_knapsack(items:list[Item],knapsack_weight:int):

    tdm = [[0 for _ in range(knapsack_weight+1)] for _ in range(len(items)+1)]
    
    for it in range(len(items)+1):
        for wt in range(len(knapsack_weight+1)):
            if it == 0 or wt == 0:
                tdm[it][wt] = 0
            elif items[it-1].wt <= wt:
                items[it][wt] = max(items[it-1].val + tdm[it-1][wt-items[it-1].wt], tdm[it-1][wt])
    

print(max_profit_knapsack([Item(100,1),Item(100,1),Item(200,3)],10))

