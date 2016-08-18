#! /usr/bin/python
from sys import argv
from fractions import Fraction
import numpy

#Define numpy functions
def median(l):
	return numpy.median(numpy.array(l))

#Def harmonic num
harmonic_num = lambda n: sum(Fraction(1,d) for d in xrange(1, n+1))

#Read in tablulated vcf
file_in = argv[1]

#Size of bin is second argument
bin_size = int(argv[2])

#set variables
Bin =1
clock = bin_size
N = []
variants = 0
tmp_chr = ""
dp = []
gq = []

#Print first line
print "chrom", "\t", "bin", "\t", "wat_estim", "\t", "DP", "\t", "GQ"

#Read in file
with open (file_in) as table:
	next(table)
	for line in table:
		try:
			chrom, pos, ncalled, multi, hom_var, het, DP, GQ = line.strip().split("\t")
		except ValueError:
			raise ValueError("Tabulated VCF does not have 8 columns")

		#Check if chrom is new - in which case re-set variable
		if tmp_chr != chrom:
			tmp_chr = chrom
			Bin = 1
			N = []
			clock = bin_size
			variants = 0
			gq = []
			dp = []
		
		#Number of individuals called stored in N
		N.append(int(ncalled))
		variants += int(hom_var)
		variants += int(het)
		dp.append(int(DP))
		gq.append(float(GQ))

		#If pos exceeds the bin_size - prints output - moves to next bin
		if int(pos) >= clock:
			m = int(median(N))
			hn = float(harmonic_num(m))
			wat_e = float(variants/hn)/bin_size
			med_DP = median(dp)
			med_GQ = median(gq)
			print chrom, "\t", Bin, "\t", str(wat_e), "\t", str(med_DP), "\t", str(med_GQ)

			Bin += 1
			N= []
			variants = 0
			clock += bin_size
			gq = []
			dp = []		


