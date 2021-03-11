#!/bin/bash

workdir=~/1.Projects/2.Sorghum.Resistance.Project/1.Sorghum.Data/ClustalData
cd $workdir

echo Keep up the work!


clustalo -i $workdir/2300Data/2300_EarlyHoney.fasta -o $workdir/2300_EarlyHoney_out
