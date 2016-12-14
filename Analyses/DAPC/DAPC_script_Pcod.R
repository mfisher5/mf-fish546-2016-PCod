######================ R CODE FOR CREATING DAPC PLOTS ==================#####


## MF 12/13/2016
## Based off of Charlie Waters' DAPC and PCA code 

# First set working directory
setwd("D:/Pacific cod/DataAnalysis/Analyses")

# Load all necessary R packages
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

###################################################################################
# Let's first run a DAPC with all individuals and all loci

## read in genepop
koreaL1L2 <-read.genepop("../L1L2stacks_m10/batch_1.filtered_MAF_MissingLoci_Individs.gen")
summary(koreaL1L2)

## note that there are 114 individuals in the file: POH = 27, GE15 = 32, NAM = 15, YS = 6, BOR = 2, GE14 = 31, SM = 1


Pohang15 <- rep("POH",27)
Geoje15 <- rep("GE15",32)
Namhae15 <- rep("NAM",15)
YellowSea16 <- rep("YS",6)
Boryeong07 <- rep("BOR",2)
Geoje14 <- rep("GE14",31)
SocMuk <- rep("SM",1)


pop_groups <- as.factor(c(rep("POH",28),rep("GE15",33),rep("NAM",16),rep("YS",7),rep("BOR",3),rep("GE14",32),rep("SM",1)))
pop_labels <- c(Pohang15, Geoje15, Namhae15, YellowSea16, Boryeong07, Geoje14, SocMuk)
pop_cols <- c("aquamarine4","deepskyblue","darkorchid1","sienna2","red","deepskyblue","black")

## run dapc
dapc_all <- dapc(koreaL1L2,koreaL1L2$pop,n.pca=465,n.da=7) ##Retain all, then identify optimal number by optim.a.score
## find optimal number of principal components
test_a_score <- optim.a.score(dapc_all)
## run dapc only on optimal number of principal components
dapc_all <- dapc(koreaL1L2,koreaL1L2$pop,n.pca=12,n.da=7) ##21 PC's is the optimal number

#2D plot WITH ALL POPULATIONS
scatter(dapc_all,scree.da=FALSE,cellipse=0,leg=FALSE,label=c("POH","GE15","NAM","YS","BOR","GE14","SM"), posi.da="bottomleft",csub=2,col=pop_cols,cex=1.5,clabel=1,pch=c(15,19,17,18,8,1,4),solid=1)
legend(x = -4.5, y = 4,bty='n', legend = c("Pohang `15", "Geoje `15", "Namhae `15", "Yellow Sea `16", "Boryeong `07", "Geoje `14", "Sokcho+Mukho `15-`16"),pch=c(15,19,17,18,8,1,4),col=pop_cols,cex=1.1)

#2D plot WITH CLUSTERING
test_snpzip<-snpzip(koreaL1L2,dapc_all,loading.plot=TRUE,method="median") 

############################################################################################################

## Run DAPC on all samples EXCEPT Yellow Sea and Boryeong. 

koreaL1L2_noYSBOR <-read.genepop("../L1L2stacks_m10/batch_1.filtered_MAF_MissingLoci_Individs_noYS_noBOR.gen")
summary(koreaL1L2_noYSBOR)
## note that there are 106 individuals in the file: POH = 27, GE15 = 32, NAM = 15, GE14 = 31, SM = 1

Pohang15 <- rep("POH",27)
Geoje15 <- rep("GE15",32)
Namhae15 <- rep("NAM",15)
Geoje14 <- rep("GE14",31)
SocMuk <- rep("SM",1)



pop_groups <- as.factor(c(rep("POH",27),rep("GE15",32),rep("NAM",15),rep("GE14",31),rep("SM",1)))
pop_labels <- c(Pohang15, Geoje15, Namhae15, Geoje14, SocMuk)
pop_cols <- c("aquamarine4","deepskyblue","darkorchid1","deepskyblue","black")

## run dapc
dapc_noYSBOR <- dapc(koreaL1L2_noYSBOR,koreaL1L2_noYSBOR$pop,n.pca=465,n.da=5) ##Retain all, then identify optimal number by optim.a.score
## find optimal number of principal components
test_a_score <- optim.a.score(dapc_noYSBOR)
## run dapc only on optimal number of principal components
dapc_noYSBOR <- dapc(koreaL1L2_noYSBOR,koreaL1L2_noYSBOR$pop,n.pca=71,n.da=5) ##71 PC's is the optimal number

#2D plot EXCLUDING YS, BORYEONG
scatter(dapc_noYSBOR,scree.da=FALSE,cellipse=0,leg=FALSE,label=c("POH","GE15","NAM","GE14","SM"), posi.da="bottomleft",csub=2,col=pop_cols,cex=1.5,clabel=1,pch=c(15,19,17,1,4),solid=1)
legend(x=4,y=4,bty='n', legend = c("Pohang `15", "Geoje `15", "Namhae `15", "Geoje `14", "Sokcho+Mukho `15-`16"),pch=c(15,19,17,1,4),col=pop_cols,cex=1.1)

#2D plot WITH CLUSTERING
test_snpzip<-snpzip(koreaL1L2_noYSBOR,dapc_noYSBOR,loading.plot=TRUE,method="median") 

###########################################################################################################

## Run DAPC on all samples EXCEPT Yellow Sea and Boryeong, with 300ng replicates parsed out as their OWN population

koreaL1L2_noYSBOR_300ng <-read.genepop("../L1L2stacks_m10/batch_1.filtered_MAF_MissingLoci_Individs_noYS_noBOR_300ng.gen")
summary(koreaL1L2_noYSBOR_300ng)
## note that there are 106 individuals in the file: POH = 27, GE15 = 32, NAM = 15, GE14 = 21, GE14_300 = 10, SM = 1

Pohang15 <- rep("POH",27)
Geoje15 <- rep("GE15",32)
Namhae15 <- rep("NAM",15)
Geoje14 <- rep("GE14",21)
Geoje14_300ng <- rep("GE14_300", 10)
SocMuk <- rep("SM",1)



pop_groups <- as.factor(c(rep("POH",27),rep("GE15",32),rep("NAM",15),rep("GE14",21),rep("GE14_300ng", 10), rep("SM",1)))
pop_labels <- c(Pohang15, Geoje15, Namhae15, Geoje14, Geoje14_300ng, SocMuk)
pop_cols <- c("aquamarine4","deepskyblue","darkorchid1","deepskyblue","dodgerblue3", "black")

## run dapc
dapc_noYSBOR_300ng <- dapc(koreaL1L2_noYSBOR_300ng,koreaL1L2_noYSBOR_300ng$pop,n.pca=465,n.da=6) ##Retain all, then identify optimal number by optim.a.score
## find optimal number of principal components
test_a_score <- optim.a.score(dapc_noYSBOR_300ng)
## run dapc only on optimal number of principal components
dapc_noYSBOR_300ng <- dapc(koreaL1L2_noYSBOR_300ng,koreaL1L2_noYSBOR_300ng$pop,n.pca=53,n.da=6) ##53 PC's is the optimal number

#2D plot EXCLUDING YS, BORYEONG
scatter(dapc_noYSBOR_300ng,scree.da=FALSE,cellipse=0,leg=FALSE,label=c("POH","GE15","NAM","GE14", "GE14_300ng","SM"), posi.da="bottomleft",csub=2,col=pop_cols,cex=1.5,clabel=1,pch=c(15,19,17,1,1,4),solid=1)
legend(x=3.5,y=4,bty='n', legend = c("Pohang `15", "Geoje `15", "Namhae `15", "Geoje `14", "Geoje `14 300ng", "Sokcho+Mukho `15-`16"),pch=c(15,19,17,1,1,4),col=pop_cols,cex=1.1)

#2D plot WITH CLUSTERING
test_snpzip<-snpzip(koreaL1L2_noYSBOR_300ng,dapc_noYSBOR_300ng,loading.plot=TRUE,method="median") 
############################################################################################################