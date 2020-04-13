

items = [ 'a', 'b', 'x', 'q', 'l']

for a in items:
    print(f"item: {a}")

for a in sorted(items):
    print(f"sort item: {a}")

stuff = { 'a': 1974, 'x': 1002,  'q': 1666, 'l': 101, 'b': 2001}

slist = sorted(stuff.keys())
for name in slist:
    print(f"key name={name} v={stuff[name]}")


slist = sorted(stuff)
for name in slist:
    print(f"name={name} v={stuff[name]}")

# https://docs.python.org/3.6/howto/sorting.html#sortinghowto

slist = sorted(stuff.keys())
for name in slist:
    print(f"name={name} v={stuff[name]}")



#slist =  sorted(repos,  key=lambda k: k[sort_key] ):
