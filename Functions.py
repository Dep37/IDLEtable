# Функция конвертирования timestamp в DataTime
def convertMs(millis):
    i = 0
    while i < len(millis):
        mseconds = int(millis[-i]) % 1000
        seconds = int(int(millis[-i]) / 1000) % 60
        minutes = int(int(millis[-i]) / (1000 * 60)) % 60
        hours = int(int(millis[-i]) / (1000 * 60 * 60)) % 24
        millis[-i] = "{}:{}:{}.{}".format(hours, minutes, seconds, mseconds)
        i += 1
    print(millis[-1])
    return millis