# for
# for (how many)
# for (start from, how many)
# for (start from, how many, step)

question=int(input("1(Ganjil), 2(Genap), 3(Keluar) = "))

if question==1:
    end=int(input("Mau sampe angka berapa? "))
    for i in range(1,end,2):
        print(i)

elif question==2:
    end=int(input("Mau sampe angka berapa? "))
    for i in range(2,end,2):
        print(i)
        
elif question==3:
    print("keluar")
    break

else:
    break