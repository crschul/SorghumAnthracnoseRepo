import sys
import os
import fnmatch
import string
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Alphabet import generic_dna
print "Reverse all "R" Reads"
print sys.argv[1]
print sys.argv[2]
haplotype = sys.argv[1]
os.chdir(sys.argv[3]) #output folder
ref = sys.argv[4] #the reference gene to align the reads to. 

#Create a combined fasta for all 
f = open('2300Combined.fasta','wa+')

fref = open(ref, 'r+')
refread = fref.read()
fref.close()
f.write(refread)
f.close


#Reverse compliment all of the sequences that contain "R"
for file_name in os.listdir('/home/coreyschultz/1.Projects/2.Sorghum.Resistance.Project/1.Sorghum.Data/ClustalData/Sorghum_PuerRico_Data/Sobic05G172300B'):
	if fnmatch.fnmatch(file_name, '*' + 'R' + '*.TXT'): #find the relevant reads in my folder
		#print(file_name)   #list the read
		os.chdir(sys.argv[2])	#actually change into the folder where the read is
		SeqRead = SeqIO.read(file_name, "fasta") #open and read the file using biopython, which isolates the sequence
		#print(SeqRead)		
		RevComp = SeqRead.reverse_complement() #Reverse compliment the sequence
		#print(RevComp)		
		sequences = RevComp
		with open(file_name, "w") as file_name:    #overwrite the original file with the new reverse compliment sequence
   			 SeqIO.write(sequences, file_name, "fasta")	


		
		

