'''
Created on Aug 4, 2017

@author: joelmire
'''
from dictBuilder import buildDict
from PIL.WmfImagePlugin import word
from Tkinter import *

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

    
# def chooseFilter():
#     """user inputs a filter choice"""
#     filter = str(raw_input("Select part of speech to set filter. Please input one of the following options: 'N' (noun), 'p' (plural), 'h' (noun phrase), 'V' (verb usu participle) "))
#     print
#     filterSearch(filter)

def chooseFilter():
    """user selects a filter choice"""
    constructor = Tk()
    frame = Frame(constructor)
    frame.grid()
    
    posLabel = Label(frame, text = 'Parts of Speech Filters')
    otherLabel = Label(frame, text = 'Other Analysis Features')
    nounButton = Button(frame, text = 'noun', command = lambda : filterSearch('N'))
    verbButton = Button(frame, text = 'verb', command = lambda : filterSearch('V'))
    pronounButton = Button(frame, text = 'pronoun', command = lambda : filterSearch('r'))
    adjectiveButton = Button(frame, text = 'adjective', command = lambda : filterSearch('A'))
    adverbButton = Button(frame, text = 'adverb', command = lambda : filterSearch('v'))
    conjunctionButton = Button(frame, text = 'conjunction', command = lambda : filterSearch('C'))
    prepositionButton = Button(frame, text = 'preposition', command = lambda : filterSearch('P'))
    interjectionButton = Button(frame, text = 'interjection', command = lambda : filterSearch('!'))
    infoButton = Button(frame, text = 'poem info', command = lambda : info(poemList))
    
    
    posLabel.grid(row = 0)
    nounButton.grid(row = 1)
    verbButton.grid(row = 2)
    pronounButton.grid(row = 3)
    adjectiveButton.grid(row = 4)
    adverbButton.grid(row = 5)
    conjunctionButton.grid(row = 6)
    prepositionButton.grid(row = 7)
    interjectionButton.grid(row = 8)
    
    otherLabel.grid(row = 0, column = 1)
    infoButton.grid(row = 1, column = 1)
    
    
    
    constructor.mainloop()
    
def filterSearch(filter):
    """directs filter input to filter search function"""
    
    if filter == "N":
        nounSearch(filter)
    if filter == "r":
        pronounSearch(filter)
    if filter == "V":
        verbUSUParticipleSearch(filter)
    if filter == "A":
        adjectiveSearch(filter)
    if filter == "V":
        adverbSearch(filter)  
    if filter == "C":
        conjunctionSearch(filter)    
    if filter == "P":
        prepositionSearch(filter)    
    if filter == "!":
        interjectionSearch(filter)    

def nounSearch(filter):   
    filteredText = []
    for line in poemList:
        line = line.strip().split(' ')
        words = []
        for i, word in enumerate(line):
            if line == ['']:                #checking for a stanza break
                break
            if word[0].isalpha():           #in the case of Dover beach, my code reads the word '--'; these two lines address the issue
                key = word[0]
            punctuationNote = 'undefined'       #this establishes a system to still analyze words that are followed by a punctuation mark like 'to-night,'
            if not word[-1].isalpha():
                punctuationNote = word[-1]
                word = word[:-1]
            if word in dict[key]:               #if the word is a noun, it is marked by capitalization
                if 'N' in dict[key][word] or 'p' in dict[key][word]:
                    word = word.upper()
            elif key.lower() + word[1:] in dict[key.lower()]:           #this allows words with a capitalized first letter to be double-checked. Most of these words are at the beginning of new sentences.
                if 'N' in dict[key.lower()][key.lower() + word[1:]] or 'p' in dict[key.lower()][key.lower() + word[1:]]:
                    word = word.upper()
#             """noun specific code begins"""
#             if word.isupper():
#                 if i > 0:                               #all possible preceding issues
#                     precedingKey = line[i - 1][0]
#                     precedingWord = line[i - 1]
#                     if not precedingWord in dict[precedingKey]:
#                         print "hello"
#                         precedingKey = precedingKey.lower()
#                         precedingWord = precedingWord.lower()
#                     else:
#                         if 'N' in dict[precedingKey][precedingWord] or 'p' in dict[precedingKey][precedingWord] or 'r' in dict[precedingKey][precedingWord]:
#                             word = word.lower()
#                     print word        
#  #               if i < len(line) - 2:                   #all possible posterior issues
#                     
#             """noun specific code ends"""
                    
            if punctuationNote == 'undefined':                      #adds words without punctuation marks
                words.append(word)
            else:
                words.append(word + punctuationNote)                    #adds words with punctuation marks   
        filteredText.append(words)                          #after the analysis, the entire line is appended to the FilteredText list
    printPoem(filteredText)                         #sends filteredText to the printing functi                          

def verbUSUParticipleSearch(filter):      
    filteredText = []
    for line in poemList:
        line = line.strip().split(' ')
        words = []
        for i, word in enumerate(line):
            if line == ['']:                #checking for a stanza break
                break
            if word[0].isalpha():           #in the case of Dover beach, my code reads the word '--'; these two lines address the issue
                key = word[0]
            punctuationNote = 'undefined'       #this establishes a system to still analyze words that are followed by a punctuation mark like 'to-night,'
            if not word[-1].isalpha():
                punctuationNote = word[-1]
                word = word[:-1]
            if word in dict[key]:               #if the word is a verb, it is marked by capitalization
                if 'V' in dict[key][word] or 't' in dict[key][word] or 'i' in dict[key][word]:
                    word = word.upper()
            elif key.lower() + word[1:] in dict[key.lower()]:           #this allows words with a capitalized first letter to be double-checked. Most of these words are at the beginning of new sentences.
                if 'V' in dict[key.lower()][key.lower() + word[1:]] or 't' in dict[key.lower()][key.lower() + word[1:]] or 'i' in dict[key.lower()][key.lower() + word[1:]]:
                    word = word.upper()
            if punctuationNote == 'undefined':                      #adds words without punctuation marks
                words.append(word)
            else:
                words.append(word + punctuationNote)                    #adds words with punctuation marks   
        filteredText.append(words)                          #after the analysis, the entire line is appended to the FilteredText list
    printPoem(filteredText)                         #sends filteredText to the printing function
    
    
    
# def nounSearch(filter):
#     filteredText = []
#     for line in poemList:  
#         line = line.strip().split(" ")
#         words = []
#         for i, word in enumerate(line):
#             wordState = ""
#             if not len(word.strip()) == 0:
#                 key = word[0]
#                 note = ''
#                 if key.isalpha():
#                     if word[-1] == "," or word[-1] ==";" or word[-1] == ".":
#                         note = word[-1]
#                         print 'there should be a note here', note
#                         word = word[:-1]
#                     if word not in dict[key]:
#                         if word.lower() in dict[key.lower()]:
#                             if filter in dict[key.lower()][word.lower()]:
#                                 wordState = word.upper()
#                             else: 
#                                 wordState = word   
#                         else:
#                             wordState = word  
#                     else:
#                         if filter in dict[key][word]: 
#                             wordState = word.upper()
#                         else:
#                             wordState = word           
# #                     if wordState != "":
# #                         words.append(wordState)
#                 else:
#                     
#                     wordState = word
#             print word        
#             if wordState == word.upper() and i < len(line) - 1:
#                 print "ok we are on the way"
#                 if line[[i + 1][0]][line[i + 1]] in dict:
#                     print "better"
#                     wordState = word    
# #             if wordState == word.upper() and 'V' in dict[line[i - 1][0]][line[i - 1]]:
# #                 wordState = word
# 
# 
#             if note != "":
#                 wordState += note
#             words.append(wordState)
#                                    
# #         if i < len(line) - 1:
# #             words = " ".join(words)                  
#         filteredText.append(words) 
#     printPoem(filteredText)                

def pronounSearch(filter):      
    filteredText = []
    for line in poemList:
        line = line.strip().split(' ')
        words = []
        for i, word in enumerate(line):
            if line == ['']:                #checking for a stanza break
                break
            if word[0].isalpha():           #in the case of Dover beach, my code reads the word '--'; these two lines address the issue
                key = word[0]
            punctuationNote = 'undefined'       #this establishes a system to still analyze words that are followed by a punctuation mark like 'to-night,'
            if not word[-1].isalpha():
                punctuationNote = word[-1]
                word = word[:-1]
            if word in dict[key]:               #if the word is a pronoun, it is marked by capitalization
                if 'r' in dict[key][word]:
                    word = word.upper()
            elif key.lower() + word[1:] in dict[key.lower()]:           #this allows words with a capitalized first letter to be double-checked. Most of these words are at the beginning of new sentences.
                if 'r' in dict[key.lower()][key.lower() + word[1:]]:
                    word = word.upper()
            if punctuationNote == 'undefined':                      #adds words without punctuation marks
                words.append(word)
            else:
                words.append(word + punctuationNote)                    #adds words with punctuation marks   
        filteredText.append(words)                          #after the analysis, the entire line is appended to the FilteredText list
    printPoem(filteredText)                         #sends filteredText to the printing function
                    
def adjectiveSearch(filter):      
    filteredText = []
    for line in poemList:
        line = line.strip().split(' ')
        words = []
        for i, word in enumerate(line):
            if line == ['']:                #checking for a stanza break
                break
            if word[0].isalpha():           #in the case of Dover beach, my code reads the word '--'; these two lines address the issue
                key = word[0]
            punctuationNote = 'undefined'       #this establishes a system to still analyze words that are followed by a punctuation mark like 'to-night,'
            if not word[-1].isalpha():
                punctuationNote = word[-1]
                word = word[:-1]
            if word in dict[key]:               #if the word is an adjective, it is marked by capitalization
                if 'A' in dict[key][word]:
                    word = word.upper()
            elif key.lower() + word[1:] in dict[key.lower()]:           #this allows words with a capitalized first letter to be double-checked. Most of these words are at the beginning of new sentences.
                if 'A' in dict[key.lower()][key.lower() + word[1:]]:
                    word = word.upper()
            if punctuationNote == 'undefined':                      #adds words without punctuation marks
                words.append(word)
            else:
                words.append(word + punctuationNote)                    #adds words with punctuation marks   
        filteredText.append(words)                          #after the analysis, the entire line is appended to the FilteredText list
    printPoem(filteredText)                         #sends filteredText to the printing function
    
def adverbSearch(filter):      
    filteredText = []
    for line in poemList:
        line = line.strip().split(' ')
        words = []
        for i, word in enumerate(line):
            if line == ['']:                #checking for a stanza break
                break
            if word[0].isalpha():           #in the case of Dover beach, my code reads the word '--'; these two lines address the issue
                key = word[0]
            punctuationNote = 'undefined'       #this establishes a system to still analyze words that are followed by a punctuation mark like 'to-night,'
            if not word[-1].isalpha():
                punctuationNote = word[-1]
                word = word[:-1]
            if word in dict[key]:               #if the word is an adverb, it is marked by capitalization
                if 'v' in dict[key][word]:
                    word = word.upper()
            elif key.lower() + word[1:] in dict[key.lower()]:           #this allows words with a capitalized first letter to be double-checked. Most of these words are at the beginning of new sentences.
                if 'v' in dict[key.lower()][key.lower() + word[1:]]:
                    word = word.upper()
            if punctuationNote == 'undefined':                      #adds words without punctuation marks
                words.append(word)
            else:
                words.append(word + punctuationNote)                    #adds words with punctuation marks   
        filteredText.append(words)                          #after the analysis, the entire line is appended to the FilteredText list
    printPoem(filteredText)                         #sends filteredText to the printing function     
                    
def conjunctionSearch(filter):      
    filteredText = []
    for line in poemList:
        line = line.strip().split(' ')
        words = []
        for i, word in enumerate(line):
            if line == ['']:                #checking for a stanza break
                break
            if word[0].isalpha():           #in the case of Dover beach, my code reads the word '--'; these two lines address the issue
                key = word[0]
            punctuationNote = 'undefined'       #this establishes a system to still analyze words that are followed by a punctuation mark like 'to-night,'
            if not word[-1].isalpha():
                punctuationNote = word[-1]
                word = word[:-1]
            if word in dict[key]:               #if the word is a conjunction, it is marked by capitalization
                if 'C' in dict[key][word]:
                    word = word.upper()
            elif key.lower() + word[1:] in dict[key.lower()]:           #this allows words with a capitalized first letter to be double-checked. Most of these words are at the beginning of new sentences.
                if 'C' in dict[key.lower()][key.lower() + word[1:]]:
                    word = word.upper()
            if punctuationNote == 'undefined':                      #adds words without punctuation marks
                words.append(word)
            else:
                words.append(word + punctuationNote)                    #adds words with punctuation marks   
        filteredText.append(words)                          #after the analysis, the entire line is appended to the FilteredText list
    printPoem(filteredText)                         #sends filteredText to the printing function     
    
def interjectionSearch(filter):      
    filteredText = []
    for line in poemList:
        line = line.strip().split(' ')
        words = []
        for i, word in enumerate(line):
            if line == ['']:                #checking for a stanza break
                break
            if word[0].isalpha():           #in the case of Dover beach, my code reads the word '--'; these two lines address the issue
                key = word[0]
            punctuationNote = 'undefined'       #this establishes a system to still analyze words that are followed by a punctuation mark like 'to-night,'
            if not word[-1].isalpha():
                punctuationNote = word[-1]
                word = word[:-1]
            if word in dict[key]:               #if the word is an interjection, it is marked by capitalization
                if '!' in dict[key][word]:
                    word = word.upper()
            elif key.lower() + word[1:] in dict[key.lower()]:           #this allows words with a capitalized first letter to be double-checked. Most of these words are at the beginning of new sentences.
                if '!' in dict[key.lower()][key.lower() + word[1:]]:
                    word = word.upper()
            if punctuationNote == 'undefined':                      #adds words without punctuation marks
                words.append(word)
            else:
                words.append(word + punctuationNote)                    #adds words with punctuation marks   
        filteredText.append(words)                          #after the analysis, the entire line is appended to the FilteredText list
    printPoem(filteredText)                         #sends filteredText to the printing function     
    
def prepositionSearch(filter):      
    filteredText = []
    for line in poemList:
        line = line.strip().split(' ')
        words = []
        for i, word in enumerate(line):
            if line == ['']:                #checking for a stanza break
                break
            if word[0].isalpha():           #in the case of Dover beach, my code reads the word '--'; these two lines address the issue
                key = word[0]
            punctuationNote = 'undefined'       #this establishes a system to still analyze words that are followed by a punctuation mark like 'to-night,'
            if not word[-1].isalpha():
                punctuationNote = word[-1]
                word = word[:-1]
            if word in dict[key]:               #if the word is a preposition, it is marked by capitalization
                if 'P' in dict[key][word]:
                    word = word.upper()
            elif key.lower() + word[1:] in dict[key.lower()]:           #this allows words with a capitalized first letter to be double-checked. Most of these words are at the beginning of new sentences.
                if 'P' in dict[key.lower()][key.lower() + word[1:]]:
                    word = word.upper()
            if punctuationNote == 'undefined':                      #adds words without punctuation marks
                words.append(word)
            else:
                words.append(word + punctuationNote)                    #adds words with punctuation marks   
        filteredText.append(words)                          #after the analysis, the entire line is appended to the FilteredText list
    printPoem(filteredText)                         #sends filteredText to the printing function             
      
def printPoem(filteredText):   
    "prints final poem"
    for line in filteredText:
        print " ".join(line)       
        
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
    print ("Stanzas: " + str(stanzaCount), "Lines: " + str(lineCount), "Words: " + str(wordCount))          
        
def identifyWords(dict):      
    print "***********************************" 


#     filteredText = [] 
#     for line in poemList:
#         print line
#         line = line.strip().split(" ")
#         words = ""
#         for i, word in enumerate(line):
#             if word.isalpha():
#                 if word == "stand,":
#                     print "something is wrong"
#                 print "yay"
#                 lowerWord = word.lower()
#                 print lowerWord
#                 wordState = ""
#                 words += " "
#                 key = lowerWord[0]
#                 print key
#                 
#                 if 'noun' in dict[key][lowerWord]:
#                     wordState = word.upper()
#                 if 'verb' in dict[key][lowerWord]:
#                     previous = ''
#                     for ch in line[i - 1]:
#                         if ch.isalpha():
#                             previous += ch
#                     print previous
#                     if 'pronoun' in dict[previous[0]][previous] or 'noun' in dict[previous[0]][previous]:
#                         wordState = word.lower()      
#                 if wordState != "":
#                     words += wordState
#                 else:
#                     words += word 
#         filteredText += words        
#     printPoem(filteredText)        

if __name__ == '__main__':
    global poemList
    poemList = fileToStringList("Dover Beach")
    global dict
    filename = "mobypos.txt"
    dictList = fileToStringList(filename)
    dict = buildDict(dictList)
    chooseFilter()
    identifyWords(dict)
    
    