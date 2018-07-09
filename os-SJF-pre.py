import random
import numpy as np
import matplotlib.pyplot as plt
def findWaitingTime(pro,n,wt,btime,order,s):
    complete=0
    t=0
    minm=max(btime)+1
    shortest=0
    check=0
    while(complete!=n):
        for j in range(n):
            if((pro[j][1] <= t) and (btime[j]<minm) and (btime[j])):
                minm=btime[j]
                shortest=j
                check=1
        if(check==0):
            t+=1
            continue
        if(pro[shortest][2] !=order[-1]):
            order.append(pro[shortest][2])
            s.append(t)
        btime[shortest]-=1
        minm=btime[shortest];
        if(minm==0):
            minm=max(btime)+1
        if(btime[shortest]==0):
            complete+=1
            finish_time=t+1
            wt[shortest]=finish_time-pro[shortest][0]-pro[shortest][1]
            if(wt[shortest]<0):
                wt[shortest]=0
        t+=1
    s.append(t)
def findTurnAroundTime(pro,n,wt,tat):
    for i in range(n):
        tat[i]=pro[i][0]+wt[i]
def findavgTime(pro,n,btime):
    wt=[0]*n
    tat=[0]*n
    total_wt=0
    total_tat=0
    order=[0]
    s=[]
    findWaitingTime(pro,n,wt,btime,order,s)
    print()
    findTurnAroundTime(pro,n,wt,tat)
    for i in range(n):
        total_wt=total_wt+wt[i]
        total_tat+=tat[i]
    l=len(order)
    y=[]
    x1=[]
    x2=[]
    const=min(s)
    print("Process\tBurst Time\tArrival Time\tWaiting Time\tFinish Time")
    for i in range(1,l):
        y.append('P'+str(order[i]))
        x1.append(s[i-1])
        x2.append(s[i])
        print(str(y[-1])+"\t"+str(pro[order[i]-1][0])+"\t\t"+str(pro[order[i]-1][1])+"\t\t"+str(x1[-1]-pro[order[i]-1][1])+"\t\t"+str(x2[-1]))
    plt.hlines(y,x1,x2,linewidth=15)
    plt.show()
def main():
    n=int(input("Enter the no. of process : "))
    pro=[]
    btime=[]
    for i in range(n):
        k=[]
        k.append(random.randint(1,10))  #burst time
        k.append(random.randint(0,n+2)) #arrival time
        k.append(i+1)                   #pid
        pro.append(k)
        btime.append(k[0])
    findavgTime(pro,n,btime)
main()
