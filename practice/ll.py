from typing import Any


class Node:
    def __init__(self,data,next) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)

class LinkedList:

    def __init__(self,data:Any) -> None:
        self.head = Node(data=data,next=None)

    def insert_element_at_beginning(self,* ,data:Any) -> None:
        """
            Inserting element at beginning happens with O(1) complexity
        """
        head = self.head
        self.head = Node(data=data,next=head)
    
    def append(self,element:Any) -> None:

        if self.head is None:
            self.head = Node(data=element,next=None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next
        
        itr.next = Node(data=element,next=None)

    
    def __str__(self):
        
        ll=""
        itr = self.head

        while itr.next:
            ll += f"{itr.next}->"
            itr = itr.next
        
        ll += f"{itr}"
        return ll


if __name__ == "__main__":
    ll = LinkedList(data='sarvesh')
    ll.append("sawant")
    print(ll)

        

