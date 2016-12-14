import sys
shellfile = open("newBOWTIEshell.sh", "w")
i = 0 
while i < len(sys.argv): 
	newbatch = sys.argv[i]
	newbowtie = "bowtie -f -v 3 --sam --sam-nohead batch"+newbatch+" batch"+newbatch+"_seqsforBOWTIE.fa batch"+newbatch+"_bowtieOut.sam"
	shellfile.write(newbowtie + "\n\n")
	i += 1
shellfile.close()
import subprocess
subprocess.call(["newBOWTIEshell.sh"], shell = True)

