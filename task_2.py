import datetime

time = int(input('Введите время (c):'))
secunda = 0
minuta = 0
chas = 0

while time > 0:
    secunda += 1
    if secunda > 59:
        minuta += 1
        secunda = 0
    if minuta > 59:
        chas += 1
        minuta = 0
    time -= 1
print(chas, minuta, secunda)

answer = datetime.datetime(1, 1, 1, hour=chas, minute=minuta, second=secunda)
print("Время в чч:мм:сс", answer.strftime("%X"))

# minutes = math.floor(time/60)
# print('минут', minutes)
# hours = math.floor(time/3600)
# print('часов', hours)