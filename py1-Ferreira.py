#Sequences input
seq1 = "ATACCGGCCTATAACXCGGAA"
seq2 = "ATGATATGGAGGAGGTAGCCGCG.CGCCATGCGCGCTXATATTTTGGTAT"


#needed variables
list_DNA = []


#Task 1 (attaching DNA string from sequence 2 to sequence 1.
task1 = seq1+seq2

print (task1)

#making a list with legal DNA sequences.
for i in task1:
    if (i == 'A' or i == 'T' or i == 'C' or i == 'G'):
        list_DNA.append(i)
        
print (list_DNA)