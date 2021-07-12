import sys
import logging

log_root = '.'
log_file = 'basic.log'

def init_basic(fname='basic.log'):
    """basic logging, level = DEBUG, log file = ??? """
    global log_root

    log_root = '|'
    fmt="%(funcName)s():%(lineno)i: %(message)s %(levelname)s"
    logging.basicConfig(level=logging.DEBUG, format=fmt, filename=fname)
    ##return get_mod_logger()
    return logging.getLogger(log_root)

def main():

    print("...")
    log = init_basic(log_file)

    log.info("BEGINS")
    log.debug('debug ')

    log.warning("we might have a problem")

    log.error("something bad")

    print(f"WROTE: {log_file} ")

    return
if __name__ == '__main__':
    #status = main()
    sys.exit(main())
