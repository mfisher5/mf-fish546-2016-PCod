## Analyses ##

This folder contains analyses completed on `stacks` pipeline output for Lanes 1 and 2 combined data.  

This includes *(1)* R scripts used to run the analyses, *(2)* excel spreadsheets with summary tables and data, *(3)* text files with summary tables, *(4)* graphs and figures from excel and R. 

<br>
<br>
*R scripts* 

`pop_structure_script.R` : heterozygosity calculations and HWE testing

`DAPC/DAPC_script_Pcod.R` : running and plotting DAPC analyses

<br>
*Excel documents* 

`L1L2_SortedTotalSeqCounts.ods` : full list of samples and their sequence counts from process_radtags FASTQ output files. sorted by population, used to determine cstacks catalog samples. 

`PopGen_Stats.xlsx` : tables with population genetic summary data -  He, Ho, HWE p values, Fis values, pairwise Fst

`SeqLociCounts_Analysis_L1L2` : Data, charts, and summary tables looking at how total # sequences and total # loci changed through the pipeline