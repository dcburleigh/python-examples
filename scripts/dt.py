
#
# https://docs.python.org/3.6/tutorial/stdlib.html#dates-and-times
# https://docs.python.org/3.6/library/datetime.html#module-datetime
#

from datetime import date, timedelta
import re

def show_past(ago=2):
    now = date.today()
    diff = timedelta(  days=ago )
    past = now - diff
    print("{} days ago = past={}".format(ago, past))

def show_now():
    now = date.today()
    print("now: {} YMD={}".format( now, now.strftime("%Y-%m-%d") ))

def show_diff(ymd):
    parts = re.split('-', ymd)
    parts = [ int(p) for p in re.split('-', ymd)]
    print("parts={}".format(parts))
    #d = date(parts)
    d = date(parts[0], parts[1], parts[2])
    print("{}: == {}".format(ymd, d.isoformat()))

    now = date.today()

    ago = now - d
    print("diff={} days".format( ago.days ))

show_now()

show_past()

show_diff('2017-12-01')
