#!/bin/bash

workdir=/home/coreyschultz/1.Projects/2.Sorghum.Resistance.Project/1.Sorghum.Data/Sorghum_PuerRico_Data_B
cd $workdir
database=$workdir/Sobi2300DB 
contigs=$workdir/2300SNP4
consens=$workdir/Sobic05G172300consB.fa

echo Good Job Corey!

##turn my consensus sequence into a databast to blast agaisnt
#makeblastdb -in $consens -dbtype nucl -out $workdir/Sobi2300DB 

##blast my contigs file against the consensus database
blastn -db $database -query $contigs -num_threads 4 -out $workdir/testsnp4
