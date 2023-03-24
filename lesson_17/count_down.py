import time
from loguru import logger
def count_time(user_time):
    while user_time > 0:
        mins, secs = divmod(user_time, 60)
        # timer = '{:02d} : {:02d}'.format(mins, secs)
        # logger.info(timer)
        logger.info(f"{mins}:{secs}")
        time.sleep(1)
        user_time -= 1
    logger.error("Time up!")    

def main_flow():
    user_time = int(input("Enter a time in seconds: "))
    count_cont = True
    while count_cont:
        count_time(user_time)
        user_count = input("Would u like to count down again ? (y/n): ")
        if user_count.lower() == 'y':
            count_cont = True
        else:
            count_cont = False

if __name__ == '__main__':
    main_flow()