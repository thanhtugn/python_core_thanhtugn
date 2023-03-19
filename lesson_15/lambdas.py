from loguru import logger
#example 1: Condition checking

#with lambda
format_check = lambda num: logger.debug(f'{num} is integer' if isinstance(num, int) else f'{num} is not integer')

#without lambda
def check_num(num):
    if isinstance(num, int):
        logger.debug(f'{num} is integer')
    else:
        logger.debug(f'{num} is not integer')

check_num(10)
format_check('abc')

#example 2:
new_list = [lambda arg=x: arg*10 for x in range(1, 5)]
for item in new_list:
    logger.debug(item())