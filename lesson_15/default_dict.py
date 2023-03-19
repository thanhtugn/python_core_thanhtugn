#EX1: Dictionary
from loguru import logger
from collections import defaultdict
def my_dict():
    dict = {1: 'Math', 2: 'Physics', 3: 'Chemistry', 4: 'History'}
    logger.debug(dict)
    logger.debug(dict[1])
    logger.debug(dict[2])
    logger.debug(dict[3])
    logger.debug(dict[4])

def error_message():
    return "Key does not present in the dictionary"

def my_default_dict():
    ddict = defaultdict(error_message)
    ddict[1] = "Math"
    ddict[2] = "Physics"
    ddict[3] = "Chemistry"
    ddict[4] = "History"

    logger.debug(ddict)
    logger.debug(ddict[1])
    logger.debug(ddict[2])
    logger.debug(ddict[3])
    logger.debug(ddict[4])

my_default_dict()