# Ввод строки от пользователя
input_string = input("Введите строку: ")

# Разделяем строку на слова
words = input_string.split()

# Создаем список для хранения результатов
result = []

# Проходим по каждому слову в списке
for word in words:
    # Проверяем, начинается ли слово на 'а' или заканчивается на 'я'
    if word.lower().startswith('а') and word.lower().endswith('я'):
        result.append(word)

# Выводим найденные слова
print("Найденные слова:", result)