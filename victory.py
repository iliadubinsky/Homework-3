#Написать или улучшить программу Викторина из предыдущего дз (не пользоваться никакими библиотеками кроме random)
#Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') - использовать строку
#Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random и функции sample

import random
while True:
    numbers = [1,2,3,4,5,6,7,8,9,10]
    sample = random.sample(numbers,5)
    #print(sample)
    print("Сыграем в игру \"Эрудит\". Введите день рождения знаменитого человека. Используйте формат \"dd.mm.yyyy\".")
    input_dict = {1: 'Пушкина', 2: 'Лермонтова',3:"Чехова", 4:'Толстого', 5:'Достоевского', 6:"Лобачевского",
                7:"Менделеева", 8:"Ломоносова", 9:"Тимирязева",10:"Павлова"}
    bd_dict = {1:'06.06.1799', 2:'15.10.1814',3:'29.01.1860', 4:'09.09.1828', 5:'11.11.1821',6:'01.12.1792',
             7:'08.02.1834',8:'19.11.1711',9:'03.06.1843', 10:'26.09.1849'}
    bd_output_dict = {1:'06 июня 1799', 2:'15 октября 1814',3:'29 января 1860', 4:'09 сентября 1828', 5:'11 ноября 1821',
             6:'01 декабря 1792', 7:'08 февраля 1834',8:'19 ноября 1711',9:'03 июня 1843', 10:'26 сентября 1849'}
    right_counter = 0
    bd0 = input("Введите день рождения "+input_dict[sample[0]]+": ")
    if bd0 == bd_dict[sample[0]]:
        print("Вы совершенно правы! Вы правильно угадали день рождения "+input_dict[sample[0]])
        right_counter+=1
    else:
        print ("Не правильно! День рождения "+input_dict[sample[0]]+ " "+bd_output_dict[sample[0]])

    bd1 = input("Введите день рождения "+input_dict[sample[1]]+": ")
    if bd1 == bd_dict[sample[1]]:
        print("Вы совершенно правы! Вы правильно угадали день рождения "+input_dict[sample[1]])
        right_counter += 1
    else:
        print ("Не правильно! День рождения "+input_dict[sample[1]]+ " "+bd_output_dict[sample[1]])

    bd2 = input("Введите день рождения "+input_dict[sample[2]]+": ")
    if bd2 == bd_dict[sample[2]]:
        print("Вы совершенно правы! Вы правильно угадали день рождения "+input_dict[sample[2]])
        right_counter += 1
    else:
        print ("Не правильно! День рождения "+input_dict[sample[2]]+ " "+bd_output_dict[sample[2]])

    bd3 = input("Введите день рождения "+input_dict[sample[3]]+": ")
    if bd3 == bd_dict[sample[3]]:
        print("Вы совершенно правы! Вы правильно угадали день рождения "+input_dict[sample[3]])
        right_counter += 1
    else:
        print ("Не правильно! День рождения "+input_dict[sample[3]]+ " "+bd_output_dict[sample[3]])

    bd4 = input("Введите день рождения "+input_dict[sample[4]]+": ")
    if bd4 == bd_dict[sample[4]]:
        print("Вы совершенно правы! Вы правильно угадали день рождения "+input_dict[sample[4]])
        right_counter += 1
    else:
        print ("Не правильно! День рождения "+input_dict[sample[4]]+ " "+bd_output_dict[sample[4]])

    print("Вы сделали "+str(right_counter)+ " правильных ответов.")
    print('Процент правильных ответов:', right_counter*100/5 )

    answer = input('Хотите сыграть еще раз?')
    if answer == 'нет':
        print('Cпасибо за игру')
        break
    print('Начинаем сначала!' )



#PushkinBD = '06.06.1799'
#LermontovBD = '15.10.1814'
#ChekhovBD = '29.01.1860'
#TolstoyBD = '09.09.1828'
#DostoyevskyBD = '11.11.1821'
#LobachevskyBD = '01.12.1792'
#MendeleevBD = '08.02.1834'
#LomonosovBD = '19.11.1711'
#TimiryazevBD = '03.06.1843'
#PavlovBD = '26.09.1849'
