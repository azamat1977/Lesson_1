print ('"Общество в начале XXI века"')
x=int(input('Enter your age: '))
if x in range (0,6):
    print ('"Вам в детский сад"')
elif x in range(7,17):
    print('"Вам в школу"')
elif x in range(18,24):
    print('"Вам в профессиональное учебное заведение"')
elif x in range(25,59):
    print('"Вам на работу"')
elif x in range(60, 120):
    print('"Вам предоставляется выбор"')
elif x < 0:
    print('"Ошибка! Это программа для людей!"' * 5)
elif x > 120:
    print('"Ошибка! Это программа для людей!"' * 5)