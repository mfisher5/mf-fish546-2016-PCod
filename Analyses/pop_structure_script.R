### R script to test population - specific HWE 
###-----from Fish 444 Population Structure lab
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
# path below
#######################################################################################

setwd("D:/Pacific cod/DataAnalysis")

#######################################################################################
# D. Import a Genepop file of the data and save it in the form of a "genind" object  (this is the adegenet package)
#######################################################################################

codL1L2_genepop <- read.genepop("L1L2stacks_m10/batch_1.filtered_MAF_MissingLoci_Individs.gen")  
summary(codL1L2_genepop) 

## note that there are 120 individuals in the file: POH = 28, GE15 = 33, NAM = 16, YS = 7, BOR = 3, GE14 = 32, SM = 1


#######################################################################################
# F. Separate the entire data set into genind objects for each population
# (this is using the adegenet package)
#######################################################################################

# First create a vector containing the population assignments of each individual;
# numbers in code are numbers of individuals in each population
pop_labels <- c(rep("POH",28),rep("GE15",33),
  rep("NAM",16),rep("YS",7),rep("BOR",3),rep("GE14",32),
  rep("SM",1))  

# Create genind objects for each population
pops_separated <- seppop(codL1L2_genepop,pop=pop_labels)

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
summary_POH <- summary(data_POH)
mean(summary_POH$Hexp)
mean(summary_POH$Hobs)

# Test whether Hobs and Hexp are significantly different
t.test(summary_POH$Hobs,summary_POH$Hexp,paired=TRUE)  

# Do the same for all of the other populations
summary_BOR <- summary(data_BOR)
mean(summary_BOR$Hexp)
mean(summary_BOR$Hobs)
t.test(summary_BOR$Hobs,summary_BOR$Hexp,paired=TRUE)

summary_GE15 <- summary(data_GE15)
mean(summary_GE15$Hexp)
mean(summary_GE15$Hobs)
t.test(summary_GE15$Hobs,summary_GE15$Hexp,paired=TRUE)

summary_NAM <- summary(data_NAM)
mean(summary_NAM$Hexp)
mean(summary_NAM$Hobs)
t.test(summary_NAM$Hobs,summary_NAM$Hexp,paired=TRUE)

summary_YS <- summary(data_YS)
mean(summary_YS$Hexp)
mean(summary_YS$Hobs)
t.test(summary_YS$Hobs,summary_YS$Hexp,paired=TRUE)

summary_GE14 <- summary(data_GE14)
mean(summary_GE14$Hexp)
mean(summary_GE14$Hobs)
t.test(summary_GE14$Hobs,summary_GE14$Hexp,paired=TRUE)

summary_SM <- summary(data_SM)
mean(summary_SM$Hexp)
mean(summary_SM$Hobs)
t.test(summary_SM$Hobs,summary_SM$Hexp,paired=TRUE)