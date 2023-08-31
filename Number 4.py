from matplotlib import pyplot as plt
from matplotlib_venn import venn3


Total people = 120
nmr = 65
tmr = 45
fmr = 42
ntmr = 20
nfmr = 25
tfmr = 15
allr = 8

venn3(subsets=(nmr, tmr, ntmr, fmr, nfmr, tfmr, allr),
                set_labels=('Newsweek', 'Time', 'Fortune'))
plt.title("Magazine Readers Venn Diagram")
plt.show()

at_least_one_reader = nmr + tmr + fmr -  \
                      ntmr - nfmr -  \
                      tfmr + allr
                    
exactly_one_reader = ((nmr - ntmr - nfmr - allr) + \
                    (tmr - tfmr - ntmr - allr) + \
                    (fmr - tfmr - nfmr - allr))

print("Number of people who read at least one magazine:", at_least_one_reader)
print("Number of people who read exactly one magazine:", exactly_one_reader)