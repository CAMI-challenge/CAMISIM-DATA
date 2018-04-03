import matplotlib.pyplot as plt
import numpy as np

def get_val(filename):
    f = open(filename, 'r')
    l = f.readlines()
    val = float(l[1].split()[1])
    return val

def get_val2(filename):
    f = open(filename, 'r')
    l = f.readlines()
    val = []
    for elem in l[1:]:
        val.append(elem.split()[1])
    return val

def get_metric(tool,metric,error,filename,l1 = "2 4 8 16 32 64 128 256 512".split()):
    res = []
    for elem in l1:
        try:
            res.append(get_val2(filename % (error,elem,metric)))
        except:
            res.append([0])
    ret = []
    for x in res:
        if len(x) == 1:
            try:
                ret.append((float(x[0]),0))
            except:
                ret.append((0,0))
            continue
        if (x[0] == '-' and x[1] == '-'):
            ret.append((0,0))
        elif (x[0] == '-'):
            ret.append((0,float(x[1])))
        elif (x[1] == '-'):
            ret.append((float(x[0]),0))
        else:
            ret.append((float(x[0]),float(x[1])))
    return ret

def create_all_genomes_data(prefix):
    p = "00 05 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95".split()
    all_sim = []
    for similarity in p:
        str_ev = []
        con_ev = []
        str_og = []
        con_og = []
        with open("%s/GFstr_09%s_ev.txt" % (prefix,similarity)) as evolved:
            for line in evolved:
                split = line.split()
                try:
                    gf = float(split[-1])
                except:
                    continue
                str_ev.append(gf)
        with open("%s/GFstr_09%s_og.txt" % (prefix,similarity)) as original:
            for line in original:
                split = line.split()
                try:
                    gf = float(split[-1])
                except:
                    continue
                str_og.append(gf)
        with open("%s/GFcon_09%s_ev.txt" % (prefix,similarity)) as evolved:
            for line in evolved:
                split = line.split()
                try:
                    gf = float(split[-1])
                except:
                    continue
                con_ev.append(gf)
        with open("%s/GFcon_09%s_og.txt" % (prefix,similarity)) as original:
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
    return (mean_str_ev, sd_str_ev, mean_str_og, sd_str_og, mean_con_ev, sd_con_ev, mean_con_og, sd_con_og)

tool = "megahit"
metric = "Genome_fraction_(%)"
filename_art = '../../art_%s_megahit/Ecoli_09%s/summary/TXT/%s.txt'
filename_wgsim = '../../metaquast_%s_megahit/Ecoli_09%s/summary/TXT/%s.txt'
l1 = "00 05 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95".split()
l2 = "00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19".split()
res_mega_con_wgsim = get_metric(tool,metric,"consensus",filename_wgsim,l1)
res_mega_strain_wgsim = get_metric(tool,metric,"strain",filename_wgsim,l1)
res_mega_con_art = get_metric(tool,metric,"consensus",filename_art,l2)
res_mega_strain_art = get_metric(tool,metric,"strain",filename_art,l2)
sim = [0.9,0.905,0.91,0.915,0.92,0.925,0.93,0.935,0.94,0.945,0.95,0.955,0.96,0.965,0.97,0.975,0.98,0.985,0.99,0.995]

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
# ecoli individual plot
ax1.plot(range(len(res_mega_strain_wgsim)),[y for (z,y) in res_mega_strain_wgsim],label="E.coli K 12", color='red')
ax1.plot(range(len(res_mega_strain_wgsim)),[z for (z,y) in res_mega_strain_wgsim],label="evolved E.coli", color='blue')
ax1.plot(range(len(res_mega_con_wgsim)),[y for (z,y) in res_mega_con_wgsim],label="E.coli K 12 consensus",ls='--', color='red')
ax1.plot(range(len(res_mega_con_wgsim)),[z for (z,y) in res_mega_con_wgsim],label="evolved E.coli consensus",ls='--', color='blue')
ax1.legend(loc='lower left',prop={'size': 21})
ax1.set_title("E.coli genome fraction with different error profiles", size=21) 
ax3.plot(range(len(res_mega_strain_art)),[y for (z,y) in res_mega_strain_art],label="E.coli K 12", color='red')
ax3.plot(range(len(res_mega_strain_art)),[z for (z,y) in res_mega_strain_art],label="evolved E.coli", color='blue')
ax3.plot(range(len(res_mega_con_art)),[y for (z,y) in res_mega_con_art],label="E.coli K 12 consensus",ls='--', color='red')
ax3.plot(range(len(res_mega_con_art)),[z for (z,y) in res_mega_con_art],label="evolved E.coli consensus",ls='--', color='blue')
ax3.legend(loc='lower left',prop={'size': 21})

# all genomes plot
mean_str_ev, sd_str_ev, mean_str_og, sd_str_og, mean_con_ev, sd_con_ev, mean_con_og, sd_con_og = create_all_genomes_data("../../itol_evaluation")
ax2.errorbar(range(len(mean_str_og)),mean_str_og,yerr=[float(x)/2 for x in sd_str_og],capsize=3,label="Unique mapping",color='red')
ax2.errorbar(range(len(mean_con_og)),mean_con_og,yerr=[float(x)/2 for x in sd_con_og],capsize=3,label="Multiple best mappings",color='blue')
ax2.legend(loc='lower left',prop={'size': 21})
ax2.set_title("Average genome fraction for all genomes", size=21)
ax4.errorbar(range(len(mean_str_ev)),mean_str_ev,yerr=[float(x)/2 for x in sd_str_ev],capsize=3,label="Unique mapping",color='red')
ax4.errorbar(range(len(mean_con_ev)),mean_con_ev,yerr=[float(x)/2 for x in sd_con_ev],capsize=3,label="Multiple best mappings",color='blue')
ax4.legend(loc='lower left',prop={'size': 21})

# general stuff
xlabels = sim[::2]
xlabels.append(1.0)
ylabels = range(40,100,20)
ax3.set_xticklabels(xlabels, size=18)
ax4.set_xticklabels(xlabels, size=18)
ax3.set_xticks(range(0,22,2))
ax4.set_xticks(range(0,22,2))
f.text(0.08,0.5,"Genome fraction (%)",ha = 'center', va = 'center', rotation='vertical', size=21)
f.text(0.5,0.05,"Genome similarity (ANI)",ha = 'center', va = 'center', size=21)
plt.show()
