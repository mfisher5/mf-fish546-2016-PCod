### Eleni Petrou
#python Eleni_FilterLoci_by_MissingValues.py Marr15_batch1_filteredMAF_genotypes.csv Marr15_batch1_FinalCleanOutput.csv Marr15_batch1_FinalBlacklisted_output.csv

## MF edit 12/8/2016 for Lanes 1 and 2 Pcod samples

import sys

# Open your files for reading and writing
genotypes_file = open(sys.argv[1],'r')
clean_output_file = open(sys.argv[2],'w')
blacklisted_output_file = open(sys.argv[3], 'w')


# Tell the computer that your files have headers
header = True

for mystring in genotypes_file:		# Read in each line in the file as a string
	if header:			# This code takes the header from the original genotypes file and saves it as the header of the output genotypes files. We do not remove any individuals in this script so we can keep the original headers
		genotypes_header = mystring
		clean_output_file.write(genotypes_header)
		blacklisted_output_file.write(genotypes_header)
		header = False
	else:
		#print mystring
		stripped_string = mystring.strip('\n')		## Make sure to strip your string of the newline, otherwise weird stuff might happen. 
		locus_name = stripped_string.split(",")[0] 	## This tells the computer how to split your string. If csv, use comma. This saves the locus name. 
		#print locus_name
		#locus_freqs = []
		#bad_locus_freqs = []
		
		# Specifying which individuals belong in each population
		# Rule = [excel column -1 : excel column]
		Pohang = stripped_string.split(",")[1:28]
		Geoje15 = stripped_string.split(",")[28:61]
		Namhae = stripped_string.split(",")[62:77]
		YellowSea = stripped_string.split(",")[78:84]
		Boryeong = stripped_string.split(",")[85:87]
		Geoje14 = stripped_string.split(",")[88:120]
		SocMuk = stripped_string.split(",")[121:132]			

### BE VERY CAREFUL!!Change column indices to fit your file . IF csv, specify comma use. This saves the genotypes associated with each locus. Remember arguments start at 0 .GOES UP TO BUT NOT INCLUDING SEVEN!!! 


		#print QlBy12_10minNaOCl_ampurebeads 						###CHECK THIS OUTPUT TO MAKE SURE YOU DID NOT FUCK UP!!
		
		## Counting occurrences of missing data per locus in each population
		Count_MissingGenotypesByLocus_Pohang = float(Pohang.count("0"))
		NumberOf_Pohang_individuals = float(len(Pohang))
		Percent_MissingData_Pohang = float(Count_MissingGenotypesByLocus_Pohang/NumberOf_Pohang_individuals)
		
		# Checks for toy data sets
		#myList = [Percent_MissingData_MaIn, Percent_MissingData_RivIn, Percent_MissingData_SpCh, Percent_MissingData_SpCh14_10minNaOCl, Percent_MissingData_QlBy12_10minNaOCl, Percent_MissingData_SpCh01_10minNaOCl, Percent_MissingData_SpCh14_10minNaOCl_ampurebeads, Percent_MissingData_QlBy12_10minNaOCl_ampurebeads]
		#print myList
		

		if (Percent_MissingData_Pohang  > 0.49):
			print "Pohang -- Fuck! missing data!"
			blacklisted_output_file.write(mystring)
		else:
			#print "all good!"
			clean_output_file.write(mystring)
		
		#Geoje15
		Count_MissingGenotypesByLocus_Geoje15 = float(Geoje15.count("0"))
		NumberOf_Geoje15_individuals = float(len(Geoje15))
		Percent_MissingData_Geoje15 = float(Count_MissingGenotypesByLocus_Geoje15/NumberOf_Geoje15_individuals)
		

		if (Percent_MissingData_Geoje15  > 0.49):
			print "Geoje15 -- Fuck! missing data!"
			blacklisted_output_file.write(mystring)
		else:
			#print "all good!"
			clean_output_file.write(mystring)
		
		#Namhae
		Count_MissingGenotypesByLocus_Namhae = float(Namhae.count("0"))
		NumberOf_Namhae_individuals = float(len(Namhae))
		Percent_MissingData_Namhae = float(Count_MissingGenotypesByLocus_Namhae/NumberOf_Namhae_individuals)
		

		if (Percent_MissingData_Namhae  > 0.49):
			print "Namhae -- Fuck! missing data!"
			blacklisted_output_file.write(mystring)
		else:
			#print "all good!"
			clean_output_file.write(mystring)
		
		# YellowSea
		Count_MissingGenotypesByLocus_YellowSea = float(YellowSea.count("0"))
		NumberOf_YellowSea_individuals = float(len(YellowSea))
		Percent_MissingData_YellowSea = float(Count_MissingGenotypesByLocus_YellowSea/NumberOf_YellowSea_individuals)

		if (Percent_MissingData_YellowSea  > 0.49):
			print "YellowSea -- Fuck! missing data!"
			blacklisted_output_file.write(mystring)
		else:
			#print "all good!"
			clean_output_file.write(mystring)
		
		
		#Boryeong
		Count_MissingGenotypesByLocus_Boryeong = float(Boryeong.count("0"))
		NumberOf_Boryeong_individuals = float(len(Boryeong))
		Percent_MissingData_Boryeong = float(Count_MissingGenotypesByLocus_Boryeong/NumberOf_Boryeong_individuals)


		if (Percent_MissingData_YellowSea  > 0.49):
			print "boryeong -- Fuck! missing data!"
			blacklisted_output_file.write(mystring)
		else:
			#print "all good!"
			clean_output_file.write(mystring)
		
		#Geoje14
		Count_MissingGenotypesByLocus_Geoje14 = float(Geoje14.count("0"))
		NumberOf_Geoje14_individuals = float(len(Geoje14))
		Percent_MissingData_Geoje14 = float(Count_MissingGenotypesByLocus_Geoje14/NumberOf_Geoje14_individuals)

		if (Percent_MissingData_Geoje14  > 0.49):
			print "Geoje14 -- Fuck! missing data!"
			blacklisted_output_file.write(mystring)
		else:
			#print "all good!"
			clean_output_file.write(mystring)

		#SocMuk
			clean_output_file.write(mystring)


# Close files

genotypes_file.close()
clean_output_file.close()
blacklisted_output_file.close()
