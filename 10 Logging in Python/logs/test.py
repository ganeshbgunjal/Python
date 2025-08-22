from logger import logging

def add(a,b):
    logging.debug('Addition operation is done.')
    return a+b

logging.debug('The addition function is called!')
add(10,15)

def sub(a,b):
    logging.debug('Substraction of 2 numbers is taking place')
    return a-b

logging.debug('The substraction function is called.')
sub(10,8)
