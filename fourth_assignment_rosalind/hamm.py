with open("rosalind_hamm.txt") as f:
    seq = f.read().splitlines()
first_string = seq[0]
second_string = seq[1]
counter = 0
for i in range(len(first_string)):
    if first_string[i] != second_string[i]:
        counter +=1
print(counter)