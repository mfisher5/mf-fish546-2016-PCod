# DESeq2 in R : Differential Expression #



source("https://bioconductor.org/biocLite.R")
biocLite("DESeq2")
library(DESeq2)

# set working directory
setwd("D:/Pacific cod/DataAnalysis/mf-fish546-2016/TranscriptomeBLAST")


# import data downloaded from github in Jupyter notebook
data <- read.table("./data/Phel_countdata.txt", header = T, sep = "\t")
rownames(data) <- data$Feature
data <- data[,-1]
dim(data)


# build data frames for data with "treated" and control"
deseq2.colData <- data.frame(condition=factor(c(rep("Treated", 3), rep("Control", 3))), type=factor(rep("single-read", 6)))
rownames(deseq2.colData) <- colnames(data)
deseq2.dds <- DESeqDataSetFromMatrix(countData = data, colData = deseq2.colData, design = ~ condition)

# run differential expression analysis
deseq2.dds <- DESeq(deseq2.dds)
deseq2.res <- results(deseq2.dds)
deseq2.res <- deseq2.res[order(rownames(deseq2.res)), ]

head(deseq2.res)



# count the number of hits (when "treated," aka transcriptome of infected seasta, is compared against "control," aka healthy seastar) with adjusted p-value less than 0.05
dim(deseq2.res[!is.na(deseq2.res$padj) & deseq2.res$padj <= 0.05, ])


# plot results
tmp <- deseq2.res
#main plot
plot(tmp$baseMean, tmp$log2FoldChange, pch=19, cex=0.75, ylim=c(-3, 3), log="x", col="darkgray",
     main="DEG Virus Exposure  (pval <= 0.05)",
     xlab="mean of normalized counts",
     ylab="Log2 Fold Change")
#plotting significant points a different color
tmp.sig <- deseq2.res[!is.na(deseq2.res$padj) & deseq2.res$padj <= 0.05, ]
points(tmp.sig$baseMean, tmp.sig$log2FoldChange, pch=20, cex=0.75, col="deepskyblue")
# 2 FC lines
abline(h=c(-1,1), col="orangered")



#create tab-delimited table of genes that were differentially expressed
write.table(tmp.sig, "./data/Phel_DEGlist.tab", row.names = T)
