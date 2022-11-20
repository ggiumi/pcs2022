with open("rosalind_iev.txt") as f:
    seq = f.readlines()
    splitted = seq[0].split(' ')
    AA_AA = 2
    AA_Aa = 2
    AA_aa = 2
    Aa_Aa = 1.5
    Aa_aa = 1
    aa_aa = 0
    a = int(splitted[0])
    b = int(splitted[1])
    c = int(splitted[2])
    d = int(splitted[3])
    e = int(splitted[4])
    f = int(splitted[5])
    dominant_offsprings = ((AA_AA*a)+(AA_Aa*b)+(AA_aa*c)+(Aa_Aa*d)+(Aa_aa*e)+(aa_aa*f))
    print(dominant_offsprings)