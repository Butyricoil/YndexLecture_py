''' Игра PitCraft  происходит в двумерном мире которвый состоит из блков
размкром 1 на 1 метр. о Сстров игрока предстовляет собой
 набор столбцов различной высоты, состояших из блоков камня и окруженный морем
Над островом арошел сильный дождь, который заполнил водой все низы,
а не поместившиеся вода в них стекла в море не увеличив его уровень'''

# по ландшафту острова определите, сколько блоков воды осталось после дождя в низах на острове
def isoeflood(h):
    maxpos = 0
    for i in range(len(h)):
        if h[i] > h[maxpos]:
            maxpos = i
    ans = 0
    nowm = 0
    for i in range(maxpos):
        if h[i] > nowm:
            nowm = h[i]
        ans += nowm - h[i]
    nowm = 0
    for i in range((len(h)) - 1, maxpos, -1):
        if h[i] > nowm:
            nowm = h[i]
        ans += nowm - h[i]
    return ans

print(isoeflood(input()))
