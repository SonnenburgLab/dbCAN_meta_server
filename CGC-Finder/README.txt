CGCFinder.py

Written by Tanner Yohe under the supervision of Dr. Yin in the Yin Lab at NIU

Rewritten specifcally for dbCAN meta server

Last updated 8/8/18

INPUT
CGCFinder accepts GFF3 format file. The Type column (3rd column) must contain
gene annotations (either TC, TF, CAZyme, or CDS).

RUNNING
python CGCFinder.py [inputFile] -d [distance] -s [signature genes] -o [output]
	[inputFile] - GFF format file.
	[distance] - Maximum distance between signature genes. Integer value between 0 and 10.
	[signature genes] - Which gene types must be in a cluster for it to be considered a CGC.
			Accepted values: all (CAZyme+TC+TF), tp (CAZyme+TC), tf (CAZyme+TF).
	[output] - Output file, default = standard out.

OUTPUT
The output file is a tab seperated file with the following columns:
[gene #] [signature gene type] [upstream distance] [downstream distance] [cluster #] [gene start] [gene end] [gene ID] [direction] [note]
	[gene #] - arbitrary number given to gene, starting with 1 given to the first gene in the input file
	[signature gene type] - The type of signature gene the gene is.
	[upstream distance] - The upstream distance to the next signature gene
	[downstream distance] - The downstream distance to the next signature gene
	[cluster #] - The number of the cluster that this gene belongs to
	[gene start] - start position of the gene
	[gene end] - end position of the gene
	[gene ID] - gene ID from the input file
	[direction] - (- or +)
	[note] - usually contains the ID of the gene that annotated this gene in a diamond blast
Each cluster is seperated by a line that contains five '+' symbols (+++++)

**NOTES**
The GFF file format supported by CGCFinder is GFF3, with Column 9 attributes delimited by a semi-colon, ";"
This is especially important in the case of recognizing the 'ID' attribute in Column 9 of GFF files
Please convert/format GFF files to GFF3 format (if they are not already) and ensure semi-colon delimiting in Column 9 for optimal performance

A more user friendly version of CGCFinder is avaliable at the dbCAN-meta server at cys.bio.niu.edu
