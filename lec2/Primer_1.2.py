'''Дана последовательность чисел, длиной N

 найти первое правое вхождение положительного числа X в нее
 или вывезти -1, если числo X не встречалось. '''

def findex(seq, x):
    ans = -1
    for i in range(len(seq)):
        if seq[i] == x:
            ans = i
    return ans

a = input()
b = input()
print(findex(a, b))


