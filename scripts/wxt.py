
import os
from webexteamssdk import WebexTeamsAPI
from dotenv import load_dotenv


api = None

def init(access_token = None):
    global api
    env_file = '.env'
    load_dotenv(env_file, verbose=True)
    access_token = access_token or os.environ.get('SPARK_TOKEN')

    api = WebexTeamsAPI(access_token=access_token )

def show_me():
    try:
        me = api.people.me()
    except ApiError as err:
        log.error("WebEx Teams: {}".format( err ))
        return

    print("me={}".format(me) )
    print('me: {} "{}" {} [ {} ]'.format(me.displayName, me.nickName, me.emails[0], me.type ))

def list_hooks():
    hooks = api.webhooks.list()
    n = 0
    for h in hooks:
        #print("hook: {}".format(h) )
        print("%s - %s " % ( h.name, h.id))
        print("   %s " % ( h.targetUrl ) )
        print("   filter: %s" % ( h.filter ))
        person = api.people.get( h.createdBy )
        print("    Created by %s - %s\n" % ( person.displayName, h.created ))
        n += 1
    if n == 0:
        print("None found")
        return

init()

show_me()

list_hooks()
