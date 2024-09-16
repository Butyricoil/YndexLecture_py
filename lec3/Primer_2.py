
'''переьерем число А за О(N)
переберем число В за О(N)
 если их сумма рвана Х то верни эту паруя'''
def towtermswithsumx(nums, x ):
    for a in nums:
        for b in nums:
            if a + b == x:
                return a, b
    return 0, 0


x = (1, 2, 3, 4)
y = 2
print(towtermswithsumx(x, y))



