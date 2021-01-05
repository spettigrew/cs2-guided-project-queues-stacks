"""
Your goal is to define a `Queue` class that uses two stacks. Your `Queue` class
should have an `enqueue()` method and a `dequeue()` method that ensures a
"first in first out" (FIFO) order.

As you write your methods, you should optimize for time on the `enqueue()` and
`dequeue()` method calls.

The Stack class that you will use has been provided to you.
"""
# Utilize these stacks. One to hold all the data, the second to change FICO order. Pop from the first, push from the second
class Stack:
    def __init__(self):
        self.data = []
        
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        return "The stack is empty"

class QueueTwoStacks:
    def __init__(self):
        # Your code here
        self.input_stack = Stack()      # left stack    
        self.output_stack = Stack()     # right stack 

        
    def enqueue(self, item):
        # Your code here - the original stack. Always add to the input stack. Here to fill if we need to add more to the output stack
        self.input_stack.push(item)


    def dequeue(self):
        # Your code here - do not add new items to the ouput stack
        # return values from the output stack
        # if the output stack is empty, fill it with values from the input stack. 
        if len(self.output_stack.data) == 0:
            # while there are items in the input stack
            # check the length to make sure it's not greater than 0
            while len(self.input_stack.data) > 0:
                # pop from the input-stack and push onto the the output-stack
                cur_item = self.input_stack.pop()
                # take each letter and move it over to the output stack, which is now in reverse (correct) order
                self.output_stack.push(cur_item)

        # if there are items in the output stack, pop one off
        if len(self.output_stack.data) == 0:
            # check if nothing is there, don't pop. Return None
            return None
        return self.output_stack.pop()

        self.input_stack.pop()

        
my_queue = QueueTwoStacks()

my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("C")
my_queue.enqueue("D")

print("The first item added was " + my_queue.dequeue())
print("The second item added was " + my_queue.dequeue())

my_queue.enqueue("E")
print("The third item added was " + my_queue.dequeue())
print("The fourth item added was " + my_queue.dequeue())
print("The fifth item added was " + my_queue.dequeue())
