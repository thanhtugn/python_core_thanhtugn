from loguru import logger

#Method 1: Implement QUEUE using a list
def create_queue_list():
    #init a queue
    queue = []

        #add elements to queue
    queue.append('a')
    queue.append('b')
    queue.append('c')

    logger.info('init queue:')
    logger.info(queue)

    #remove elements from queue
    logger.info('elements dequeued from queue:')
    for _ in range(len(queue)):
        logger.info(queue.pop(0))

    logger.info('queue after removing elements:')
    logger.info(queue)

#Method 2: Implement QUEUE using collections.deque
from collections import deque

def create_queue_coll(max_size = 5):
    #init a queue
    queue = deque()

    #add elements to queue
    if len(queue) <= max_size:
        queue.append('x')
        queue.append('y')
        queue.append('z')
        logger.info('init queue:')
        logger.info(queue)

    #remove elements from queue
    logger.info('elements dequeued from queue:')
    for _ in range(len(queue)):
        logger.info(queue.popleft())

    logger.info('queue after removing elements:')
    logger.info(queue)

# create_queue_coll()

#Method 3: Implement QUEUE using queue.Queue
from queue import Queue

def create_queue_building():
    #init a queue
    queue = Queue(maxsize=5)
    logger.info(f'max_size: {queue.qsize()}')

    #put some elements in queue
    list_elements = ['Ha Noi', 'Ha Nam', 'Thai Binh', 'Hung Yen', 'Bac Ninh', 'Hai Duong']
    for e in list_elements:
        if (not queue.full()):
            queue.put(e)

    #check queue wether full or not
    logger.info(f'queue is full: {queue.full()}')
    logger.info(f'max size of queue: {queue.qsize()}')

    #remove some elements from queue
    logger.info('elements dequeued from queue:')
    for _ in range(queue.qsize()):
        logger.info(queue.get())

    #check queue wether empty or not
    logger.info(f'queue is empty: {queue.empty()}')

create_queue_building()