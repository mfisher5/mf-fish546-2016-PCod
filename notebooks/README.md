## Jupyter notebooks

**Purpose:** Contain command line code for class projects and for Korean Pacific cod project. Links to Evernote notes within the notebook [P.cod RADseq Data Processing](https://www.evernote.com/pub/mfisher5171/p.codradseqdataprocessing) are embedded in each notebook; Evernote has research / more in-depth explanation of work, as well as specific versions of python code or shells that may be changed when running a stacks program multiple times. 
<br>
<br>
<br>

**Contents:** 

`BLAST_SeaStarTranscriptome.ipynb` : class project. extracting differentially expressed genes from a seastar transriptome infected by wasting disease, and BLASTing the Atlantic cod transcriptome against these DEG
<br>
<br>
`Class Notebook.ipynb` : notes from guest lecturers in class. 
<br>
<br>
`DNA Methylation_Oysters.ipynb` : Class project visualizing methylation in oyster DNA using program IGV, and then blasting methylated sequences against Atlantic cod. 
<br>
<br>
`Lane1data_full stacks pipeline.ipynb` : Korean Pacific cod. Stacks pipeline from process_radtags to sstacks for the first 60 P. cod samples that were sequenced (Lane 1, Illumina HiSeq 4000). Linked Evernote notebook contains helpful explanations of each step and visualizations of data. 
<br>
<br>
`Testing stacks Parameters 10.21-22.ipynb` : Korean Pacific cod. Attempt to use Jupyter to optimize u- and cstacks parameters for later analysis of cod data. 
<br>
<br>
`Testing stacks Parameters I.ipynb` : Korean Pacific cod. Full code for optimizing u- and cstacks parameters, 10/18/2016 to 11/3/2016
<br>
<br>
`Testing stacks Parameters II.ipynb` : Korean Pacific cod. Full code for finishing ustacks parameter -M, and for comparing outputs from different ustacks parameters, 11/7/2016
<br>
<br>
`stacks-Undercalling Heterozygotes I.ipynb` : Korean Pacific cod. Description of alternations and testing with additional filtering scripts from Marine Brieuc, for use with pstacks (with reference genome). 
<br>
<br>
`stacks-Undercalling Heterozygotes II.ipynb` : Korean Pacific cod. Description of alternations and testing with additional filtering scripts from Marine Brieuc, for use with cstacks (without reference genome). 
<br>
<br>
`Lane2data_radtags to ustacks.ipynb` : Korean Pacific cod. Stacks pipeline from process_radtags to sstacks for the second 72 P. cod samples that were sequenced (Illumina HiSeq 4000). Includes assesssing the effectiveness of new protocols for use with 300ng or low quality DNA. Linked Evernote notebook contains visualizations of data. 
<br>
<br>
<br>
**Program Versions:**

(1) Virtual Machine: VMWare Workstation 12 Player, Ubuntu 64-bit. *used to run all command line arguments, including those from Jupyter notebooks, and any blast / bowtie alignemnts*

(2) Python 2.7.0

(3) Anaconda2 - 4.2.0

(4) RStudio 0.99.903 *run in Windows 10 environment*


*information on HOW VMware and stacks pipeline were installed [here](http://www.evernote.com/l/Aoryz9urcLxDMKAbS8TjTle88gzwAKM56og/)
