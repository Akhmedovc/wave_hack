
def hack_crypto():
    crypted = input("Введите зашифрованный текст: ")

    for key in range(1, 256):
        decrypted = ""
    
        for z in crypted:
            decrypted += chr(ord(z) ^ key)
    
        print("Ключ:", key, "->", decrypted)    