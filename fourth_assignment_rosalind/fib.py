with open("rosalind_fib.txt") as f:
    seq = f.readlines()
    splitted = seq[0].split(' ')
n = int(splitted[0])
k = int(splitted[1])
a = 1                    
b = 1                  
for months in range(1, n-1):
      c = a+b*k   
      b = a              
      a = c
print(a)