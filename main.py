
# 6.22 (г) Дано натуральное число. Определить сумму его цифр > 5

number = int(input('Input number: '))

summ = 0
while number > 0:
    num = number % 10
    if num > 5:
        summ = summ + num
    number = number // 10
print('summa =', summ)


# 6.22 (д) Дано натуральное число. Определить произведение его цифр > 7

number = int(input('Input number: '))

mult = 1
while number > 0:
    num = number % 10
    if num > 7:
         mult = mult * num
    number = number // 10
print('Multiply =', mult)


# 6.23 (а) Дано натуральное число. Определить сколько раз в нем
#          встречается цифра "а"

number = int(input('Input number: '))
a = int(input('Input number a: '))

countNumber = 0
while number > 0:
    num = number % 10
    if num == a:
        countNumber = countNumber + 1
    number = number // 10
print('Result =', countNumber)


# 6.23 (в) Дано натуральное число. Определить сумму его цифр > "a"
#          (значение "а" вводится с клавиатуры)

number = int(input('Input number: '))
a = int(input('Input number a: '))

summ = 0
while number > 0:
    num = number % 10
    if num > a:
        summ = summ + num
    number = number // 10
print('Summa =', summ)


# 6.27 (б) Дано натуральноле число. Определить на сколько его
#          максимальная цифра превышает минимальную.

number = int(input('Input number: '))

maxNumber = 0
minNumber = number % 10

while number > 0:
    num = number % 10
    if num > maxNumber:
        maxNumber = num
    if num < minNumber:
        minNumber = num
    number = number // 10

result = maxNumber - minNumber
print('Разница =', result)


# 6.8 Вводите "n" c клавиатуры пока не будет > 20
#     1, 2, 3, 4, 5
#     1*1, 2*2  ...

mult = 1
while mult < 20:
    n = int(input('Input number: '))
    mult = n * n
print('result', mult)
