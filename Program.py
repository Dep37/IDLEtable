import csv
import matplotlib.pyplot as plt
from subprocess import Popen
import Functions


# Запуск скрипта распаковки архива
stdout, stderr = Popen("BinReader.bat").communicate()

# Открытие данных по загрузке процессора
uptime_file = open('uptime.txt', 'r')

# Парсинг данных работы контроллера
timestamp = []
idle = []
loadAv = []
ram = []
nvram = []
lan1 = []
lan12 = []
lan2 = []
lan22 = []

with open("perfmon.csv", encoding='ANSI') as r_file:
    file_reader = csv.reader(r_file, delimiter = "	")
    count = 0
    for row in file_reader:
        if count == 0:
            print(f'Столбцы: {" ".join(row)}')
        else:
            timestamp.append(row[0])
            idle.append(row[1])
            loadAv.append(row[2])
            ram.append(row[3])
            nvram.append(row[4])
            lan1.append(row[5])
            lan12.append(row[6])
            lan2.append(row[7])
            lan22.append(row[8])
        count +=1
    # timestamp.reverse()
    # idle.reverse()
    # loadAv.reverse()
    # ram.reverse()
    # nvram.reverse()
    # lan1.reverse()
    # lan12.reverse()
    # lan2.reverse()
    # lan22.reverse()

# Массивы значений
timestampDt = Functions.convertToDt(timestamp.copy())
Functions.convertIDLE(idle)

print(f"Тип данных IDLE: {type(idle[0])}")
# Функция 'convertIDLE' не конвертирует в 'int', остаётся всё 'str'



listIdle = list(map(int, idle))
# listIdle = idle
listTimestamp = list(map(int, timestamp))


   
# Проверка распарсенных данных
chekParseData = False
if chekParseData:
    chekNumData = 20
    print(f"Проверка распарсенных данных по первым {chekNumData} значениям")
    
    i = 1
    while i < chekNumData:
        print(f'Time:{timestampDt[-i]}')
        i += 1
    i = 1
    while i < chekNumData:
        print(f'Idle:{idle[-i]}')
        i += 1    
    print(f'Строк {count}')
    print(uptime_file.read())
else: print("Проверка распарсенных данных отключена")

# Пример графика
# uptime_file.close()
# plt.figure(figsize=(20,20))#создаю график
# plt.grid(True)
# plt.plot(timestampDT, idle)
# #plt.axis([0,20,0,20])
# plt.ylabel('idle')
# plt.xlabel('timestampDT')
# plt.show()

# Проверка поиска ближайшего значения
indexTimestamp = Functions.nearestIndex(listTimestamp, 1705990270)
print(f"Индекс ближайшего значения Timstamp: {indexTimestamp}")
print(f"Значение Timestamp по найденому индексу: {listTimestamp[indexTimestamp]}")
print(f"Значение IDLE по найденому индексу: {listIdle[indexTimestamp]}")
