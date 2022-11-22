with open("rosalind_fibd.txt") as f:
    seq = f.readlines()
    splitted = seq[0].split(' ')
months = int(splitted[0])
pairs = int(splitted[1])
