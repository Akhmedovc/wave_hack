
def decrypt():
    Y = str(input("Enter your shifr text: "))
    K1 = int(input("Enter your key: "))
    cipher = ""


    for z in Y:
        cipher += chr(ord(z) ^ K1)
    print("Дешифртекст:", cipher)


