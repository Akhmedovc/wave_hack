import potoch_shifr as crypto
import potoch_deshifr as decrypt
import vzlom_shirf_potok as hack_crypto

question = int(input("Выберите действие: \n1. Зашифровать данные\n2. Расшифровать данные\n3. Взломать шифр\n"))

if question == 1:
    crypto.crypto()
elif question == 2:
    decrypt.decrypt()
elif question == 3:
    hack_crypto.hack_crypto()

