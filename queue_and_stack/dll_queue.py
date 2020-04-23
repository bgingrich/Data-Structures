import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

 # Why is our DLL a good choice to store our elements?
 # FIFO
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return
        self.size -=1
        value = self.storage.remove_from_head()
        return value

    def len(self):
        return self.size
