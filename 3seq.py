#Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
#Затем он вводит элементы 2-го списка
#Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран

usr_input1 = input("Please input first sequence of numbers, separating them by commas: ")
lst1 = usr_input1.split(",")
lst1a = [int(c) for c in lst1]
usr_input2 = input("Please input second sequence of numbers, separating them by commas: ")
lst2 = usr_input2.split(",")
lst2a = [int(c) for c in lst2]

print("Your first list:")
print(lst1a)
print("Your second list:")
print(lst2a)

lst_1st_not_2nd = [item for item in set(lst1a).difference(lst2a)]
print("The first list, without the elements from the second list:")
print(lst_1st_not_2nd)