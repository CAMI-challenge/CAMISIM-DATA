#!/usr/bin/env python

import os

# To be called in /net/metagenomics/projects/afritz_assemblies/Simpipeline_Coverage_Sweep

# variables needed for tidy data format
variables = ["Assembler", "Error rate", "Coverage", "metric", "value"]
# folders with different error rate assembly results and mapping to string
folders = ['000_error', '020_error', '050_error', 'ART']
mapping = {folders[0] : "0%", folders[1] : "2%", folders[2] : "5%", folders[3] : "ART CAMI"}
# used assemblers and their version + evaluation
assemblers =  {"MEGAHIT_1.0.3" : "quast/report.txt", "MEGAHIT_1.1.2" :  "MEGAHIT_111/quast/report.txt", "metaSPAdes" : "quast_metaSPAde/report.txt", "Gold Standard" : "quast_gsa/report.txt"}

with open("Coverage_Sweep_results.tsv",'wb+') as matrix:
    matrix.write("\t".join(variables))
    matrix.write("\n")

for folder in folders:
    coverages = os.listdir(folder)
    for coverage in coverages:
        if coverage == "Ecoli_1024":
            continue # no evaluation for this
        for assembler in assemblers:
            quast_path = assemblers[assembler]
            path = os.path.join(folder, coverage, quast_path)
            with open(path, 'r') as report:
                for line in report:
                    if line.startswith("# contigs  "):
                        contigs = line.strip().split()[-1]
                        to_write = "{assembler}\t{error_rate}\t{coverage}\t{metric}\t{value}\n".format(
                            assembler = assembler,
                            error_rate = mapping[folder],
                            coverage = coverage.split('_')[-1][3:],
                            metric = "#_contigs",
                            value = contigs
                        )
                        with open("Coverage_Sweep_results.tsv",'a+') as matrix:
                            matrix.write(to_write)
                    elif line.startswith("Genome fraction (%)"):
                        gf = line.strip().split()[-1]
                        to_write = "{assembler}\t{error_rate}\t{coverage}\t{metric}\t{value}\n".format(
                            assembler = assembler,
                            error_rate = mapping[folder],
                            coverage = coverage.split('_')[-1][3:],
                            metric = "Genome fraction(%)",
                            value = gf
                        )
                        with open("Coverage_Sweep_results.tsv",'a+') as matrix:
                            matrix.write(to_write)
                    elif line.startswith("NGA50"):
                        nga50 = line.strip().split()[-1]
                        to_write = "{assembler}\t{error_rate}\t{coverage}\t{metric}\t{value}\n".format(
                            assembler = assembler,
                            error_rate = mapping[folder],
                            coverage = coverage.split('_')[-1][3:],
                            metric = "NGA50",
                            value = nga50
                        )
                        with open("Coverage_Sweep_results.tsv",'a+') as matrix:
                            matrix.write(to_write)
