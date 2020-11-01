code = {"GLY":"G", "ALA":"A", "LEU":"L", "ILE":"I", "ARG":"R", "LYS":"K", "MET":"M", "CYS":"C", "TYR":"Y", "THR":"T", "PRO":"P", "SER":"S", "TRP":"W", "ASP":"D", "GLU":"E", "ASN":"N", "GLN":"Q", "PHE":"F", "HIS":"H", "VAL":"V"}

a = [['A', 'T', 'G'], ['A', 'T', 'A'], ['T', 'G', 'G'], ['A', 'G', 'G'], ['A', 'G', 'G'], ['T', 'A', 'G']]
nicer = []
for i in a:
    nicer.append(''.join(i))
print (nicer) 