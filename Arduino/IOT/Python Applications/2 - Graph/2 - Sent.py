from matplotlib import pyplot as plt
from matplotlib import style

Size = [15,30,50,75,100,150]
PADR = [5860,5261,5724,5700,5293,5062]
PAR = [5846,4964,5533,5194,4723,4730]
SARA = [5829,4934,5015,4819,4473,4944]
AODV = [4848,4495,5033,4375,3893,3347]


style.use('ggplot')

plt.plot(Size,PADR,'b',label='PADR',marker='^', linewidth=1)
plt.plot(Size,PAR,'g',label='PAR', marker='x',linewidth=1)
plt.plot(Size,SARA,'r',label='SARA',marker='|', linewidth=1)
plt.plot(Size,AODV,'y',label='AODV', marker='o',linewidth=1)

plt.title('Network Size .vs. Packet Sent')
plt.ylabel('Packet Generated')
plt.xlabel('Network Size')
plt.xticks([0,20,40,60,80,100,120,140,160])
plt.legend()

plt.show()
