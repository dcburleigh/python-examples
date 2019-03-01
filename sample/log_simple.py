import logging

log_file = 'test.log'
log_level = 'DEBUG'
#log_level = 'INFO'

logger = logging.getLogger()
#logger = logging.getLogger('simple')
#logger = logging.getLogger(__name__ )
logger.setLevel(log_level)

# console logger at INFO level
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)
handler.set_name('console')

logger.addHandler(handler)
#logger.setLevel(logging.INFO)
#logger.setLevel(logging.DEBUG)
#logger.setLevel(log_level)

if log_file:
    # log file at DEBUG level
    file_handler = logging.FileHandler(log_file, mode='a')
    #file_handler = TimedRotatingFileHandler(log_file, when='midnight', backupCount=7)

    #file_handler.setLevel(log_level)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    file_handler.set_name('file')
    logger.addHandler(file_handler)

l2 = logging.getLogger('aux')

logger.debug('often makes a very good meal of %s', 'visiting tourists')
logger.info('Info message')
l2.debug("testing ")
l2.info('got here')
