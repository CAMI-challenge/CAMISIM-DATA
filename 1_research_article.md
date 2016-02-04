#### Manuscript #1: [*GigaScience* Research article](http://www.gigasciencejournal.com/authors/instructions/research)

- Broadly introduce the CAMI metagenome simulation pipeline
- Goal #1: Motivate the use of simulated data instead of real data
  - In-depth comparison of the JGI mock *in vitro* metagenome with an 1:1 simulated *in silico* dataset
    - Only run second part of the pipeline, start with *real* abundances
    - Derive an ART error profile from the actual JGI mock sequencing run
    - Compare both profiles (no specific tool, count mapped reads instead – we have the references)
    - Run 2-4 metagenome assemblers (Ray Meta, MegaHIT, ... pick a few based on citation counts?)
  - Result: It makes sense to use simulated data for benchmarking, such as the CAMI challenge
    - Way easier to evaluate submissions, because we know the ground truth
    - A tool's performance on simulated data is a proxy (or an indicator) for its performance on real data
- Goal #2: Motivate the use of Aaron's strain evolver
  - Strain heterogeneity poses one (if not the biggest) challenge in metagenome assembly
    - Toy example: Adrian's *E. coli* experiments (scaled up?)
    - We need to play around with the strain evolver itself
      - As far as I know, it has not been described in a publication before?
      - Aaron modified its source code specifically for CAMI (no more truncated genes)
- Goal #3: Motivate our choice to sample abundances from a log-normal distribution
  - Probably enough to cite some papers stating log-normal is the norm
  - Pipeline selling point: time-series and differential-abundance settings
- Conclusion: Awesome pipeline
  - Was already used for the first CAMI challenge, and will be used in subsequent challenges
  - Free and open source, for the whole community to re-use for tool development and benchmarking

---

# Title

Task force (alphabetically):
- [Andreas Bremges](https://github.com/abremges)
- [Adrian Fritz](https://github.com/AlphaSquad)
- [Peter Hofman](https://github.com/p-hofmann)
- [Alice McHardy](https://github.com/alicemchardy)

Co-authors (alphabetically):
- [Aaron Darling](https://github.com/koadman)
- [Johannes Dröge](https://github.com/fungs)
- [Alex Sczyrba](https://github.com/asczyrba)
- Tanja Woyke
- ...

## Abstract

**Background:**
the context and purpose of the study

**Results:**
the main findings

**Conclusions:**
brief summary and potential implications

## Background
The background section should be written in a way that is accessible to researchers without specialist knowledge in that area and must clearly state - and, if helpful, illustrate - the background to the research and its aims. The section should end with a brief statement of what is being reported in the article.

## Data Description
A statement providing background and purpose for collection of these data should be presented for readers without specialist knowledge in that area. A brief description of the protocol for data collection, data curation and quality control, as well as potential uses should be included, as well as outlining how the data can be accessed if it is not deposited in our repository.

## Analyses
This section should provide details of all of the experiments and analyses that are required to support the conclusions of the paper. The authors should make clear the goal of each analysis and state the basic findings.

## Discussion
The discussion should spell out the major conclusions and interpretations of the work, including some explanation on the importance and relevance of the dataset and analysis. It should not be restatement of the analyses done and their basic conclusions. The discussion section can end with a concluding paragraph that clearly states the main conclusions of the research along with directions for future work. Summary illustrations can be included.

## Potential Implications
This is an optional section of no more than 250 words, where authors can provide some additional comments about potential, more broad-ranging implications of their work that are not directly related to the current focus of their manuscript. This section is meant to promote discussion on possible ways the findings or data presented might be used in or have a relationship with other areas of research that may not be directly apparent in the work. Explicit personal opinions by the authors are permitted, however, references or related information to support the propositions should be included.

## Methods
The methods section should include the design of the study, the type of materials involved, a clear description of all comparisons, and the type of analysis used, to enable replication of the work. Ease of reproducibility is one of the key criteria on which reviewers will by asked to comment, so we strongly advocate the use of the reporting checklists recommended by the BioSharing network and workflow management systems such as Galaxy and myExperiment. All test datasets and other relevant material used for assessing their data and analyses need to be made available through the journal database, supplementary information, or an equally accessible site, as appropriate.

## Availability of supporting data
- JGI *in vitro* mock metagenome will be available in IMG and/or GOLD
- All simulated reads can be submitted to *GigaScience*'s [GigaDB](http://gigadb.org/)
