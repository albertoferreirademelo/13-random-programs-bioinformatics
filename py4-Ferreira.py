DNA_Sequence_raw = [] #necessary variables
DNA_Sequence = []

#open the FASTA file
file = ("DNA.fasta")
f = open(file,'r')

#taking out the lines that starts with (">") and saving in a new list (raw)
for i in f:
    if (i[0] != ">"):
        DNA_Sequence_raw.extend(i)        
        
#cleaning the list to just A, T, C and G        
for i in DNA_Sequence_raw:
    if (i == "A" or i == "T" or i == "C" or i == "G"):
        DNA_Sequence.append(i)
print (DNA_Sequence)
f.close