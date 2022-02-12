
number1 = input('Введите первое число:')
number2 = input('Введите второе число:')

summary = number1 + number2

print(summary)

number3 = int(input('Введите третье число:'))

if number3 > 10:
     print('Ваше число больше 10')
else:
     print('Ваше число меньше 10')
     number4 = 0

     while number4 < 10:
         number5 = number4 + number3
         print(number4)
         number4 += 1
         if number4 == 10:
             print('Ваше число равно 10')



