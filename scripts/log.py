"""Logging example
Usage:

python log.py

python log.py [ basic | simple | code ]


"""
import sys
import re
from utils import logger
from sample import sample

def main():
    ltype = 'basic'
    ext = None
    if len(sys.argv) >= 2:
        ltype = sys.argv[1]

    result = re.match('.+\.(.+)$', ltype)
    if result:
        ext = result.group(1)

    if ltype == 'basic':
        log = logger.init_basic(fname='simple.log')
    elif ltype == 'simple':
        log = logger.init_logging()
    elif ltype == 'rot':
        log = logger.init_logging(rotate_size=1000)
    elif ltype == 'trot':
#        log = logger.init_logging(rotate_interval=5)
        log = logger.init_logging(rotate_seconds=30)


    elif ltype == 'code':
        log = logger.init_logging(err_file="err.log")
    elif ext == 'yml':
        log = logger.init_logging_yaml(ltype)
    elif ext == 'ini':
        log = logger.init_logging_ini(ltype)
    else:
        print("invalid arg "+ ltype)
        return 1

    print("got here ")
    log.warning("BEGINS")
    log.debug('debug ')

    log.info("some info")

    log.warning("we might have a problem")

    log.error("something bad")

    sample.func1()

    logger.list_handlers()

    print(f"wrote: {logger.log_file}")

    return 0

if __name__ == '__main__':
    #status = main()
    sys.exit(main())
