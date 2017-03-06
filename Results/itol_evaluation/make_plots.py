import numpy as np
import matplotlib.pyplot as plt

p = "00 05 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95".split()

all_sim = []
for similarity in p:
	seq_ev = []
	seq_og = []
	with open("GF_09%s_ev.txt" % similarity) as evolved:
		for line in evolved:
			split = line.split()
			gf = float(split[-1])
			seq_ev.append(gf)
	with open("GF_09%s_og.txt" % similarity) as original:
		for line in original:
			split = line.split()
			gf = float(split[-1])
			seq_og.append(gf)
	all_sim.append((seq_ev,seq_og))

mean_ev = []
sd_ev = []
mean_og = []
sd_og = []
for pair in all_sim:
	ev = pair[0]
	og = pair[1]
	mean_ev.append(np.mean(ev))
	mean_og.append(np.mean(og))
	sd_ev.append(np.std(ev))
	sd_og.append(np.std(og))

print mean_ev
print sd_ev
print mean_og
print sd_og

fig,ax = plt.subplots()
#plt.errorbar(range(len(mean_ev)),mean_ev,yerr=sd_ev,capsize=3,color='red')
plt.errorbar(range(len(mean_og)),mean_og,yerr=sd_og,capsize=3,color='red')
plt.xticks(np.arange(0,20,1))
ax.set_xticklabels(p)
plt.title("Average genome fraction of all original genomes")
plt.xlabel("Similarity")
plt.ylabel("Genome fraction")
plt.show()
