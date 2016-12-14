## Oyster DNA methylation

This note is for the class homework on DNA methylation data analysis using a single oyster sample. 


**Setting up the Alignment on CoGe**

Went to CoGe site and logged in >> `My Data`

Created a new experiment using the `new` button on the left of the website. 
![image](https://github.com/mfisher5/mf-fish546-2016/blob/master/DNA_Methylation/NewExperiment.png)

Added the link to the data under the `Data` tab for the new experiments

*Options:* Keep all of the defaults except: 
- Aligner Bismark (methylation)
- enable methylation analysis
- Add results to a new notebook
<br>
<br>
<br>

**Finding an interesting region**

On the CoGe website, I opened the notebook for this project and looked at the data... 
<br>
![picture](https://github.com/mfisher5/mf-fish546-2016/blob/master/DNA_Methylation/Genome_data.png)
<br>
<br>
And added in the stacked reads using the dropdown arrow on the right side. 
![picture](https://github.com/mfisher5/mf-fish546-2016/blob/master/DNA_Methylation/methylation_region_sequences.png)

<br>
The lighter blue bars show areas of methylation.
Zooming in on those regions, and hovering over them with the mouse, I can see more information on which areas are methylated, and the type of methylation (CpG, CHH, CHG). 

![methylation data](https://github.com/mfisher5/mf-fish546-2016/blob/master/DNA_Methylation/Methylation_data.png)


<br>
<br>
The region on **scaffold 770:** base pairs 28531 - 28826 has a lot of methylation. I chose to specifically look at sequence *HWI-C00124:164:C7URDANXX:2:2313:4364:51321_1:N:0:AGTTCC* ==
`GATATACGTACGATAGGATAGGATTTACGTACGATACGATAGGATATACGT`

![sequence picture](https://github.com/mfisher5/mf-fish546-2016/blob/master/DNA_Methylation/methylation_region_sequence1.png)

<br>
<br>
**BLAST alignment to Atlantic cod**

*default using megablast, optimized for highly similar sequences*

I used the NCBI BLASTn website to align the above sequence to all Atlantic cod (by copying the sequence from CoGe notebook into the BLAST query box). 

No significantly similar sequences were found. 
<br>

I tried another BLAST search for the following sequences, *optimized for somewhat similar sequences (blastn) rather than highly similar sequences (megablast)*::  

*HWI-C00124:164:C7URDANXX:2:1101:3794:60422_1:N:0:AGTTCC* == `ATATTCACGATAAACCTAATAAACGCAAAACCCGATAAACGATCTTAG` <br>(scaffold 770)


One alignment: Gadus morhua mRNA for T-cell receptor beta chain, clone T1-71 (L-V-D-J-C)
![blast output pic](https://github.com/mfisher5/mf-fish546-2016/blob/master/DNA_Methylation/blast_vAcod.png)



I wasn't very impressed with this E value, so I tried aligning to an invertebrate as well...

**BLAST alignment to Atlantic oyster**

Not a great e value here either!
![blast output pic](https://github.com/mfisher5/mf-fish546-2016/blob/master/DNA_Methylation/blast_vOyster.png)
