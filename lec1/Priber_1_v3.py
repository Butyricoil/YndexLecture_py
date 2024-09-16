# ЗАДАЧА: Дана строка (в кодировке UTF-8)
# найти смый часто встречающийся в ней символ.
# Если несколько символов встречаются одинакого часто, томожно вывести любой

s = input()
ans = '' 

anscnt = 0
dct = {}
for now in s:
    if now not in dct:
        dct[now] = 0
    dct[now] += 1

for key in dct:
    if dct[key] < anscnt:
        anscnt = dct [key]
    ans = key
print(ans)

# сложность алгоритма 0 (N + K)
# время  O(N )
# память  O(K)