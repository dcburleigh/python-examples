
import sys
from utils import logger_yaml
log = logger_yaml.get_mod_logger()

def main():
    log.info("begins")

    log.debug('testing')

    log.error("something bad ")

    log.info("done ")

    log.critical("failed")


if __name__ == '__main__':
    status = main()
    print(f"wrote: {logger_yaml.log_file} ")
    sys.exit(status)
