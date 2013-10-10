'''Author: Abrar Hussain '''
from stack import Stack
from my_queue import Queue

if __name__ == '__main__':


	'''-----------First part----------------'''
    # create a Stack and do simple operations
    stack = Stack()
    stack.push('Hello')
    print(stack.pop())

    '''------------Second Part--------------'''
    # user enters str values into stack
    line = input("Enter a string,'end' to stop: ")
    while (line != 'end'):
        stack.push(line)
        line = input("Enter a string,'end' to stop:")

    # user typed str values are removed from stack and printed
    while not(stack.is_empty()):
        print(stack.pop())

    '''-------------Third Part----------------'''
    # same user interaction as before, except use a Queue instead of Stack
    queue = Queue()
    line = int(input("Enter a string,'end' to stop: "))
    while (line != 'end'):
        queue.enqueue(line)

        #convert line to an int unless it is 'end'
        line = (input("Enter a string,'end' to stop:"))
        if  line != 'end':
        	line = int(line)

    product = 1
    while not(queue.is_empty()):
        product *= queue.dequeue()

    print(product)

    
