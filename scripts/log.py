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
    log.debug('debug ')

    log.info("some info")

    log.warning("we might have a problem")

    log.error("something bad")

    sample.func1()

    return 0

if __name__ == '__main__':
    #status = main()
    sys.exit(main())
