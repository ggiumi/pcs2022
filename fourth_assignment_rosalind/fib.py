with open("rosalind_fib.txt") as f:
    seq = f.readlines()
    splitted = seq[0].split(' ')
n = int(splitted[0])
k = int(splitted[1])
big = 1                    
small = 1                  
for months in range(1,n-1):
      bigger = big + small*k   
      small = big              
      big = bigger             
print(big) 