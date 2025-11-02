from collections import Counter

# Запрашиваем имя
name = (str("Напишите имена: "))
names1 = input(str("Напишите имя 1:  \n 1:"))
names2 = input(str("Напишите имя 2:  \n 2:"))
names3 = input(str("Напишите имя 3:  \n 3:"))
names4 = input(str("Напишите имя 4:  \n 4:"))
names5 = input(str("Напишите имя 5:  \n 5:"))

#Запрашиваем номер телефона
phone_number1 = input(str("Напишите номер телефона пользователя 1 : \n 1: "))
phone_number2 = input(str("Напишите номер телефона пользователя 2 : \n 2:"))
phone_number3 = input(str("Напишите номер телефона пользователя 3 : \n 3:"))
phone_number4 = input(str("Напишите номер телефона пользователя 4 : \n 4:"))
phone_number5 = input(str("Напишите номер телефона пользователя 5 : \n 5:"))

#Определим класс переменных
print(type(names1))
print(type(phone_number1))

# Создаем список всех имен для подсчета
all_names = [names1, names2, names3, names4, names5]

# Подсчитываем сколько раз встречается имя
name_counter = Counter(all_names)

#Запишем картеж (Для  не изменяемых значений )
name_phoneNum1 = tuple("1." + names1 + ": " "1." + phone_number1 + ":")
for name_phoneNums in name_phoneNum1:
    name_phoneNum = name_phoneNums.split('.')
print(name_phoneNum1)

name_phoneNum2 = tuple("2." + names2 + ": " "2." + phone_number2 + ":")
for name_phoneNums in name_phoneNum2:
    name_phoneNum = name_phoneNums.split('.')
print(name_phoneNum2)

name_phoneNum3 = tuple("3." + names3 + ": " "3." + phone_number3 + ":")
for name_phoneNums in name_phoneNum3:
    name_phoneNum = name_phoneNums.split('.')
print(name_phoneNum3)

name_phoneNum4 = tuple("4." + names4 + ": " "4." + phone_number4 + ":")
for name_phoneNums in name_phoneNum4:
    name_phoneNum = name_phoneNums.split('.')
print(name_phoneNum4)

name_phoneNum5 = tuple("5." + names5 + ": " "5." + phone_number5 + ":")
for name_phoneNums in name_phoneNum5:
    name_phoneNum = name_phoneNums.split('.')
print(name_phoneNum5)
#Выведем количество повторений
print(name_counter)
# Напишем общий список контактов
name_list1 = ("1."+ names1 +" "+ phone_number1)
name_list2 = ("2."+ names2 +" "+ phone_number2)
name_list3 = ("3."+ names3 +" "+ phone_number3)
name_list4 = ("4."+ names4 +" "+ phone_number4)
name_list5 = ("5."+ names5 +" "+ phone_number5)
#Вывод
print(name_list1)
print(name_list2)
print(name_list3)
print(name_list4)
print(name_list5)


