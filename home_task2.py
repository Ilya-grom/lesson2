#2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

spisok = [1, 'gogi', [3,14], 'Pi', 'Hi', 24.02]
print(spisok)
spisok[0], spisok[-1], spisok[1], spisok[2],spisok[-2], spisok[3] =\
    spisok[-1], spisok[0], spisok[3], spisok[1], spisok[2], spisok[-2]
print(spisok)