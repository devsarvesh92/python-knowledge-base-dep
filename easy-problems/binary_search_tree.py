# Binary search tree
# Time complexity for search and insert O(log n)
# Space complexity O(n) if done by recurssion
# Left side is has value less than current node value
# Right side has value more than current value
# Every Node in a tree is subtree

class BinarySearchTree:
    """
    Binary Search Tree
    """

    def __init__(self,val:int) -> None:
        self.val = val
        self.left = None
        self.right = None

    def insert(self,val)->None:
        """
        Insert value in binary search tree
        """

        if val == self.val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BinarySearchTree(val=val)

        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BinarySearchTree(val=val)

    def search(self,val):
        """
        Search with inorder traversal
        traverse left, node, right
        """
        if val == self.val:
            return True
        
        if val < self.val:
            if self.left:
                return self.left.search(val=val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val=val)
            else:
                return False

    def traverse(self):
        """
        Traverse using Inorder -> Left, Self, Right
        """
        elements = []
        if self.left:
            elements.extend(self.left.traverse())

        elements.append(self.val)

        if self.right:
            elements.extend(self.right.traverse())

        return elements



def build_tree(numbers):
    """
    Build tree
    """
    root = BinarySearchTree(numbers[0])
    for num in numbers[1:]:
        root.insert(num)
    return root


if __name__ == '__main__':
    numbers = [17,4,5,6,23,38,18,4]
    tree = build_tree(numbers=numbers)
    print(tree.search(4))
    print(tree.traverse())