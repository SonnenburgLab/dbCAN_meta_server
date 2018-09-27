##################################################
# CGCFinder v3
#
# Rewriten for dbCAN2
#
# Written by Tanner Yohe under the supervision of
# Dr. Yin at NIU
#
# Last Update on Aug 2 2018
#
##################################################


import argparse
import csv
import sys
import re

#set up argument parser
parser = argparse.ArgumentParser(description='CAZyme Gene Cluster Finder')

parser.add_argument('gffFile', help='GFF file containing genome information')
parser.add_argument('--distance', '-d', type=int, choices=[0,1,2,3,4,5,6,7,8,9,10], default=2, help='The distance allowed between two signature genes')
parser.add_argument('--siggenes', '-s', choices=['all', 'tp', 'tf'], default='all', help='Signature genes types required. all=CAZymes,TC,TF; tp=CAZymes,TC; tf=CAZymes,TF')
parser.add_argument('--output', '-o', default='none', help='Output file name. If none specified, standard out')

args = parser.parse_args()


#open output file
if args.output == 'none':
	out = sys.stdout
else:
	out = open(args.output, 'w+')

#global vars
cluster = [0, 0, 0] #cazyme, tp, tf
num_clusters = 0

#define boolean function to determine if a cluster meets cluster requirements
def isCluster(): 
	global cluster
	if args.siggenes == 'all':
		if cluster[0] > 0 and cluster[1] > 0 and cluster[2] > 0:
			return True
	elif args.siggenes == 'tf':
		if cluster[0] > 0 and cluster[2] > 0:
			return True
	elif args.siggenes == 'tp':
		if cluster[0] > 0 and cluster[1] > 0:
			return True
	else:
		print('Warning: invalid siggenes argument')
	return False

#define boolean function to detemine if a gene is important (a signature gene)
def isImportant(gene):
	if gene == 'CAZyme':
		return True
	else:
		if gene == 'TC' and (args.siggenes == 'tp' or args.siggenes == 'all'):
			return True
		if gene == 'TF' and (args.siggenes == 'tf' or args.siggenes == 'all'):
			return True
	return False

def isSigGene(gene):
	if gene == 'CAZyme' or gene == 'TC' or gene == 'TF':
		return True
	else:
		return False
		
#define function to increase the cluster count
def increaseClusterCount(gene):
	global cluster
	if gene == 'CAZyme':
		cluster[0] += 1
	elif gene == 'TC':
		cluster[1] += 1
	elif gene == 'TF':
		cluster[2] += 1
	else:
		print("Warning: increaseClusterCount was called on bad functional domain")

#define function to search for a cluster once an important gene has been found
#this function also handles output
def startSearch(startRow, contig):
	global cluster
	global num_clusters
	dis = args.distance
	index = startRow
	between = 0
	lastImportant = 0
	while index < len(contig):
		index += 1
		fd = contig[index][2]
		if isImportant(fd):
			increaseClusterCount(fd)
			lastImportant = index
			between = 0
		else:
			between += 1
		if between > dis or index >= (len(contig)-1):
			if isCluster():
				num_clusters += 1
				#output file columns
				#geneNumber type[2] downDis upDis CGC# contig[0] geneStart[3] geneEnd[4] geneID[8,ID] direc[6] note[8]
				for j in range(startRow, lastImportant + 1):
					fd = contig[j][2]
					if isSigGene(fd):
						upDown = findNear(contig, j)
						notes = contig[j][8].split(";")
						ID= ""
						for note in notes:
							if "ID" in note:
								ID = note.split("=")[1]
						global genome
						row = [str(j), fd, str(upDown[1]), str(upDown[0]), 'CGC'+str(num_clusters), contig[j][0], contig[j][3], contig[j][4], ID, contig[j][6], contig[j][8]]
					else:
						notes = contig[j][8].split(";")
						ID= ""
						for note in notes:
							if "ID" in note:
								ID = note.split("=")[1]
						row = [str(j), 'null', 'null', 'null', 'CGC'+str(num_clusters), contig[j][0], contig[j][3], contig[j][4], ID, contig[j][6]]
					try:
						row.append(contig[j][8])
					except:
						pass
					out.write('\t'.join(row) + '\n')
				out.write('+++++' + '\n')
			cluster = [0, 0, 0]
			return index
			
#define function to find how close important genes are to each other
def findNear(contig, index):
	vals = ['null', 'null']
	k = index - 1
	l = index + 1
	while k >= 0:
		if isImportant(contig[k][2]):
			vals[0] = index - k - 1
			break
		else:
			k -= 1
	while l <= len(contig) - 1:
		if isImportant(contig[l][2]):
			vals[1] = l - index - 1
			break
		else:
			l += 1
	return vals


#load contig into an array 
contigs = {}
with open(args.gffFile) as f:
	for line in f:
		row = line.rstrip().split('\t')
		if row[0] not in contigs:
			contigs[row[0]] = []
		contigs[row[0]].append(row)


#loop through contig
for key in contigs:
	contig = contigs[key]
	i = 0
	while i < len(contig) - 1:
		#print contig[i]
		fd = contig[i][2]
		if isImportant(fd):
			increaseClusterCount(fd)
			i = startSearch(i, contig)
		else:
			i += 1

			
if args.output != 'none':
	out.close()

