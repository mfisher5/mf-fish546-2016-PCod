####################### batch 303 #######################
batch_303Het <- read.delim("D:/Pacific cod/DataAnalysis/UCstacksL1/populations/batch_303Het.txt")
head(batch_303Het)
#create a vector of unique loci
uniqueloci <- unique(batch_303Het$Locus.ID)

#create two empty vectors
Het.o <- c()
Het.e <- c()

#for loop to calculate per locus observed and expected heterozygosity
for (locus in uniqueloci) {
  temp.df <- subset(batch_303Het, Locus.ID == locus, c("Obs.Het", "Exp.Het"))
  temp.He <- mean(temp.df$Obs.Het)
  temp.Ho <- mean(temp.df$Exp.Het)
  end = length(Het.o)
  Het.o <- append(Het.o, temp.Ho, end)
  Het.e <- append(Het.e, temp.He, after=length(Het.o))
}

#vector for the difference between observed and expected heterozygosity
Het.diff <- Het.o - Het.e

#create data frame of all vectors
MeanHeterozygosity_303 <- cbind(uniqueloci, Het.o, Het.e, Het.diff)

#write dataframe to file
write.table(MeanHeterozygosity_303, file = "batch303_meanHet.txt", row.names = FALSE)


####################### batch 330 #######################
batch_330Het <- read.delim("D:/Pacific cod/DataAnalysis/UCstacksL1/populations/batch_330Het.txt")
head(batch_303Het)
#create a vector of unique loci
uniqueloci <- unique(batch_330Het$Locus.ID)
#create two empty vectors
Het.o <- c()
Het.e <- c()
#for loop to calculate per locus observed and expected heterozygosity
for (locus in uniqueloci) {
  temp.df <- subset(batch_330Het, Locus.ID == locus, c("Obs.Het", "Exp.Het"))
  temp.He <- mean(temp.df$Obs.Het)
  temp.Ho <- mean(temp.df$Exp.Het)
  end = length(Het.o)
  Het.o <- append(Het.o, temp.Ho, end)
  Het.e <- append(Het.e, temp.He, after=length(Het.o))
}
#vector for the difference between observed and expected heterozygosity
Het.diff <- Het.o - Het.e
#create data frame of all vectors
MeanHeterozygosity_330 <- cbind(uniqueloci, Het.o, Het.e, Het.diff)
#write dataframe to file
write.table(MeanHeterozygosity_330, file = "batch330_meanHet.txt", row.names = FALSE)


####################### batch 1030 #######################
batch_1030Het <- read.delim("D:/Pacific cod/DataAnalysis/UCstacksL1/populations/batch_1030Het.txt")
head(batch_1030Het)
#create a vector of unique loci
uniqueloci <- unique(batch_1030Het$Locus.ID)
#create two empty vectors
Het.o <- c()
Het.e <- c()
#for loop to calculate per locus observed and expected heterozygosity
for (locus in uniqueloci) {
  temp.df <- subset(batch_1030Het, Locus.ID == locus, c("Obs.Het", "Exp.Het"))
  temp.He <- mean(temp.df$Obs.Het)
  temp.Ho <- mean(temp.df$Exp.Het)
  end = length(Het.o)
  Het.o <- append(Het.o, temp.Ho, end)
  Het.e <- append(Het.e, temp.He, after=length(Het.o))
}
#vector for the difference between observed and expected heterozygosity
Het.diff <- Het.o - Het.e
#create data frame of all vectors
MeanHeterozygosity_1030 <- cbind(uniqueloci, Het.o, Het.e, Het.diff)
#write dataframe to file
write.table(MeanHeterozygosity_1030, file = "batch1030_meanHet.txt", row.names = FALSE)



####################### DATA COMPARISONS #######################

#compare differences in observed heterozygosity, by locus


colnames(MeanHeterozygosity_1030) <- paste(c("locus", "m.Obs.Het", "m.Exp.Het", "Obs-Exp.Het"))
colnames(MeanHeterozygosity_303) <- paste(c("locus", "m.Obs.Het", "m.Exp.Het", "Obs-Exp.Het"))
colnames(MeanHeterozygosity_330) <- paste(c("locus", "m.Obs.Het", "m.Exp.Het", "Obs-Exp.Het"))

par(mfrow = c(1,3))
  #m3 v. m5
merged_Het <- merge(MeanHeterozygosity_330, MeanHeterozygosity_303, by.x = "locus", by.y = "locus", all = FALSE, suffixes = c(".m3", ".m5"))
head(merged_Het)
Obs.3v5 <- merged_Het$m.Obs.Het.m5 - merged_Het$m.Exp.Het.m3
boxplot(Obs.3v5, ylab = "Obs.Het.m5 - Obs.Het.m3")

  #m5 v. m10
merged_Het2 <- merge(MeanHeterozygosity_303, MeanHeterozygosity_1030, by.x = "locus", by.y = "locus", all = FALSE, suffixes = c(".m5", ".m10"))
Obs.5v10 <- merged_Het2$m.Obs.Het.m10 - merged_Het2$m.Exp.Het.m5
boxplot(Obs.5v10, ylab = "Obs.Het.m10 - Obs.Het.m5")

  #m3 v. m10
merged_Het3 <- merge(MeanHeterozygosity_330, MeanHeterozygosity_1030, by.x = "locus", by.y = "locus", all = FALSE, suffixes = c(".m3", ".m10"))
Obs.3v10 <- merged_Het3$m.Obs.Het.m10 - merged_Het3$m.Exp.Het.m3
boxplot(Obs.3v10, ylab = "Obs.Het.m10 - Obs.Het.m3")

names(merged_Het)

#visually compare all observed - expected per batch
par(mfrow = c(1,3), mar = c(5,4,4,1))
boxplot(merged_Het$`Obs-Exp.Het.m3`, main = "Batch 330", xaxt = "n", xlab = "", ylab = "Observed - Expected Heterozygosity")
boxplot(merged_Het$`Obs-Exp.Het.m5`, main = "Batch 303", xaxt = "n", xlab = "", yaxt = "n")
boxplot(merged_Het2$`Obs-Exp.Het.m10`, main = "Batch 1030", xaxt = "n", xlab = "", yaxt = "n")


#visually compare distribution of observed heterozygosities
par(mfrow = c(1,3))
boxplot(MeanHeterozygosity_330[,2], main = "Batch 330", xaxt = "n", xlab = "", ylab = "Observed Heterozygosity")
boxplot(MeanHeterozygosity_303[,2], main = "Batch 303", xaxt = "n", xlab = "", ylab = "Observe Heterozygosity")
boxplot(MeanHeterozygosity_1030[,2], main = "Batch 1030", xaxt = "n", xlab = "", ylab = "Observe Heterozygosity")
