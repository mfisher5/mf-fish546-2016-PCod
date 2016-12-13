#!/bin/bash

##### This shell script will count the number of sequences in gzipped fastq OR fasta files (raw data + post process_radtags) #####
## M. Fisher 12/1/2016 ##
## Starting within the file directory `DataAnalysis` ##

#Set Variables
POST_DATE=$(date '+%Y-%m-%d') #find the date and save as POST_DATE
OUTPUT_FILENAME="SequenceCounts.$POST_DATE.txt" #create output file that contains the date


#Ask for input from user
echo "Enter file directory. Note - must be subdirectory within current location ::"
read DIRECTORY 		#reads entry typed at command line as new variable "DIRECTORY"
echo "Is file type '.fa.gz' or '.fq.gz'?"
read FILE_TYPE 		#reads entry typed at command line as new variable "FILE_TYPE"
echo "--"
echo "--"

#(1) navigate to directory with process_radtags output (specified above)
cd $DIRECTORY
pwd

#(2) find all files that end in *fq.gz or *fa.gz (specified above) and save to array
echo "Searching for all $FILE_TYPE files..." 		#print message at command line that confirms the file type entered
file_array="$(find . -name "*$FILE_TYPE")" 			# find all files of that type using `find` command and save into a bash array


#(3) count number of sequences in each file (counted differently if fasta or fastq)
echo "Saving counts to $OUTPUT_FILENAME..." 		#print message at command line that confirms output filename
if [ "$FILE_TYPE" = ".fq.gz" ] 						#if files are fastq files, then for each file in the array...
then
	for file in $file_array
	do
		echo $file | tee -a $OUTPUT_FILENAME		#print the file name to the terminal and append to a new file
		zcat file | awk '((NR-2)%4==0){read=$1;total++;count[read]++}END{for(read in count){if(!max||count[read]>max) {max=count[read];maxRead=read};if(count[read]==1){unique++}};print total,unique,unique*100/total,maxRead,count[maxRead],count[maxRead]*100/total}' | tee -a $OUTPUT_FILENAME		#print the number of sequences to the terminal and append to the file. The first count is the total number of sequences; for meaning of other numbers, see Stephen Turner's github page, "Bioinformatics one-liners"
	done
fi

if [ "$FILE_TYPE" = ".fa.gz" ]						#if files are fasta files, then for each file in the array...
then
	for file in $file_array
	do
		echo $file | tee -a $OUTPUT_FILENAME		#print the file name to the terminal and append to a new file
		N_LINES=$(zcat $file | wc -l)				#count the number of lines in the file and save as variable "N_LINES"
		echo $((N_LINES / 2)) | tee -a $OUTPUT_FILENAME				#Divide N_LINES by 2 to get number of sequences"
	done
fi
