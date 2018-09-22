'''
Created on Aug 4, 2017

@author: joelmire
'''

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

def buildDict(dictList):
    dict = {}
    for item in dictList:
        key = item[0]
        if key not in dict:
            letterDict = {}
            dict[key] = letterDict
        item = item.split("\\")
        if item[0] not in dict:
            dict[key][item[0]] = item[1]
        else:
            pass   
    return dict    
        
        
        
    
    
    
if __name__ == '__main__':
    filename = "mobypos.txt"
    dictList = fileToStringList(filename)
    print buildDict(dictList)
    