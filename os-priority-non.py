import matplotlib.pyplot as plt
import random
n=int(input("Enter the no. of process : "))
processes=[]
btime=[]
y=[]
for i in range(0,n):
 processes.insert(i,i+1)
 btime.append(random.randint(1,10))
#Input Priority of every process
priority=random.sample(range(1,n+1),n)
wtime=[0]
#print("priority =",priority)
y=[]
print("process\tburst time\tpriority\twaiting time")
for i in range(1,n+1):
    k=priority.index(i)
    y.append('P'+str(k))
    wtime.insert(i,wtime[i-1]+btime[k])
    print("P"+str(i)+"\t"+str(btime[k])+"\t\t"+str(i)+"\t\t"+str(wtime[-2]))
#calculating average waiting time and average turn around time
avgwt=0
avgwt=float(sum(wtime[:-1]))/n
print("average waiting time =",avgwt)
plt.hlines(y,wtime[1:],wtime[:-1],linewidth=15)
plt.show()
