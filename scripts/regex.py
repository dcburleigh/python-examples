import re

pat1 = re.compile("[\']")

text_in = "abc'xyz"

result = pat1.search( text_in )
print("{}:  matched={}".format( text_in, result ))

result = pat1.match( text_in )
print("{}:  matched={}".format( text_in, result ))

result = pat1.sub('.', text_in )
print("{}:  matched={}".format( text_in, result ))

text_in = "abc'xy'z"
result = pat1.sub('.', text_in )
print("{}:  matched={}".format( text_in, result ))

pat2 = re.compile('whois (\w+) ')
text_in = "tell me, whois johndoe "

result = pat2.match( text_in)
print("{}:  matched={}".format( text_in, result ))

result = pat2.search( text_in)
n = len( result.groups() )
print("{}:  n={} matched={}".format( text_in, n, result ))
print("got 0) {}".format( result.group(0)))
print("got 1) '{}' ".format( result.group(1)))

n = len( result.groups(0) )
print("group 0, n={}".format(n))
n = len( result.groups(1) )
print("group 1, n={}".format(n))

#print("got 2) {}".format( result.group(2)))

text_in = "tell me, who is johndoe "
result = pat2.search( text_in)
if result:
    print("{}:  matched={}".format( text_in, result ))
else:
    print("{} - no match".format( text_in ))
