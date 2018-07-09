import numpy as np 
import matplotlib.pyplot as plt
import random
n=int(input("Enter the no.of process : "))
btime=[]
wtime=[]
pro=[]
wtime=[0]
for i in range(n):
    pro.append(i)
    btime.append(random.randint(1,10))      #generating burst time using random function
for i in range(n):
    for j in range(i+1,n):
        if btime[i]>btime[j]:
            temp=btime[j]
            btime[j]=btime[i]
            btime[i]=temp
            temp=pro[i]
            pro[i]=pro[j]
            pro[j]=temp
print("Process\tBurst Time\tWaiting Time")
avg_wt_time=0
y=[]
for i in range(n):
    print("P"+str(i)+"\t"+str(btime[i])+"\t\t"+str(wtime[i]))
    y.append("P"+str(i))
    wtime.append(wtime[-1]+btime[i])
print("Average Waiting Time =",sum(wtime)/n)
plt.hlines(y,wtime[:-1],wtime[1:],linewidth=15)
plt.show()
