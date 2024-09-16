# ЗАДАЧА: Дана строка (в кодировке UTF-8)
# найти смый часто встречающийся в ней символ.
# Если несколько символов встречаются одинакого часто, томожно вывести любой

s = input()
ans = ''
anscnt = 0
for i in range (len(s)):
    nowcnt = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            nowcnt += 1
        if nowcnt > anscnt:
            ans = s[i]
            anscnt = nowcnt
print(ans)

# сложность алгоритма O(N^2)
# время  O(N^2)
# память  O(N)