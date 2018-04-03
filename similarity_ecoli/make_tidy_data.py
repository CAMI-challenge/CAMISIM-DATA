#!/usr/bin/env python

import os

folders = os.listdir(".")

contig_metric = "summary/TXT/#_contigs.txt"
gf_metric = "summary/TXT/Genome_fraction_(%).txt"
nga50_metric = "summary/TXT/NGA50.txt"

with open("Similarity_metrics.tsv","wb+") as matrix:
    matrix.write("Assembler\tSimilarity\tEvaluation_type\tGenome\tmetric\tvalue\n")

for folder in folders:
    if not os.path.isdir(folder):
        continue
    error, eval_type, assembler = folder.split("_")
    if error == "art":
        assembler += "_" + error
    similarities = os.listdir(folder)
    for similarity in similarities:
        name, sim = similarity.split("_")
        sim = float(sim)/10.
        if name == "Ecoli":
            path = os.path.join(folder, similarity, contig_metric)
            to_write = ""
            with open(path,'r') as c:
                for line in c:
                    strain, contigs = line.strip().split()
                    genome_type = strain.split("_")
                    if len(genome_type) > 1: # this is the pairs we need
                        genome_type = genome_type[1]
                        if genome_type == "ancestor" or (assembler.startswith("megahit") and int(genome_type) == 920): # the 20th created genome, (second number - 900)*0.5 + 90 is the real similarity
                            genome = "Ancestor"
                        else:
                            genome = "Evolved"
                        to_write += "{assembler}\t{similarity}\t{eval_type}\t{genome}\t{metric}\t{value}\n".format(
                            assembler = assembler,
                            similarity = sim,
                            eval_type = eval_type,
                            genome=genome,
                            metric="#_contigs",
                            value=contigs
                        )
            with open("Similarity_metrics.tsv",'a+') as tidy:
                tidy.write(to_write)
            path = os.path.join(folder, similarity, gf_metric)
            to_write = ""
            with open(path,'r') as gf:
                for line in gf:
                    strain, gen_frac = line.strip().split()
                    genome_type = strain.split("_")
                    if len(genome_type) > 1: # this is the pairs we need
                        genome_type = genome_type[1]
                        if genome_type == "ancestor" or (assembler.startswith("megahit") and int(genome_type) == 920): # the 20th created genome, (second number - 900)*0.5 + 90 is the real similarity
                            genome = "Ancestor"
                        else:
                            genome = "Evolved"
                        to_write += "{assembler}\t{similarity}\t{eval_type}\t{genome}\t{metric}\t{value}\n".format(
                            assembler = assembler,
                            similarity = sim,
                            eval_type = eval_type,
                            genome=genome,
                            metric="Genome_fraction_(%)",
                            value=gen_frac
                        )
            with open("Similarity_metrics.tsv",'a+') as tidy:
                tidy.write(to_write)
            path = os.path.join(folder, similarity, nga50_metric)
            to_write = ""
            with open(path,'r') as nga50:
                for line in nga50:
                    strain, nga = line.strip().split()
                    genome_type = strain.split("_")
                    if len(genome_type) > 1: # this is the pairs we need
                        genome_type = genome_type[1]
                        if genome_type == "ancestor" or (assembler.startswith("megahit") and int(genome_type) == 920): # the 20th created genome, (second number - 900)*0.5 + 90 is the real similarity
                            genome = "Ancestor"
                        else:
                            genome = "Evolved"
                        to_write += "{assembler}\t{similarity}\t{eval_type}\t{genome}\t{metric}\t{value}\n".format(
                            assembler = assembler,
                            similarity = sim,
                            eval_type = eval_type,
                            genome=genome,
                            metric="NGA50",
                            value=nga
                        )
            with open("Similarity_metrics.tsv",'a+') as tidy:
                tidy.write(to_write)
