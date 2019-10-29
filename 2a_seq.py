#Пользователь вводит количество цифр и потом любые цифры
#Сохранить цифры в список
#Получить новый список в котором будут только уникальные элементы исходного
# ...(уникальным считается символ, который встречается в исходном списке только 1 раз)
#Вывести новый список на экран
#Порядок цифр в новом списке не важен

number_elements = int(input("Please enter number of elements in the list "))
lst = [int(input("Enter any number ")) for i in range(1,number_elements+1)]
print("You created the following list:")
print(lst)
lst_unique = set(lst)
print("Your list, but only with unique elements:")
print(lst_unique)