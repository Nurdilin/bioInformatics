#!/bin/usr/python3

genome = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
pattern = "ATTCTGGA"
d = 3

def _hammingDistance(s1, s2):
	hd = 0 #hamming distance
	if len(s1) != len(s2):
		print("strings must be equal lenghts, exiting")
		return -1
	for c in range(len(s1)):
		if s1[c] != s2[c]:
			hd = hd +1
	return hd

def _PatternStartingPosition(Genome, Pattern, d): 
	startingPositionList = []
	genomeSize = len(Genome)
	patternSize = len(Pattern)
	count = 0

	for i in range(0, genomeSize - patternSize +1):
		s1 = Genome[i:i+patternSize]
		s2 = Pattern
		hd = _hammingDistance(s1, s2)
		#this can be written as:
		# if _hammingDistance(Genome[i:i+patternSize], Pattern) <= d 
		#but it's nice to have some readability for the poor guy who will use that
		if hd <= d:
			count = count +1
	return startingPositionList


a=_PatternStartingPosition(genome, pattern, d)
#print(a)  #-> prin , separated List
print(*a) #-> print space separated List
#print(*a, sep=' -> ')  # 1 -> 2 -> 3 -> 4 -> 5
