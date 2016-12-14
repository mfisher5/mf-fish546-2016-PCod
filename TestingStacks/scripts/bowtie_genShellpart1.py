###### create a shell script that unzips catalog.tags.tsv.gz files ##########

### in the command line, start from the `DataAnalysis/scripts/` folder
import sys 
inputfile = open(sys.argv[1], "r")
batch_list = []
catfolder_list = []


# create a list of the batch numbers, and the associated folders for those batches' catalogs
for line in inputfile: 
	linelist = line.strip().split("\t")
	batch_list.append(linelist[0])
	catfolder_list.append(linelist[1])
print "batches for bowtie: ", batch_list
print "batches found in folders: ", catfolder_list

# write gzip code to unzip that appropriate catalog.tags files
newfile = open("BOWTIEshellp1.sh", "w")
newfile.write("cd ../UCstacksL1" + "\n" + "\n")
nbatches = len(batch_list)
i = 0
while (i < nbatches): 
	newdir = "cd " + catfolder_list[i] + "\n"
	newline = "gzip -d " + "batch_" + batch_list[i] + ".catalog.tags.tsv.gz" + "\n"
	newfile.write(newdir + newline + "cd ../" + "\n")
	i += 1
newfile.close()
import subprocess
subprocess.call(["./BOWTIEshellp1.sh"], shell = True)
