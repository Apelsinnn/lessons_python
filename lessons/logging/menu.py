from logic import calculate
from logging import getLogger

logger = getLogger(__name__)


def start():
    while True:
        expression = input('Введите выражение для вычисления: ')
        # Было
        # print(f'Expression is {expression}')

        # Стало
        logger.debug('Expression is %s', expression)
        if not expression:
            # Было
            # print('empty expression, stopping...')

            # Стало
            logger.info('empty expression, stopping...')
            break
        result = calculate(expression)
        if result is None:
            # Было
            # print('No result back, stopping...')

            # Стало
            logger.info('No result back, stopping...')
            break
        print(f'Result is {result}')
