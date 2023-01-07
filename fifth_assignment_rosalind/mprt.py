import re
from urllib.request import urlopen
import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
with open("rosalind_mprt.txt") as h:
    ID = []
    for i in h.readlines():
        ID.append(i.strip())
with open("rosalind_mprt_ans.txt", 'x') as f:
    sys.stdout = f
    for j in ID:
        id = ""
        for m in j:
            if m == "_":
                break
            id += m
        seq = ''.join(fasta[1:])
        match = re.finditer("(?=(N[^P][ST][^P]))", seq)
        ans = urlopen(f"http://www.uniprot.org/uniprot/{id}.fasta")
        fasta = ans.read().decode("utf-8", "ignore").splitlines()
        list = [m.start()+1 for m in match]
        if list != []:
            print(j)
            print(*list)
print(ID)