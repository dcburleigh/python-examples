"""
wrapper for database access

see: http://pymysql.readthedocs.io/en/latest/

Usage:
  from utils import db

  dbh = db.DB()
  dbh = db.DB(f='/path/to/config', t='TABLE')

  n = dbh.count()
  print("%s rows" % n)




"""

import pymysql.cursors
import sys

from configparser import ConfigParser
#from config import Config

class DB:
    dbh = None
    #cfg_file = 'deldev_db.cfg'
    cfg_file = 'deldev_db.ini'
    fields = [ ]
    cfg = None
    errors = []
    messages = []
    table_name = None

    def __init__(self,f=None, t=None):

        if t:
            self.table_name = t

        if f:
            self.cfg_file = f

        if not self.cfg_file:
            raise Exception('no config file')

        fh = open(self.cfg_file)
        if not fh:
            raise Exception("cannot open " + self.cfg_file)

        try:
            config = ConfigParser()
            config.read(self.cfg_file)
            self.cfg = config['client']
        except Exception as err:
            print("ERROR: config file {} failed: {}".format( self.cfg_file, err))
        return

    def open(self):
        try:
            self.dbh = pymysql.connect(
                host=self.cfg.get('host', 'localhost'),
                user=self.cfg.get('user'),
                password=self.cfg.get('password'),
                port=self.cfg.get('port',3306),
                db=self.cfg.get('database', 'deldev'),
                #charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
                )
        except Exception as err:
            raise Exception("connect failed: {}".format(err) )
            return

    def close(self):
        self.dbh.close()

    def add_item(self, item ):
        #print "add item: p=", item['project']
        self.open()

        flist = ''
        vlist  = ''
        # calling program is responsible for making sure
        #  all values are of type 'string'
        for f in self.fields:
            if f in item:
                if item[f] == None:
                    continue

                if flist:
                    flist += ', '
                    vlist += ', '
                flist += "`"  + f + "`"
                vlist += "'" + item[f] + "'"

        #raise Exception("got here")
        if flist == '':
            raise Exception("no valid fields")
            #print "ERROR: no valid fields"
            #return

        sql =  "INSERT INTO `%s`  ( %s ) VALUES ( %s ) " % ( self.table_name, flist, vlist )

        #cursor = self.dbh.cursor( dictionary=True)
        cursor = self.dbh.cursor( )
        if not cursor:
            raise Exception('no cursor')
        cursor.execute(sql)
        #return
        self.dbh.commit()
        id = cursor.lastrowid
        self.close
        return id

    def count_column(self, col):
        """ return the number of occurrences of the values
        in a specified column"""

        self.open()
        n = 0

        # set:
        #  fields, col_name, select_field
        if type(col) is list:
            #print "list", col
            for c in col:
                if not c in self.fields:
                    raise Exception("invalid column " + c)
                    return
            fields = ', '.join(col)
            col_name =  '_'.join(col)

            x = '," ",'.join( col )
            select_field = 'concat(' + x + ') as ' + col_name


        else:
            ###print col,"type", type(col)
            if not col in self.fields:
                raise Exception("invalid column " + col)
                return
            fields = col
            select_field = col
            col_name = col

        sql =  "select count(*) as num, %s from %s group by %s order by count(*) DESC " % ( select_field, self.table_name, fields )
        sql = "select count(*) as num, " + select_field + " from application_usage "

        clist = []
        try:
            cursor = self.dbh.cursor()
            cursor.execute(sql)
            while True:
                result = cursor.fetchone()
                if not result:
                    break
                n += 1
                #print("{} r={}".format( n, result ))

                clist.append( { 'name': result[col_name], 'count': result['num']})
        except Exception as err:
            #return "count failed: " + str(err)
            print( "count failed: " + str(err))
            return

        return clist

    def count(self, args=None):
        self.open()
        n = 0
        sql = "select count(*) as num from %s " % self.table_name
        try:
            cursor = self.dbh.cursor()
            cursor.execute(sql)
            result = cursor.fetchone()
            #print "got results, type", type(result)
        except Exception as err:
            return( "count failed: " + str(err))
            return

        return result['num']
