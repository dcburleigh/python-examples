from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased

import deldev_db_creds as creds
from db_tables.apt_config import APT_Config
from db_tables.client import Client

Session = None

def init_dbh():
    global Session
    #
    # dialect[+driver]://user:password@host/dbname[?key=value..],
    #

    connect = "mysql+pymysql://%s:%s@%s/%s" % ( creds.db_user, creds.db_password, creds.db_host, creds.db_name)
    #print("connect: {}".format( connect ))
    engine = create_engine(connect,
                            encoding='latin1', echo=True)

    Session = sessionmaker(bind=engine)

def show_row():
    session = Session()
    rec = session.query(APT_Config).filter_by(config_name='Test').first()
    if rec:
        print("got rec={}".format( rec ))
    else:
        print("NO MATCH")

def list2():
    session = Session()

    query = session.query(APT_Config.config_name, APT_Config.customer, Client.state)
    query = query.join(Client, APT_Config.fk_customer == Client.id)
    query = query.filter(APT_Config.config_name.like('Test%'))
    query = query.order_by(APT_Config.id)
    for instance in query:
        print("%s - %s ( %s )" % (instance.config_name, instance.customer, instance.state) )

def list_rows():
    session = Session()
    #
    #for instance in session.query(APT_Config).filter_by(config_name='Test%').order_by(APT_Config.id):
    for instance in session.query(APT_Config).filter(APT_Config.config_name.like('Test%')).order_by(APT_Config.id):
        print(instance.config_name, instance.customer)

#help(creds)
init_dbh()
#show_row()
#list_rows()
list2()
