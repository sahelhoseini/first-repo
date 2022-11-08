
num1, num2, num3, num4, num5 =input('inter 5 number whit space finaly press inter').split()
result=(num1,num2,num3,num4,num5)

string=input('inter your string')
if string=='tuple':
    print(tuple(result))
elif string=='list':
    print(list(result))
else:
    print('nothing to show')
   