#! /usr/bin/python
#Script takes a single multi-sample vcf as input and returns numeric SNP matrix
from sys import argv

#Read in VCF
file_in = argv[1]

#Function turns vcf SNP calls, ./., 0/0, 0/1, 1,1 etc into numeric values
def SNPr(snp):
	s = snp.split("/")
	if s[0] == ".":
		return "NA"
	else:
		val = float(int(s[0]) + int(s[1])) /2
		return val
#print header
with open(file_in) as f:
	first = f.readline().split()
	tmp= first[0:2] + first[9:]
	print('\t'.join(map(str,tmp)))

#print rest of file
with open (file_in) as table:
	next(table)
	for line in table:
		tmp = []
		l = line.split()
		head= l[0:2] 
		snps = l[9:]
		for i in snps:
			parts = i.split(":")
			tmp.append(parts[0])
			tmp2 = [SNPr(x) for x in tmp]
		row = head + tmp2
		print('\t'.join(map(str,row)))
