import numpy as np
import csv

a = []

with open('raw_data/MERGED2014_15_PP.csv', 'rb') as f:
	csvfile = csv.reader(f, delimiter=',', quotechar='"')
	n = 0
	for row in csvfile:
		if n>0:
			a.append(row)
		n += 1

stat = np.array(a)
name_list = stat[:, 3]

b = []

with open('raw_data/ranking.csv', 'rb') as f:
	csvfile = csv.reader(f, delimiter=',', quotechar='"')
	for row in csvfile:
		if row[0]!='':
			b.append(row[:2])

rank = np.array(b)

def rep(i, pat1, pat2, head, tail):
	temp = head + rank[i, 1].replace(pat1, pat2) + tail
	if temp in name_list:
		rank[i, 1] = temp

for i in range(len(rank)):
	rep(i, "St. ", "St ", "", "")
	rep(i, "St. ", "Saint ", "", "")
	rep(i, "--", "-", "", "")
	rep(i, "--", " at ", "", "")
	rep(i, "--", "-", "The ", "")
	rep(i, "--", " at ", "The ", "")
	rep(i, "--", " in ", "", "")
	rep(i, "--", " in ", "The ", "")
	rep(i, "--", " ", "", "")
	rep(i, "--", " ", "The ", "")
	rep(i, "", "", "The ", "")
	rep(i, "&", "and", "", "")
	rep(i, "", "", "", "-Main Campus")

bad_names = []

for i in range(len(rank)):
	sch = rank[i, 1]
	if sch not in name_list:
		count = 0
		revised = ""
		for name in name_list:
			if sch in name:
				count += 1
				revised = name
		if count==1:
			rank[i, 1] = revised
		else:
			bad_names.append(i)

new_rank = []
good_names = []
for i in range(len(rank)):
	if i not in bad_names:
		new_rank.append(rank[i])
		good_names.append(rank[i, 1])

for nr in new_rank:
	print(nr)

np.save('data/1-new_rank.npy', np.array(new_rank))



new_stat = []
for row in stat:
	if row[3] in good_names:
		new_stat.append(row)

for ns in new_stat:
	print(ns[3])

np.save('data/1-new_stat.npy', np.array(new_stat))