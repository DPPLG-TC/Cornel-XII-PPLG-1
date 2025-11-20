import time,os,random

def tanyaSoal(soal, jawaban_benar):
    jawab=float(input(f"Berapa hasil {soal} = "))
    if jawab == jawaban_benar:
        print(f"Benar! Jawaban Anda tepat = {jawaban_benar}")
    else:
        print(f"Salah! Jawaban Anda salah = {jawaban_benar}")
    
    time.sleep(2)
        

def levelMudah():
    a=random.randint(1,9)
    b=random.randint(1,9)
    symbol=['+','-','/','*']
    operator=random.choice(symbol)
    soal=f"{a} {operator} {b}"
    if operator=="+":
        jawaban_benar=a+b
    elif operator=="-":
        jawaban_benar=a-b
    elif operator=="/":
        jawaban_benar=round(a/b,2)
    elif operator=="*":
        jawaban_benar=a*b
    
    tanyaSoal(soal, jawaban_benar)
    
def levelMenengah():
    a=random.randint(10,99)
    b=random.randint(10,99)
    symbol=['+','-','/','*']
    operator=random.choice(symbol)
    soal=f"{a} {operator} {b}"
    if operator=="+":
        jawaban_benar=a+b
    elif operator=="-":
        jawaban_benar=a-b
    elif operator=="/":
        jawaban_benar=round(a/b,2)
    elif operator=="*":
        jawaban_benar=a*b
    
    tanyaSoal(soal, jawaban_benar)
    
def levelSusah():
    a=random.randint(100,999)
    b=random.randint(100,999)
    symbol=['+','-','/','*']
    operator=random.choice(symbol)
    soal=f"{a} {operator} {b}"
    if operator=="+":
        jawaban_benar=a+b
    elif operator=="-":
        jawaban_benar=a-b
    elif operator=="/":
        jawaban_benar=round(a/b,2)
    elif operator=="*":
        jawaban_benar=a*b
    
    tanyaSoal(soal, jawaban_benar)
    
def main():
    os.system("clear")
    print("Selamat datang Math Quiz")
    time.sleep(2)
    while True:
        print("Silahkan pilih tingkat kesusahan =")
        pilihan=input('("mudah", "menengah", "susah") atau "keluar"= ').lower()
        if pilihan=="mudah":
            levelMudah()
        elif pilihan=="menengah":
            levelMenengah()
        elif pilihan=="susah":
            levelSusah()
        elif pilihan=="keluar":
            print("Terima kasih telah bermain!")
            break
        else:
            print("Input Valid")
    
if __name__ == "__main__":
    main()
    
