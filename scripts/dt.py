
#
# https://docs.python.org/3.6/tutorial/stdlib.html#dates-and-times
#
"""
https://docs.python.org/3.6/library/datetime.html#module-datetime


class datetime.date

    An idealized naive date, assuming the current Gregorian calendar always was, and always will be, in effect. Attributes: year, month, and day.

class datetime.time

    An idealized time, independent of any particular day, assuming that every day has exactly 24*60*60 seconds (there is no notion of “leap seconds” here). Attributes: hour, minute, second, microsecond, and tzinfo.

class datetime.datetime

    A combination of a date and a time. Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.

class datetime.timedelta

    A duration expressing the difference between two date, time, or datetime instances to microsecond resolution.

class datetime.tzinfo

    An abstract base class for time zone information objects. These are used by the datetime and time classes to provide a customizable notion of time adjustment (for example, to account for time zone and/or daylight saving time).

class datetime.timezone

    A class that implements the tzinfo abstract base class as a fixed offset from the UTC.

"""

from datetime import date, timedelta, datetime
import re

def show_ymd( year=2020, mm=1, day=2):

    d = date(year, mm, day)
    print(f"ymd={year}-{mm}-{day} == {d} type={type(d)}  ")

def show_past(ago=2):
    """timedelta """
    now = date.today()
    diff = timedelta(  days=ago )
    past = now - diff
    print("{} days ago = past={}".format(ago, past))


def show_now():

    d = datetime.utcnow()
    print(f"date,utc now={d} ( type={type(d)}  ")
    d = datetime.today()
    print(f"date,utc now={d} ( type={type(d)}  ")

    now = date.today()
    print("now: {}  type={type(now)} YMD={}".format( now, now.strftime("%Y-%m-%d") ))

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

show_ymd()

show_past()

show_diff('2017-12-01')
