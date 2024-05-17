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
    
# Проверка распарсенных данных
Functions.convertMs(timestamp)
Functions.convertIDLE(idle)
i = 1
while i < 20:
    print(f'Time:{timestamp[-i]}')
    i += 1
i = 1
while i < 20:
    print(f'Idle:{idle[-i]}')
    i += 1    
print(f'Строк {count}')
print(uptime_file.read())

# Пример графика
uptime_file.close()
plt.figure(figsize=(20,20))#создаю график
plt.grid(True)
plt.plot(timestamp, idle)
#plt.axis([0,20,0,20])
plt.ylabel('idle')
plt.xlabel('timestamp')
plt.show()

