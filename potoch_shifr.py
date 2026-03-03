import random

def crypto():
    surname = str(input("Введите фамилию: "))
    name = str(input("Введите имя: "))
    otchestvo = str(input("Введите отчество: "))
    birth_yeat = int(input("Введите год рождения: "))
    study_group = int(input("Введите учебную группу: "))
    hobby = str(input("Введите направление: "))

    Y = surname + " " + name + " " + otchestvo + " " + str(birth_yeat) + " " + str(study_group) + " " + hobby
    K1 = random.randint(1, 255)
    print("ваш ключ:", K1)

    crypted = ""
    for z in Y:
        crypted += chr(ord(z) ^ K1)
        print("Шифртекст:", crypted)