'''Интернат, последовательность слов.
Привести самые короткие слова. Через пробел. '''
# def shortwords(words):
#     minlen = len(words[0])
#     for word in words:
#          if len(word)< minlen:
#              minlen = len(words)
#     ans = ''
#     for word in words:
#         if len(word) == minlen:
#             ans += word + ''
#     return ans
def shortwords(words):
    minlen = len(words[0])
    for word in words:
         if len(word)< minlen:
             minlen = len(words)
    ans = []
    for word in words:
        if len(word) == minlen:
            ans.append(word)
    return ' '.join(ans)

print(shortwords(input()))