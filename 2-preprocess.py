import numpy as np

stat = np.load('data/1-new_stat.npy')

def isnum(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

print(np.shape(stat))
n = 210 # number of universities
m = 1743 # number of attributes

ind = []
for j in range(m):
	count = 0
	old = -1
	for i in range(n):
		if isnum(stat[i, j]):
			count += 1
			old = i
	ind.append((j, count))

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



for j in range(m):
	average = np.mean([float(e) for e in final_stat[:, j] if isnum(e)])
	for i in range(n):
		if not isnum(final_stat[i, j]):
			final_stat[i, j] = average
		else:
			final_stat[i, j] = final_stat[i, j]

final_stat = np.array(final_stat, dtype=np.float32)
np.save('data/2-final_stat.npy', final_stat)