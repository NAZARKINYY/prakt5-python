arr = [2, 5, 4, 3, 6, 8, 9, 7]
even_on_odd_pos = 0  # количество четных элементов на нечетных позициях
odd_on_even_pos = 0  # количество нечетных элементов на четных позициях
for i in range(len(arr)):
    if i % 2 != 0:  # нечетная позиция
        if arr[i] % 2 == 0:  # четный элемент
            even_on_odd_pos += 1
        else:  # нечетный элемент
            pass  # можно не обрабатывать этот случай
    else:  # четная позиция
        if arr[i] % 2 != 0:  # нечетный элемент
            odd_on_even_pos += 1
        else:  # четный элемент
            pass  # можно не обрабатывать этот случай
print("Количество четных элементов на нечетных позициях:", even_on_odd_pos)
print("Количество нечетных элементов на четных позициях:", odd_on_even_pos)
