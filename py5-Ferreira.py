#function that makes the sequence to a list
def sequence_list(Seq):
    listan = []
    for i in Seq:
        listan.append(i)
    return listan


#function that makes the complement from a DNA string 
def complement(Seq):
    rev_DNA = []

    for i in Seq:    
        if (i == 'A'):
            rev_DNA.append("T")
        if (i == 'T'):
            rev_DNA.append("A")
        if (i == 'C'):
            rev_DNA.append("G")
        if (i == 'G'):
            rev_DNA.append("C")
    return rev_DNA

#function that do the reading frame
def amino_acid2(Seq):
    n = 3
    Start_Sequence = []
    End_Sequence = []
    for reading in range(3):
        a = [Seq[i:i+n] for i in range(reading, len(Seq), n)]
        Start_Sequence.append(a)
    for i in Start_Sequence:
        tabela = []
        for j in i:
            if (len(j) == 3):
                tabela.append(j)
        End_Sequence.append(tabela)
    return (End_Sequence)
    #return Sequence


#function that changes the sequence backwards (usefull for sequences that are from 3' to 5' and I want to reverse it)
def Backwards(Seq):
    a = (Seq[::-1])
    return a

DNA = "ATGATATGGAGGAGGTAGCCGCGCGCCATGCGCGCTATATTTTGGTAT"

#making the DNA sequence to a list
DNA = sequence_list(DNA)

#This variable will reverse the DNA and save the complement of the reverse
DNA_Rev = Backwards(complement(DNA))


#make a variable with the reading frames
forward = (amino_acid2(DNA))
reverse = (amino_acid2(DNA_Rev))

#Here is just a print for a better visualisation of each reading frame

for row in forward:
    print (row)
    
for row in reverse:
    print (row)

    
