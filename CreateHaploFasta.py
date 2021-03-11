print "Create Haplotype Fasta"

import sys
import os
import fnmatch

print sys.argv[1]
#print sys.argv[2]
haplotype = sys.argv[1]
os.chdir(sys.argv[3]) #output folder
ref = sys.argv[4] #the reference gene to align the reads to. 

#create a new fasta file with the name of the haplotype
f= open('%s.fasta' % haplotype,'wa+')

#open and write the reference gene to the fasta file
fref = open(ref, 'r+')
refread = fref.read()
fref.close()
f.write(refread)


#Get the relevant haplotype sequences and put them into the fasta
for file_name in os.listdir('/home/coreyschultz/1.Projects/2.Sorghum.Resistance.Project/1.Sorghum.Data/ClustalData/Sorghum_PuerRico_Data/Sobic05G172300B'):
	if fnmatch.fnmatch(file_name, '*' + haplotype + '*.TXT'): #find the relevant reads in my folder
		print(file_name)   #list the read
		os.chdir(sys.argv[2])	#actually change into the folder where the read is
		fReads = open(file_name, 'r+') #open my read of interest
		fCode = fReads.read() #read the sequence
		f.write(fCode) #write the sequence to my haplotype fasta
		

f.close()

print "fasta file created"


