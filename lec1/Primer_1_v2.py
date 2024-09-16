# ЗАДАЧА: Дана строка (в кодировке UTF-8)
# найти смый часто встречающийся в ней символ.
# Если несколько символов встречаются одинакого часто, томожно вывести любой



s = input()
ans = ''
anscnt = 0
for now in set(s):
    nowcnt = 0
    for j in range(len(s)):
        if now == s[j]:
            nowcnt += 1
        if nowcnt > anscnt:
            ans = s[j]
            anscnt = nowcnt
print(ans)

# сложность алгоритма O(NK)
# время  O(NK)
# память  O(N+K)=O(N)