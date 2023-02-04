from binary_search_tree import build_tree

current_sum = 0

def branch_sums(root):
    sums = []
    branch_sum_recur(root,0,sums)
    return sums

def branch_sum_recur(root,current_sum,sums):
    
    if root.left:
        current_sum+=root.val
        branch_sum_recur(root.left,current_sum,sums)

    if root.right:
        current_sum+=root.val
        branch_sum_recur(root.right,current_sum,sums)

    if root.right is None and root.left is None:
        current_sum+=root.val
        sums.append(current_sum)
        return


    
if __name__ == '__main__':
    numbers = [1,2,3,4,5,6,7,8,9,10]
    tree = build_tree(numbers=numbers)
    print(branch_sums(tree))
    
