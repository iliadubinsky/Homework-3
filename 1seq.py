#Пользователь вводит количество элементов будущего списка
#После этого по очереди по одной вводит любые цифры
#Сохранить цифры в список
#Отсортировать список по возрастанию и вывести на экран
number_elements = int(input("Enter number of elements in the list "))
lst = [int(input("Enter any number ")) for i in range(1,number_elements+1)]
lst.sort()
print("Sorted list is:")
print(lst)