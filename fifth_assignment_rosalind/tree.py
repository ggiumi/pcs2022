with open("rosalind_tree.txt") as f:
    data = f.readlines()
n = int(data[0])
list = (data[1:])
edges = (n-len(list)-1)
print(edges)