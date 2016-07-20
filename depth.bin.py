#! /usr/bin/python
from sys import argv

#For this example - read in mpileup depth 
file_in = argv[1]

#Size of bin is second argument
bin_size = int(argv[2])

#Functions
#Calculates max size of contig / chromosome
def contig_size(chrom, depth_dict):
        details = depth_dict.get(chrom)
        return max(details.keys())

#Creates 'bins' along contig
def binner(chrom, depth_dict, bin_size):
        lower = 0
        upper = bin_size
        max = contig_size(chrom, depth_dict)
        #Total bins on contig
	bin_num = max / bin_size
        
	for i in range(1, bin_num):
		#looks up positions in the range (upper, lower) and finds the depth in depth_dict
		l = [depth_dict.get(chrom).get(x) for x in range(lower,upper)]
		#
		try:
			#Convert list elements to float
			l2 = [float(x) for x in l]
			#Print contig, bin number and mean depth in bin
                        print chrom, "\t", i, "\t",  sum(l2) / float(bin_size)
                except TypeError:
                        pass
		#Iteratively increase lower and upper values by bin size
		lower += bin_size
                upper += bin_size
        
#Read in file line by line -adding to depth dict
depth_dict = {}

with open (file_in) as pileup:
	for line in pileup:
		#Extract 3 values from file - assumes 3 columns
		try:
			chrom, pos, depth = line.strip().split("\t")
			depth_dict.setdefault(chrom, {})[int(pos)] = depth
		except ValueError:
			raise ValueError("Pileup Files does not have 3 columns")

#Create unique set of keys (contigs)
contig_set = set()
for i in depth_dict.keys():
	contig_set.add(i)

for i in contig_set:
	binner(i, depth_dict, bin_size)


