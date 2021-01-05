# <<<-------------- Stacks ----------------------->>> 
"""
Stack - Last in, First out = LIFO - stack of dishes in sink

push - add to the top of the stack
pop - remove from the top of the stack

Very efficient to add or delete from the front (or the top)
"""

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        # add to the end of the array or bottom
        self.items.append(item)

    def pop(self):
        # always pops items off the back of the array
        if len(self.items) == 0:
            return None
        last_item = self.items.pop()
        return last_item


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LLStack:
    def __init__(self):
        self.top = None

    def push(self, item):
        # create a new LL node
        new_node =  LinkedListNode(item)
        # point new node to the current top of the stack
        new_node.next = self.top
        # set the TOP variable, to the new node
        self.top = new_node

    def pop(self):
        # don't remove anything from an empty stack
        if self.top is None:
            # if stack is empty, return none
            return None

        old_top = self.top
        #new top replaced old top
        self.top = old_top.next
        # now old top is none because it's been replaced by a new top
        old_top.next = None 

        return old_top.data 


class ArrayStack:
    def __init__I(self):
        #initialize self.item to an empty array
        self.item = []

    def push(self, item):
        # add items to the top of the stack in the array
        self.items.append(item)

    def pop(self):
        # if there are no items, return None
        if len(self.items) == 0:
            return None  
        # if there are items, remove the top from the stack      
        last_item = self.items.pop()
        # return the last item in the array
        return last_item


