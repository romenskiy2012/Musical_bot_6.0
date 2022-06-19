import sqlite3

import time
import random
bd = sqlite3.connect("csv-bd.bd")
sql = bd.cursor()

import csv


sql.execute("CREATE TABLE IF NOT EXISTS fiel (url TEXT, type TEXT, beginning TEXT, end TEXT)")
bd.commit()
    
    
    
with open("sponsorTimes_1619030483069.csv", encoding='utf-8') as r_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ",")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла
    for row in file_reader:
        if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
            print(f'Файл содержит столбцы: {", ".join(row)}')
        else:
            # Вывод строк
            print(f'    {row[0]} {row[10]}     {row[1]} - {row[2]}')
            sql.execute(f"INSERT INTO fiel VALUES ('{row[0]}', '{row[10]}', '{row[1]}', '{row[2]}')")
        count += 1
    print(f'Всего в файле {count} строк.')
bd.commit()

bd.close()









