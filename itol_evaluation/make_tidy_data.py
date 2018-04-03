#!/usr/bin/env python

# based on the files created by the make_data.py script in the ../itol folder
metrics = { "NGA50" : "../itol/NGA50.tsv", "Genome fraction(%)": "../itol/Genome_fraction.tsv", "#_contigs" : "../itol/contigs.tsv"}

with open("Similarity_metrics.tsv",'wb+') as matrix:
    matrix.write("Genome\tSimilarity\tevaluation_type\tTree_genome\tmetric\tvalue\n")

for metric in metrics:
    with open(metrics[metric]) as cong:
        for line in cong:
            if line.startswith("Name"):
                continue
            else:
                genome, con_anc, con_ev, strain_anc, strain_ev = line.strip().split()
                name, sim = genome.rsplit("_",1)
                sim = float(sim)/10 + 90.
                to_write = "{genome}\t{sim}\t{eval_type}\t{tree}\t{metric}\t{value}\n".format(
                    genome = name,
                    sim = sim,
                    eval_type = "consensus",
                    tree = "Ancestor",
                    metric = metric,
                    value = con_anc
                )
                to_write += "{genome}\t{sim}\t{eval_type}\t{tree}\t{metric}\t{value}\n".format(
                    genome = name,
                    sim = sim,
                    eval_type = "consensus",
                    tree = "Evolved",
                    metric = metric,
                    value = con_ev
                )
                to_write += "{genome}\t{sim}\t{eval_type}\t{tree}\t{metric}\t{value}\n".format(
                    genome = name,
                    sim = sim,
                    eval_type = "strain",
                    tree = "Ancestor",
                    metric = metric,
                    value = strain_anc
                )
                to_write += "{genome}\t{sim}\t{eval_type}\t{tree}\t{metric}\t{value}\n".format(
                    genome = name,
                    sim = sim,
                    eval_type = "strain",
                    tree = "Evolved",
                    metric = metric,
                    value = strain_ev
                )
                with open("Similarity_metrics.tsv",'a+') as matrix:
                    matrix.write(to_write)
