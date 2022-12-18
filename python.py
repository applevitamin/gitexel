#name=input("Как Вас зовут? ")
#age=int(input("Сколько Вам лет? "))
#print("Добрый день,", name+"!")
#print("Вы родились в,", 2022-age,"году!")

#список из чисел
nums=[1,54,6,3,87,243,23,11]
#Отображение содержимого списка 
print("Список чисел",nums)
#Длина чисел
print("Длинна чисел", len(nums))
#первый элемент
print("first_element", nums[0])
#Последний элемент
print("last_element", nums[-1])
#наибольшее значение
print("max_nambers", max(nums))
print("min_meaning", min(nums))
print("summa", sum(nums))
#Список в обратно порядке
print("reversed_list", list(reversed(nums)))
#Сортировка значений
print("сортировка значений списка", list(sorted(nums)))
#исходный список
print("исходный список", nums)
#Изменение значений списка, для применения вывод списка
nums[1]="3333333"
print("После изменений", nums)
#Получение среза (4 элемент и последний элемент длины списка)
print("Получение среза", nums[4: len(nums)-1])
#Замена части эжлемента
nums[1:-1]=["A","B"]
print("После замены",nums)
#Список от 5 до 10 и вывод результата
nums=list(range(5,11))
print("от 5 до 10", nums)