'''
Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
'''
def task2 ():
  useNumber = input('Enter your three-digit number, please: ')
  lenghtNumber = int(len(useNumber))
  if lenghtNumber != 3:
    print(f'Error! The number {useNumber} not correspond to the bit depth!') 
  else:
    sum = 0
    for i in range(len(useNumber)):
      sum += int(useNumber[i])
    print(f'{useNumber} # -> {sum} ({useNumber[0]} + {useNumber[1]} + {useNumber[2]})') 
  
'''
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
*Пример:*
6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
'''
def task4 ():
  useNumber = int(input('Enter the number of cranes, please: '))
  man = useNumber//6
  girl = man*2
  if useNumber % 6 != 0:
    man += float(round((useNumber / 6), 2))
    girl = man*2
  print(f'{useNumber} # -> {man} - Петр; {girl} - Екатерина; {man} - Сергей') 
  
'''
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались
за проезд и получали билет с номером. Счастливым билетом называют такой билет
с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
'''
def task6 ():
  useNumber = input('Enter your ticket number, please: ')
  lenghtNumber = int(len(useNumber))                             # число с разрядностью от 3 цифр подлежит проверке
  if lenghtNumber < 3:
    print(f'Error! There are not enough numbers in your ticket "{useNumber}"!') 
  else:
    sum = 0
    check = 3
    
    for i in range(len(useNumber[:check])):
      sum += int(useNumber[i]) - int(useNumber[-check+i])
      print (f'sum = {sum}')
      if sum != 0:
        message = 'No'
      else:
        message = 'Yes'
    print(f'{useNumber} -> {message}') 
  
'''
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками
(то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
'''
def task8 ():
  rowChocolate      = int(input('Enter rows of Chocolate, please: '))
  columnChocolater  = int(input('Enter column of Chocolate, please: '))
  faulChocolater    = int(input('Enter size faul of Chocolate, please: '))
  if ((faulChocolater % rowChocolate == 0 or faulChocolater % columnChocolater == 0) and
              rowChocolate*columnChocolater > faulChocolater):
    message = 'YES'
  else:
    message = 'No'
    
  print(f'{rowChocolate} {columnChocolater} {faulChocolater} -> {message})') 
  
  
task2 ()
task4 ()
task6 ()
task8 ()