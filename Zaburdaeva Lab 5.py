import re
import csv


# Задание 1

with open('task1-ru.txt', 'r', encoding='utf-8') as file:
    text = file.read()

result_word = re.findall(r'\b[а-яА-яёЁa-zA-Z]{3,5}\b', text)
result_num = re.findall(r'\b\d{4,}\b', text)

print("Слова от 3 до 5 букв:", result_word)
print("Числа большие трёх знаков:", result_num)


# Задание 2

with open('task2.html', 'r', encoding='utf-8') as file:
    website = file.read()

tags = re.findall(r'<([a-zA-Z][a-zA-Z0-9]*)\b', website)

uniq = set(tags)

print("Все открывающиеся теги без повторений:", uniq)


# Задание 3

with open('task3.txt', 'r', encoding='utf-8') as file:
    table = file.read()

surnames = re.findall(r'[A-Z][a-z]+(?!\d\d@|@)', table)  
table = re.sub(r'[A-Z][a-z]+(?!\d\d@|@)', ' ', table)
emails = re.findall(r'[a-z][a-z0-9-]*@[a-z0-9-]+\.[a-z]{2,}', table)
dates = re.findall(r'\d{4}-\d{2}-\d{2}', table)
addresses = re.findall(r'https?://[a-zA-Z0-9.-]+/', table)
table = re.sub(r'https?://[a-zA-Z0-9.-]+/', ' ', table)

ids = []
id = 1
while True:
    if str(id) in table:
        ids.append(id)
        id += 1
    else:
        break

new_table = []
num_entries = min(len(ids), len(surnames), len(emails), len(dates), len(addresses))

for i in range(num_entries):
    new_table.append([ids[i], surnames[i], emails[i], dates[i], addresses[i]])

with open('new.csv', 'w', newline='', encoding='utf-8') as csvfile:
    table_2 = csv.writer(csvfile)
    table_2.writerow(['ID', 'Фамилия', 'Email', 'Дата регистрации', 'Сайт'])
    table_2.writerows(new_table)

print("Данные сохранены в файл new.csv :)")


# Дополнительное задание

with open('task_add.txt', 'r', encoding='utf-8') as file:
    symbols = file.read()

dates = re.findall (r'\b(?:(?:\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4})|(?:\d{4}[-/.]\d{1,2}[-/.]\d{1,2})|(?:\d{1,2}\s+[a-zA-Z]{3,9}\s+\d{2,4})|(?:[a-zA-Z]{3,9}\s+\d{1,2},\s+\d{4})\b)', symbols)
emails = re.findall(r'\s([\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,})',symbols)
adresses = re.findall(r'\s(https?://[a-zA-Z0-9.-]+)',symbols)

fragments = []

for date in dates[:5]:
    fragments.append(['Дата',date])
for email in emails[:5]:
    fragments.append(['Email',email])
for adress in adresses[:5]:
    fragments.append(['Сайт',adress])



for name, item in fragments:
    print(f'{name}: {item}')

