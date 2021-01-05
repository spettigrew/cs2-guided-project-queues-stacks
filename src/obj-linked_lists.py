#<<<----------- Linked Lists ------------->>>

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

head = LinkedListNode("0")
head.next = LinkedListNode("1")
head.next.next = LinkedListNode("2")

# Add to the front of the linked list

new_head = LinkedListNode("-1")

new_head.next = head

head =  new_head