from _functools  import reduce#задача 5 урок 4
my_list=[i for i in range(100,1001) if i%2==0]
my_mult=reduce(lambda a,b:a*b,my_list)
print(my_list)
print(my_mult)