from binary_search_tree import build_tree,BinarySearchTree


def find_closest_in_bst(*,tree:BinarySearchTree,target:int):
    return find_closest_in_bst_recur(tree=tree,target=target,closest=float('inf'))


def find_closest_in_bst_recur(*,tree:BinarySearchTree,target:int,closest:int)->int:
    if target == tree.val:
        return target
    
    if target < tree.val:
        if tree.left:
            closest = tree.left.val if abs(target - tree.left.val) < abs(target-closest) else closest
            return find_closest_in_bst_recur(tree=tree.left,target=target,closest=closest)
        else: 
            return closest
    
    if target > tree.val:
        if tree.right:
            closest = tree.right.val if abs(target - tree.right.val) < abs(target-closest) else closest
            return find_closest_in_bst_recur(tree=tree.right,target=target,closest=closest)
        else: 
            return closest
    



if __name__ == '__main__':
    numbers = [100,502,55000,1001,4500,204,205,207,208,206,203,5,15, 22, 57, 60, 3,2,3,1,-1,-2,-3,-4,-51,-403]
    tree = build_tree(numbers=numbers)
    print(find_closest_in_bst(tree=tree,target=4500))
    