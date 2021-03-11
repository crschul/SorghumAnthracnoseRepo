import sys
import os
import fnmatch
import string

print "Add haplotype consensus to gene consensus file"

print sys.argv[1]

haplotype = sys.argv[1]
os.chdir(sys.argv[3]) #output folder

f = open('2300Combined.fasta','a+')

fref = open(sys.argv[5], 'r+')
refread = fref.read()
fref.close()
f.write(refread)
f.close




