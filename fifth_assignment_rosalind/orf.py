table = {'TTT': 'F','CTT':'L','ATT':'I','GTT':'V','TTC':'F','CTC':'L','ATC':'I',
'GTC':'V','TTA':'L','CTA':'L', 'ATA':'I', 'GTA': 'V',
'TTG':'L',     'CTG':'L'     ,'ATG':'M'  ,   'GTG':'V',
'TCT':'S',     'CCT':'P'     ,'ACT':'T',     'GCT': 'A',
'TCC':'S' ,    'CCC':'P'   ,  'ACC':'T',      'GCC':'A',
'TCA':'S'  ,   'CCA':'P'  ,   'ACA':'T'    , 'GCA':'A',
'TCG':'S'   ,  'CCG':'P' ,    'ACG':'T'   ,  'GCG': 'A',
'TAT':'Y'   ,  'CAT':'H',     'AAT':'N'  ,   'GAT':'D',
'TAC':'Y'   ,  'CAC':'H'    , 'AAC':'N' ,    'GAC':'D',
'TAA':' '  , 'CAA':'Q'    , 'AAA':'K',     'GAA': 'E',
'TAG':' '  , 'CAG':'Q'   ,  'AAG':'K',      'GAG' :'E',
'TGT':'C'   ,  'CGT':'R'  ,   'AGT':'S'     ,'GGT': 'G',
'TGC':'C'  ,   'CGC':'R' ,    'AGC':'S'    , 'GGC': 'G',
'TGA':' ' ,  'CGA':'R',     'AGA':'R'   ,  'GGA':'G',
'TGG':'W'    , 'CGG':'R'    ,  'AGG':'R'  ,   'GGG':'G' }
def read_fasta(file):
	seq = {}
	f = open(file, 'r')
	for i in f:
		if i.startswith('>'):
			name = i.replace('>', '')
			name = name.replace('\n', '')
			seq[name] = ''
		else:
			seq[name] += i.replace('\n', '')
	return seq
def reverse_complement(dna):
  dna = dna.replace('A','t')
  dna = dna.replace('G','c')
  dna = dna.replace('T','a')
  dna = dna.replace('C','g')
  dna = dna[::-1].upper()
  return dna
def orfs(dna):
  orfs = []
  orfs += dna,dna[1:], dna[2:]
  reverse_complement_dna = reverse_complement(dna)
  orfs += reverse_complement_dna, reverse_complement_dna[1:], reverse_complement_dna[2:]
  return(orfs)
def translate(dna):
  seqs = orfs(dna)
  pro_seqs=[]
  for seq in seqs:
    for i in range(0, len(seq)-2,3):
      if  seq[i:i+3] == 'ATG':
        pro_seq='M'
        for i in range(i+3,len(seq)-2,3):
          if table[seq[i:i+3]] == ' ':
            break
          elif seq[i:i+3] in table:
            pro_seq = pro_seq+table[seq[i:i+3]]
        pro_seqs.append(pro_seq)
  return(list(set(pro_seqs)))
for dna in read_fasta("rosalind_orf.txt").values():
  for i in translate(dna):
    print(i)