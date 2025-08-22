import logging

logger = logging.getLogger()
for handler in logger.handlers[:]:
    logger.removeHandler(handler)

    
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format = '%(asctime)s-%(name)s-%(levelname)s-%(message)s',    
    datefmt = '%Y-%m-%d %H-%M-%S'
)
