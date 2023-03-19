import threading
from loguru import logger
import time
def task_one(size):
    start_time = time.time()

    list_val = []
    for i in range(0, size):
        list_val.append(i)

    logger.info("Finish first task")
    end_time = time.time()
    logger.info(f'Time elaps task one: {end_time - start_time}')

def task_two(size):
    start_time = time.time()

    dict_val = {}
    for i in range(0, size):
        dict_val[i] = i

    logger.info("Finish second task")
    end_time = time.time()
    logger.info(f'Time elaps task two: {end_time - start_time}')

if __name__ == "__main__":
    start_time = time.time()
    # task_one()
    # task_two()
    thread_one = threading.Thread(target=task_one, args = (1000000000,))
    thread_two = threading.Thread(target=task_two, args = (1000000000,))

    thread_one.start()
    thread_two.start()
    thread_one.join()
    thread_two.join()
    end_time = time.time()
    logger.info(f'Time elaps: {end_time - start_time}')