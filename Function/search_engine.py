def makeInverseIndex(strlist):
	inverseindex = {}
	strpairlist = list(enumerate(strlist))
	for idx, str in strpairlist:
		wordlist = str.split()
		for word in wordlist:
			if word in inverseindex:
				if idx not in inverseindex[word]:
					inverseindex[word].append(idx)
			else:
				inverseindex[word] = [idx]
	return inverseindex

f = open('stories_small.txt')
mystrlist = list(f)
myinverseIndex = makeInverseIndex(mystrlist)
print(myinverseIndex)