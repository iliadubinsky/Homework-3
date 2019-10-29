#Пользователь вводит любые цифры через запятую
#Сохранить цифры в список
#Получить новый список в котором будут только уникальные элементы исходного
# ...(уникальным считается символ, который встречается в исходном списке только 1 раз)
#Вывести новый список на экран
#Порядок цифр в новом списке не важен

usr_input = input("Please input several numbers, separating them by commas: ")
lst1 = usr_input.split(",")
lst2 = [int(c) for c in lst1]
print("You created the following list:")
print(lst2)
lst_unique = set(lst2)
print("Your list, but only with unique elements:")
print(lst_unique)