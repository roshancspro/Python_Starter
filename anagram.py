def anagrams(word, words):
    """
    Write a function that will find all the 
    anagrams of a word from a list. You will 
    be given two inputs a word and an array 
    with words. You should return an array 
    of all the anagrams or an empty array 
    if there are none.
    """
    anagramWords = []
    anagramseq = {}

    wordLen = len(word)

    for chr in word:
        if(chr in anagramseq):
            count = anagramseq.get(chr)
            anagramseq[chr] = count+1
        else:
            anagramseq[chr] =1

    for str in words:
        
        if(len(str) != wordLen):
            continue
        
        notAnagram = False
        for item in anagramseq:
            
            
            if(str.count(item) != anagramseq.get(item)):
                notAnagram = True
                break
        
        if(notAnagram):
            continue
        
        anagramWords.append(str)

    print(anagramWords)
    return anagramWords

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
anagrams('laser', ['lazing', 'lazy',  'lacer'])




