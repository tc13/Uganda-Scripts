#! /usr/bin/python
from sys import argv
import argparse
import numpy

#Argparse
parser = argparse.ArgumentParser(description= "Return binned depth from samtools depth (as file or STDIN). Can be returned as mean, median or sd.")
parser.add_argument("Input file", metavar="depth", type=str, help="samtools depth file")
parser.add_argument("Bin size", metavar="bin", type=int, help="bin size (int)")
parser.add_argument("Function", metavar="stat", type=str, help="statistic (mean, median or sd)")
args = parser.parse_args()

#Define numpy functions
def median(l):
	return numpy.median(numpy.array(l))

def sd(l):
	return numpy.std(numpy.array(l))

#For this example - read in mpileup depth 
file_in = argv[1]

#Size of bin is second argument
bin_size = int(argv[2])

#Function is third arguement - can take 3 forms - mean, median, standard deviation
func = argv[3]
func_list = ["mean", "median", "sd"]
if func not in func_list:
	raise ValueError(func +" is not a valid statistic. Use mean, median or sd.")

#set variables
Bin =1 
clock = bin_size
D = []
tmp_chr = ""

#print first line of file
print "contig", "\t", "bin", "\t", func

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
                        D = []
                        clock = bin_size
		
		#Depth for the current bin stored in D 
		D.append(float(depth))
		
		#If the position is equal to the bin_size - prints depth and moves onto next bin		
		if int(pos) >= clock:
			if func == "mean":
				print chrom, "\t", Bin, "\t", sum(D) /bin_size
			elif func == "median":
				print chrom, "\t", Bin, "\t", median(D)
			else:
				print chrom, "\t", Bin, "\t", sd(D)
			
			Bin += 1
                        D = []
                        clock += bin_size
		
	




