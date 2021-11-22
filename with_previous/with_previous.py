def with_previous(sequence, *, fillvalue=None):
    sequence = list(sequence)
    if len(sequence) > 1:
        returned_list = [(sequence[0], fillvalue)]
        for idx in range(1, len(sequence)):
            returned_list.append((sequence[idx], sequence[idx-1]))
        return returned_list
    elif len(sequence) == 1:
        return [(sequence[0], fillvalue)]
    else:
        return []
