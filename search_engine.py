def makeInverseIndex(strlist):
	inverseindex = {}
	strpairlist = list(enumerate(strlist))
	for idx, str in strpairlist:
		wordlist = str.split()
		for word in wordlist:
			if word in inverseindex:
				inverseindex[word].append(idx)
			else:
				inverseindex[word] = [idx]
	return inverseindex


mystrlist = ['the quick brown fox jumps over the lazy dog', 'that maps each word to the set consisting of the document numbers']
myinverseIndex = makeInverseIndex(mystrlist)
print(myinverseIndex)