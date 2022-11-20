with open("rosalind_iprb.txt") as f:
    seq = f.readlines()
    splitted= seq[0].split(' ')
    number_organisms = 0
    for line in seq:
        words = line.split()
        for i in words:
            if i.isdigit() == True:
                number_organisms += int(i)
    k = int(splitted[0]) #AA
    m = int(splitted[1]) #Aa
    n = int(splitted[2]) #aa
probability_dominant_allele = (4*k*(k-1)+3*m*(m-1)+4*(2*k*m+2*k*n+m*n))/(4*number_organisms*(number_organisms-1))
print(probability_dominant_allele)



