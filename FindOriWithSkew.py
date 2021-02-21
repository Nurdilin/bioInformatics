#!/usr/bin/python3

# locating ori: it should be found where the skew attains a minimum.

genome = """TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"""
range_max = len(genome)
range_min = 0

def _skew(genome, range_min, range_max):
	skew = []
	skew.append(0)
	for i in range(range_min, range_max):
		if genome[i] == 'C':
			skew.append(skew[i] -1)
		elif genome[i] == 'G':
			skew.append(skew[i] +1)
		else:
			skew.append(skew[i])
	return skew

def _listMin(mylist):
	results = []
	_min = min(mylist)
	pos = 0
	for item in mylist:
		if item == _min:
			results.append(pos)
		pos = pos +1
	return results

Skew = _skew(genome,range_min,range_max)
SkewMin = _listMin(Skew)
print(*SkewMin)
