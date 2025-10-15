from functools import reduce


class Ruslan:

    def __init__(self ,weith , toll , ayes ):

        self.weith = weith
        self.toll = toll
        self.ayes = ayes

print("Их характеристики : - ")
ruslan = Ruslan(f"180 toll", "110 kg","red")

print(ruslan.weith)
print(ruslan.toll)
print(ruslan.ayes, " - Цвет глаз")



class Masha(Ruslan):

    def __init__(self,Hair ,Nails):
        self.Hair = Hair
        self.Nails = Nails

masha = Masha(f"100 Hair"," 10 Nails"  )

print(masha.Hair)
print(masha.Nails)

class Meet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_couple(self):
        if self.age >= 18:
            print("Заебись вы пара")
        else:
            print("Пошел нахуй Рус")


# Основная программа
if __name__ == "__main__":
    entering = input("Введите возраст: ")
    age = int(entering)  # преобразуем в число

    result = Meet("Руслан", age)
    result.check_couple()



