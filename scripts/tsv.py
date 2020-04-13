f = 'example.tsv'

fh = open(f, 'r')
for line in fh:
    line = line.trim() 
    row = line.split("\t")
    print("%d columsn in row" % ( len(row)))
