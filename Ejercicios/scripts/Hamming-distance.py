if __name__ == "__main__":

    '''
    Hamming ditance

    Computes the Hamming distance between two or more sequences and add a deletion or insertion.

    Args:
        seq1: The first sequence.
        seq2: The second sequence.
        seq3: The tirth sequence.    
        
    Returns:
        The number of the Hamming distance.

    '''

    def Hamming_distance():

        seq1 = ("ACGT ACGT")
        seq2 = ("ACT ACGT")
        seq3 = ("ACC ACGT")
        space = (' ')


        sequences = (seq1, seq2, seq3)
        
        for l in sequences:

            if space in l:
                
                l.remove(space)

            print(list(l))
        
        for i in sequences:
        
            print(f'La secuencia "{i}" contiene {len(i)} caracteres.')

        if seq1 == seq2 and seq1 == seq3:
        
            print(f'Las secuencias "{seq1}", "{seq2}" y "{seq3}", son similares')
        
        else:
            print(f'Las secuencias "{seq1}", "{seq2}" y "{seq3}", no son similares.')             

    print(Hamming_distance())