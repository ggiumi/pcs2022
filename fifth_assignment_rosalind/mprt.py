import re
import requests
def get_sequence(id: str):
    response = requests.get(f"http://www.uniprot.org/uniprot/{id}.fasta").text
    return "".join(line.strip() for line in response.splitlines()[1:])
with open("rosalind_mprt.txt") as inFile:
    list = [line.strip() for line in inFile.readlines()]
with open("rosalind_mprt_ans.txt", "w") as outFile: 
    N_gly = {}
    for id in list:
        prot_sequence = get_sequence(id) 
        N_gly[id] = [m.start() + 1 for m in re.finditer(r"(?=[N][^P][ST][^P])", prot_sequence)]      
    for id, idx in N_gly.items():
        if len(idx) > 0:
            print(id, file=outFile)
            print(" ".join(map(str, idx)), file=outFile)