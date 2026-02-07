def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    
    pairs = zip(strand_a, strand_b)
    
    return len([pair for pair in pairs if pair[0] != pair[1]])