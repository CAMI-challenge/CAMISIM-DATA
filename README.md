# Results of the CAMISIM paper
This repository contains 5 folders:
 - coverage_sweep
 - figures
 - itol
 - itol_evaluation
 - similarity_ecoli

All the scripts used for creating tables and plots are provided within the repository, alongside the data used for creating them. *Internal note: the full data, i.e. all the assemblies and raw data can be found on the BIFO servers under /net/metagenomics/projects/afritz_assemblies*

### coverage_sweep
Contains the quast output of the coverage sweep data, sorted by error profile (0,2,5% and ART), once with SPAdes and MEGAHIT 1.0.3 and in the subfolder megahit_111 with MEGAHIT 1.1.2

### figures
Contains figures for the coverage_sweep and similarity experiment and in the case of similarity the plot to create the panelfig appearing in the CAMISIM paper

### itol
Contains the quast results for all the 158 itol genomes, both consensus and strain as subfolder for every genome. Additionally a script summarizing all the three required metrics and the corresponding output files

### itol_evaluation
Given the summaries from itol, has the genome fraction values for all genomes sorted by similarity and whether the evaluation was done with the consensus/strain quast, additionally a plot for creating individual plots

### similarity_ecoli
Contains the metaquast consensus/strain output for both MEGAHIT 1.0.3 and SPAdes, both for error-free reads and for reads with the ART CAMI error profile
