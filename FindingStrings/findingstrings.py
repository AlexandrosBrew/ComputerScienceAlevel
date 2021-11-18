def charcount(text, char):
    charcount = 0
    for i in range(len(text)):
        if text[i] == char:
            charcount += 1
    return charcount

def wcount(text, word):
    wcount = 0
    text = text.split()
    for i in range(len(text)):
        if text[i] == word:
            wcount +=1 
    return wcount

def subString(text, start, numchars):
    return text[start:start+numchars]

def wcountfile(myfile, targetword):
    file = open("/Users/alexandrosbrew/Documents/ComputerScienceAlevel/FindingStrings/" + myfile, "r")
    filewcount = 0
    line = file.read().split()
    for i in range(len(line)):
        if line[i] == targetword:
            filewcount += 1
    return filewcount

counter = charcount("Hello", "H")
wcounter = wcount("Hello how are you today?", "how")
fcounter = wcountfile("beemovie.txt","and")
print(f'File word count: {fcounter} \nWord count in string: {wcounter}\nCharacter counter: {counter}')

