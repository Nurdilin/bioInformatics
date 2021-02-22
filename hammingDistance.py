
#!/bin/usr/python3

# We say that position i in k-mers p1 … pk and q1 … qk is a mismatch if pi ≠ qi. 
# For example, CGAAT and CGGAC have two mismatches. 
# The number of mismatches between strings p and q is called the Hamming distance between these strings 
# and is denoted HammingDistance(p, q).

s1 = "GGGCCGTTGGT"
s2 = "GGACCGTTGAC"

def _hammingDistance(s1, s2):
	hd = 0 #hamming distance
	if len(s1) != len(s2):
		print("strings must be equal lenghts, exiting")
		return -1
	for c in range(len(s1)):
		if s1[c] != s2[c]:
			hd = hd +1
	return hd

print(_hammingDistance(s1, s2))
