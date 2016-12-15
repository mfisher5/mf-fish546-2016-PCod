## UCstacksL1 ##

This folder is for testing parameters in u- and cstacks using the lane 1 data (subset, not including Yellow Sea samples, so n = 57). It contains:

(1) data from stacks runs for each parameter change (not limited to u- and cstacks output)

(2) shell scripts that were used to run stacks

(3) stacks reporting output (stderr) saved into text files. 
<br>
<br>
*Subdirectories*

**blast/** : NCBI's blast output when aligning catalog loci from `cstacks` to themselves. 
<br>
**bowtie/** : BOWTIE output when aligning catalog loci from `cstacks` to themselves. 
<br>
**populations/** : output from `populations` and altered files that were used to create the .fasta file for bowtie
<br>
**sstacks_batch/** : output from `sstacks` for each of the batches run when testing changes to `ustacks` or `cstacks` parameters
<br>
**stacks_param/** : output from `ustacks` and `cstacks` for each of the parameter changes

<br>


*The associated Jupyter notebooks*

Testing stacks Parameters [part 1](https://github.com/mfisher5/mf-fish546-PCod/blob/master/notebooks/testing%20stacks/Testing%20stacks%20Parameters%20I%20.ipynb) and [part 2](https://github.com/mfisher5/mf-fish546-PCod/blob/master/notebooks/testing%20stacks/Testing%20stacks%20Parameters%20II.ipynb)
