## Jupyter notebooks

**Purpose:** Contain command line code for class projects and for Korean Pacific cod project. Links to Evernote notes within the notebook [P.cod RADseq Data Processing](https://www.evernote.com/pub/mfisher5171/p.codradseqdataprocessing) are embedded in each notebook; Evernote has research / more in-depth explanation of work, as well as specific versions of python code or shells that may be changed when running a stacks program multiple times. 
<br>
<br>
<br>

**Contents:** 
<br>

`Lanes 1 and 2 combined pipeline.ipynb` : stacks v1.44. Stacks pipeline (process_radtags to populations) + additional filtering (biallelic loci, MAF, loci with missing data, individuals with missing data). 
<br>
<br>
`Lanes 1 and 2 combined, Analyses + Results` : stacks v1.44. Uses the outputs from the `Lanes 1 and 2 combined pipeline` notebook to run analyses on (1) population structure, (2) stacks pipeline, and (3) 300ng / degraded protocols. 
<br>
<br>
`Lane1data_full stacks pipeline.ipynb` : stacks v1.42. Stacks pipeline from process_radtags to sstacks for the first 60 P. cod samples that were sequenced (Lane 1, Illumina HiSeq 4000). Linked Evernote notebook contains helpful explanations of each step and visualizations of data. 
<br>
<br>
<br>
*TESTING STACKS/*
<BR>
`Testing stacks Parameters I.ipynb` : stacks v1.42. Full code for optimizing u- and cstacks parameters, 10/18/2016 to 11/3/2016
<br>
<br>
`Testing stacks Parameters II.ipynb` : stacks v1.42. Full code for finishing ustacks parameter -M, and for comparing outputs from different ustacks parameters, 11/7/2016
<br>
<br>
`stacks-Undercalling Heterozygotes I.ipynb` : stacks v1.42. Description of alternations and testing with additional filtering scripts from Marine Brieuc, for use with pstacks (with reference genome). 
<br>
<br>
`stacks-Undercalling Heterozygotes II.ipynb` : stacks v1.42. Description of alternations and testing with additional filtering scripts from Marine Brieuc, for use with cstacks (without reference genome). 
<br>
<br>
<br>
<br>
**Program Versions:**

(1) Virtual Machine: VMWare Workstation 12 Player, Ubuntu 64-bit. *used to run all command line arguments, including those from Jupyter notebooks, and any blast / bowtie alignemnts*

(2) Python 2.7.0

(3) Anaconda2 - 4.2.0

(4) RStudio 0.99.903 *run in Windows 10 environment*

(5) stacks v1.42 OR 1.44 (noted)


*information on HOW VMware and stacks pipeline were installed [here](http://www.evernote.com/l/Aoryz9urcLxDMKAbS8TjTle88gzwAKM56og/)
