#!/bin/bash

# This script downloads and configures all of the database files
# needed to run the dbCAN meta server analyses.
# Run this script within the "db" directory
# You'll need to have diamond and hmmer in your PATH or
# in an active conda environment

wget https://bcb.unl.edu/dbCAN2/download/CAZyDB.09242021.fa
wget https://bcb.unl.edu/dbCAN2/download/dbCAN-HMMdb-V10.txt
wget http://bcb.unl.edu/dbCAN2/download/Databases/tcdb.fa
wget http://bcb.unl.edu/dbCAN2/download/Databases/tf.fa

diamond makedb --in CAZyDB.09242021.fa --db CAZy
diamond makedb --in tcdb.fa --db tcdb
diamond makedb --in tf.fa --db tf
ln -s dbCAN-HMMdb-V10.txt dbCAN.txt
hmmpress dbCAN.txt
