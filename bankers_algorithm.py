import matplotlib.pyplot as plt
for _ in range(int(input())):
	t=[]
	pq=[]
	pql=[]
	print("Enter the number of types of resources available")
	types = int(input())
	maximum_available_resources = []
	print("Enter the number of instances available of each resource")
	available_instances = []
	for i in range(types):
		maximum_available_resources.append(int(input()))
		available_instances.append(maximum_available_resources[i])
	print("Enter the number of processes in queue")
	processes = int(input())
	allocation_table=[]
	max_table = []
	need_table = []
	processes_left = []
	safe_order = []
	print("Enter the resource instances allocated, max required and needed for each process")
	for i in range(processes):
		pq.append(i)
		pql.append('Process_'+str(i))
		print("Process ",i)
		print("Enter the resources allocated")
		allocation_table.append(list(map(int,input().split(' '))))
		print("Enter the maxium resources required")
		max_table.append(list(map(int,input().split(' '))))
		l = []
		for j in range(types):
			l.append(max_table[i][j]-allocation_table[i][j])
		need_table.append(l)
		if(need_table[i].count(0)==types):
			processes_left.append(1)
			t.append(0)
		else:
			processes_left.append(0)
			t.append(0)
	for i in range(processes):
		for j in range(types):
			available_instances[j] -= allocation_table[i][j]
	print(available_instances)
	i=0
	while(True):
		if(processes_left.count(1)==processes):
			break
		elif(i>100*processes):
			print("deadlock")
			break
		else:
			p = i%processes
			if(p not in safe_order):
				if(need_table[p].count(0)!=types):
					flag = 0
					for j in range(types):
						if(need_table[p][j]<=available_instances[j]):
							flag += 1
					if(flag==types):
						for k in range(types):
							need_table[p][k]=0
							available_instances[k]+=allocation_table[p][k]
						processes_left[p]=1 
						t[p] = i
						safe_order.append(p)
						i +=1
					else:
						i+=1
				else:
					i+=1
			else:
				i+=1
	print(safe_order)
	plt.plot(pq,t,marker='o',color='black',label='time')
	plt.legend(loc='upper right')
	plt.xlabel('Process number')
	plt.ylabel('time')
	plt.title('Banker\'s Algorithm',color='black')
	plt.xticks(pq,pql)
	plt.style.use('ggplot')
	plt.show()
