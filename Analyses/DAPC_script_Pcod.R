
setwd("D:/Pacific cod/DataAnalysis/Analyses")
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

?read.genepop


# Let's first run a DAPC with all individuals and all loci
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

dapc_all <- dapc(koreaL1L2,koreaL1L2$pop,n.pca=465,n.da=7) ##Retain all, then identify optimal number by optim.a.score
test_a_score <- optim.a.score(dapc_all)
dapc_all <- dapc(koreaL1L2,koreaL1L2$pop,n.pca=12,n.da=7) ##21 PC's is the optimal number

#2D plot WITH ALL POPULATIONS
scatter(dapc_all,scree.da=FALSE,cellipse=0,leg=FALSE,label=c("POH","GE15","NAM","YS","BOR","GE14","SM"), posi.da="bottomleft",csub=2,col=pop_cols,cex=1.5,clabel=1,pch=c(15,19,17,18,8,1,4),solid=1)
legend(x = -4.5, y = 4,bty='n', legend = c("Pohang `15", "Geoje `15", "Namhae `15", "Yellow Sea `16", "Boryeong `07", "Geoje `14", "Sokcho+Mukho `15-`16"),pch=c(15,19,17,18,8,1,4),col=pop_cols,cex=1.1)


test_snpzip<-snpzip(koreaL1L2,dapc_all,loading.plot=TRUE,method="median") 
?snpzip
############################################################################################################

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

dapc_noYSBOR <- dapc(koreaL1L2_noYSBOR,koreaL1L2_noYSBOR$pop,n.pca=465,n.da=5) ##Retain all, then identify optimal number by optim.a.score
test_a_score <- optim.a.score(dapc_noYSBOR)
dapc_noYSBOR <- dapc(koreaL1L2_noYSBOR,koreaL1L2_noYSBOR$pop,n.pca=71,n.da=5) ##71 PC's is the optimal number

#2D plot EXCLUDING YS, BORYEONG
scatter(dapc_noYSBOR,scree.da=FALSE,cellipse=0,leg=FALSE,label=c("POH","GE15","NAM","GE14","SM"), posi.da="bottomleft",csub=2,col=pop_cols,cex=1.5,clabel=1,pch=c(15,19,17,1,4),solid=1)
legend(x=4,y=4,bty='n', legend = c("Pohang `15", "Geoje `15", "Namhae `15", "Geoje `14", "Sokcho+Mukho `15-`16"),pch=c(15,19,17,1,4),col=pop_cols,cex=1.1)

test_snpzip<-snpzip(koreaL1L2_noYSBOR,dapc_noYSBOR,loading.plot=TRUE,method="median") 

###########################################################################################################


PUT 300NG GEOJE 14 SAMPLES AS SEPARATE SAMPLES


############################################################################################################