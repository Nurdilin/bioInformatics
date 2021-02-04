#!/usr/bin/python3

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

k = 3

ori = """atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccac
aacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgacca
cggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtg
cttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaa
gcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtt
tttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatt
tacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaa
ttctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctatttt
ttacggaagaatgatcaagctgctgctcttgatcatcgtttc""".replace('\n',' ')

print(_FrequencyMap(ori, k)) 	

# Example output
#{'atc': 21, 'tca': 17, 'caa': 11, 'aat': 9, 'atg': 15, 'tga': 25, 'gat': 21, 'aac': 3, 'acg': 6, 'cgt': 5, 'gta': 4, 'taa': 6, 'aag': 11, 'agc': 9, 'gct': 9, 'ctt': 17, 'ttc': 12, 'tct': 16, 'cta': 3, 'gca': 3, 'cat': 16, 'agg': 5, 'ggt': 4, 'gtg': 5, 'tgc': 7, 'ctc': 14, 'cac': 4, 'aca': 6, 'cag': 2, 'agt': 2, 'gtt': 11, 'ttt': 11, 'tta': 9, 'tat': 6, 'tcc': 7, 'cca': 8, 'ac ': 1, 'c a': 1, ' aa': 1, 'acc': 5, 'cct': 9, 'ctg': 10, 'gag': 6, 'tgg': 4, 'gga': 7, 'gac': 13, 'aga': 8, 'ata': 7, 'tag': 5, 'gtc': 1, 'tcg': 7, 'ttg': 17, 'tgt': 10, 'tac': 7, 'act': 9, 'ca ': 1, 'a c': 1, ' cg': 1, 'cgg': 5, 'gaa': 7, 'aaa': 4, 'att': 10, 'ggc': 3, 'gcc': 8, 'cgc': 4, 'tg ': 1, 'g c': 1, ' ct': 1, 'gcg': 4, 'ggg': 1, 'cga': 7, 'aa ': 2, 'a g': 1, ' gc': 1, 'tt ': 3, 't t': 3, ' tt': 3, 'ccg': 3, ' ta': 1, 'a t': 1, 'ccc': 1}

