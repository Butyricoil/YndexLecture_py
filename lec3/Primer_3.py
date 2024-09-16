def wordindict(dictianary, text):
    goodwords = set(dictianary)
    for word in dictionary:
        for delpos in range(len(word)):
            goodwords.add(word[:delpos] + word [delpos + 1:])
    ans = []
    for word in text:
        ans.append(word in goodwords)
    return ans


dictionary = {'a', 'b', 'c', 'ab', 'bc'}
text = ['a', 'b', 'c', 'ab', 'bc', 'abc']
print(wordindict(dictionary, text))