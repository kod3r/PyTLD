from TLDList import TLDList
from Date import Date
from sys import argv

if len(argv) != 4:
    print "main.py DD/MM/YY DD/MM/YY file.txt"
    exit()

tldlist = TLDList(argv[1], argv[2])

io = open(argv[3], "r")
lines = io.readlines()
io.close()

for line in lines:
    lineargs = line.rstrip().split(" ")
    tldlist.addtld(lineargs[1].split(".")[-1], Date(lineargs[0]))

for key in sorted(tldlist.tlds, key=tldlist.tlds.get):
    print key, round(tldlist.gettldcount(key)/float(tldlist.getcount())*100,2)