import numpy as np
import matplotlib.pyplot as plt

p = "00 05 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95".split()

all_sim = []
for similarity in p:
    str_ev = []
    con_ev = []
    str_og = []
    con_og = []
    with open("GFstr_09%s_ev.txt" % similarity) as evolved:
        for line in evolved:
            split = line.split()
            try:
                gf = float(split[-1])
            except:
                continue
            str_ev.append(gf)
    with open("GFstr_09%s_og.txt" % similarity) as original:
        for line in original:
            split = line.split()
            try:
                gf = float(split[-1])
            except:
                continue
            str_og.append(gf)
    with open("GFcon_09%s_ev.txt" % similarity) as evolved:
        for line in evolved:
            split = line.split()
            try:
                gf = float(split[-1])
            except:
                continue
            con_ev.append(gf)
    with open("GFcon_09%s_og.txt" % similarity) as original:
        for line in original:
            split = line.split()
            try:
                gf = float(split[-1])
            except:
                continue
            con_og.append(gf)
    all_sim.append((str_ev, str_og, con_ev, con_og))

mean_str_ev = []
sd_str_ev = []
mean_str_og = []
sd_str_og = []
mean_con_ev = []
sd_con_ev = []
mean_con_og = []
sd_con_og = []
for pair in all_sim:
    str_ev = pair[0]
    str_og = pair[1]
    con_ev = pair[2]
    con_og = pair[3]
    mean_str_ev.append(np.mean(str_ev))
    mean_str_og.append(np.mean(str_og))
    sd_str_ev.append(np.std(str_ev))
    sd_str_og.append(np.std(str_og))
    mean_con_ev.append(np.mean(con_ev))
    mean_con_og.append(np.mean(con_og))
    sd_con_ev.append(np.std(con_ev))
    sd_con_og.append(np.std(con_og))

#print mean_str_ev
#print sd_str_ev
#print mean_str_og
#print sd_str_og
#print mean_con_ev
#print sd_con_ev
#print mean_con_og
#print sd_con_og

fig,ax = plt.subplots()
#plt.errorbar(range(len(mean_str_og)),mean_str_og,yerr=[float(x)/2 for x in sd_str_og],capsize=3,label="Strain contigs",color='red')
#plt.errorbar(range(len(mean_con_og)),mean_con_og,yerr=[float(x)/2 for x in sd_con_og],capsize=3,label="Consensus contigs",color='blue')
plt.errorbar(range(len(mean_str_ev)),mean_str_ev,yerr=[float(x)/2 for x in sd_str_ev],capsize=3,label="Strain contigs",color='red')
plt.errorbar(range(len(mean_con_ev)),mean_con_ev,yerr=[float(x)/2 for x in sd_con_ev],capsize=3,label="Consensus contigs",color='blue')
plt.legend(loc='lower left')
plt.xticks(range(0,22,2))
xlabels = [(float(x)/10 + 90)/100 for x in p[::2]]
xlabels.append(1.0)
ax.set_xticklabels(xlabels)
#plt.title("Average genome fraction for all genomes")
plt.xlabel("Similarity")
plt.ylabel("Genome fraction")
plt.show()
