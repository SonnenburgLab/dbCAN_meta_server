#!/bin/bash

# This script downloads and configures all of the database files
# needed to run the dbCAN meta server analyses.
# Run this script within the "db" directory
# You'll need to have diamond and hmmer in your PATH or
# in an active conda environment

wget http://cys.bios.niu.edu/dbCAN2/download/CAZyDB.07312018.fa
wget http://cys.bios.niu.edu/dbCAN2/download/dbCAN-HMMdb-V7.txt
wget http://cys.bios.niu.edu/dbCAN2/download/Databases/tcdb.fa
wget http://cys.bios.niu.edu/dbCAN2/download/Databases/tf.fa

diamond makedb --in CAZyDB.07312018.fa --db CAZy
diamond makedb --in tcdb.fa --db tcdb
diamond makedb --in tf.fa --db tf
ln -s dbCAN-HMMdb-V7.txt dbCAN.txt
hmmpress dbCAN.txt
