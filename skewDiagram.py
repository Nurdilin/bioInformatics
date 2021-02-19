#!/usr/bin/python3

# Give all values of *Skewi* (GAGCCACCGCGATA) for *i* ranging from 0 to 14.
# **Sample Input:**     CATGGGCATCGGCCATACGCC
 #**Sample Output:**     0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2

genome = """GAGCCACCGCGATA"""
range_max = 14
range_min = 0

def _skew(genome, range_min, range_max):
	skew = []
	skew.append(0)
	for i in range(range_min, range_max):
		print(i)
		if genome[i] == 'C':
			skew.append(skew[i] -1)
		elif genome[i] == 'G':
			skew.append(skew[i] +1)
		else:
			skew.append(skew[i])
	return skew

fou = _skew(genome,range_min,range_max)
print(*fou)
