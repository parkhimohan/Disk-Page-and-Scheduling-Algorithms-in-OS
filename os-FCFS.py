import matplotlib.pyplot as plt
n=int(input("Enter the no. of process : "))
import random
btime=[]
wtime=[]
wt=0
y=[]
wtime.insert(0,0)
for i in range(n):
    y.append('P'+str(i))
    btime.append(random.randint(1,10))    #generating burst times using random
print("process\tburst time\twaiting time")
for i in range(1,len(btime)+1):
    wtime.insert(i,wtime[i-1]+btime[i-1])
    wt+=wtime[i]
    print("P"+str(i-1)+"\t"+str(btime[i-1])+"\t\t"+str(wtime[i-1]))
avg_wt_time=float(wt/n)
print("average waiting time =",avg_wt_time)
plt.hlines(y,wtime[:-1],wtime[1:],linewidth=15)
plt.show()
