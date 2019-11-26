#Q8
filename='dictionary.txt'
def f(word1,word2):
	with open(filename) as txtfile:
		active1=False
		active2=False
		index1=0
		index2=0
		for i,line in enumerate(txtfile):
			line=line.strip('\n')
			if word1 == line:
				active1=True
				index1=i
			if word2 == line:
				active2=True
				index2=i
			if active1 and active2:
				break
		num_word=abs(index2-index1)-1
		if word1==word2:
			if not active1:
				print(f'{word1} not found in the dictionary')
			else:
				print(f'{word1} found in the dictionary')
		elif active1 and active2:
			print(f'there are at least {num_word} between {word1} and {word2}')
f('AARHUS','ABANDONED')
f('ABANDONS','ABANDONS')
f('ABANDONSaa','ABANDONSaa')
#这题原题要求记不清了，反正做题过程差不多是这样

