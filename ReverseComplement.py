#!/usr/bin/python3

#Input: A DNA string Pattern.
#Output: Patternrc , the reverse complement of Pattern.

def _ReverseComplement(Pattern):
  Patternrc = list(Pattern)
  sizePatternrc = len(Patternrc)
  for i in range(0, sizePatternrc):
    if Patternrc[i] == 'A':
      Patternrc[i] = 'T'
    elif Patternrc[i] == 'T':
      Patternrc[i] = 'A'
    elif Patternrc[i] == 'C':
      Patternrc[i] = 'G'
    elif Patternrc[i] == 'G':
      Patternrc[i] = 'C'
    else:
      print("error")
      return 1
  Patternrc.reverse()
  strPatternrc = ''.join(Patternrc)
  return strPatternrc 

p="ACGT"
print(_ReverseComplemen(p))
