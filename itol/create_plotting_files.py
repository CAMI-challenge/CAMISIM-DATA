#!/usr/bin/env python

metric_file = "Genome_fraction.tsv"
prefix = "../itol_evaluation/GF"
sims = "00 05 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95".split()

with open(metric_file, 'r') as metric:
	evolved_strain = {}
	evolved_consensus = {}
	original_strain = {}
	original_consensus = {}
	for line in metric:
		if line.startswith("Name"):
			continue
		values = line.split('\t')
		name, similarity = values[0].rsplit("_",1)
		if not name in original_consensus:
			original_consensus[name] = {}
			evolved_consensus[name] = {}
			original_strain[name] = {}
			evolved_strain[name] = {}
		original_consensus[name][similarity] = values[1].strip()
		evolved_consensus[name][similarity] = values[2].strip()
		original_strain[name][similarity] = values[3].strip()
		evolved_strain[name][similarity] = values[4].strip()

for genome in evolved_strain:
	for sim in sims:
		out_name_ev_str = prefix + "str_09" + sim + "_ev.txt"
		out_name_ev_con = prefix + "con_09" + sim + "_ev.txt"
		out_name_og_str = prefix + "str_09" + sim + "_og.txt"
		out_name_og_con = prefix + "con_09" + sim + "_og.txt"
		try:
			with open(out_name_ev_str, 'a+') as f:
				f.write(genome + '\t' + evolved_strain[genome][sim] + "\n")
			with open(out_name_ev_con, 'a+') as f:
				f.write(genome + '\t' + evolved_consensus[genome][sim] + "\n")
			with open(out_name_og_str, 'a+') as f:
				f.write(genome + '\t' + original_strain[genome][sim] + "\n")
			with open(out_name_og_con, 'a+') as f:
				f.write(genome + '\t' + original_consensus[genome][sim] + "\n")
		except:
			continue # skip missing genomes/similarities
