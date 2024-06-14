num=int(input('Enter any number:'))

a=0
b=1

if num<0:
    print('The number is less than zero')
    print(a)

elif num==0:
    print('The number is equal to zero')
    print(a)

elif num==1:
    print('The number is equal to one')
    print(b)

else:
    print('The Fibonacci series are:')

    for x in range(2, num):
        c=a+b
        a=b
        b=c
        print(b)
