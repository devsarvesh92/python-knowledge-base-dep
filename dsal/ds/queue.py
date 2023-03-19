from collections import deque

class Queue:
    """
    Creates Queue
    """

    def __init__(self) -> None:
        self.col = deque()

    def enque(self,val):
        self.col.appendleft(val)
    
    def deque(self):
        self.col.pop()

    def __len__(self):
        return self.col.__len__()

    def __str__(self) -> str:
        elements = ""
        for el in self.col:
           elements += f"{el} --> "
        
        return elements

q = Queue()
q.enque(10)
q.enque(11)
q.enque(12)
print(q)
q.deque()

print(q)