setwd("D:/Pacific cod/DataAnalysis/mf-fish546-2016/TranscriptomeBLAST")
Phel_DEGnames <- read.csv("Phel_DEGnames.txt", sep="", header = TRUE)
Phel_transcriptome <- read.delim("data/Phel_transcriptome_edited.txt", header=FALSE, comment.char="#")
names(Phel_DEGnames)[1] <- "DEGnames" #changed column heading
View(Phel_DEGnames)
Phel_transcriptome <- Phel_transcriptome[1:2]
names(Phel_transcriptome)[1:2] <- c("GeneNames", "Sequence") #changed column headings
View(Phel_transcriptome)

#merge the datasets by the gene names columns, don't include any genes from the transcriptome that were not in the DEGnames file. 
DEGsequences <- merge(x = Phel_DEGnames, y = Phel_transcriptome, by.x = "DEGnames", by.y = "GeneNames", all.x = TRUE, all.y = FALSE) 

View(DEGsequences)


write.table(DEGsequences, file = "Phel_DEGsequences.txt", sep = "\n", row.names = FALSE, col.names = FALSE)
