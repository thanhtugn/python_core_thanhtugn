from collections import Counter
from loguru import logger

str_examples = 'python default_dict.py'
count = Counter(str_examples)
for key, val in count.elements():
    logger.debug(f'{key}:{count[val]}')