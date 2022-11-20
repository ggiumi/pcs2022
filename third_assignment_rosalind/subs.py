with open("rosalind_subs.txt") as f:
    seq = f.read().splitlines()
string = seq[0]
substring = seq[1]
for position in range(len(string)):
    if string[position:].startswith(substring):
        print(position+1)