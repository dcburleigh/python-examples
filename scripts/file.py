
def get_file(f):
    with open(f, 'r') as fh:
        text = fh.read()

    print("got file={}  size={}".format( f, len(text)))

def show_tsv_file(f):
    n = 0
    with open(f, 'r') as fh:
        for line in fh:
            n += 1
            row = line.strip("\n").split("\t")
            print("%4d) %s" % (n,row[0]))

show_tsv_file('data/example1.tsv')
