#OPTIMAL

import matplotlib.pyplot as plt
import functools
import random
page_fault = []
frameno = []
page=[]
frame=[]
temp=[]
counter=0
faults=0
print("NUMBER OF PAGES:")
'''n=int(input())

print("PAGE NUMBERS : ")
'''
n = 15
for i in range(n):
    page.append(random.randint(1,20))
print(page)    

for x in range(1,8):
	print("NUMBER OF FRAMES : ", end=" ")
	print(x)
	frame=[]
	faults = 0
	d=x
	for i in range(0,d):
	    frame.append(-1)

	for i in range(0,n):
	    flag1=0
	    flag2=0
	    for j in range(0,d):
	        if(frame[j] == page[i]):
	            flag1=1
	            flag2=1
	            break
	    if ( flag1== 0 ):
	        for j in range(0,d):
	            if(frame[j] == -1):
	                faults=faults+1
	                frame[j]=page[i]
	                flag2=1
	                break
	    if (flag2 == 0):
	        flag3=0
	        for j in range(0,d):
	            temp.append(-1)
	            for k in range(i+1,d):
	                if (frame[j] == page[k]):
	                    temp[j]=k
	                    break
	        for j in range(0,d):
	            if (temp[j] == -1):
	                pos=j
	                flag3=1
	                break
	        if(flag3==0):
	            m=temp[0]
	            pos=0
	            for j in range(1,d):
	                if(temp[j]>m):
	                    m=temp[j]
	                    pos=j
	        frame[pos]=page[i]
	        faults=faults+1
	    print(frame)
	print("total page faults ",end=" ")
	print(faults)
	page_fault.append(faults)
	frameno.append(x)

plt.plot(frameno[0:],page_fault[0:],marker='o',color='black',label='page faults')
plt.legend(loc='upper right')
plt.xlabel('No. of frames')
plt.ylabel('page faults')
plt.xticks(frameno[0:],frameno[0:])
plt.style.use('ggplot')
plt.show()
