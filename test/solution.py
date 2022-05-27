arraychik = open('input.txt', 'r') 
file = open('output.txt', 'w+') 
j = arraychik.readline() 
j = j.split() # разбиваем файл с входными данными на массив из двух чисел
n = j[0]
k = j[1]
# присваиваем значени чисел в массиве переменным
if int(n) > 10**9 or int(k) > int(n):
    print ("напишите другие входные числа")
# создаём ограничения по условию
file.write(str(sorted(str(i) for i in range(1,int(n)+1)).index(k)+1))
# index(k)+1 показывает место искомого k
# (k)+1, т. к. Python считает с нуля
# str(i) for i in range(1,int(n)+1) создаёт список чисел от 1 до n включительно
# sorted сортирует список чисел в лексикографическом порядке
file.close()
