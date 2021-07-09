"""Custom Logging Handler."""

import logging
import logging.config
import sys
#from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler
from ruamel.yaml import YAML
import json

# https://stackoverflow.com/questions/9065136/allowed-characters-in-map-key-identifier-yaml#21195482
# label for logger; also top-level root for logging label
log_root = 'TOP'
log_root = None
log_root = '|'

log_file = 'test.log'
log_file = None

# https://opensource.com/article/17/9/python-logging
ATTR_TO_JSON = ['created', 'filename', 'funcName', 'levelname', 'lineno', 'module', 'msecs', 'msg', 'name', 'pathname', 'process', 'processName', 'relativeCreated', 'thread', 'threadName']
class JsonFormatter:
    def format(self, record):
        obj = {attr: getattr(record, attr)
                  for attr in ATTR_TO_JSON}
        return json.dumps(obj, indent=4)

class MyFormatter(logging.Formatter):
    format_str = '%(name)s,  %(levelname)s - %(message)s'

    # attributes:
    # https://docs.python.org/3/library/logging.html#logrecord-attributes
    # can't expect all attributes
    # https://stackoverflow.com/questions/32301522/logrecord-does-not-have-expected-fields#32301798
    #  To have message and asctime set, you must first call self.format(record) inside the emit method.

    def format(self, record):
        #print("rec=" + str(dir(record))  )
        record.asctime = self.formatTime(record)
        #k = record._dict__.keys()
        # debug
        #return  "... %s - %s - %s" % (record.name, record.levelname, 'msg')
        #return  "... %s - %s - %s" % (record.name, record.levelname, record.message )
        #return  "... %s - %s - %s keys=%s" % (record.name, record.levelname, record.msg, type(record))
        return  "%s - %s - %s - %s IN %s" % (self.formatTime(record), record.name, record.levelname, record.msg, record.module )
        #return  "%s - %s - %s - %s keys=%s" % (record.asctime, record.name, record.levelname, record.msg, type(record))
        #return  "%s - %s - %s - %s IN %s: %s #%s" % (record.asctime, record.name, record.levelname, record.msg, record.funcName, record.filename, record.lineno)

def get_mod_logger(mod_name=None):

    if mod_name:
        name = mod_name.split('.')[-1]
        log_name = '{}.{}'.format( log_root, name )
        #log_name = name
        #log_name = log_root
    else:
        log_name = log_root
        name = '-'

    #print("logger='{}'  mod={} name={}".format(log_name, mod_name, name))
    return logging.getLogger(log_name)

def init_basic(fname='basic.log'):
    """basic logging, level = DEBUG, log file = ??? """
    global log_root

    log_root = '|'
    fmt="%(funcName)s():%(lineno)i: %(message)s %(levelname)s"
    logging.basicConfig(level=logging.DEBUG, format=fmt, filename=fname)
    return get_mod_logger()
    return logging.getLogger(log_root)

def init_logging_ini(config_file, root_name=None):
    logging.config.fileConfig(config_file)
    return get_mod_logger()
    #log = logging.getLogger('|')

def init_logging_yaml(config_file, root_name=None):
    """initialize logging configuration via a dict specified from a YAML file """
    # https://docs.python.org/3/library/logging.config.html#logging-config-api

    global log_root
    yaml=YAML(typ='safe')   # default, if not specfied, is 'rt' (round-trip)
    with open(config_file) as fh:
        text = fh.read()
    cfg = yaml.load(text)

    if 'log_root' in cfg:
        log_root = cfg['log_root']
    if root_name:
        print("change root from {} to {} -- {}".format(log_root, root_name, cfg['loggers'][log_root]))
        cfg['loggers'][root_name] = cfg['loggers'][log_root]
        log_root = root_name.upper()
    if log_file:
        cfg['handlers']['file']['filename'] = log_file

    #print("format={}".format( cfg['formatters']['file']['format']))

    #print("using formatters={}".format(cfg['formatters']))
    try:
        logging.config.dictConfig(cfg)
    except Exception as err:
        #log.critical(f"bad config file {config_file} - {err}")
        print(f"ERROR bad config file {config_file} - {err}")
        exit(1)
        #return
    return get_mod_logger()

def init_logging(console_level: str='info', file_level: str='debug',
                 fname: str='debug.log', name='|', err_file: str=None):
    """
    Initialize logging for the package.

    This function is executed in the csetup module and imported from there in other modules.

    Args:
        console_level (str): Console logging level
        file_level (str): File logging level
        fname (str): file name for logging to file
        name: root logger name

    Returns:
        Logger object
    """
    global log_root
    levels = {'debug': logging.DEBUG, 'info': logging.INFO, 'warn': logging.WARN,
              'error': logging.ERROR, 'critical': logging.CRITICAL}

    # attributes;
    # https://docs.python.org/3/library/logging.html#logrecord-attributes
    console_fmt = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    #console_fmt = logging.Formatter('%(asctime)s, %(name)s - %(levelname)s - %(message)s')

    file_fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_fmt = logging.Formatter('%(asctime)s - F=%(module)s - %(name)s - %(levelname)s - %(message)s')

    if name:
        log_root = name

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    #console_log = logging.StreamHandler()
    console_log = logging.StreamHandler(stream=sys.stdout)
    console_log.setLevel(levels[console_level.lower()])
    console_log.setFormatter(console_fmt)
    logger.addHandler(console_log)

    #e = False
    #e = True
    if err_file:
        if err_file:
            err_log = logging.FileHandler(err_file, mode='w')
        else:
            err_log = logging.StreamHandler(stream=sys.stderr)
        err_log.setLevel(levels['warn'])
        err_fmt = logging.Formatter('ERROR -- %(name)s - %(message)s')
        err_fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - IN %(module)s: %(filename)s #%(lineno)s  ')

        err_log.setFormatter(err_fmt)
        logger.addHandler(err_log)

    if fname:
        file_log = logging.FileHandler(fname, mode='w')
        file_log.setLevel(levels[file_level.lower()])
        file_log.setFormatter(file_fmt)
        logger.addHandler(file_log)

    return logger
