import string

def is_pangram(s):
    removeSpecialCharacters = [character for character in s if character.isalpha()]
    
    cleanSentenceWithLowerCase = ("".join(removeSpecialCharacters)).lower()
    
    convertToSet = set(list(cleanSentenceWithLowerCase))
    
    allAlphabetSet = set(list(string.ascii_lowercase))
    
    if(allAlphabetSet == convertToSet):
        return True
    else:
        return False