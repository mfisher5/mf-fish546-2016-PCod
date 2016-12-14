# mf-fish546-PCod
repo for bioinformatics course final project. 

This README reviews relevant information for final project only. for class notes, homeworks, and other class projects, please refer to this folder: [FISH546](https://github.com/mfisher5/mf-fish546-PCod/tree/master/FISH546)

<br>

## Project: Pacific cod around the Korean peninsula
<br>

The Korean peninsula is the southern edge of the Pacific cod's (*Gadus macrocephalus*) range in the western Pacific Ocean. Pacific cod used to be a productive domestic fishery for South Korea, but there have been recent declines and high variability in catch between fishing seasons. This has led to stock enhancement programs which release hatchery-raised juveniles and larvae. 

A better understanding of the genetic population structure of Pacific cod around the Korean peninsula can address two critical research needs of Korean fisheries management: (1) the correct way to subset the domestic fishery into separate stocks for assessment and policy, and (2) the creation of a quantitative genetic baseline (such as divergence between spawning aggregates, per aggregate heterozygosity, etc.) to allow for future monitoring of hatchery effects on the wild populations.
<br>
<br>
<br>
### Project Goal: Clarify population structure of Pacific cod spawning aggregates in South Korean waters 
![Sample information Map](https://github.com/mfisher5/mf-fish546-PCod/blob/master/Diagrams/SampleMaps.png)
*Figure: Map of Korean peninsula with sampled spawning aggregates marked. Samples were taken across two spawning seasons*

<br>

<br>


###Class Objectives: 

**(1) Become familiar with the `stacks` pipeline using Lane 1 sequence data**

*[Jupyter notebook](https://github.com/mfisher5/mf-fish546-PCod/blob/master/notebooks/Lane1data_full%20stacks%20pipeline.ipynb)*
<br>


  **(2) Optimize parameters for `stacks` pipeline**
  
       (a) Research previous papers / labmate work on parameters for c and ustacks, and come up with a list of parameter values to test. 

*[Evernote](https://www.evernote.com/shard/s650/sh/122752f1-9ab7-4f9b-a9af-0c3331617436/0c84d3e0f73055a6)*
       
       (b) Determine quantitative measures that will be used for comparing different batches of c/ustacks parameters
       
       (c) Run through stacks with the Lane 1 data
*Jupyter notebook [p1](https://github.com/mfisher5/mf-fish546-PCod/blob/master/notebooks/testing%20stacks/Testing%20stacks%20Parameters%20I%20.ipynb)*, *[p2](https://github.com/mfisher5/mf-fish546-PCod/blob/master/notebooks/testing%20stacks/Testing%20stacks%20Parameters%20II.ipynb)*
       
       (d) Analyze output to decide which parameters to use going forward 
*[Evernote](https://www.evernote.com/shard/s650/sh/138af148-ea28-416e-b79d-2550b2829d50/3dd0a2619d17e859)*

<br>
  **(3) Get a preliminary analysis of population structure between 7 populations in the Lanes 1 and 2 data.** *[Here is a helpful workflow diagram of population structure analysis](https://github.com/mfisher5/mf-fish546-2016/blob/master/Diagrams/PopGen_Workflow.md).*

      (a) Run through the full `stacks` pipeline with Lanes 1 and 2 data
*[Jupyter notebook](https://github.com/mfisher5/mf-fish546-PCod/blob/master/notebooks/Lanes%201%20and%202%20combined%20pipeline.ipynb)*

      (b) Obtain measures of population structure (paired and overall Fst), and conduct Discriminant Analysis of Principle Components (DAPC)
*[Jupyter notebook](https://github.com/mfisher5/mf-fish546-PCod/blob/master/notebooks/Lanes%201%20and%202%20combined%2C%20Analyses%20%2B%20Results.ipynb)*
<br>


  **(4) Compare sequencing output from 300ng and degraded DNA protocols to determine if these protocols will be used on the rest of the samples.**
  
*[Jupyter notebook](https://github.com/mfisher5/mf-fish546-PCod/blob/master/notebooks/Lanes%201%20and%202%20combined%2C%20Analyses%20%2B%20Results.ipynb)*

<br>
<br>
 
### Repository structure

**[RAW_DATA/](https://github.com/mfisher5/mf-fish546-PCod/tree/master/raw_data)**     *raw data from both sequencing lanes; FastQC on raw data; Flowcell Summaries from sequencing facility*

**[L1L2samplesT142/](https://github.com/mfisher5/mf-fish546-PCod/tree/master/L1L2samplesT142)**   *demultiplexed, quality filtered, and trimmed data from `process_radtags`*

**[samplesT142/](https://github.com/mfisher5/mf-fish546-PCod/tree/master/L1L2samplesT142)**   *demultiplexed, quality filtered, and trimmed data from `process_radtags`*

**[L1L2stacks_m10/](https://github.com/mfisher5/mf-fish546-PCod/tree/master/L1L2stacks_m10)**   *folder for `stacks` pipeline output, and output from end filtering steps. Uses samples from* L1L2samplesT142/

**[SCRIPTS/](https://github.com/mfisher5/mf-fish546-PCod/tree/master/scripts)**  *shell scripts to run stacks from command line, python scripts to generate shell scripts with repetitive code, barcode and population map files needed for `stacks`*
	
--[**UndercallingHets_MB_CW/**](https://github.com/mfisher5/mf-fish546-PCod/tree/master/scripts/UndercallingHets_MB_CW) *scripts that are used to conduct additional filtering on the output from `populations`. This includes creating genotype files at the end of the filtering steps to complete population structure analyses.*

**[NOTEBOOKS/](https://github.com/mfisher5/mf-fish546-PCod/tree/master/notebooks)**  *jupyter notebooks*

**[ANALYSES/](https://github.com/mfisher5/mf-fish546-PCod/tree/master/Analyses)** *output of analyses that are not included in stacks; ie. genepop analysis of population structure.*
	
--[**dapc/**](https://github.com/mfisher5/mf-fish546-PCod/tree/master/Analyses/DAPC) *scripts and graphs from R used to run DAPC analyses.*
    
--[**fastq_SeqComparisons/**](https://github.com/mfisher5/mf-fish546-PCod/tree/master/Analyses/FASTQ%20_SeqComparisons) *text files and R script used to compare the number of sequences between 500ng, 300ng, and degraded DNA samples output from `process_radtags`.*
	
--[**genepop/**](https://github.com/mfisher5/mf-fish546-PCod/tree/master/Analyses/Genepop) *output from genepop analyses; contains only examples, as genepop output files too large to store on github.*

[**DIAGRAMS/**](https://github.com/mfisher5/mf-fish546-2016/tree/master/Diagrams) *helpful pictures and diagrams linked in Jupyter notebooks, ie. sample site map and `genepop` executable screen*

<br>
<br>

