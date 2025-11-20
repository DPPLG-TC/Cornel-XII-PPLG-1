# tebak angka
import random, os, time
angka1=int(input("Angka pertama= "))
angka2=int(input("Angka kedua= "))


target = random.randint(angka1,angka2)
tebak=int(input("Angka Tebakan= "))
while True:
    if tebak==target:
        
        print("Anda benar, jawabannya",target,",dalam pencobaan ke-",percobaan)
        time.sleep(3)
        break
    elif tebak<=target:
        print("Anda salah, angka target lebih besar")
        time.sleep(3)
        tebak=int(input("Angka Tebakan= "))
    elif tebak>=target:
        print("Anda salah, angka target lebih kecil")
        time.sleep(3)
        tebak=int(input("Angka Tebakan= "))
    else:
        print("Error")
        tebak=int(input("Angka Tebakan= "))
        
    
    