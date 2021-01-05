# <<<----------- Queues ---------------->>>
"""
Queue - First in, First out = FIFO - line in a store
(Linked Lists very good for implementing queues)
Queues are LL's with Very specific requirements that can only add to the front and remove from the end.
Enqueue - insert at the end
Dequeue - delete at the front
"""

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    # Add to the queue
    def enqueue(self, item):
        # create a new linked list node
        new_node = LinkedListNode(item)
        # if the queue is empty
        if self.back is None:
            self.back = new_node
            self.front = new_node
        # add the new_node to the backf
        # make sure the old back points to the new node
        else:
            self.back.next = new_node
            # make the back point to the new node
            self.back = new_node
            
        # Removing from the queue
    def dequeue(self, item):
        if self.front is None:
            return None
        
        # stire a temporary variable so we don't lose our node
        old_front = self.front
        # move the front pointer, to the next node over
        self.front = self.front.next

        # special case, if the queue should now be empty
        if self.front is None:
            self.back = None
            
        return old_front.data


my_queue = Queue()

my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("C")

print(f'The front is now {my_queue.front.data}')

print("Remove the value from the front")
print(f'removed value is {my_queue.dequeue()}')
print(f'The front is now {my_queue.front.data}')

print("Remove the value from the front")
print(f'removed value is {my_queue.dequeue()}')
print(f'The front is now {my_queue.front.data}')

print("Remove the value from the front")
print(f'removed value is {my_queue.dequeue()}')
print(f'The front is now {my_queue.front.data}')
