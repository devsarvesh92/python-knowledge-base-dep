# https://youtu.be/xDEuM5qa0zg
# leetcode: https://leetcode.com/problems/lfu-cache/
# LRU Cache
# Solve in O(1) time complexity
# dict -> cache and tail pointer linked list for maintaining order

import gc
from typing import Any


class Node:
    def __init__(self,data,next_el,prev_el) -> None:
        self.data = data
        self.next_el = next_el
        self.prev_el = prev_el

    def __str__(self) -> str:
        return f"{self.data}"

class DoublyLinkedList:

    """Linked list"""

    def __init__(self,data) -> None:
        node = Node(data=data,next_el=None,prev_el=None)
        self.head = node
        self.tail = node

    def insert_at_beginning(self,data:Any):
        """
         head -> node -> ... last_node<- tail
         head-> new_node -> node.... last_node <- tail
        """
        node = Node(data=data,next_el=None,prev_el=None)
        if self.head is not None:
            node.next_el = self.head
            self.prev_el = None
            self.head.prev_el = node
        else:
            node.next_el = None
            node.prev_el = None
            self.tail = node
        
        self.head = node
        return node
    
    def remove_from_end(self):
        """remove from end"""
        last_element = self.tail
        second_last_element = last_element.prev_el


        self.tail = second_last_element
        second_last_element.next_el = None

        last_element = None

        del last_element

        gc.collect()


    def remove_element(self,node:Node):
        """ Remove node from linked list"""
        
        prev_node = node.prev_el
        next_node = node.next_el

        if prev_node:
            prev_node.next_el = next_node
        else:
            self.head = next_node
        
        if next_node:
            next_node.prev_el = prev_node
        else:
            self.tail = prev_node
            
        del node

        gc.collect()

    def __str__(self) -> str:
        el = self.head
        elments = []
        elments.append(str(el))

        while el.next_el:
            elments.append(str(el.next_el))
            el = el.next_el
        
        return "->".join(elments)


class LRUCache:

    def __init__(self,capacity:int) -> None:
        self.capacity = capacity
        self.storage = {}

    def set(self,key,value):

        if len(self.storage.keys())==0:
            self.index = DoublyLinkedList(data=value)
            self.storage[key] = self.index.head
        elif len(self.storage.keys()) < self.capacity:
            node = self.index.insert_at_beginning(value)
            self.storage[key] = node
        else:
            self.remove_lfu_element()
            node = self.index.insert_at_beginning(value)
            self.storage[key] = node
            
    def get(self,key):
        result = -1
        if res:=self.storage.get(key):
            result = res.data
            self.index.insert_at_beginning(data=result)
            self.index.remove_element(res)
        return result


    def remove_lfu_element(self):
        self.index.remove_from_end()


if __name__ == "__main__":
    lru_cache = LRUCache(3)

    lru_cache.set("a","a")
    lru_cache.set("b","b")
    lru_cache.set("c","c")

    print(lru_cache.get("a"))

    lru_cache.set("d","d")

    
    
