if __name__ == "__main__":

    '''
    Similarity 

    Computes the similarity between two sequences.

    Args:
        seq1: The first sequence.
        seq2: The second sequence.
  
    Returns:
        True if the sequences are equal, False otherwise.
    '''

    seq1 = ('ACGT ACGT')
    seq2 = ('ACCT ACGT')

    def similarity(seq1, seq2):

        if seq1 == seq2:
            return (f'Las secuencias "{ seq1 }" y "{ seq2 }" son similares.')
            
        else:
            return (f'Las secuencias "{ seq1 }" y "{ seq2 }" no son similares.')

    print(similarity(seq1, seq2))