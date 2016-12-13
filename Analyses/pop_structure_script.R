### R script from Fish 444 Population Structure lab
### Charlie Waters 4/21/2016

## Edited MF 12/8/2016 for Korean Pcod


#######################################################################################
# A. Install each of the following packages
# To minimize the chance of errors, press Ctrl+Enter (or Run) for 
# each line separately (I don't know why but it helps)
#######################################################################################

install.packages("ape")
install.packages("ade4")
install.packages("adegenet")
install.packages("diveRsity")
install.packages("doParallel")
install.packages("foreach")
install.packages("genetics")
install.packages("hierfstat")
install.packages("iterators")
install.packages("sendplot")
install.packages("httpuv")
install.packages("xlsx")
install.packages("pegas")
install.packages("plotrix")


#######################################################################################
# B. Load the installed packages into R for use
# Again, press Ctrl+Enter (or Run) for each line separately
#######################################################################################

library(ape)
library(ade4)
library(adegenet)
library(diveRsity)
library(doParallel)
library(foreach)
library(genetics)
library(hierfstat)
library(httpuv)
library(iterators)
library(sendplot)
library(xlsx)
library(pegas)
library(plotrix)

#######################################################################################
# C. Now set the working directory to a specific folder by typing the folder 
# path below, or by navigating to a specific folder using the menu above 
# by going to Session > Set Working Directory > Choose Directory 
#######################################################################################

setwd("D:/Pacific cod/DataAnalysis")

#######################################################################################
# D. Import a Genepop file of the data and save it as the object "cod_data_genepop" 
# in the form of a "genind" object  (this is the adegenet package)
#######################################################################################

cod_data_genepop <- read.genepop("L1L2stacks_m10/batch_1_forR.gen")  

#######################################################################################
# E. Look at a summary of the data, including number of individuals per population, 
# alleles per locus, Ho and He per pop.(this is the adegenet package)
#######################################################################################

summary(cod_data_genepop)  

#######################################################################################
# F. Separate the entire data set into genind objects for each population
# (this is using the adegenet package)
#######################################################################################

# First create a vector containing the population assignments of each individual;
# numbers in code are numbers of individuals in each population
pop_labels <- c(rep("POH",28),rep("GE15",33),
  rep("NAM",16),rep("YS",7),rep("BOR",3),rep("GE14",33),
  rep("SM",12))  

# Create genind objects for each population
pops_separated <- seppop(cod_data_genepop,pop=pop_labels)

# Verify that the new object contains each population
names(pops_separated)

# Create a genind object comprising only the AD individuals
data_BOR <-pops_separated$BOR

# Verify that the genind object has the correct number of individuals and loci
data_BOR            

# Repeat for all populations
data_POH <-pops_separated$POH  
data_GE15 <-pops_separated$GE15
data_NAM <-pops_separated$NAM
data_YS <-pops_separated$YS
data_GE14 <-pops_separated$GE14
data_SM <-pops_separated$SM

# Compute observed and expected heterzygosity for each population over all loci
summary_AD <- summary(data_AD)
mean(summary_AD$Hexp)
mean(summary_AD$Hobs)

# Test whether Hobs and Hexp are significantly different
t.test(summary_AD$Hobs,summary_AD$Hexp,paired=TRUE)  

# Do the same for all of the other populations
summary_AI <- summary(data_AI)
mean(summary_AI$Hexp)
mean(summary_AI$Hobs)
t.test(summary_AI$Hobs,summary_AI$Hexp,paired=TRUE)

summary_AT <- summary(data_AT)
mean(summary_AT$Hexp)
mean(summary_AT$Hobs)
t.test(summary_AT$Hobs,summary_AT$Hexp,paired=TRUE)

summary_HS <- summary(data_HS)
mean(summary_HS$Hexp)
mean(summary_HS$Hobs)
t.test(summary_HS$Hobs,summary_HS$Hexp,paired=TRUE)

summary_JA <- summary(data_JA)
mean(summary_JA$Hexp)
mean(summary_JA$Hobs)
t.test(summary_JA$Hobs,summary_JA$Hexp,paired=TRUE)

summary_KI <- summary(data_KI)
mean(summary_KI$Hexp)
mean(summary_KI$Hobs)
t.test(summary_JA$Hobs,summary_JA$Hexp,paired=TRUE)

summary_KO <- summary(data_KO)
mean(summary_KO$Hexp)
mean(summary_KO$Hobs)
t.test(summary_KO$Hobs,summary_KO$Hexp,paired=TRUE)

summary_PS <- summary(data_PS)
mean(summary_PS$Hexp)
mean(summary_PS$Hobs)
t.test(summary_PS$Hobs,summary_PS$Hexp,paired=TRUE)

summary_SG <- summary(data_SG)
mean(summary_SG$Hexp)
mean(summary_SG$Hobs)
t.test(summary_SG$Hobs,summary_SG$Hexp,paired=TRUE)

summary_UP <- summary(data_UP)
mean(summary_UP$Hexp)
mean(summary_UP$Hobs)
t.test(summary_UP$Hobs,summary_UP$Hexp,paired=TRUE)

summary_WA <- summary(data_WA)
mean(summary_WA$Hexp)
mean(summary_WA$Hobs)
t.test(summary_WA$Hobs,summary_WA$Hexp,paired=TRUE)

##################################################################################################################################
# QUESTION:
# ARE THERE ANY POPULATIONS THAT SIGNIFICANTLY DEVIATE FROM HWE? IF SO, WHICH ONES?
##################################################################################################################################

#######################################################################################
# G. Now test for deviations from HWE at each locus within each population
# (this is using the pegas package)
#######################################################################################

HWE_AD <- hw.test(data_AD,B=10000) # Tests HWE based on Monte Carlo permutations
HWE_AD  # Just to see the actual results
HWE_AD_adj <- p.adjust(HWE_AD[,4],method='fdr') #adjust Monte Carlo p-values for multiple testing
which(HWE_AD_adj < 0.05) #Identify which loci are out of HWE using the adjusted p-values
HWE_AD <- cbind(HWE_AD,HWE_AD_adj) #Add the adjusted p-values to the original HWE results
HWE_AD

# Now repeat for all other populations
HWE_AI <- hw.test(data_AI,B=10000) 
HWE_AI_adj <- p.adjust(HWE_AI[,4],method='fdr')
which(HWE_AI_adj < 0.05)
HWE_AI <- cbind(HWE_AI,HWE_AI_adj)

HWE_AT <- hw.test(data_AT,B=10000) 
HWE_AT_adj <- p.adjust(HWE_AT[,4],method='fdr')
which(HWE_AT_adj < 0.05)
HWE_AT <- cbind(HWE_AT,HWE_AT_adj)

HWE_HS <- hw.test(data_HS,B=10000) 
HWE_HS_adj <- p.adjust(HWE_HS[,4],method='fdr')
which(HWE_HS_adj < 0.05)
HWE_HS <- cbind(HWE_HS,HWE_HS_adj)

HWE_JA <- hw.test(data_JA,B=10000) 
HWE_JA_adj <- p.adjust(HWE_JA[,4],method='fdr')
which(HWE_JA_adj < 0.05)
HWE_JA <- cbind(HWE_JA,HWE_JA_adj)

HWE_KI <- hw.test(data_KI,B=10000) 
HWE_KI_adj <- p.adjust(HWE_KI[,4],method='fdr')
which(HWE_KI_adj < 0.05)
HWE_KI <- cbind(HWE_KI,HWE_KI_adj)

HWE_KO <- hw.test(data_KO,B=10000) 
HWE_KO_adj <- p.adjust(HWE_KO[,4],method='fdr')
which(HWE_KO_adj < 0.05)
HWE_KO <- cbind(HWE_KO,HWE_KO_adj)

HWE_PS <- hw.test(data_PS,B=10000) 
HWE_PS_adj <- p.adjust(HWE_PS[,4],method='fdr')
which(HWE_PS_adj < 0.05)
HWE_PS <- cbind(HWE_PS,HWE_PS_adj)

HWE_SG <- hw.test(data_SG,B=10000) 
HWE_SG_adj <- p.adjust(HWE_SG[,4],method='fdr')
which(HWE_SG_adj < 0.05)
HWE_SG <- cbind(HWE_SG,HWE_SG_adj)

HWE_UP <- hw.test(data_UP,B=10000) 
HWE_UP_adj <- p.adjust(HWE_UP[,4],method='fdr')
which(HWE_UP_adj < 0.05)
HWE_UP <- cbind(HWE_UP,HWE_UP_adj)

HWE_WA <- hw.test(data_WA,B=10000) 
HWE_WA_adj <- p.adjust(HWE_WA[,4],method='fdr')
which(HWE_WA_adj < 0.05)
HWE_WA <- cbind(HWE_WA,HWE_WA_adj)

# concatenate all of the results 
HWE_all_pops <- cbind(HWE_AD,HWE_AI,HWE_AT,HWE_HS,HWE_JA,HWE_KI,
                      HWE_KO,HWE_PS,HWE_SG,HWE_UP,HWE_WA)

# write the results to a .csv file
write.csv(HWE_all_pops, file="HWE_results.csv")

#################################################################################################################################
# QUESTION: IS THERE ANY EVIDENCE FOR DEVIATIONS FROM HWE AT ANY OF THE LOCI? 
# BOLD THE LOCI IN THE .CSV FILE
##################################################################################################################################


######################################################################################################
# CODE FOR PART B - TEST FOR GENETIC DIFFERENTIATION BETWEEN PAIRS OF POPULATIONS 
######################################################################################################

# Test to see if population has a significant effect on genetic structure
#(A test for homogeneity across all populations)

# convert data for use in package "hierfstat"
data_hierfstat <- genind2hierfstat(cod_data_genepop)  

# Create a vector that assigns each individual (total 132) to one panmictic population
one_pop <- rep(1,132)

# Create a vector of the actual population (or subpopulation) assignments 
levels <- data_hierfstat[,1]  

# Create a data frame only of genotypes (formatted for hierfstat)
locus_data <- data_hierfstat[,2:12]

# Permute the populations and estimates G statistics 
testwithin <- test.within(locus_data,within=one_pop,test.lev=levels,nperm=1000) 
testwithin$p.val    # significance of the effect of populations on genetic differentiation

#################################################################################################################################
### QUESTION: 
###  Is there evidence that the samples comprise one single population?
##################################################################################################################################


######################################################################################################
# CODE FOR PART C - DERIVE GENETIC DISTANCES BETWEEN POPULATIONS (FST) 
######################################################################################################

# Calculate pairwise Fst per population
# Function in package "diveRsity" that calculates pairwise W&C's Fst; 
# Samples individuals with replacement to create a new dataset and recalculates Fst 
# repeats 500 times to generate a mean and 95% CI's 

pop_stats <- diffCalc(infile="cod_genepop.txt",outfile="Pairwise_Fst_diveRsity",fst=TRUE,pairwise=TRUE,bs_pairwise=TRUE,boots=500,para=FALSE) ##diveRsity package

# The function above produces a folder with four files. You can find 
# pairwise Fst values in the "pairwise.txt" file. Confidence intervals
# are found in the "bs_pairwise.txt" file.

#################################################################################################################################
# QUESTION: 
# EXAMINE THE CONFIDENCE INTERVALS FOR ALL PAIRWISE COMPARISIONS. 
# WHICH POPULATION PAIRWISE COMPARISONS ARE SIGNIFICANTLY DIFFERENT FROM ZERO? 
# HINT: THEY ARE DIFFERENT IF THEIR CI'S DO NOT INCLUDE ZERO
##################################################################################################################################

# Before lab, I took the list of actual pairwise Fst values 
# and transformed them into a simple pairwise matrix (file=Fst.csv). 
# Import this matrix now. 

pairwise_fst <- read.csv("Fst.csv",header=TRUE,row.names=1)
pairwise_fst

# Convert pairwise_fst to a distance object
fst <- as.dist(pairwise_fst) 
fst  # we'll use this matrix later in the lab analysis


######################################################################################################
# CODE FOR PART D - VISUALIZE THE DATA BY CONSTRUCTING A NEIGHBOR-JOINING TREE 
######################################################################################################

# Now let's make a phylogenetic tree!!
# We have to import actual genotypic data to construct 
# population distances and a phylogenetic tree
genotype_data <- read.csv("Genotype_data.csv",header=TRUE) 

# Remove the first column of the data file, 
# which contains the sample ID, so that the matrix only has genotypes
genotypes <- genotype_data[,2:12] 

# Create a vector containing the population assignments of each individual
pop_labels <- c(rep("POH",28),rep("GE15",33),
                rep("NAM",16),rep("YS",7),rep("BOR",3),rep("GE14",33),
                rep("SM",12))  

# Convert labels to "factor"
pops <- as.factor(pop_labels) 

# Convert genotypes to format compatible for use with phylogenetic tree 
# packages in R; stores data as gene frequencies
genet_file <- char2genet(genotypes,pops,complete=TRUE)  

# Compute Nei's distances between populations
Nei_dist <- dist.genet(genet_file,method=1)    

# View the distance matrix
Nei_dist 

# Construct a Neighbor-joining tree from the distance matrix
tree <- nj(Nei_dist) 

# Plot the Neighbor-joining tree
plot.phylo(tree)  

# Write a function to bootstap the NJ tree
func <- function(x) nj(dist.genet(char2genet(x,pops)))  
bootstraps <- boot.phylo(tree,genotypes,func,B=100,block=1,rooted=TRUE)

# Plot your original tree
plot.phylo(tree)    

# Add the bootstrap values from 
# the 100 trees made from randomly sampling your data
nodelabels(bootstraps)  
bootstraps

#################################################################################################################################
# SAVE THE IMAGE OF YOUR TREE FOR YOUR LAB WRITE-UP!!
##################################################################################################################################


###################################################################################################################################
# CODE FOR PART E - VISUALIZE THE DATA THROUGH MULTIDIMENSIONAL SCALING ANALYSIS (ALSO KNOWN AS A PRINCIPAL COORDINATES ANALYSIS)
##################################################################################################################################

# Conduct a Principal Coordinates Analysis on the Nei_dist matrix generated previously

# Conduct the PCoA; choose to retain 2 axes; ignore any warnings from R
pcoa<-dudi.pco(Nei_dist,scannf=FALSE,nf=2)  

# List the eigenvalues for the axes, which can be used to determine the proportion of variation explained by each axis
pcoa$eig

# Plot the populations on the first two axes
scatter(pcoa,xax=1,yax=2,clab.row=1,posieig="topright") 

# This code yields the proportion of 
# total variation explained by the x-axis in your plot
variance_explained1<-pcoa$eig[1]/sum(pcoa$eig)   
variance_explained1 

# This code yields the proportion of 
# total variation explained by the y-axis in your plot
variance_explained2<-pcoa$eig[2]/sum(pcoa$eig)   
variance_explained2

#################################################################################################################################
# SAVE THE IMAGE OF YOUR TREE FOR YOUR LAB WRITE-UP!!

# QUESTION: HOW MUCH VARIATION DOES THE X-AXIs EXPLAIN? THE Y-AXIS? 
# What population relationships are described by these axes?
##################################################################################################################################


###################################################################################################################################
# CODE FOR PART F - VISUALIZE THE DATA: 
# THE RELATIONSHIP BETWEEN GENETIC AND GEOGRAPHIC DISTANCE
##################################################################################################################################

# Read in the matix of geographic distances
geo_dists <- read.csv("geographic_distances.csv",header=TRUE,row.names=1)  

# convert to a distance object
geo_dist_object <- as.dist(geo_dists)
geo_dist_object
par(mar=c(5,5,5,5))
plot(geo_dist_object,fst,type='p',pch=19,col="blue",
  main="Genetic vs. Geographic Distance", xlab="Geographic Distance (km)",
  ylab="Genetic Distance (W&C Fst)",cex.main=2.5,cex.lab=2,cex.axis=2)

# Fit a linear model to the data
relationship <- lm(fst~geo_dist_object)  

# Gives the statistical results: the r-squared value and 
# the signficance of the explanatory variable
summary(relationship)     

# Plot the regression line to the graph of genetic vs. geographic distance
abline(relationship,lwd=3,col="black")  

# Add r-squared value to the plot
text(1500,0.08,labels="R-squared = 0.6735", cex=1.25)


#################################################################################################################################
# QUESTION: 
# WHAT IS THE R-SQUARED VALUE OF THE LINEAR MODEL?
# IS THERE A SIGNIFICANT RELATIONSHIP BETWEEN GENETIC DISTANCE 
# AND GEOGRAPHIC DISTANCE? 
##################################################################################################################################
