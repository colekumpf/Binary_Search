# extract values from a sorted list

# subroutines if any, go here
def search(word, wordlist):
    word = str(word).lower()
    wordlist_middle = str(wordlist[len(wordlist) // 2]).lower()
    while (word != wordlist_middle) and (len(wordlist) > 1):
        if word < wordlist_middle:  # if word  would be in front half of list
            wordlist = wordlist[:len(wordlist) // 2]  # get front half excluding middle
            if (len(wordlist) < 1):  # if list is now empty
                return False  
            wordlist_middle = str(wordlist[len(wordlist) // 2]).lower()
        else:  # word would be in back half of list
            wordlist = wordlist[(len(wordlist) // 2) + 1:]  # get back half excluding middle
            if (len(wordlist) < 1):  # if list is now empty
                return False
            wordlist_middle = str(wordlist[len(wordlist) // 2]).lower()
    if word == wordlist_middle:
        return True
    return False
            

# your subroutine goes here
def new_words(words, wordlist):
    if (words is None) or (wordlist is None) or \
       (not isinstance(words, tuple)) or (not isinstance(wordlist, tuple)):
        return None
    elif words == ():
        return ()
    elif wordlist == ():
        return tuple(words)
    new_list = []
    for word in words:
        if not search(word, wordlist):  # word is not in word list
            new_list.append(word)
    return tuple(new_list)


'''
PSEUDOCODE

validate inputs
for word in words
    search word list by string comparison
    while word is not equal to the middle of wordlist AND
        wordlist has at least one word in it
        if word < middle of wordlist
            slice wordlist in half non inclusive
        else 
            slice wordlist to back half of string
    if word == wordlist of middle
        return true
    return false    
'''
