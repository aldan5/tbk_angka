import random
sdan = 0
spy = 0
us = input("enter your name users : ")
for ronde in range(1,4):
    while True:
        me = int(input("masukkan Angka 1,2,atau 3 : "))
        bot = random.randint(1,3)
        if(me > 3):
            print("masukkan Ulang \n")
            break
        print(f"{us} menjawab {me}")
        print(f" PyBot menjawab {bot} \n")
        if(me != bot):
            spy += 5
            print(f"Pybot {spy} poin")
            print(f"{us} {sdan} poin")
            print("XXXXX---SALAH--XXX-XXXX \n")
        else:
            sdan += 5
            print(f"Pybot {spy} poin")
            print(f"{us} {sdan} poin")
            print("-----BENAAAAAARRRR------\n")
        break
    if (ronde >=3 ):
        print("---------------------------")
        print(f"skor {us} : {sdan}")
        print(f"skor Pybot : {spy}")
        if (sdan > spy):
            print(f"{us} Menang !!!!")
        else:
            print("PyBot Menang !!!")
        print("---------------------------")      