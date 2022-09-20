#!/usr/local/bin/python3
import numpy as np
from matplotlib import pyplot as plt
import math
import os
i=np.arange(1,48+1,1, dtype=int)
g=np.array([\
               0.0431, 0.0398, 0.0555, 0.0597, 0.0503, 0.0299, 0.0433, 0.0611, \
               0.0422, 0.0619, 0.0437, 0.0714, 0.0896, 0.0488, 0.0500, 0.0433, \
               0.0453, 0.0492, 0.0613, 0.0673, 0.0626, 0.0496, 0.0781, 0.0892, \
               0.0682, 0.0712, 0.0641, 0.0864, 0.0262, 0.0674, 0.0928, 0.078,  \
               0.0337, 0.0334, 0.0742, 0.120,  0.057,  0.105,  0.142,  0.0503, \
               0.0488, 0.0548, 0.0572, 0.069,  0.0434, 0.0405, 0.0595, 0.0736])

plt.figure (num=1,dpi=120)
plt.title  ('HTCC Gains')
plt.xlabel ('PMT number')
plt.ylabel ('Gain=Nphe/FADC count')
#plt.yscale("log")
plt.grid()
#plt.xlim(0.0,10)
plt.ylim(0.001,0.150)

col=['Black','Red','Blue','Magenta','Grey','Green']
lab=['Sector 1', 'Sector 2', 'Sector 3', 'sector 4', 'sector 5', 'sector 6']
#plt.plot(i,g,marker='o',color='Green')
for j in [0,1,2,3,4,5]:
    j1=j*8; j2=j1+8
    plt.plot(i[j1:j2],g[j1:j2],marker='o',color=col[j],label=lab[j])
plt.legend()
plt.savefig('HTCC_gains.png')
os.system("open -a Preview HTCC_gains.png")

#plt.show()
