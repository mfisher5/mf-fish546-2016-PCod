## TestingStacks

This folder contains all relevant directories, subdirectories, scripts, and small output files that were used to (1) test changes to stacks parameters, (2) test additional filtering scripts at the end of the `stacks` pipeline, and (3) manually check stacks output in version 1.44. 

**IMPORTANT::** This directory was created for organization purposes AFTER running all code in the Jupyter notebooks above. In order to replicate any analyses, extract all files / subdirectories from this folder and put them directly into the root directory, mf-fish546-PCod. 

<br>
<br>

*Subdirectories*

**[scripts/](https://github.com/mfisher5/mf-fish546-PCod/tree/master/TestingStacks/scripts)** all scripts run in the Jupyter notebooks below. used for stacks v1.42 AND v1.44

**[UCstacksL1](https://github.com/mfisher5/mf-fish546-PCod/tree/master/TestingStacks/UCstacksL1)** the `stacks`, `blast`, and `bowtie` output from changing parameter values in `ustacks` and `cstacks`. Uses Lane 1 sequencing data, stacks v1.44

**[L2samplesT110](https://github.com/mfisher5/mf-fish546-PCod/tree/master/TestingStacks/L2samplesT110)** Lane 2 samples produced with stacks v1.44, but ultimately not used.

**[L2samplesT142](https://github.com/mfisher5/mf-fish546-PCod/tree/master/TestingStacks/L2samplesT142)** Lane 2 samples used for testing stacks v1.44  

<br>

*The associated Jupyter notebooks are as follows:*

1. Testing changes to stacks parameters [part 1](https://github.com/mfisher5/mf-fish546-PCod/blob/master/notebooks/testing%20stacks/Testing%20stacks%20Parameters%20I%20.ipynb) and [part 2](https://github.com/mfisher5/mf-fish546-PCod/blob/master/notebooks/testing%20stacks/Testing%20stacks%20Parameters%20II.ipynb)

2. Practice runs of [post-populations filtering scripts](https://github.com/mfisher5/mf-fish546-PCod/tree/master/scripts/UndercallingHets_MB_CW) to account for stack's undercalling of heterozygotes (Notebook [here](https://github.com/mfisher5/mf-fish546-PCod/blob/master/notebooks/testing%20stacks/stacks%20-%20Undercalling%20Heterozygotes%20II.ipynb))

3. Testing the calling of genotypes in [stacks v1.44](https://github.com/mfisher5/mf-fish546-PCod/blob/master/notebooks/testing%20stacks/Testing%20stacks%20output%20v1.44.ipynb)

