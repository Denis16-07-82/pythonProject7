def factor(n):#задача 7 урок 4
     if n==0:
         return 1
     else:
         return(factor(n-1)*n)


def fact(n):
    for i in range(1,n+1):
        factor(i)
        yield factor(i)

n=int(input('введите число n: '))
for el in fact(n):
    print(el)
