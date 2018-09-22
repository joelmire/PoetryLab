'''
Created on Aug 3, 2017

@author: joelmire
'''
# from workspace import nounSearch

speechList = ["noun", "verb", "pronoun", "adjective", "preposition", "adverb", "article"]

def fileToStringList(filename):
    """
    filename is a file, 
    returns a list of strings, each string represents
    one line from filename
    """
    wordlist = []
    f = open(filename)
    for line in f:
        line = line.strip()
        wordlist.append(line)
    f.close()
    return wordlist

def dictBuilder():
    dict = {}
    for item in range(len(speechList)):
        speechPart = speechList[item]
        filename = speechPart + " dictionary"
        wordList = fileToStringList(filename)
        for word in wordList:
            if len(word) > 0:
                key = word[0]
                if key not in dict:
                    letterDict = {}    
                    dict[key] = letterDict  
                if word in dict[key]:
                    dict[key][word].append(speechPart)                   
                else:
                    dict[key][word] = [speechPart]   
    return dict

             
             
if __name__ == '__main__':
    print dictBuilder() 
    
    
    
    