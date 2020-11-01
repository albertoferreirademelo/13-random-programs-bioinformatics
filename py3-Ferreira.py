#Sequences input
seq1 = "ATGAATTCATGGAGGAGGTAGTACCACGGCGCGCGCCATGCGCGCTATATTTTGGTAT"


#needed variables
list_DNA = []
EcoRI = ("GAATTC")
Dsal1 = ("CCGCGG")
Dsal2 = ("CCGTGG")
Dsal3 = ("CCACGG")
Dsal4 = ("CCATGG")


#Finding the pattern GAATTC in the DNA sequence and gives the location of the first amino acid (G) from the sequence
for i in seq1:
    list_DNA.append(i)
    #finding the EcoRI pattern
    if (list_DNA[-1] == EcoRI[-1] and list_DNA[-2] == EcoRI[-2] and list_DNA[-3] == EcoRI[-3] and list_DNA[-4] == EcoRI[-4] and list_DNA[-5] == EcoRI[-5] and list_DNA[-6] == EcoRI[-6]):
        print ("The position of the EcoRI :GAATTC(pattern) is from", len(list_DNA)-5, "to", len(list_DNA),".")
        
    #finding the Dsal pattern CCGCGG
    if (list_DNA[-1] == Dsal1[-1] and list_DNA[-2] == Dsal1[-2] and list_DNA[-3] == Dsal1[-3] and list_DNA[-4] == Dsal1[-4] and list_DNA[-5] == Dsal1[-5] and list_DNA[-6] == Dsal1[-6]):
        print ("The position of the Dsal pattern CCGCGG is from", len(list_DNA)-5, "to", len(list_DNA),".")
        
    #finding the Dsal pattern CCGTGG
    if (list_DNA[-1] == Dsal2[-1] and list_DNA[-2] == Dsal2[-2] and list_DNA[-3] == Dsal2[-3] and list_DNA[-4] == Dsal2[-4] and list_DNA[-5] == Dsal2[-5] and list_DNA[-6] == Dsal2[-6]):
        print ("The position of the Dsal pattern CCGTGG is from", len(list_DNA)-5, "to", len(list_DNA),".")
        
    #finding the Dsal pattern CCACGG
    if (list_DNA[-1] == Dsal3[-1] and list_DNA[-2] == Dsal3[-2] and list_DNA[-3] == Dsal3[-3] and list_DNA[-4] == Dsal3[-4] and list_DNA[-5] == Dsal3[-5] and list_DNA[-6] == Dsal3[-6]):
        print ("The position of the Dsal pattern CCACGG is from", len(list_DNA)-5, "to", len(list_DNA),".")
        
    #finding the Dsal pattern CCATGG
    if (list_DNA[-1] == Dsal4[-1] and list_DNA[-2] == Dsal4[-2] and list_DNA[-3] == Dsal4[-3] and list_DNA[-4] == Dsal4[-4] and list_DNA[-5] == Dsal4[-5] and list_DNA[-6] == Dsal4[-6]):
        print ("The position of the Dsal pattern CCATGG is from", len(list_DNA)-5, "to", len(list_DNA),".")