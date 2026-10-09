FASTA Analyzer 🧬

A beginner-friendly bioinformatics project built with Python to analyze DNA sequences stored in FASTA files.

Features

- Reads DNA sequences from FASTA files.
- Supports multiple sequences in one file.
- Calculates sequence length.
- Counts A, T, G, and C nucleotides.
- Calculates GC content for valid DNA sequences.
- Detects unexpected characters in DNA sequences.
- Handles common file and input errors.

Requirements

- Python 3
- No external libraries required.

How to Run

1. Download or clone this repository.

2. Open a terminal in the project folder.

3. Run:
   
   python fasta_analyzer.py

4. Enter the FASTA filename when prompted, for example:
   
   dna.txt

What I Learned

Through this project, I practiced Python functions, file handling, loops, dictionaries, sequence validation, exception handling, and basic DNA sequence analysis.

Limitations

This is an educational project. It performs basic character validation and sequence analysis; it does not confirm the biological identity or correctness of a DNA sequence. Only A, T, G, and C are currently accepted as valid DNA bases.

Future Improvements

- Support additional FASTA formats and ambiguous nucleotide codes.
- Add reverse-complement analysis.
- Create a more detailed sequence analysis report.

Data Source

The example sequence is the human hemoglobin subunit alpha 1 (HBA1) mRNA reference sequence.

- Accession: NM_000558.5
- Database: NCBI Nucleotide
- Source: https://www.ncbi.nlm.nih.gov/nuccore/NM_000558.5

The sequence is provided as a nucleotide FASTA record. The analyzer currently counts A, T, G, and C and performs basic character validation.
---

Author: Habiba Mohamed