#!/bin/bash
# e.g., run with:
# run_dbcan_and_counts.sh genome.fa
# genome name is first argument
genome=$1
# strip everything down to genome name after last backslash and strip .fna extension
name=`echo $genome | sed 's:.*/::' | sed 's/.fna//'`

# run dbcan on genome
python /LAB_DATA/DATABASES/dbCAN_meta_server/run_dbcan.py --cluster --out_dir ${name} --out_pre ${name}_ ${genome} prok

# generate consensus counts by calls
python /LAB_DATA/DATABASES/dbCAN_meta_server/generate_dbCAN_consensus_and_counts.py ${name} --out_pre ${name}_ --min_tools 2


