import logging

logging.basicConfig(
    level=logging.DEBUG,
    format = '%(asctime)s-%(name)s-%(levelname)s-%(message)s',    
    datefmt = '%Y-%m-%d %H-%M-%S',
    handlers = [
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('ArithmaticApp')

def add(a,b):
    result = a+b
    logger.debug(f'Adding {a} + {b} = {result}')
    return result

def sub(a,b):
    result = a-b
    logger.debug(f'Subtracting {a} - {b} = {result}')
    return result

def multiply(a,b):
    result = a*b
    logger.debug(f'Multiplying {a} * {b} = {result}')
    return result

def divide(a,b):
    try: 
        result = a/b
        logger.debug(f'Dividing {a} / {b} = {result}')
        return result
    except ZeroDivisionError:
        logger.error('Division by zero Error!')
        return None

add(20,15)
sub(20,10)
multiply(15,10)
divide(20,0)
