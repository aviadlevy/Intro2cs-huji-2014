#from NonRecursiveMystery import mystery_computation
#from GetToTheZero import *
#from AlignDNA import *
from align import *
from AlignDNA import *
#x=is_solvable(0,[[2]+[3]*499+[0]])
#x=get_alignment_score('CTGAGCTGACTGATGCTGAGCTAGTGCTAGTCGTACGATCGTCGTCAGTACTGCGTGTCGTCCGCGCGAGTCGTAGTAGCTGCTGTACGTACGTCAGTCGT', '-----------------------------------------------------------------------------------------------------', 1, -1, -2)
#x= findOptimalAlignment('ACCG-T', 'ACCGG-',1,-1,-2)
x= get_best_alignment_score('AAAAA', 'CCCCC', 30, 26, 10)
print(x)
