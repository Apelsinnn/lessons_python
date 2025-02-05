from logging import getLogger

logger = getLogger(__name__)

def calculate(exp: str):
    # Было
    # print(f'Get expression {exp}')

    # Стало
    logger.debug('Get expression %s', exp)
    try:
        result = eval(exp)
        # Было
        # print(f'Evaluated {result}')

        # Стало
        logger.debug('Evaluated %s', exp)
        return result
    except Exception as e:
        # Было
        # print(f'Exception {e}')

        # Стало
        logger.error('Exception %s', e)
        return None
