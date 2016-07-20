#! /usr/bin/python
from sys import argv

#For this example - read in mpileup depth 
file_in = argv[1]

#Size of bin is second argument
bin_size = int(argv[2])

#Functions
#Read through file and calculate max size of contig - hold as dictionary
size_dict = {}
depth_dict = {}

with open (file_in) as pileup:
        for line in pileup:
                #Extract 3 values - assumes 3 columns
                try:
                        chrom, pos, depth = line.strip().split("\t")
   		except ValueError:
                        raise ValueError("Pileup Files does not have 3 columns")
                size_dict[chrom]= pos

Bin = 1
clock = bin_size
D = 0.0

with open (file_in) as pileup:
        for line in pileup:
                #Extract 3 values - assumes 3 columns
                try:
                        chrom, pos, depth = line.strip().split("\t")
                except ValueError:
                        raise ValueError("Pileup Files does not have 3 columns")

		D += float(depth)
		#print "The depth is  " +str(D)

		if int(pos) == clock:
			print chrom, "\t", Bin, "\t", float(D/bin_size)
			Bin += 1
			D = 0
			clock += bin_size


		#clock += 1
		#print "The clock is "+ str(clock)

		if size_dict.get(chrom) == pos:
			Bin = 1
			clock = bin_size		



