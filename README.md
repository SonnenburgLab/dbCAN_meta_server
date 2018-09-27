# dbCAN_meta_server
This repo contains code obtained from http://cys.bios.niu.edu/dbCAN2/download/

SignalP is not included here. See http://www.cbs.dtu.dk/cgi-bin/nph-sw_request?signalp.
## Setup
dbCAN meta server analyses need several dependencies in order to run, including:
- [Diamond](https://github.com/bbuchfink/diamond)
- [HMMER](http://hmmer.org)
- [natsort](https://natsort.readthedocs.io)
- [fraggenescan](https://sourceforge.net/projects/fraggenescan/)
One way to get all of the dependencies is to create a new conda environment.  
```
conda create -n dbcan -c bioconda python3 diamond hmmer natsort fraggenescan
```

Alternatively, if you plan on using this program with [anvi'o](http://merenlab.org/software/anvio/), you can just run
`conda install natsort fraggenescan` inside of your activated anvio conda environment. 

Next, you'll need to activate your new dbcan or existing anvio environment, go into the `db/` folder and run:
```
bash get_and_configure_db_files.sh
```

Everything is now ready to go!

## Running dbCAN_meta_server
To run this program, you can either add `/path/to/dbCAN_meta_server` to your `$PATH`, or just point to `run_dbcan.py`.
```
python /path/to/dbCAN_meta_server/run_dbcan.py
```
Running `run_dbcan.py` with no options (or with `-h`) will give you the usage instructions.

To run all analyses on a single prokaryote (`prok`) genome, just do:
```
python /path/to/run_dbcan.py --cluster --out_dir dbcan_output genome.fasta prok
```

To run all analyses on protein sequences, just do:
```
python /path/to/run_dbcan.py --cluster --gff gene_calls.gff --out_dir dbcan_output proteins.faa protein
```
