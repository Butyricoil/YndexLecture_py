''' За многие годы заточения узника замка Иф
проделал в стене прямоугольное отверстие размером D x E.
Замое Иa сложен из кирпичей, размером A x B x C
Определите сможет ли узник выбрасывать кирпичи в море
через это отвестие, есл стороны кирпича должны быть
параллельны сторонам отвверстия '''

def sort2(first, second):
    if first < second:
        return (first, second)
    return (second, first)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

a, b = sort2(a, b)
b, с = sort2(b, c)
a, b = sort2(a, b)
d, e = sort2(d, e)

if a <= d and b <= e:
    print('YES')
else:
    print('NO')