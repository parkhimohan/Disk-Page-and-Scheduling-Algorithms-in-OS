import random
import numpy as np
import matplotlib.pyplot as plt
import copy
n=int(input("Enter the number of processes : "))
btime=[]
atime=[]
for i in range(n):
    btime.append(random.randint(1,10))  #burst time
    atime.append(random.randint(0,n+2)) #arrival time
const=min(atime)
btime1=copy.deepcopy(btime)
start=[]
finish=[]
y=[]
tquantum=int(input("Enter the time quantum : "))
time=0
while(1):
    flag=0
    for i in range(n):
        if(btime[i]>0 and atime[i]<=time):
            start.append(time)
            y.append("P"+str(i))
            if btime[i]>tquantum:
                time+=tquantum
                btime[i]-=tquantum
                flag=1
            else:
                time+=btime[i]
                btime[i]=0
                flag=1
            finish.append(time)
    if(flag==0):
        time+=1
    if(sum(btime)==0):
        break
l=len(y)
print("Process\tBurst time\tArrival Time\tWaiting time\tfinish time")
for i in range(n):
    k1=y.index("P"+str(i))
    y.reverse()
    k2=y.index("P"+str(i))
    y.reverse()
    print(y[k1]+"\t"+str(btime1[i])+"\t\t"+str(atime[i])+"\t\t"+str(start[k1]-atime[i])+"\t\t"+str(finish[l-k2-1]))
plt.hlines(y,start,finish,linewidth=15)
plt.show()
