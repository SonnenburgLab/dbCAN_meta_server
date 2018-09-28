##########################################################
# This script takes the output directory from run_dbcan.py
# and exports a functions file that anvio can import.
# Written by Bryan Merrill
##########################################################
import os
import argparse
import csv

parser = argparse.ArgumentParser(description='Turn anvio gene calls (generated using anvi-export-gene-calls) for **proteins only** into GFF3 format suitable for dbCAN analysis.')
parser.add_argument('inputFile', help='Anvio gene calls file. Exports file with *.gff added.')
args = parser.parse_args()

genecalls = args.inputFile
gff = os.path.basename(genecalls)+".gff"

with open(genecalls, 'r') as inFile, open(gff, 'w') as outFile:
	outFile.write("##gff-version 3\n")
	gff_writer = csv.writer(outFile, delimiter = '\t')
	line = inFile.readline()
	line = inFile.readline()
	while line != "":
		line = line.strip().split()
		contig = line[1]
		source = line[6]
		start = int(line[2])+1
		stop = line[3]
		strand = line[4].replace('f','+').replace('r','-')
		ID = "ID="+str(line[0])
		if source != "Ribosomal_RNAs":
			gff_writer.writerow([line[1], line[6], "CDS", str(start), str(stop), ".", strand, ".", ID])
		line = inFile.readline()
inFile.close()
outFile.close()