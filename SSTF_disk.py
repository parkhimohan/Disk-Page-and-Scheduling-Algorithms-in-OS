##### SSTF DISC SCHEDULING ALGO IN OS#####
import matplotlib.pyplot as plt
import functools
import random
queue=[]
t=[]
print("LENGTH OF QUEUE:")
#n=int(input())
n=8
print("ENTER THE QUEUE : ")
#for i in range(0,n):
 #   queue.append(int(input()))
queue=[98,183,37,122,14,124,65,67]
print("STARTING HEAD : ")
#head=int(input())
head=53
for i in range(0,n):
    t.append(abs(head-queue[i]))
print(t)
for i in range(0,n):
    for j in range(i,n):
        if(t[i]>t[j]):
            temp=t[i]
            t[i]=t[j]
            t[j]=temp
            temp=queue[i]
            queue[i]=queue[j]
            queue[j]=temp
print(t)
seek=0
a=[head]
print(queue)
for i in range(0,n):
    seek=seek+abs(head-queue[i])
    head=queue[i]
    a.append(head)
print(a)    
print("Total Seek Time : " + str(seek))
print("Average Seek Time : " + str(seek/float(n)))

plt.plot(a[0:],marker='o',color='black',label='head movement')
plt.legend(loc='upper left')
plt.ylabel('Disk I/O requests')
plt.yticks(a[0:],a[0:])
plt.style.use('ggplot')
plt.show()
