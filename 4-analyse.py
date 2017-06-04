import numpy as np
import csv

train = []
test = []

def parse(s, holder):

	with open('data/2-'+s+'.txt', 'r') as f:
		for line in f:
			a = line.split(' ')
			holder.append(int(a[0][1:]))

	with open('data/3-prediction_'+s+'.dat', 'r') as f:
		for i in range(len(holder)):
			line = f.readline()
			holder[i] = (holder[i], float(line))

parse('train', train)
parse('test', test)
sorted_train = sorted(train, key=lambda x:x[1], reverse=True)
sorted_test = sorted(test, key=lambda x:x[1], reverse=True)

with open('data/4-train_score.txt', 'w') as f:
	for entry in sorted_train:
		f.write(str(entry[0])+"\t"+str(entry[1])+"\n")

with open('data/4-test_score.txt', 'w') as f:
	for entry in sorted_test:
		f.write(str(entry[0])+"\t"+str(entry[1])+"\t")
		
		for i in range(len(train)):
			if sorted_train[i][1]<entry[1]:
				f.write(str(sorted_train[i][0])+"\n")
				break



with open('raw_data/MERGED2014_15_PP.csv', 'rb') as f:

	attrs = 0
	csvfile = csv.reader(f, delimiter=',', quotechar='"')
	for row in csvfile:
		attrs = row
		break

	num = np.load('data/2-attr.npy')
	waiting = []
	for n in num:
		waiting.append((n, attrs[n]))



	with open('data/3-parameter.dat', 'r') as fpara:
		for i in range(11):
			fpara.readline()

		para_line = fpara.readline()
		para_pair_ori = para_line.split(' ')[1:-1]
		para_pair = [(int(p.split(':')[0])-1, float(p.split(':')[1]))
			for p in para_pair_ori]

		
		final_triple = []
		for p in para_pair:
			i = p[0]
			temp = (i, p[1], waiting[i][0], waiting[i][1])
			final_triple.append(temp)

		with open('data/4-parameter_analysis.txt', 'w') as fout:
			final_sorted = sorted(final_triple,
				key=lambda x:abs(x[1]), reverse = True)

			for fs in final_sorted:
				fout.write(str(fs[0])+"\t"+str(fs[1])+"\t")
				fout.write(str(fs[2])+"\t"+str(fs[3])+"\n")