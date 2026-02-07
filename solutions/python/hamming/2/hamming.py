def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    
    pairs = zip(strand_a, strand_b)
    
    return sum(one != two for one, two in pairs)