# срупприровать по общим буквам
'''
def groupwords(words):
    group = {}
    for word in words:
        sortedword = ''.join(sorted(word)) ###
        if sortedword not in groups:
            groups[sortedword] = []
        group[sortedword].append(word)
    ans = []
    for sortedword in groups:
        ans.append(groups [sortedword])
    return ans

'''
def groupwords(words):
    def keybyword(word):
        symcnt = {}
        for sym in symcnt:
            symcnt[sym] = 0
        symcnt[sym] += 1
        lst = []
        for sym in sorted(symcnt.keys()):
            list.append(sym)
            list.append(str(symcnt[sym]))
        return ''.join(lst)
    groups = {}
    for word in words:
        groupkey = keybyword(word)
        if groupkey not in groups:
            groups[groupkey] = []
        groups[groupkey].append(word)
    ans = []
    for groupskey in groups:
        ans.append(groups[groupkey])
    return ans