'''
Created on Jul 20, 2017
@author: joelmire

1) create dictionary of words; key should contain part of speech
2) GUIs
3) 
'''
from Crypto.Util.RFC1751 import wordlist
from dictStuff import dictBuilder

dict = dictBuilder()

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

# def dictStuff():
#     dict = {}
#     for item in range(len(speechList)):
#         speechPart = speechList[item]
#         filename = speechPart + " dictionary"
#         wordList = fileToStringList(filename)
#         for word in wordList:
#             if len(word) > 0:
#                 key = word[0]
#                 if key not in dict:
#                     letterDict = {}    
#                     dict[key] = letterDict  
#                 if word in dict[key]:
#                     dict[key][word].append(speechPart)                   
#                 else:
#                     dict[key][word] = [speechPart]   
#     return dict

def chooseFilter():
    """user inputs a filter choice"""
    filter = str(raw_input("Type the filter of your choice ('noun', 'pronoun', 'verb', 'adjective', 'preposition', or 'adverb'):"))
    print 
    filterSearch(filter)
    
def filterSearch(filter):
    """directs filter input to filter search function"""
    if filter == "noun":
        nounSearch(filter)
    if filter == "pronoun":
        pronounSearch(filter)
    if filter == "verb":
        verbSearch(filter)
    if filter == "adjective":
        adjectiveSearch(filter)   
    if filter == "adverb":
        adverbSearch(filter)    
    if filter == "preposition":
        prepositionSearch(filter)
    if filter == "article":
        articleSearch(filter)   
        
                
def articleSearch(filter):
    filteredText = []
    for line in poemList:
        line = line.split(" ")
        words = ""
        for i, word in enumerate(line):
            if word.isalpha():
                words += " "
                key = word[0]
                if 'article' in dict[key][word]:
                    wordState = word.upper()
                words += wordState 
        filteredText += words        
    printPoem(filteredText)           

def adjectiveSearch(filter):
    filteredText = []
    for line in poemList:
        line = line.split(" ")
        words = ""
        for i, word in enumerate(line):
            if word.isalpha():
                words += " "
                key = word[0]
                if 'adjective' in dict[key][word]:
                    wordState = word.upper()
                words += wordState 
        filteredText += words        
    printPoem(filteredText)
    
def adverbSearch(filter):    
    filteredText = []
    for line in poemList:
        line = line.split(" ")
        words = ""
        for i, word in enumerate(line):
            if word.isalpha():
                words += " "
                key = word[0]
                if 'adverb' in dict[key][word]:
                    wordState = word.upper()
                words += wordState 
        filteredText += words        
    printPoem(filteredText)
    
def prepositionSearch(filter):    
    filteredText = []
    for line in poemList:
        line = line.split(" ")
        words = ""
        for i, word in enumerate(line):
            if word.isalpha():
                words += " "
                key = word[0]
                if 'preposition' in dict[key][word]:
                    wordState = word.upper()
                words += wordState 
        filteredText += words        
    printPoem(filteredText)
    
    
def printPoem(filteredText):   
    "prints final poem"
    for item in filteredText:
        print item

def info(poemList):
    print 
    stanzaCount = 1
    lineCount = 0
    wordCount = 0
    for item in poemList:
        if item == "":
            stanzaCount += 1
        if item != "":    
            lineCount += 1
        for word in item.split():
            wordCount += 1
    return ("Stanzas: " + str(stanzaCount), "Lines: " + str(lineCount), "Words: " + str(wordCount))     

# def nounSearch(filter):
#     """
#     Searches through noun dictionary to capitalize nouns in the poem text. 
#     """
#     nouns = fileToStringList("noun dictionary")
#     filteredText = []
#     for line in poemList:
#         line = line.split(" ")
#         words = ""
#         for word in line:
#             words += " "
#             if word in nouns:
#                 words += word.upper()
#             else:
#                 words += word         
#         filteredText += [words]
#     printPoem(filteredText) 

def nounSearch(filter):
    filteredText = [] 
    for line in poemList:
        print line
        line = line.strip().split(" ")
        words = ""
        for i, word in enumerate(line):
            if word.isalpha():
                if word == "stand,":
                    print "something is wrong"
                print "yay"
                lowerWord = word.lower()
                print lowerWord
                wordState = ""
                words += " "
                key = lowerWord[0]
                print key
                
                if 'noun' in dict[key][lowerWord]:
                    wordState = word.upper()
                if 'verb' in dict[key][lowerWord]:
                    previous = ''
                    for ch in line[i - 1]:
                        if ch.isalpha():
                            previous += ch
                    print previous
                    if 'pronoun' in dict[previous[0]][previous] or 'noun' in dict[previous[0]][previous]:
                        wordState = word.lower()      
                if wordState != "":
                    words += wordState
                else:
                    words += word 
        filteredText += words        
    printPoem(filteredText)
    
                                      
def pronounSearch(filter):
    """
    Searches through pronoun dictionary to capitalize pronouns in the poem text. 
    """
    pronouns = fileToStringList("pronoun dictionary")
    filteredText = []
    for line in poemList:
        line = line.split(" ")
        words = ""
        for word in line:
            words += " "
            if word in pronouns:
                words += word.upper()
            else:
                words += word         
        filteredText += [words]
    printPoem(filteredText)    
    
def verbSearch(filter):   
    """
    Searches through verb dictionary to capitalize verbs in the poem text. 
    """
    verbs = fileToStringList("verb dictionary")
    filteredText = []
    for line in poemList:
        line = line.split(" ")
        words = ""
        for word in line:
            words += " "
            if word in verbs:
                words += word.upper()
            else:
                words += word         
        filteredText += [words]
    printPoem(filteredText) 
    

            
                            
def main(): 
    filename = "Dover Beach"
    global poemList
    poemList = fileToStringList(filename)
    dictBuilder()
    chooseFilter()
    print info(poemList)
    


if __name__ == '__main__':
    main()
    
    
    