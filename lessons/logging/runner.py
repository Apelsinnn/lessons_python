import json

from menu import start
import logging.config
from logging import getLogger

# from logging import getLogger, basicConfig, DEBUG, ERROR, FileHandler, StreamHandler

with open("logging.conf") as file:
    config = json.load(file)

logging.config.dictConfig(config)
logger = getLogger()

# logger = getLogger()
# FORMAT = '%(asctime)s : %(name)s : %(levelname)s : %(message)s'
# file_handler = FileHandler('Data.log')
# file_handler.setLevel(DEBUG)
# console = StreamHandler()
# console.setLevel(ERROR)
# # Для выключения показа логов дебага, можно ниже просто поменять уровень показа вложенности (DIWEC)
# basicConfig(level=DEBUG, format=FORMAT, handlers=[file_handler, console])


if __name__ == '__main__':
    # Было
    # print('Start service')
    # start()
    # print('Stop service')

    # Стало
    logger.info('Start service')
    start()
    logger.info('Stop service')
