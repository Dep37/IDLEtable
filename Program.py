import csv
import matplotlib.pyplot as plt
from subprocess import Popen
p = Popen("BinReader.bat") #выполняю скрипт, который вытаскивает файлики
stdout, stderr = p.communicate()

timestamp = [] #объявляю списки, в которые занашу данные. Название списка = название столбца
idle = []
loadAv = []
ram = []
nvram = []
lan1 = []
lan12 = []
lan2 = []
lan22 = []

uptime_file = open('uptime.txt', 'r') #открываю файл с данными по загрузке процессора

with open("perfmon.csv", encoding='ANSI') as r_file: #открываю и паршу таблицу с данными IDLE и другими
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
    #timestamp.reverse()
    #idle.reverse()
    #loadAv.reverse()
    #ram.reverse()
    #nvram.reverse()
    #lan1.reverse()
    #lan12.reverse()
    #lan2.reverse()
    #lan22.reverse()
    def convertMs(millis): #конвертирую мс в нормальное время
      i = 0
      while i < len(millis):
            mseconds=int(millis[-i])%1000
            seconds=int(int(millis[-i])/1000)%60
            minutes=int(int(millis[-i])/(1000*60))%60
            hours=int(int(millis[-i])/(1000*60*60))%24
            millis[-i] = "{}:{}:{}.{}".format(hours, minutes, seconds, mseconds)
            i += 1
      print(millis[-1])
      return millis
convertMs(timestamp)
i = 1
while i < 20: #Это просто печать нескольких значений для проверки, потом можно удалить
      print(f'Time:{timestamp[-i]}')
      i += 1
i = 1
while i < 20:
      print(f'Idle:{idle[-i]}')
      i += 1    
print(f'Строк {count}')
print(uptime_file.read())

uptime_file.close()
plt.figure(figsize=(20,20))#создаю график
plt.grid(True)
plt.plot(timestamp, idle)
#plt.axis([0,20,0,20])
plt.ylabel('idle')
plt.xlabel('timestamp')
plt.show()

