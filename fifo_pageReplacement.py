#FIFO
import matplotlib.pyplot as plt
import functools
import random
page_fault = []
frameno = []
page=[]
print("NUMBER OF PAGES: 15")
#page = [20, 13, 9, 14, 12, 17, 5, 2, 16, 7, 14, 7, 8, 7, 13]
n = 15
for i in range(n):
    page.append(random.randint(1,20))
print(page)
print("pages =",page)
for x in range(1,8):
	print("NUMBER OF FRAMES: ",end =" ")
	print(x)
	frame=[]
	d=x
	for i in range(0,d):
	    frame.append(-1)
	j=0
	count=0
	for i in range(0,n):
	    available=0
	    for k in range(0,d):
	        if(frame[k]==page[i]):
	            available=1
	    if(available == 0):
	        frame[j]=page[i]
	        j=(j+1)%d
	        count=count+1
	        print(frame)
	print("page fault is: ",end=" ")
	print(count)
	page_fault.append(count)
	frameno.append(x)

plt.plot(frameno[0:],page_fault[0:],marker='o',color='black',label='page faults')
plt.legend(loc='upper right')
plt.xlabel('No. of frames')
plt.ylabel('page faults')
plt.xticks(frameno[0:],frameno[0:])
plt.style.use('ggplot')
plt.show()



'''
1. Start the process

2. Declare the size with respect to page length

3. Check the need of replacement from the page to memory

4. Check the need of replacement from old page to new page in memory

5. Forma queue to hold all pages

6. Insert the page require memory into the queue

7. Check for bad replacement and page fault

8. Get the number of processes to be inserted

9. Display the values

10. Stop the process '''
