from main import new_words
from main import search

# TEST NONE INPUTS
print(new_words(None, ('a','b','c')) == None)
print(new_words(('a','b','c'), None) == None)

# TEST NON TUPLE INPUTS
print(new_words('abc', 123) == None)
print(new_words(('a','b','c'), 1221) == None)
print(new_words([1,2,1,3], ('a','b','c')) == None)

# TEST EMPTY TUPLE INPUTS
print(new_words((),('a','a','a')) == ())
print(new_words(('a','a','a'), ()) == ('a','a','a'))

# TEST VALID INPUTS
print(new_words(('a',),('a',)) == ()) # might be wrong, maybe should equate to None
print(new_words(('a','b'),('a',)) == ('b',))
print(new_words(('a','b'),('a',)) == ('b',))
print(new_words(('a','b','c'),('a',)) == ('b','c'))

# TEST CASE INSENSITIVE
print(new_words(('aBC','123'),('Abc',)) == ('123',))
print(new_words(('aBC','123','456','a1b2c3','b2c3d4'),('456','Abc','B2C3D4')) == ('123', 'a1b2c3'))

# TEST SEARCH METHOD
print(search('1',('1','2','3','4','5','6','7','8','9')) == True)
print(search('2',('1','2','3','4','5','6','7','8','9')) == True)
print(search('3',('1','2','3','4','5','6','7','8','9')) == True)
print(search('4',('1','2','3','4','5','6','7','8','9')) == True)
print(search('5',('1','2','3','4','5','6','7','8','9')) == True)
print(search('6',('1','2','3','4','5','6','7','8','9')) == True)
print(search('7',('1','2','3','4','5','6','7','8','9')) == True)
print(search('8',('1','2','3','4','5','6','7','8','9')) == True)
print(search('9',('1','2','3','4','5','6','7','8','9')) == True)
print(search('0',('1','2','3','4','5','6','7','8','9')) == False)
print(search('a',('1','2','3','4','5','6','7','8','9','a','b','c','D')) == True)
print(search('b',('1','2','3','4','5','6','7','8','9','a','b','c','D')) == True)
print(search('c',('1','2','3','4','5','6','7','8','9','a','b','c','D')) == True)
print(search('d',('1','2','3','4','5','6','7','8','9','a','b','c','D')) == True)
print(search('f',('1','2','3','4','5','6','7','8','9','a','b','c','D')) == False)

