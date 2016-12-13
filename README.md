# mf-fish546-2016
repo for bioinformatics course. 


## Project: Pacific cod around the Korean peninsula
<br>
<br>
The Korean peninsula is the southern edge of the Pacific cod's (*Gadus macrocephalus*) range in the western Pacific Ocean. Pacific cod used to be a productive domestic fishery for South Korea, but recent declines in catch have led to attempted stock enhancement programs. These programs release hatchery-raised juveniles and larvae. 

A better understanding of the genetic population structure of Pacific cod around the Korean peninsula can address two critical research needs of Korean fisheries management: (1) the correct way to subset the domestic fishery into separate stocks for assessment and policy, and (2) the creation of a quantitative genetic baseline (such as divergence between spawning aggregates, per aggregate heterozygosity, etc.) to allow for future monitoring of hatchery effects on the wild populations. 
<br>
<br>
<br>
### Project Goals: 
<br>
**(1)** Clarify population structure of spawning aggregates in South Korean coastal waters ([Sample information](https://github.com/mfisher5/mf-fish546-2016/blob/master/Diagrams/SampleMaps.png))
<br>

**(2)** Look at genomic architecture of population divergence by identifying islands of divergence (clusters of outlier loci)
  
#### Class goals: focusing within Project Goal Num. 1

**(1)** Optimize parameters for stacks pipeline

**(2)** Get a preliminary analysis of population structure between 3 populations in lane 1 data

*[Helpful workflow diagram of population structure analysis](https://github.com/mfisher5/mf-fish546-2016/blob/master/Diagrams/PopGen_Workflow.md)*


###Class Objectives: 

  **(1)** Optimize parameters for stacks pipeline
  
       (a) Research previous papers on parameters for c and ustacks, and come up with a list of parameter values to test
       
       (b) Determine quantitative measures that will be used for comparing different batches of c/ustacks parameters
       
       (c) Decide which parameters to use with the lane 1 data. 
  

  **(2)** Get a preliminary analysis of population structure between 3 populations in lane 1 data

      (a) Create a reference genome for lane 1 data using the optimized stacks parameters
      
      (b) Run through the full stacks pipeline with Lane 1 data
      
      (b) Obtain measures of population structure (paired and overall Fst), and identify outlier loci that are potentially under selection
       

 
### Repository structure
*(Goals for repository structure - in process of transferring files)*

**[RAW_DATA/](https://github.com/mfisher5/mf-fish546-2016/tree/master/raw_data)**     *raw data from all sequencing lanes*

**[L1samplesT142/](https://github.com/mfisher5/mf-fish546-2016/tree/master/samplesT142)**   *data separated by sample, from process_radtags, trimmed*
 
**[L1samplesT146/](https://github.com/mfisher5/mf-fish546-2016/tree/master/samplesT146)**   *data separated by sample, from process_radtags, not trimmed*

**[UCStacksL1/](https://github.com/mfisher5/mf-fish546-2016/tree/master/UCstacksL1)**   *folder for practice runs of ustacks and cstacks to identify appropriate parameters*
      
    stacks_base/
      
    stacks_M2/
     
    stacks_m3/ 
     
    etc...

**[SCRIPTS/](https://github.com/mfisher5/mf-fish546-2016/tree/master/scripts)**  *shell scripts to run stacks from command line, python scripts to generate shell scripts with repetitive code*

**[NOTEBOOKS/](https://github.com/mfisher5/mf-fish546-2016/tree/master/notebooks)**  *jupyter notebooks-- in progress as I transfer over material from evernote*

**ANALYSIS/** *output of analyses that are not included in stacks, ie. DAPC plot. Not complete.*


[**DIAGRAMS/**](https://github.com/mfisher5/mf-fish546-2016/tree/master/Diagrams) *helpful pictures and diagrams related to the Korean Pacific cod project, ie. sample site map


[**TranscriptomeBLAST/**](https://github.com/mfisher5/mf-fish546-2016/tree/master/TranscriptomeBLAST) *data and output of differential expression analysis for class project on the seastar transcriptome. 



### Project Timeline: 

#### Weeks 1 - 3: [Lane 1 full stacks pipeline](https://github.com/mfisher5/mf-fish546-2016/blob/master/notebooks/Lane1data_full%20stacks%20pipeline.ipynb)

   ~~(1) Become familiar with Lane 1 sequencing data~~
   
   ~~(2) Learn important steps in the stacks pipeline using Lane 1 data~~

#### Week 4: [Testing stacks Parameters](https://github.com/mfisher5/mf-fish546-2016/blob/master/notebooks/Testing%20stacks%20Parameters.ipynb)
  ~~(1) Finish running different varieties of ustack and cstacks:~~
  
  
  ~~(2) Run sstacks to align all individuals' sequences to each different catalog of loci generated in (1)~~
  
#### Week 5: [Testing stacks Parameters](https://github.com/mfisher5/mf-fish546-2016/blob/master/notebooks/Testing%20stacks%20Parameters.ipynb)

  ~~(1) Calculate heterozygosities for all of the data from Week 4, to compare parameters~~
  
  ~~(2) start bowtie processing BLAST filtering to build reference genome~~
  
#### Week 6: 
   (1) Repeat Week 5 comparisons made with *ustacks -m* parameter for the *ustacks -M* and *cstacks # individs in catalog*
   
   (2) Determine which quantitative measurements should matter the most when comparing parameter outputs. 
   

#### Week 7: 
   (1) Decide which parameters to use
   
   (2) Produce reference genome from lane 1 data

#### Week 8: 
   (1) Run sstacks of lane 1 data against the new reference genome
   
   (2) Begin population structure analyses
<br>
<br>


  
  








































