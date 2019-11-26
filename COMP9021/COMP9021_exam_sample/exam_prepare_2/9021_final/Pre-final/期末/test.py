#test
filename='dictionary.txt'
with open(filename) as txtfile:
	index=0
	lines=txtfile.readlines()
	for i in lines:
		i=i.strip('\n')
		index+=1
		print(i)
		if index==3:
			break

