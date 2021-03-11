#!/bin/bash

workdir=~/1.Projects/2.Sorghum.Resistance.Project/ResequencingData
cd $workdir
inputfolder=$workdir/SangerData
outputfolder=$workdir/AlignmentOut
reference=$workdir/Sobic05G172300cons.TXT


haplotype=SC1033						#Run once for every haplotype

echo And now it begins.

########################################################## Run Once per gene then comment out ########################################

###Reverse Compliment all of the the "R" fasta files and creats a combined fasta for the gene. Only Run this once per gene then comment out.

#python ReverseSeqString.py $haplotype $inputfolder $outputfolder $reference

######################################################################################################################################

### creat a haplotype fasta file using a shell script

python CreateHaploFasta.py $haplotype $inputfolder $outputfolder $reference
echo  
echo  $haplotype fasta created

#### use clustalo to align all of the same genotypes
#add -dealign to have them all ontop of eachother

clustalo -i $outputfolder/$haplotype.fasta  -o $outputfolder/$haplotype.2300.clustalo.output 
echo    
echo  fasta aligned to consensus
outputcons=$outputfolder/$haplotype.2300.consensus

### combine the aligned output file into one sequence and add that sequence to the combined fasta

cons $outputfolder/$haplotype.2300.clustalo.output $outputfolder/$haplotype.2300.consensus -name $haplotype -plurality 2 -setcase 2

echo 
echo  haplotype consensus created

outputcons=$outputfolder/$haplotype.2300.consensus

python AddtoFinAlign.py $haplotype $inputfolder $outputfolder $reference $outputcons

echo created consensus sequence added it to to combined fasta

### Align all haplotype consensus sequences for this gene to identify SNPs - FINAL STEP

clustalo -i $outputfolder/2300Combined.fasta -dealign -o $outputfolder/2300AlignedSNPFile 
