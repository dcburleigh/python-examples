import sys
import re
from utils import logger

def main():

    log = logger.init_logging_yaml('ex1.log.yml')
    print("got here")

if __name__ == '__main__':
    sys.exit(main())
