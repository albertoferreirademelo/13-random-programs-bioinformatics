#Sequences input
seq1 = "ATGATATGGAGGAGGTAGCCGCGCGCCATGCGCGCTATATTTTGGTAT"


#needed variables
list_DNA = []
rev_DNA = []


#DNA to RNA (Changes T to U)
for i in seq1:
    if (i == 'A' or i == 'T' or i == 'C' or i == 'G' or i == 'X'):
        if (i == "T"):
            list_DNA.append("U")
        else:
            list_DNA.append(i)
        
print (list_DNA)

for i in list_DNA:    
    if (i == 'A'):
        rev_DNA.append("U")
    if (i == 'U'):
        rev_DNA.append("A")
    if (i == 'C'):
        rev_DNA.append("G")
    if (i == 'G'):
        rev_DNA.append("C")
        
print (rev_DNA)
        