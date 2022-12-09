with open("rosalind_fibd.txt") as f:
    seq = f.readlines()
    splitted = seq[0].split(' ')
months = int(splitted[0])
months_alive = int(splitted[1])
list = []
list.append(0)
list.append(1)
for i in range(1, months+1):
    if i < months_alive:
        list.append(list[i]+list[i-1])
    elif i > months_alive:
        list.append(list[i]+list[i-1]-list[i-months_alive])
    else:
        list.append(list[i]+list[i-1]-list[i-months_alive+1])
print(list[months])