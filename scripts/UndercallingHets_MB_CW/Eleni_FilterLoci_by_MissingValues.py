### Eleni Petrou
#python Eleni_FilterLoci_by_MissingValues.py Marr15_batch1_filteredMAF_genotypes.csv Marr15_batch1_FinalCleanOutput.csv Marr15_batch1_FinalBlacklisted_output.csv

import sys

# Open your files for reading and writing
genotypes_file = open(sys.argv[1],'r')
clean_output_file = open(sys.argv[2],'w')
blacklisted_output_file = open(sys.argv[3], 'w')


# Tell the computer that your files have headers
header = True

for mystring in genotypes_file:										# Read in each line in the file as a string
	if header:														# This code takes the header from the original genotypes file and saves it as the header of the output genotypes files. We do not remove any individuals in this script so we can keep the original headers
		genotypes_header = mystring
		clean_output_file.write(genotypes_header)
		blacklisted_output_file.write(genotypes_header)
		header = False
	else:
		#print mystring
		stripped_string = mystring.strip('\n')						## Make sure to strip your string of the newline, otherwise weird stuff might happen. 
		locus_name = stripped_string.split(",")[0] 					## This tells the computer how to split your string. If csv, use comma. This saves the locus name. 
		#print locus_name
		#locus_freqs = []
		#bad_locus_freqs = []
		
		# Specifying which individuals belong in each population
		# Rule = [excel column -1 : excel column]
		Pcod = stripped_string.split(",")[1:55]			### BE VERY CAREFUL!!Change column indices to fit your file . IF csv, specify comma use. This saves the genotypes associated with each locus. Remember arguments start at 0 .GOES UP TO BUT NOT INCLUDING SEVEN!!! 


		#print QlBy12_10minNaOCl_ampurebeads 						###CHECK THIS OUTPUT TO MAKE SURE YOU DID NOT FUCK UP!!
		
		## Counting occurrences of missing data per locus in each population
		Count_MissingGenotypesByLocus_Pco = float(Pcod.count("0"))
		NumberOf_Pcod_individuals = float(len(Pcod15))
		Percent_MissingData_Pcod = float(Count_MissingGenotypesByLocus_Pcod/NumberOf_Pcod_individuals)

		

		
		
		# Checks for toy data sets
		#myList = [Percent_MissingData_MaIn, Percent_MissingData_RivIn, Percent_MissingData_SpCh, Percent_MissingData_SpCh14_10minNaOCl, Percent_MissingData_QlBy12_10minNaOCl, Percent_MissingData_SpCh01_10minNaOCl, Percent_MissingData_SpCh14_10minNaOCl_ampurebeads, Percent_MissingData_QlBy12_10minNaOCl_ampurebeads]
		#print myList
		
		if (Percent_MissingData_Pcod  > 0.49):
			#print "Fuck! missing data!"
			blacklisted_output_file.write(mystring)
		else:
			#print "all good!"
			clean_output_file.write(mystring)
		
		
	


	

		
		
		
		
		
# Close files

genotypes_file.close()
clean_output_file.close()
blacklisted_output_file.close()
