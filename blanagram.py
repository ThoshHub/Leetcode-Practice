# def checkBlanagrams(word1, word2):
#     count = 0;
    
#     # if words are different length
#     if(len(word1) != len(word2)):
#         return False;
    
#     wordset1 = set(list(word1))
#     wordset2 = set(list(word2))
    
#     diff = wordset1 - wordset2
#     print(wordset1)

#     if len(diff) == 1:
#         return True
#     else :
#         return False

def checkBlanagrams(word1, word2):
    if(len(word1) != len(word2)):
        return False
    
    count = 0
    
    wlist1 = list(word1)
    wlist2 = list(word2)
    wlist1 = wlist1.sort()
    wlist2 = wlist2.sort()

    print(wlist1)
    print(wlist2)
    
    for i in range (0, len(word1)):
        if(word1[i] == word2[i]):
            count += 1
    
    return(count == 1 or count == 2)

a = 'aba'
b = 'bab'
c = 'tangram'
d = 'anagram'

result = checkBlanagrams(c, d) # expect True

print(result)

# can do it by emulating stacks in hashmap
# or just use sort and then loop through it
