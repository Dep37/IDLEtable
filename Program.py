import csv
from subprocess import Popen
p = Popen("BinReader.bat", cwd=r"IDLEtable")
stdout, stderr = p.communicate()

timestamp = []
idle = []
with open("IDLEtable\\perfmon.csv", encoding='ANSI') as r_file:
    file_reader = csv.reader(r_file, delimiter = "	")
    count = 0
    for row in file_reader:
            if count == 0:
                  print(f'Столбцы: {" ".join(row)}')
            else:
                  timestamp.append(row[0])
                  idle.append(row[1])
            count +=1
    timestamp.reverse()
    idle.reverse()
    print(timestamp[-1])
    print(idle[-1])
    print(f'Строк {count}')
