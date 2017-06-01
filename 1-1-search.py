import sys

s = sys.argv[1]

with open('raw_data/MERGED2014_15_PP.csv', 'r') as f:
	for line in f:
		a = line.split(',')[3]
		if s in a:
			print(a)