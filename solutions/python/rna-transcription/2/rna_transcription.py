def to_rna(dna_strand):
    rna_map = str.maketrans("GCTA", "CGAU")
    return dna_strand.translate(rna_map)