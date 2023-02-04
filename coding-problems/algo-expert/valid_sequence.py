def is_valid_sequence(array, sequence):
    arridx = 0
    seqidx = 0
    while arridx < len(array) and seqidx < len(sequence):
        if sequence[seqidx] == array[arridx]:
            seqidx += 1
        arridx += 1
    return seqidx == len(array)


result = is_valid_sequence(array=[1, 1, 6, 1], sequence=[1, 1, 1, 6])
print(result)
