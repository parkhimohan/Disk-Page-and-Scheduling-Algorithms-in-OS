import random
import copy
import matplotlib.pyplot as plt
n=int(input("Enter the no. of process : "))
priority=random.sample(range(1,n+1),n)
atime=[]
btime=[]
btime1=copy.deepcopy(btime)
pro=[]
for i in range(n):
    atime.append(random.randint(1,n+2))
    btime.append(random.randint(1,10))
    pro.append("P"+str(i))
print()
for i in range(n-1):
    for j in range(i+1,n):
        if priority[i]>priority[j]:
            temp=priority[i]
            priority[i]=priority[j]
            priority[j]=temp

            temp=btime[i]
            btime[i]=btime[j]
            btime[j]=temp

            temp=atime[i]
            atime[i]=atime[j]
            atime[j]=temp

            temp1=pro[i]
            pro[i]=pro[j]
            pro[j]=temp1
time=0
const=max(atime)
order=[]
st=[]
fn=[]
btime1=copy.deepcopy(btime)
while(time<const):
    flag=0
    for i in range(n):
        if atime[i]<=time and btime[i]:
            st.append(time)
            time+=1
            btime[i]-=1
            order.append(pro[i])
            fn.append(time)
            flag=1
            break
    if flag==0:
        time+=1
for i in range(n):
    order.append(pro[i])
    st.append(time)
    time+=btime[i]
    fn.append(time)
#print(order)
#print(st)
#print(fn,end="\n\n")
const1=min(atime)
print("Process\tBurst Time\tArrival Time\tPriority\tWaiting Time")
for i in range(n):
    k=order.index("P"+str(i))
    k1=pro.index("P"+str(i))
    print(str(order[k])+"\t"+str(btime1[k1])+"\t\t"+str(atime[k1])+"\t\t"+str(priority[k1])+"\t\t"+str(st[k]-atime[k1]))
plt.hlines(order,st,fn,linewidth=15)
plt.show()
