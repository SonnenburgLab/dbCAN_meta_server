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
`conda install natsort` inside of your activated anvio conda environment.  
