#name=input("Как Вас зовут? ")
#age=int(input("Сколько Вам лет? "))
#print("Добрый день,", name+"!")
#print("Вы родились в,", 2022-age,"году!")

# #список из чисел
# nums=[1,54,6,3,87,243,23,11]
# #Отображение содержимого списка 
# print("Список чисел",nums)
# #Длина чисел
# print("Длинна чисел", len(nums))
# #первый элемент
# print("first_element", nums[0])
# #Последний элемент
# print("last_element", nums[-1])
# #наибольшее значение
# print("max_nambers", max(nums))
# print("min_meaning", min(nums))
# print("summa", sum(nums))
# #Список в обратно порядке
# print("reversed_list", list(reversed(nums)))
# #Сортировка значений
# print("сортировка значений списка", list(sorted(nums)))
# #исходный список
# print("исходный список", nums)
# #Изменение значений списка, для применения вывод списка
# nums[1]="3333333"
# print("После изменений", nums)
# #Получение среза (4 элемент и последний элемент длины списка)
# print("Получение среза", nums[4: len(nums)-1])
# #Замена части эжлемента
# nums[1:-1]=["A","B"]
# print("После замены",nums)
# #Список от 5 до 10 и вывод результата
# nums=list(range(5,11))
# print("от 5 до 10", nums)
# #удаление двух элементов из списка
# nums[2:4]=[]
# print("Удалили 2 элемента",nums)
# #Удаление последнего элемента
# del nums[len(nums)-1]
# print("Удалили последний элемент списка намс", nums)
# #Нечетные числа
# nums=[2*k+1 for k in range(5)]
# print("Нечетные числа", nums)
# #Список из символов создается на основе текста
# symbs=list("Python")
# #Отображение содержимого списка
# print("Содержимое списка", symbs)
# print("Два первых символа за двоеточием", symbs[:2])
# print("Остальные символы перед двоеточием", symbs[2:])

#Условный оператор if & else
#Считывание целого числа
# number=int(input("Введите целое число: "))
# #Если число четное
# if number%2==0:
#     print("Вы ввели четное число")
# #Если число не четное
# else:
#     print("Вы ввели нечетное число")

# #Знакомство с оператором цикла
# #Считывание верхней границы суммы:
# n=int(input("Укажите верхнюю границу суммы: "))
# #начальное значение суммы
# s=0
# #начальное знач индексной переменной
# k=0
# #оператор цикла для вычисления суммы:
# while k<n:
#     #увеличение индекса
#     k=k+1
#     #прибавление слагаемого к сумме
#     s=s+k
# print("Сумма чисел от 1 до", n,"равна", s)

#Альтернативный способ вычисления суммы
n=input("Укажите кол-во слагаемых")
txt="1"
k=1
while str(k)!=n:
    k=k+1
    txt=txt+"+"+str(k)
    print(txt, "=", eval(txt))