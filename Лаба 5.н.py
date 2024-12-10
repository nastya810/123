#зад 1
# Ввод количества элементов списка
n = int(input("Введите количество элементов списка -> "))
x = []

# Ввод элементов списка
for i in range(n):
    x.append(int(input(f"Введите элемент {i} -> ")))

# Создаем словарь для хранения индексов элементов
element_indices = {}

for index, value in enumerate(x):
    if value in element_indices:
        element_indices[value].append(index)
    else:
        element_indices[value] = [index]

# Выводим повторяющиеся элементы и их индексы
duplicates_found = False
for element, indices in element_indices.items():
    if len(indices) > 1:
        duplicates_found = True
        print(f"Элемент '{element}' найден на индексах: {indices}")

if not duplicates_found:
    print("Повторяющихся элементов нет.")
#зад 2
    # Ввод количества элементов списка
    n = int(input("Введите количество элементов списка -> "))
    x = []

    # Ввод элементов списка
    for i in range(n):
        x.append(float(input(f"Введите элемент {i} -> ")))

    # Проверяем, достаточно ли элементов в списке
    if n < 2:
        print("Недостаточно элементов в списке для выполнения операции.")
    else:
        # Значение второго с конца элемента
        decrement_value = x[-2]

        # Уменьшаем элементы на четных позициях
        for i in range(0, n, 2):  # четные позиции: 0, 2, 4, ...
            x[i] -= decrement_value

        # Выводим преобразованный список
        print("Преобразованный список:", x)