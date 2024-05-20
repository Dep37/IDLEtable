
import datetime
# Функция конвертирования timestamp в DataTime
def convertMs(millis):
    i = 0
    while i < len(millis):
        base_datetime = datetime.datetime(1970, 1, 1)
        delta = datetime.timedelta(milliseconds=float(millis[-i])*1000)
        dt = base_datetime + delta
        millis[-i] = "{}".format(dt)
        i += 1
    print(millis[-1])
    return millis
# Функция конвертирования IDLE в формат int
def convertIDLE(idle):
    i = 0
    while i < len(idle):
        idle[-i] = "{}".format(int(float(idle[-i])))
        i += 1
    print(idle[-1])
    return idle

# Функция поиска ближайшего значения
def nearestIndex(list, target):
    result = min(list, key = lambda x: abs(x - target)) if list else None
    return list.index(result)