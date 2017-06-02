import numpy as np
import sys


# 1 read data
stat = np.load('data/1-new_stat.npy')
rank = np.load('data/1-new_rank.npy')
dic = {}
for r in rank:
	dic[r[1]] = r[0]

def isnum(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

print(np.shape(stat))
n = 217 # number of universities (210train + 7test)
m = 1743 # number of attributes


# 2 count how many values in a column is number
ind = []
for j in range(m):
	count = 0
	old = -1
	for i in range(n):
		if isnum(stat[i, j]):
			count += 1
			old = i
	ind.append((j, count))


# 3 pick effective columns

attr = [pair[0] for pair in ind if pair[1]>=150]

np.save('data/2-attr.npy', np.array(attr))

final_stat = []
for i in range(n):
	row = []
	for j in range(m):
		if j in attr:
			row.append(stat[i, j])
	final_stat.append(row)

final_stat = np.array(final_stat)

(n, m) = np.shape(final_stat)
print(n, m)


# 4 insert average value for non-number blank
for j in range(m):
	average = np.mean([float(e) for e in final_stat[:, j] if isnum(e)])
	for i in range(n):
		if not isnum(final_stat[i, j]):
			final_stat[i, j] = average
		else:
			final_stat[i, j] = final_stat[i, j]


# 5 normalize
final_stat = np.array(final_stat, dtype=np.float32)
final_stat_normalized = final_stat / (final_stat.max(axis=0) + 1e-10) # avoid divided by zero


# 6 save to npy and txt
np.save('data/2-final_stat.npy', final_stat_normalized)

def output(s, n, add):
	with open('data/'+s+'.txt', 'w') as f:
		for ii in range(n):
			i = ii + add

			f.write("-");
			f.write(dic[stat[i, 3]])
			f.write(" qid:1")
			for j in range(m):
				f.write(" ")
				f.write(str(j+1))
				f.write(":")
				f.write(str(final_stat_normalized[i, j]))
			f.write("\n")

output('train', 210, 0)
output('test', 7, 210)