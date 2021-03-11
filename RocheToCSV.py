#!/usr/bin/python
import csv

txt_file = r"/home/coreyschultz/1.Projects/2.Sorghum.Resistance.Project/1.Sorghum.Data/ROCHE.data/6.28.19KASPtable"
csv_file = r"/home/coreyschultz/1.Projects/2.Sorghum.Resistance.Project/1.Sorghum.Data/ROCHE.data/6.28.19KASPtable.csv"

# use 'with' if the program isn't going to immediately terminate
# so you don't leave files open
# the 'b' is necessary on Windows
# it prevents \x1a, Ctrl-z, from ending the stream prematurely
# and also stops Python converting to / from different line terminators
# On other platforms, it has no effect


in_txt = csv.reader(open(txt_file, "r"), delimiter = '\t')
out_csv = csv.writer(open(csv_file, 'w'))

out_csv.writerows(in_txt)
