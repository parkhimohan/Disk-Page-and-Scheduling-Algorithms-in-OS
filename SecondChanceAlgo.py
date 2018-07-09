#SECOND CHANCE
import matplotlib.pyplot as plt
import random
page=[]
frame=[]
page_fault=[]
frameno=[]
ref=[]
repptr=0
count=0
full=0
print("ENTER NUMBER OF PAGES:")
n=int(input())

print("PAGE NUMBERS : ")
for i in range(0,n):
    page.append(random.randint(1,n+5))
    ref.append(0)
for x in range(1,n):
    print("NUMBER OF FRAMES : ",end=" ")
    d=x
    print(x)
    frame = []
    for i in range(0,d):
        frame.append(0)
    for i in range(0,n):
        q=page[i]
        flag=0
        if(full!=0):
            for j in range(0,full):
                if(q==frame[j]):
                    flag=1
                    ref[j]=1
                    break
        if(flag!=1):
            ele=page[i]
            if(full!=d):
                #print(full)
                ref[full]=1
                frame[full]=ele
                full=full+1
            else:
                while(ref[repptr]!=0):
                    ref[repptr]=0
                    repptr=repptr+1
                    if(repptr==d):
                        repptr=0
                temp=frame[repptr]
                frame[repptr]=ele
                ref[repptr]=1

            print("elements in frame : ",end=" ")
            print(frame)
            count=count+1
    print("Number of page faults "+ str(count-1))
    page_fault.append(int(count-1))
    frameno.append(x)

plt.plot(frameno,page_fault,marker='p',color='black',label='Page Faults')
plt.legend(loc='upper right')
plt.xlabel('No. of frames')
plt.ylabel('Page Faults')
plt.xticks(frameno,frameno)
plt.style.use('ggplot')
plt.show()
