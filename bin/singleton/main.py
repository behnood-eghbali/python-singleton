import logger

for i in range(4):
    logger.critical('log message {}'.format(i))
    logger.error('log message {}'.format(i))
    logger.warn('log message {}'.format(i)) 
    logger.info('log message {}'.format(i))
    logger.debug('log message {}'.format(i))
