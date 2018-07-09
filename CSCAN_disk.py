##### C_SCAN DISC SCHEDULING ALGO IN OS#####

import matplotlib.pyplot as plt
import functools
import random
def sorting(queue,n):
    for i in range(0,n-1):
        small = queue[i]
        l = i
        for j in range(i+1,n):
            if(small > queue[j]):
                small = queue[j]
                l = j
        temp = queue[l]
        queue[l] = queue[i]
        queue[i] = temp

def clook_algo(left,right,count,n,head):
    seek=0
    arr = []
    arr.append(head)
    x = count - 1
    y = count + 1
    c = 0
    d = 0
    while y < n + 1:
        arr.append(right[c])
        c += 1
        y += 1
    arr.append(199)
    arr.append(0)
    while x > -1:
        arr.append(left[x])
        x -= 1
        d += 1
    for i in range(0,len(arr)):
        seek=seek+abs(head-arr[i])
        head=arr[i]
    print("Scanning Order : ")
    print(arr)
    print("Total Seek Time : " + str(seek))
    print("Average Seek Time : " + str(seek/float(n)))

    plt.plot(arr[0:],marker='o',color='black',label='head movement')
    plt.legend(loc='upper left')
    plt.ylabel('Disk I/O requests')
    plt.yticks(arr[0:],arr[0:])
    plt.style.use('ggplot')
    plt.show()

def division(queue,n,head):
    left = []
    right = []
    for i in range(0,n):
        if(queue[i] > head):
            break
    p = 0
    m = n
    left.append(queue[0])
    for q in range(1,i):
        left.append(queue[q])
    k=i
    left=left[::-1]
    for x in range(k,n):
        right.append(queue[x])
    clook_algo(left,right,i,n,head)

queue=[]
t=[]
print("LENGTH OF QUEUE: 8")
n=8
print("THE QUEUE : 98,183,37,122,14,124,65,67")
queue=[98,183,37,122,14,124,65,67]
print("STARTING HEAD : 53")
head=53
print(queue)
sorting(queue,n)
division(queue,n,head)
