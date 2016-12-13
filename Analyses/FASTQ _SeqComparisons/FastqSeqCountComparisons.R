###### Comparing the number of sequences in FastQ files AFTER process_radtags #######

################ DEGRADED DNA: TRIM TO 142 v. 110 ###################################
FastQseqCountsComparison_deg <- read.delim("D:/Pacific cod/DataAnalysis/Analyses/FastQseqCountsComparison_deg.txt")
attach(FastQseqCountsComparison_deg)

t.test(T_142, T_110, alternative = "two.sided", paired = TRUE)
# significantly different, p value = 0.00003965

t.test(pU_142, pU_110, alternative = "two.sided", paired = TRUE)
# significantly different, p value = 1.755 * 10^14

t.test(U_142, U_110, alternative = "two.sided", paired = TRUE)
# significantly different, p value = 0.00004772


################ 300NG v. 500NG DNA ##################################################
FastQseqCountsComparison_300V500 <- read.delim("D:/Pacific cod/DataAnalysis/Analyses/FastQseqCountsComparison_300V500.txt")
attach(FastQseqCountsComparison_300V500)
View(FastQseqCountsComparison_300V500)

t.test(FastQseqCountsComparison_300V500$T_500, FastQseqCountsComparison_300V500$T_300, alternative = "two.sided", paired = TRUE)
# significantly different, p value = 0.000104

t.test(FastQseqCountsComparison_300V500$pU_500, FastQseqCountsComparison_300V500$pU_300, alternative = "two.sided", paired = TRUE)
# NOT significantly different, p value = 0.2662

t.test(FastQseqCountsComparison_300V500$U_500, FastQseqCountsComparison_300V500$U_300, alternative = "two.sided", paired = TRUE)
# significantly different, p value = 0.0002014



################ 500NG GOOD V. DEG DNA ##################################################


t.test(FastQseqCountsComparison_300V500$T_500, FastQseqCountsComparison_deg$T_142, alternative = "two.sided", paired = FALSE)
# significantly different, p value = 1.29 E-6

t.test(FastQseqCountsComparison_300V500$pU_500, FastQseqCountsComparison_deg$pU_142, alternative = "two.sided", paired = FALSE)
# NOT significantly different, p value = 2.38 E-7

t.test(FastQseqCountsComparison_300V500$U_500, FastQseqCountsComparison_deg$U_142, alternative = "two.sided", paired = FALSE)
# significantly different, p value = 3.69 E-5


