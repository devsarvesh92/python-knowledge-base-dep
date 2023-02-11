"""
Linked list
head -> [data|ptr_to_next_node]->new->[data|ptr_to_next_node]->None
Insert at beginning -> O(1)
Delete at beginning -> O(1)
Insert at end/middle -> O(n)
Delete at end/middle -> O(n)
Does not require space preallocation
"""

from typing import Any


class Node:
    """
    Node of LinkedList
    """
    def __init__(self,data,next_el) -> None:
        self.data = data
        self.next = next_el

class LinkedList:
    """
    Defines LinkedList
    """
    def __init__(self,data) -> None:
        self.head = Node(data,None)

    def insert_at_beginning(self,data)->None:
        """
        Insert node at the beginning of linked list
        """
        node = Node(data=data,next_el=self.head)
        self.head = node

    def append(self,data)->None:
        """
        Insert node at the end of linked list
        """
        if self.head is None:
            node = Node(data,None)
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None)

    def extend(self,list:list[Any]):
        """
        Appends list at the end
        """
        if self.head is None:
            node = Node(list[0],None)
            self.head = node
            list = list[1:]
        
        for el in list:
            self.append(el)
    
    def insert_at(self,index,element):
        """
        Insert element at index
        """

        if index<0 or index>len(self):
            raise Exception("Invalid index")
        
        if index==0:
            self.insert_at_beginning(element)
            return
        
        if index == len(self):
            self.append(element)
            return

        counter = 0
        itr= self.head
        while itr:
            if counter == (index-1):
                itr.next = Node(element,itr.next.next)
                break
            itr = itr.next
            counter+=1

    def remove_at(self,index):
        """
        Remove element at specified index
        """
        if index<0 or index>=len(self):
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        counter = 0
        while itr:
            if counter == index-1:
                itr.next = itr.next.next
                break

            itr = itr.next
            counter+=1

    def __getitem__(self, index):
        if index<0 or index>=len(self):
            raise Exception("Invalid index")

        itr = self.head
        counter = 0
        while itr:
            if index == counter:
                return itr.data
            itr = itr.next
            counter+=1

    def __len__(self):

        if self.head is None:
            return 0

        itr = self.head
        count=0
        while itr:
            count+=1
            itr = itr.next
        
        return count

    def __str__(self):
        """
        Prints elements of Linked list
        """
        if self.head is None:
            return "No elements are present"

        itr = self.head
        elements = ""
        
        while itr:
            elements+=f"{str(itr.data)} --> "
            itr=itr.next
        return elements

ll = LinkedList(0)
ll.extend([1,3,4,5,6])
ll.insert_at(6,7)
ll.remove_at(4)
print(ll)
print(len(ll))
print(ll[2])