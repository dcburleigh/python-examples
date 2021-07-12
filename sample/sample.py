"""Sample module """

import re
import sys
from utils import logger

log = logger.get_mod_logger(__name__)

def func1():
    #print("test")
    log.info("got here ")
    log.warn("nothing to do")
