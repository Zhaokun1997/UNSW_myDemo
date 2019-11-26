#Q5
from collections import defaultdict
def f(text):
	'''
	>>> text='I am Iron Man I hate Thanos I hope to kill him'
	>>> f(text)
	length 1 word:
	['i', 'i', 'i']
	length 2 word:
	['am', 'to']
	length 4 word:
	['iron', 'hate', 'hope', 'kill']
	length 3 word:
	['man', 'him']
	length 6 word:
	['thanos']
	'''
	word_dict=defaultdict(list)
	word=text.split()
	for i in word:
		if not i.islower():
			word_dict[len(i)].append(i.lower())
		else:
			word_dict[len(i)].append(i.lower())
	for i in word_dict.keys():
		print(f'length {i} word:')
		print(f'{word_dict[i]}')
		
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print('Test Done! If not show "Test Failed", you pass my test')
			
