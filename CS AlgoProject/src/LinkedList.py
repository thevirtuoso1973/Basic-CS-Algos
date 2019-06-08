#Implementation of a linked list in python:

# a node of the list:
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        #self.prev = None (<--- If doubly-linked list)

# the list itself (consists of nodes)
class LinkedList:
    def __init__(self, headVal):
        self.head = Node(headVal)
        #self.tail = etc..

    # adds a value in the correct position
    def add(val):
        curr = self.head
        if val < curr.val:
            self.head = Node(val)
            self.head.next = curr
        else:
            while curr and val >= curr.val:
                prev = curr
                curr = curr.next
            prev.next = Node(val)
            prev.next.next = curr

    # deletes a node with the value given
    def delete(val):
        curr = self.head
        if val == curr.val:
            self.head = curr.next
        else:
            while curr.next and curr.next.val != val:
                curr = curr.next
            if curr.next:
                curr.next = curr.next.next
            else:
                print("Value not in linked list.")
