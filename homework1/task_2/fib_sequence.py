seq = [0, 1, 1, 2, 3, 5, 9, 13]


def check_sequence(seq):
    if any(seq) == False:
        return False
    a, b, c = seq[0], seq[1], seq[2]
    if a + b != c:
        return False
    seq = seq[3:]
    if len(seq) == 0:
        return True
    while len(seq) != 0:
        a, b, c = b, c, seq[0]
        if a + b != c:
            return False
        seq = seq[1:]
    return True


print(check_sequence(seq))
