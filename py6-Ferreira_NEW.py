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


#function that changes the sequence backwards (usefull for sequences that are from 3' to 5' and I want to reverse it)
def Backwards(Seq):
    a = (Seq[::-1])
    return a
def open_reading(Seq):
    
    Seq_Leng = len(Seq)
    
    starting  = ['ATG']
    ending = [['TAA'],['TAG'],['TGA']]
    
    temp_seq = []
    Sequence = []
    start_codon = []
    end_codon = []
    
    glue = 0
    count = 0
    
    for i in Seq:
        count = count+1                        
        i = ''.join(i)
        if (i == starting[0] and glue == 0):                        
            glue = 1            
            start_codon.append(count)            
        if (i == ending[0][0] or i == ending[1][0] or i == ending[2][0] and glue == 1):
            end_codon.append(count-1)                    
            Sequence.append(temp_seq)            
            temp_seq = []            
            glue = 0
        if (glue == 1):
            temp_seq.append(i)
        if (glue == 1 and Seq_Leng == count):
            end_codon.append("END")
            Sequence.append(temp_seq)            
            temp_seq = []
            glue = 0    
    return (Sequence,start_codon,end_codon)
    #return (Sequence,start_codon)
def open_a_file(file):
    f = open(file,'r')
    return f
    f.close()
def clean_list(listan):
    nicer = []
    for i in listan:
        nicer.append(''.join(i))
    return (nicer)



DNA = "ATGATATGGAGGAGGTAGCCGCGCGCCATGCGCGCTATATTTTGGTAT"

#making the DNA sequence to a list
DNA = sequence_list(DNA)

#This variable will reverse the DNA and save the complement of the reverse
DNA_Rev = Backwards(complement(DNA))


#make variables with the reading frames
forward = (amino_acid2(DNA))
reverse = (amino_acid2(DNA_Rev))

number_erf = 1
#position = 0
for i in forward:
    position = 0    
    calling = (open_reading(i))
    result = calling[0]
    starting = calling[1]
    ending = calling[2]
    #print (starting,ending)
    for i in result:       
        if (len(i)>0):
            print ("From the sequence",clean_list(forward[number_erf-1]))
            print ("At open reading frame forward",number_erf,"from codon",starting[position],"to",ending[position],":",i)
            print ("")
            position = position+1
    number_erf = number_erf+1
    
    
number_erf = 1    
for i in reverse:
    position = 0    
    calling = (open_reading(i))
    result = calling[0]
    starting = calling[1]
    ending = calling[2]
    #print (starting,ending)
    for i in result:       
        if (len(i)>0):
            print ("From the sequence",clean_list(reverse[number_erf-1]))
            print ("At open reading frame reverse",number_erf,"from codon",starting[position],"to",ending[position],":",i)
            print ("")
            position = position+1
    number_erf = number_erf+1    
    
    
