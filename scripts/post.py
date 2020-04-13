import sys
# import argparse
#
from configparser import ConfigParser
import requests
from requests.auth import HTTPBasicAuth

cfg = {}

def get_auth(ip, user, pwd, path=None ):
    headers = None
    auth=HTTPBasicAuth(user, pwd)
    print("auth=%s" % auth )

    url = "http://%s/" % (  ip )
    url = "http://%s/getxml?location=/Status/Standby" % (  ip )
    print("u=%s" % url)

    r = requests.get(url, verify=False, auth=auth)
    print("got={}".format(r))
    if not r.status_code == 200:
        print("get failed")
        return

    print("got=\n%s" % r.text )



def read_server_config(f):
    global cfg

    config = ConfigParser()
    config.read(f)
    cfg  = config['server']


def main():

    f = 'post.cnf'
    read_server_config(f)
    print("user=%s" % ( cfg['username']))
    get_auth( cfg['ip'], cfg['username'], cfg['password'])

if __name__ == '__main__':
    sys.exit(main())
