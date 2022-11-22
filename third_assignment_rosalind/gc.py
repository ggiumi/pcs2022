with open("rosalind_gc.txt") as f:
    sequence = f.readlines()
    max_perc_gc = 0
    for i, line in enumerate(sequence):
        if line.startswith(">"):
            id = line[1:]
            seq = " "
        else:
            new_sequence = line.strip()
            seq = seq + new_sequence
            if i==((len(sequence))-1) or sequence[i+1].startswith(">"):
                gc_content = (seq.count("G")+seq.count("C"))
                total = (seq.count("G")+seq.count("C")+seq.count("T")+seq.count("A"))
                gc_content_percent = (gc_content/total)*100
                if gc_content_percent > max_perc_gc:
                    max_id = id
                    max_perc_gc = gc_content_percent
print(f'{max_id}{max_perc_gc}')