#! /usr/bin/python
from sys import argv

#For this example - read in mpileup depth 
file_in = argv[1]

#Size of bin is second argument
bin_size = int(argv[2])

#set variables
Bin =1 
clock = bin_size
D = 0.0
tmp_chr = ""

#Open file - read line by line
with open (file_in) as pileup:
        for line in pileup:
		#Strips values from 3 columns - will return error if input file is not 3 cols
                try:
                        chrom, pos, depth = line.strip().split("\t")
   		except ValueError:
                        raise ValueError("Pileup File does not have 3 columns")

		#This checks if chrom is new - in which case re-sets variables
		if tmp_chr != chrom:
                        tmp_chr = chrom
                        Bin = 1
                        D = 0.0
                        clock = bin_size
		
		#Depth for the current bin stored in D 
		D += int(depth)
		
		#If the position is equal to the bin_size - prints depth and moves onto next bin		
		if int(pos) == clock:
			print chrom, "\t", Bin, "\t", float(D/bin_size)
			Bin += 1
                        D = 0
                        clock += bin_size
		
	




