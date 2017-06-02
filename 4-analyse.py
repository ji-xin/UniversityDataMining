import numpy as np

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
