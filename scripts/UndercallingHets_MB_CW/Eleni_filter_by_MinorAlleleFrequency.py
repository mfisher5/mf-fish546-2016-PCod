### Eleni Petrou
### June 15, 2015
### This script takes an input haplotype file with loci in rows and individuals in columns and calculated the allele frequencies for each allele at
### each locus. This script is based on Charlie's MAF_corrected_gebotypes script
#cd /mnt/hgfs/D/sequencing_data/Herring_PopulationStructure/output_stacks
#python Eleni_filter_by_MinorAlleleFrequency.py

## MF edited 12/9/2016 for P.cod


import sys

# Open your files for reading and writing
genotypes_file = open("batch1_corrected_genotypes_genepop_transposed.txt",'r')
output_freqs = open("batch1_filteredMAF.csv",'w')
filtered_genotypes = open("batch1_filteredMAF_genotypes.csv",'w')
blacklisted_genotypes = open("batch1_blacklistedMAF_genotypes.csv" ,'w')
blacklisted_MAF = open("batch1_blacklistedMAF.csv",'w')

# Tell the computer that your files have headers
header = True

# This code creates a list of each allele for each population. This will be the headers for the file that outputs the allele frequencies. Modify as needed. 
MAF_header = str("Locus" + '\t' +  
"Allele1_PortGamble2014" + '\t' + "Allele2_PortGamble2014" + '\t' +
"Allele1_CherryPoint2014" + '\t' + "Allele2_CherryPoint2014" + '\t' +
"Allele1_QuilceneBay2014" + '\t' + "Allele2_QuilceneBay2014"+ '\t' +
"Allele1_PortOrchard2014" + '\t' + "Allele2_PortOrchard2014" + '\t' +
"Allele1_SimilkBay2015" + '\t' + "Allele2_SimilkBay2015" + '\t' + 
"Allele1_SquaxinPass2014" + '\t' + "Allele2_SquaxinPass2014" + '\t' + 
"Allele1_ElliotBay2015" + '\t' + "Allele2_ElliotBay2015" + '\t' +
"Allele1_CherryPoint2016" + '\t' + "Allele2_CherryPoint2016" )
output_freqs.write(MAF_header + '\n')
blacklisted_MAF.write(MAF_header + '\n')



for mystring in genotypes_file:							# Read in each line in the file as a string
	if header:											# This code takes the header from the original genotypes file and saves it as the header of the output genotypes files. We do not remove any individuals in this script so we can keep the original headers
		genotypes_header = mystring
		filtered_genotypes.write(genotypes_header)
		blacklisted_genotypes.write(genotypes_header)
		header = False
	else:
		#print mystring
		stripped_string = mystring.strip('\n')					## Make sure to strip your string of the newline, otherwise weird stuff might happen. 
		locus = stripped_string.split(",")[0] 					## This tells the computer how to split your string. If csv, use comma. This saves the locus name. 
		locus_freqs = []
		bad_locus_freqs = []
		#print locus
		# Specifying which individuals belong in each population
		# Rule = [excel column -1 : excel column]
		### BE VERY CAREFUL!!Change column indices to fit your file . IF csv, specify comma use. This saves the genotypes associated with each locus. Remember arguments start at 0 .GOES UP TO BUT NOT INCLUDING SEVEN!!! 
		PortGamble2014 = stripped_string.split(",")[1:36]
		QuilceneBay2014  = stripped_string.split(",")[36:65]
		SimilkBay2015 = stripped_string.split(",")[65:112]
		CherryPoint2014 = stripped_string.split(",")[112:149]
		PortOrchard2014 = stripped_string.split(",")[149:194]		
		SquaxinPass2014 = stripped_string.split(",")[194:238]
		ElliotBay2015 = stripped_string.split(",")[238:284]
		CherryPoint2016 = stripped_string.split(",")[238:334]
		print SquaxinPass2014 [1:4]
		
		 
		###CHECK THIS OUTPUT TO MAKE SURE YOU DID NOT FUCK UP!!

		## Counting occurrences of hets and homos in each population
		
		CountOf_homo1_PortGamble2014 = float(PortGamble2014.count("0101"))
		CountOf_homo2_PortGamble2014 = float(PortGamble2014.count("0202"))
		CountOf_het_PortGamble2014 = float(PortGamble2014.count("0102"))
		#print CountOf_homo1_PortGamble2014
		
		CountOf_homo1_CherryPoint2014 = float(CherryPoint2014.count("0101"))	
		CountOf_homo2_CherryPoint2014 = float(CherryPoint2014.count("0202"))
		CountOf_het_CherryPoint2014 = float(CherryPoint2014.count("0102"))
		
		CountOf_homo1_QuilceneBay2014 = float(QuilceneBay2014.count("0101"))
		CountOf_homo2_QuilceneBay2014 = float(QuilceneBay2014.count("0202"))
		CountOf_het_QuilceneBay2014 = float(QuilceneBay2014.count("0102"))
		
		CountOf_homo1_PortOrchard2014 = float(PortOrchard2014.count("0101"))	
		CountOf_homo2_PortOrchard2014 = float(PortOrchard2014.count("0202"))
		CountOf_het_PortOrchard2014 = float(PortOrchard2014.count("0102"))
		
		CountOf_homo1_SimilkBay2015 = float(SimilkBay2015.count("0101"))
		CountOf_homo2_SimilkBay2015 = float(SimilkBay2015.count("0202"))
		CountOf_het_SimilkBay2015 = float(SimilkBay2015.count("0102"))
		
		CountOf_homo1_SquaxinPass2014 = float(SquaxinPass2014.count("0101"))	
		CountOf_homo2_SquaxinPass2014 = float(SquaxinPass2014.count("0202"))
		CountOf_het_SquaxinPass2014 = float(SquaxinPass2014.count("0102"))
		
		CountOf_homo1_ElliotBay2015 = float(ElliotBay2015.count("0101"))
		CountOf_homo2_ElliotBay2015 = float(ElliotBay2015.count("0202"))
		CountOf_het_ElliotBay2015 = float(ElliotBay2015.count("0102"))
		
		CountOf_homo1_CherryPoint2016 = float(CherryPoint2016.count("0101"))
		CountOf_homo2_CherryPoint2016 = float(CherryPoint2016.count("0202"))
		CountOf_het_CherryPoint2016 = float(CherryPoint2016.count("0102"))
		

		# Calculating allele frequencies for each population.  Add 0.00001 so you don't divide by zero.
		total_alleles_SimilkBay2015=2*(CountOf_homo1_SimilkBay2015 + CountOf_homo2_SimilkBay2015 + CountOf_het_SimilkBay2015 + 0.000000001) 
		FrequencyOf_allele1_SimilkBay2015 = ((2 * CountOf_homo1_SimilkBay2015) + (CountOf_het_SimilkBay2015)) / (total_alleles_SimilkBay2015) 
		FrequencyOf_allele2_SimilkBay2015 = ((2 * CountOf_homo2_SimilkBay2015) + (CountOf_het_SimilkBay2015)) / (total_alleles_SimilkBay2015)
		
		total_alleles_PortGamble2014=2*(CountOf_homo1_PortGamble2014 + CountOf_homo2_PortGamble2014 + CountOf_het_PortGamble2014 + 0.000000001)  
		FrequencyOf_allele1_PortGamble2014 = ((2 * CountOf_homo1_PortGamble2014) + (CountOf_het_PortGamble2014)) / (total_alleles_PortGamble2014) 
		FrequencyOf_allele2_PortGamble2014 = ((2 * CountOf_homo2_PortGamble2014) + (CountOf_het_PortGamble2014)) / (total_alleles_PortGamble2014)
		
		total_alleles_QuilceneBay2014=2*(CountOf_homo1_QuilceneBay2014 + CountOf_homo2_QuilceneBay2014 + CountOf_het_QuilceneBay2014 + 0.000000001)  
		FrequencyOf_allele1_QuilceneBay2014 = ((2 * CountOf_homo1_QuilceneBay2014) + (CountOf_het_QuilceneBay2014)) / (total_alleles_QuilceneBay2014) 
		FrequencyOf_allele2_QuilceneBay2014 = ((2 * CountOf_homo2_QuilceneBay2014) + (CountOf_het_QuilceneBay2014)) / (total_alleles_QuilceneBay2014)
		
		total_alleles_SquaxinPass2014=2*(CountOf_homo1_SquaxinPass2014 + CountOf_homo2_SquaxinPass2014 + CountOf_het_SquaxinPass2014 + 0.000000001)  
		FrequencyOf_allele1_SquaxinPass2014 = ((2 * CountOf_homo1_SquaxinPass2014) + (CountOf_het_SquaxinPass2014)) / (total_alleles_SquaxinPass2014) 
		FrequencyOf_allele2_SquaxinPass2014 = ((2 * CountOf_homo2_SquaxinPass2014) + (CountOf_het_SquaxinPass2014)) / (total_alleles_SquaxinPass2014)
		
		total_alleles_CherryPoint2014=2*(CountOf_homo1_CherryPoint2014 + CountOf_homo2_CherryPoint2014 + CountOf_het_CherryPoint2014 + 0.000000001)  
		FrequencyOf_allele1_CherryPoint2014 = ((2 * CountOf_homo1_CherryPoint2014) + (CountOf_het_CherryPoint2014)) / (total_alleles_CherryPoint2014) 
		FrequencyOf_allele2_CherryPoint2014 = ((2 * CountOf_homo2_CherryPoint2014) + (CountOf_het_CherryPoint2014)) / (total_alleles_CherryPoint2014)
		
		total_alleles_PortOrchard2014=2*(CountOf_homo1_PortOrchard2014 + CountOf_homo2_PortOrchard2014 + CountOf_het_PortOrchard2014 + 0.000000001)  
		FrequencyOf_allele1_PortOrchard2014 = ((2 * CountOf_homo1_PortOrchard2014) + (CountOf_het_PortOrchard2014)) / (total_alleles_PortOrchard2014) 
		FrequencyOf_allele2_PortOrchard2014 = ((2 * CountOf_homo2_PortOrchard2014) + (CountOf_het_PortOrchard2014)) / (total_alleles_PortOrchard2014)
		
		total_alleles_ElliotBay2015=2*(CountOf_homo1_ElliotBay2015 + CountOf_homo2_ElliotBay2015 + CountOf_het_ElliotBay2015 + 0.000000001) 
		FrequencyOf_allele1_ElliotBay2015 = ((2 * CountOf_homo1_ElliotBay2015) + (CountOf_het_ElliotBay2015)) / (total_alleles_ElliotBay2015) 
		FrequencyOf_allele2_ElliotBay2015 = ((2 * CountOf_homo2_ElliotBay2015) + (CountOf_het_ElliotBay2015)) / (total_alleles_ElliotBay2015)
		
		total_alleles_CherryPoint2016=2*(CountOf_homo1_CherryPoint2016 + CountOf_homo2_CherryPoint2016 + CountOf_het_CherryPoint2016 + 0.000000001) 
		FrequencyOf_allele1_CherryPoint2016 = ((2 * CountOf_homo1_CherryPoint2016) + (CountOf_het_CherryPoint2016)) / (total_alleles_CherryPoint2016) 
		FrequencyOf_allele2_CherryPoint2016 = ((2 * CountOf_homo2_CherryPoint2016) + (CountOf_het_CherryPoint2016)) / (total_alleles_CherryPoint2016)
		
		#print FrequencyOf_allele2_CherryPoint2016
		
		
	
		if ((FrequencyOf_allele1_SimilkBay2015 >= 0.05) or (FrequencyOf_allele1_PortGamble2014 >= 0.05) \
			or (FrequencyOf_allele1_QuilceneBay2014 >= 0.05) or (FrequencyOf_allele1_SquaxinPass2014 >= 0.05) \
			or (FrequencyOf_allele1_CherryPoint2014 >= 0.05) or (FrequencyOf_allele1_PortOrchard2014 >= 0.05) or (FrequencyOf_allele1_ElliotBay2015 >= 0.05) or (FrequencyOf_allele1_CherryPoint2016 >= 0.05) )\
			and ((FrequencyOf_allele2_SimilkBay2015 >= 0.05) or (FrequencyOf_allele2_PortGamble2014 >= 0.05) \
			or (FrequencyOf_allele2_QuilceneBay2014 >= 0.05) or (FrequencyOf_allele2_SquaxinPass2014 >= 0.05) \
			or (FrequencyOf_allele2_CherryPoint2014 >= 0.05) or (FrequencyOf_allele2_PortOrchard2014 >= 0.05) or (FrequencyOf_allele2_ElliotBay2015 >=
			0.05) or (FrequencyOf_allele2_CherryPoint2016 >= 0.05)):    
			
			locus_freqs.append(locus+'\t'+
			str(FrequencyOf_allele1_PortGamble2014) + '\t' + str(FrequencyOf_allele2_PortGamble2014) + '\t' +
			str(FrequencyOf_allele1_CherryPoint2014) + '\t' + str(FrequencyOf_allele2_CherryPoint2014) + '\t' +
			str(FrequencyOf_allele1_QuilceneBay2014) + '\t' + str(FrequencyOf_allele2_QuilceneBay2014) + '\t' +
			str(FrequencyOf_allele1_PortOrchard2014) + '\t' + str(FrequencyOf_allele2_PortOrchard2014) + '\t' +
			str(FrequencyOf_allele1_SimilkBay2015) + '\t' + str(FrequencyOf_allele2_SimilkBay2015) + '\t' +
			str(FrequencyOf_allele1_SquaxinPass2014) + '\t' + str(FrequencyOf_allele2_SquaxinPass2014) + '\t' +
			str(FrequencyOf_allele1_ElliotBay2015) + '\t' + str(FrequencyOf_allele2_ElliotBay2015) + '\t' + 
			str(FrequencyOf_allele1_CherryPoint2016) + '\t' + str(FrequencyOf_allele2_CherryPoint2016))
			
			
			locus_write = str(locus_freqs).replace('[','').replace(',','\t').replace(']', '').replace("'", '').replace(' ','').replace('\\n','').replace('\\t','\t')		
			output_freqs.write(locus_write + '\n')
			filtered_genotypes.write(mystring)
		else:
			bad_locus_freqs.append(locus+'\t'+ 
			str(FrequencyOf_allele1_PortGamble2014) + '\t' + str(FrequencyOf_allele2_PortGamble2014) + '\t' +
			str(FrequencyOf_allele1_CherryPoint2014) + '\t' + str(FrequencyOf_allele2_CherryPoint2014) + '\t' +
			str(FrequencyOf_allele1_QuilceneBay2014) + '\t' + str(FrequencyOf_allele2_QuilceneBay2014) + '\t' +
			str(FrequencyOf_allele1_PortOrchard2014) + '\t' + str(FrequencyOf_allele2_PortOrchard2014) + '\t' +
			str(FrequencyOf_allele1_SimilkBay2015) + '\t' + str(FrequencyOf_allele2_SimilkBay2015) + '\t' +
			str(FrequencyOf_allele1_SquaxinPass2014) + '\t' + str(FrequencyOf_allele2_SquaxinPass2014) + '\t' +
			str(FrequencyOf_allele1_ElliotBay2015) + '\t' + str(FrequencyOf_allele2_ElliotBay2015) + '\t' +
			str(FrequencyOf_allele1_CherryPoint2016) + '\t' + str(FrequencyOf_allele2_CherryPoint2016))
			
			bad_locus_write = str(bad_locus_freqs).replace('[','').replace(',','\t').replace(']', '').replace("'", '').replace(' ','').replace('\\n','').replace('\\t','\t')
			print bad_locus_write
			blacklisted_MAF.write(bad_locus_write + '\n')
			blacklisted_genotypes.write(mystring)

#close open files
genotypes_file.close()			
blacklisted_genotypes.close()
blacklisted_MAF.close()
filtered_genotypes.close()
output_freqs.close()
