
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

def _FindClumps(Text, k, L, t):
    patterns = []
    textSize = len(Text)
    windowSize = L
    for i in range(0, textSize - windowSize +1):
        window = Text[i:i+windowSize]
        freqMapDict=_FrequencyMap(window, k)
        #print("FrequencyMap of ", k ,"-mer in window [",i , i+windowSize, "] is: ", freqMapDict)
        for key in freqMapDict:
            #print("Checking for key", key)
            #print("Key", key, "appears", freqMapDict[key], "times")
            if freqMapDict[key] >= t:
                patterns.append(key)
    patternsUnique = list(set(patterns))
    return patternsUnique

k = 9 #kmers
window = 500
t = 3 #appearance

f = open("E_coli.txt", "r")
genome = f.read()
f.close()

a = _FindClumps(genome, k, window, t)
print("In windows", window, "we had ", t, "appearances of the following ",k , "-mers")
print(*a)
