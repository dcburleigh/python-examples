import sys
import re
from utils import logger
from utils import db

def main():

    log = logger.init_logging_yaml('ex1.log.yml')
    #dbh = db.DB(f='/usr/local/etc/deldev/deldev_db_local.cfg', t='staff')
    dbh = db.DB(f='/usr/local/etc/deldev/deldev_mysql.cnf', t='staff')

    n = dbh.count()
    print("{} rows".format( n ))

    print("got here")

if __name__ == '__main__':
    sys.exit(main())
