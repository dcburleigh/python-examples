
f = 'test.tsv'

def next_row(f):
    fh = open(f)
    if not fh:
        print("can't open file " + f)
        return

    for line in fh:
        yield line

def process_file(f):
