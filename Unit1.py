x=int(input('Enter digit from 1 to 9: '))
s=int(input('Please enter digit: '))
m=int(input('Please give erect a number: '))
if x in range (1,3):
    print (s, x*s, s*x)
elif x in range (4,6):
    print (x*m)
elif x in range (7,9):
    print (x*1*10)
else:
    pgitgit rint('"Login Error"')