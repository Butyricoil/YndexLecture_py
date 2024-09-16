'''Дана последовательность чисел, длиной N

 найти первое левое вхождение положительного числа X в нее
 или вывезти -1, если числo X не встречалось. '''

def findex(seq, x):
    ans = -1
    for i in range(len(seq)):
        if ans == -1 and seq[i] == x:
            ans = i
    return ans

a = input()
b = input()
print(findex(a, b))



