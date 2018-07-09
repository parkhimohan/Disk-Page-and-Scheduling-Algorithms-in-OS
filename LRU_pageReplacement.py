#LRU (least recently used)
import matplotlib.pyplot as plt
import functools
import random
page_fault = []
frameno = []
page=[]
frame=[]
time=[]
def findLRU (n):
    minimum=time[0]
    pos=0
    for i in range(0,n):
        if(time[i]<minimum):
            minimum=time[i]
            pos=i
    return pos

counter=0
faults=0
print("NUMBER OF PAGES:")
'''n=int(input())

print("PAGE NUMBERS : ")
'''
n = 15
for i in range(n):
    page.append(random.randint(1,20))
print("pages=",page)

for x in range(1,8):
	print("NUMBER OF FRAMES : ")
	print(x)
	frame = []
	faults = 0
	d = x
	for i in range(0,d):
	    frame.append(-1)
	print(page)

	for i in range(0,n):
	    flag1=0
	    flag2=0
	    for j in range(0,d):
	        if(frame[j] == page[i]):
	            counter = counter+1
	            time.append(counter)
	            flag1=1
	            flag2=1
	            break
	    if ( flag1== 0 ):
	        for j in range(0,d):
	            if(frame[j] == -1):
	                counter = counter+1
	                faults=faults+1
	                frame[j]=page[i]
	                time.append(counter)
	                flag2=1
	                break
	    if (flag2 == 0):
	        pos=findLRU(d)
	        counter = counter+1
	        faults=faults+1
	        frame[pos]=page[i]
	        time[pos]=counter
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
