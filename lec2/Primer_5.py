'''Дана последовательность чисел длиной N
найти минимальное четное число в последовательности или
вывести-1 , если такого не существует'''

# def findmineven(seq):
#     ans = -1
#     for i in range(len(seq)):
#         if (seq[i] % 2 == 0) and (ans == -1 or seq[i] < ans):
#             ans = seq[i]
#     return ans
#
# x = (1, 3 ,5 ,5,5 ,9)
# print(findmineven(x))

def findmineven(seq):
    ans = -1
    flag = False
    for i in range(len(seq)):
        if (seq[i] % 2 == 0) and (not flag or seq[i] < ans):
            ans = seq[i]
            flag = True
    return ans

x = (1, 3 ,5 ,4,5 ,9)
print(findmineven(x))