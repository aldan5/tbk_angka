import random


me = int(input("masukkan Angka : "))
bot = random.randint(1,3)
print(me)
print(bot)
while True:
    if(me != bot):
        print("kalian salah")
        break
    else:
        print("benar")
        break
    
        