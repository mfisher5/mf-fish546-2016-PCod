import sys

# Open your files for reading and writing
genotypes_file = open(sys.argv[1],'r')
clean_output_file = open(sys.argv[2],'w')
blacklisted_output_file = open(sys.argv[3], 'w')

count = 0
bad_count = 0
for mystring in genotypes_file:		# Read in each line in the file as a string
	if count == 0: 
		genotypes_header = mystring
		clean_output_file.write(genotypes_header)
		blacklisted_output_file.write(genotypes_header)
		count += 1
	else:
		count += 1
		overall_percent_missingdata = []
		stripped_string = mystring.strip('\n')
		locus_name = stripped_string.split(",")[0]
		Pohang = stripped_string.split(",")[1:28]
		Geoje15 = stripped_string.split(",")[28:61]
		Namhae = stripped_string.split(",")[62:77]
		Geoje14 = stripped_string.split(",")[88:120]
#Pohang
		Count_MissingGenotypesByLocus_Pohang = float(Pohang.count("0000"))
		NumberOf_Pohang_individuals = float(len(Pohang))
		Percent_MissingData_Pohang = float(Count_MissingGenotypesByLocus_Pohang/NumberOf_Pohang_individuals)
		overall_percent_missingdata.append(Percent_MissingData_Pohang)


#Geoje15
		Count_MissingGenotypesByLocus_Geoje15 = float(Geoje15.count("0000"))
		NumberOf_Geoje15_individuals = float(len(Geoje15))
		Percent_MissingData_Geoje15 = float(Count_MissingGenotypesByLocus_Geoje15/NumberOf_Geoje15_individuals)
		overall_percent_missingdata.append(Percent_MissingData_Geoje15)


#Namhae
		Count_MissingGenotypesByLocus_Namhae = float(Namhae.count("0000"))
		NumberOf_Namhae_individuals = float(len(Namhae))
		Percent_MissingData_Namhae = float(Count_MissingGenotypesByLocus_Namhae/NumberOf_Namhae_individuals)
		overall_percent_missingdata.append(Percent_MissingData_Namhae)


#Geoje14
		Count_MissingGenotypesByLocus_Geoje14 = float(Geoje14.count("0000"))
		NumberOf_Geoje14_individuals = float(len(Geoje14))
		Percent_MissingData_Geoje14 = float(Count_MissingGenotypesByLocus_Geoje14/NumberOf_Geoje14_individuals)
		overall_percent_missingdata.append(Percent_MissingData_Geoje14)


		
		if all(i < 0.50 for i in overall_percent_missingdata):
			clean_output_file.write(mystring)
		else: 
			blacklisted_output_file.write(mystring)
			bad_count += 1
			

n_loci = str(count - 1)
print "processed " + n_loci + " loci" 
print "Number of loci removed: " + str(bad_count)

