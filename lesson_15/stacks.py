from loguru import logger
#Method 1: Implement stack using list

def create_stack_list():
    #init stack 
    stack = []

    #add some elements to stack 
    stack.append('a')
    stack.append('b')
    stack.append('c')

    logger.info('initial stack:')
    logger.info(stack)

    #remove elements from stack
    logger.info('element popped from stack:')
    for i in range (len(stack)):
        logger.info(stack.pop())


    logger.info('Stack after all elements are popped:')
    logger.info(stack)

# create_stack_list()

#Method 2: Implement stack
from collections import deque

def create_stack_coll(max_size = 5):
    #init a stack
    stack = deque()

    #add elements to stack
    if len(stack) <= max_size:
        stack.append('x')
        stack.append('y')
        stack.append('z')
        logger.info('init stack:')
        logger.info(stack)

    #remove elements from stack
    logger.info('elements dequeued from stack:')
    for _ in range(len(stack)):
        logger.info(stack.popleft())

    logger.info('stack after removing elements:')
    logger.info(stack)
    
# create_stack_coll()
#Method 3: Implement stack using queue.Queue
from queue import LifoQueue

def create_stack_buildin():
    #init a stack
    stack = LifoQueue(maxsize=5)
    logger.info(f'stack size: {stack.qsize}')

    #put some elements to stack
    list_e = ['Dog', 'Cat', 'Horse', 'Dog', 'Cat', 'Horse', ]
    for e in list_e:
        if not stack.full():
            stack.put(e)

    logger.info('stack full: ' + str(stack.full()))
    logger.info(f'stack size: {stack.qsize}')

    #remove elements from stack
    logger.info('elements popped from stack:')
    for _ in range(0, stack.qsize()):
        logger.info(stack.get())

    #check if stack is empty
    logger.info(f'stack is empty: {stack.empty()}')

create_stack_buildin()