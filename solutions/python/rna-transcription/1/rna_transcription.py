def to_rna(dna_strand):
    return "".join(map(get_rna, dna_strand))

def get_rna(dna):
    if dna == "G":
        return "C"
    if dna == "C":
        return "G"
    if dna == "T":
        return "A"
    if dna == "A":
        return "U"
    
    raise ValueError("Unknown DNA")