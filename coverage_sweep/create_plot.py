#!/usr/bin/env python

from matplotlib.ticker import ScalarFormatter
import matplotlib
import matplotlib.pyplot as plt

def get_metric(metric, statistics):
    with open(metric) as metrics:
        for line in metrics:
            if line.startswith("All") or len(line.split()) > 4:
                continue # woops
            if line.startswith("0") or line.startswith("ART"):
                error, cov, tool, raport = line.split("/")
                error = error.split("_")[0]
                cov = cov.split("_")[-1][3:]
                tool = tool.split("_")
                if len(tool) == 1:
                    tool = "MEGAHIT"
                else:
                    tool = "metaSPAdes"
            else:
                stuff = line.split()
                value = stuff[-1]
                if tool in statistics:
                    if metric in statistics[tool]:
                        if error in statistics[tool][metric]:
                            statistics[tool][metric][error].append((int(cov),value))
                        else:
                            statistics[tool][metric][error] = [(int(cov),value)]
                    else:
                        statistics[tool][metric] = {error : [(int(cov),value)]}
                else:
                    statistics[tool] = {metric: {error : [(int(cov),value)]}}
        for tool in statistics:            
            for error in statistics[tool][metric]:
                statistics[tool][metric][error] = [x[1] for x in sorted(statistics[tool][metric][error])]
        return statistics

def create_plot(statistics, gs_statistics):
    x_points = [0,1,2,3,4,5,6,7,8]
    x = [2,4,8,16,32,64,128,256,512]
    matplotlib.rcParams['xtick.labelsize'] = 23
    matplotlib.rcParams['ytick.labelsize'] = 23
    f, axes = plt.subplots(3,2,sharex='col', sharey='row')
    #f.suptitle("Coverage dependent assembly performance", fontsize=20)
    labels = {'000' : '0% error rate', '020':'2% error rate','050':'5% error rate','ART':'ART CAMI error profile'}
    metrics = {'gf':"Genome fraction (%)",'nga':"NGA50",'contigs':"# contigs"}
    i = 0
    for tool in statistics:
        j = 0
        for metric in statistics[tool]:
            for error in sorted(statistics[tool][metric].keys()):
                if len(statistics[tool][metric][error]) < len(x):
                    statistics[tool][metric][error] = ['0']*(len(x) - len(statistics[tool][metric][error])) +  statistics[tool][metric][error]
                values = [z if z != '-' else '0' for z in statistics[tool][metric][error]]
                values = [z if z != '0' else 1 for z in values]
                axes[j][i].plot(x_points,values,label=labels[error])
                if metric != "gf":
                    axes[j][i].set_yscale("log")
                    #axes[j][i].get_yaxis().set_major_formatter(ScalarFormatter())
                    #axes[j][i].get_yaxis().get_major_formatter().set_scientific(False)
                if j == 0:
                    axes[j][i].set_title(tool, size=23)
                axes[j][i].set_ylabel(metrics[metric],size=23)
                axes[j][i].set_xticks(x_points)
                axes[j][i].set_xticklabels(x)
            values_gs = gs_statistics['metaSPAdes'][metric+"_gs"]['ART']
            axes[j][i].plot(x_points,values_gs,color='black',label="Gold Standard")
            j += 1
        i += 1
    axes[-1][0].set_xlabel("Coverage", size = 23)
    axes[-1][1].set_xlabel("Coverage", size = 23)
    lgd = plt.legend(loc=9, bbox_to_anchor=(-0.1, -0.35), ncol=5, fontsize=23)
    #plt.show()
    f.set_size_inches(19.2,11.8)
    f.savefig('samplefigure', bbox_extra_artists=(lgd,), bbox_inches='tight')
    return


def main():
    stats = {}
    stats = get_metric("gf", stats)
    stats = get_metric("nga", stats)
    stats = get_metric("contigs", stats)
    gs_stats = {}
    gs_stats = get_metric("gf_gs", gs_stats)
    gs_stats = get_metric("nga_gs", gs_stats)
    gs_stats = get_metric("contigs_gs", gs_stats)
    create_plot(stats, gs_stats)

main()
