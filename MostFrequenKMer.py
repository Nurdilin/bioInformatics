#!/usr/bin/python3

ori = """atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccac
aacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgacca
cggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtg
cttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaa
gcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtt
tttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatt
tacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaa
ttctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctatttt
ttacggaagaatgatcaagctgctgctcttgatcatcgtttc""".replace('\n',' ')

def _FrequencyMap(Text, k):   
    freqDict = {}   #create a dictionary
    textSize = len(Text)   
    for i in range(0, textSize-k+1):   #for i in range(textSize-k+1):
        pattern = Text[i:i+k]   
        if pattern in freqDict:   
            freqDict[pattern] += 1   
        else:   
            freqDict[pattern] = 1   
    return freqDict

def _MostFrequenKMer(Text, k):
    kmers=[]
    freqMapDict=_FrequencyMap(Text,k)
    _max = max(freqMapDict.values())
    for most_frequent_kmer in freqMapDict:   
        if freqMapDict[most_frequent_kmer] == _max:   
            kmers.append(most_frequent_kmer)
    return kmers   

#def _MostFrequenKMer(Text,k): 
# Note to self
# This will not work correctly as it does not take into account ties
#	freqMapDict=_FrequencyMap(Text,k)
#	_max=max(freqMapDict, key=freqMapDict.get)
#	return _max


print("most frequent 4-mer is ",_MostFrequenKMer(ori, 4))
