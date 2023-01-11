"""
Represents Stack
"""
from collections import deque

class Stack:
    """
    Represents Stack
    """
    def __init__(self):
        self.col = deque()

    def push(self,val):
        """
        Push element to stack
        """
        self.col.append(val)
    
    def pop(self):
        """
        Pop element from stack
        """
        return self.col.pop()
    
    def peek(self):
        """
        Get last element from stack without poping
        """
        return self.col[-1]
    
    def is_empty(self):
        """
        Checks if stack is empty
        """
        return len(self.col) == 0

    def size(self):
        """
        Returns length of stack
        """
        return len(self.col)

    def __str__(self) -> str:
        elements = []
        for el in self.col:
            elements.append(str(el))
        
        return " --> ".join(elements)



s = Stack()
s.push(12)
s.push(13)
s.push(14)
s.pop()
print(s.peek())
print(s.is_empty())
print(s)