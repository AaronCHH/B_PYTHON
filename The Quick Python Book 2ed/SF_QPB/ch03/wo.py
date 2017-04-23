"""wo module. Contains function: WordsOccur()"""

# other modules used by this module
import string

# interface functions

def WordsOccur():
    """WordsOccur() - count the occurrences of words in a file."""
    
    # Prompt user for the name of the file to use.
    fileName = raw_input("Enter the name of the file: ")
    
    # Open the file, read it and store its words in a list.
    f = open(fileName, 'r')
    wordList= string.split(f.read())
    f.close()
    
    # Count the number of occurences of each word in the file
    occursDict = {}
    for word in wordList:
        # increment the occurrences count for this word
        occursDict[word] = occursDict.get(word, 0) + 1
    
    # print out the results
    print "File: %s, contains a total of %d words (%d of which are unique)" % \
        ( fileName, len(wordList), len(occursDict) )
    print occursDict

if __name__ == '__main__':
    WordsOccur()