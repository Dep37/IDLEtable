import datetime
import time

# Функция конвертирования Timestamp в DataTime
def convertToDt(millis):
    i = 0
    while i < len(millis):
        base_datetime = datetime.datetime(1970, 1, 1)
        delta = datetime.timedelta(milliseconds=int(float(millis[-i]))*1000)
        dt = base_datetime + delta
        millis[-i] = dt
        i += 1
    return millis
# Функция конвертирования Timestamp в DataTime для одиночного значения
def convertToDt1(millis):
    base_datetime = datetime.datetime(1970, 1, 1)
    delta = datetime.timedelta(milliseconds=int(float(millis))*1000)
    dt = base_datetime + delta
    millis = dt
    return millis
# Функция конвертирования DataTime в Timstamp, формат (2024-01-30 04:45:50)
def convertToTimestamp(dt):
    try:
        datetime.datetime.fromisoformat(dt)
        timestamp = int(time.mktime(datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M:%S").timetuple()))
    except ValueError:
        raise ValueError("Не правильный формат даты, введите дату в формате: %Y-%m-%d %H:%M:%S")
    return timestamp

# Функция конвертирования IDLE в формат int
def convertIDLE(idle):
    i = 0
    while i < len(idle):
        idle[-i] = int(float(idle[-i]))
        i += 1
    print(idle[-1])
    return idle

# Функция поиска ближайшего значения
def nearestIndex(list, target):
    result = min(list, key = lambda x: abs(x - target)) if list else None
    return list.index(result)