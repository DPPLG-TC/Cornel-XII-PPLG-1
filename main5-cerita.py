import time
import sys
def jeda(detik):
    time.sleep(detik)
def tampilkan_teks(teks):
    print(teks)
    jeda(1.2)
def dapatkan_pilihan(opsi_valid):
    while True:
        pilihan_str = input(f"Pilihan ({'/'.join(map(str, opsi_valid))}): ")
        if pilihan_str.isdigit():
            pilihan_int = int(pilihan_str)
            if pilihan_int in opsi_valid:
                return pilihan_int
        tampilkan_teks("Pilihan tidak valid. Coba lagi.")
def good_ending(pesan):
    tampilkan_teks("\n=====================================")
    tampilkan_teks(f"--- GOOD ENDING ({pesan}) ---")
    tampilkan_teks("Kamu selamat... untuk malam ini.")
    tampilkan_teks("=====================================")
    sys.exit()
def bad_ending(pesan):
    tampilkan_teks("\n*************************************")
    tampilkan_teks(f"--- BAD ENDING ({pesan}) ---")
    tampilkan_teks("Semuanya menjadi gelap.")
    tampilkan_teks("*************************************")
    sys.exit()
def mulai_cerita():
    tampilkan_teks("Once upon time at XII PPLG 1...")
    tampilkan_teks("Suasana kelas sudah sepi, hanya kamu yang tersisa.")
    tampilkan_teks("Di sudut ruangan, tergeletak sebuah gitar tua.")
    tampilkan_teks("Apa yang kamu lakukan?")
    tampilkan_teks("1. Mainkan gitar itu.")
    tampilkan_teks("2. Tinggalkan dan segera keluar kelas.")
    tampilkan_teks("3. Periksa tasmu dulu, mencari sesuatu yang berguna.")
    pilihan = dapatkan_pilihan([1, 2, 3])
    if pilihan == 1:
        adegan_mainkan_gitar()
    elif pilihan == 2:
        adegan_tinggalkan_gitar()
    elif pilihan == 3:
        adegan_periksa_tas()
def adegan_mainkan_gitar():
    tampilkan_teks("Kamu mengambil gitar itu...")
    tampilkan_teks("jreng... jreng... jreng...")
    jeda(2)
    tampilkan_teks("Tiba-tiba ada sosok hitam tinggi dari belakang... bayangannya menutupi cahaya bulan.")
    tampilkan_teks("Apa yang kamu lakukan?")
    tampilkan_teks("1. Terus mainkan lagu 'Kemesraan Ini'")
    tampilkan_teks("2. Lempar gitar dan lari")
    tampilkan_teks("3. Diam mematung ketakutan")
    pilihan = dapatkan_pilihan([1, 2, 3])
    if pilihan == 1:
        tampilkan_teks("Kamu nekat terus bermain... 'janganlah cepat berlalu...'")
        jeda(2)
        tampilkan_teks("Sosok itu ikut bernyanyi dengan suara berat... 'kemesraan iniii...'")
        jeda(2)
        tampilkan_teks("Kamu menoleh...")
        tampilkan_teks("Ternyata itu Pak Satpam yang sedang patroli. 'Lho, Dek, belum pulang?'")
        good_ending("Duet Maut")
    elif pilihan == 2:
        tampilkan_teks("Kamu melempar gitar itu ke arahnya dan lari ke pintu!")
        tampilkan_teks("BRAK! Pintunya terkunci.")
        jeda(2)
        tampilkan_teks("Sosok itu mengambil gitar... dan mulai memainkannya dengan nada yang sangat sumbang.")
        bad_ending("Terkunci")
    elif pilihan == 3:
        tampilkan_teks("Kamu diam mematung. Sosok itu perlahan mendekat...")
        tampilkan_teks("Bayangannya kini menyelimutimu.")
        tampilkan_teks("1. Tutup mata rapat-rapat.")
        tampilkan_teks("2. Berteriak minta tolong.")
        pilihan_nested = dapatkan_pilihan([1, 2])
        if pilihan_nested == 1:
            tampilkan_teks("Kamu menutup mata... kamu merasakan hawa dingin...")
            tampilkan_teks("Saat kamu buka mata, kamu sudah di UKS.")
            tampilkan_teks("'Kamu pingsan kecapekan, Dek,' kata guru piket.")
            good_ending("Pingsan di UKS")
        else:
            tampilkan_teks("Kamu berteriak... tapi suaramu tidak keluar.")
            tampilkan_teks("Sosok itu mencondongkan tubuhnya...")
            bad_ending("Ditelan Bayangan")
def adegan_tinggalkan_gitar():
    tampilkan_teks("Kamu memutuskan untuk tidak menyentuh gitar itu dan bergegas keluar.")
    tampilkan_teks("Saat di depan pintu...")
    tampilkan_teks("Tiba-tiba ada sosok putih pendek dari depan... menghalangi jalanmu.")
    jeda(2)
    tampilkan_teks("Dia menunduk.")
    tampilkan_teks("Apa yang kamu lakukan?")
    tampilkan_teks("1. Menyapa, 'Permisi, Dek?'")
    tampilkan_teks("2. Mendorongnya dan lari")
    tampilkan_teks("3. Mencoba menyelinap diam-diam lewat sampingnya")
    pilihan = dapatkan_pilihan([1, 2, 3])
    if pilihan == 1:
        tampilkan_teks("Kamu menyapanya dengan sopan...")
        tampilkan_teks("Sosok itu mengangkat kepalanya... ternyata adik kelas yang menangis.")
        tampilkan_teks("'Kak... HP-ku ketinggalan di laci meja guru...'")
        tampilkan_teks("Kamu membantunya mengambil HP itu. Kalian pun pulang bersama.")
        good_ending("Salah Sangka")
    elif pilihan == 2:
        tampilkan_teks("Kamu mendorongnya kasar... 'MINGGIR!'")
        tampilkan_teks("Sosok itu jatuh... tapi dia tidak menangis.")
        jeda(2)
        tampilkan_teks("Dia mengangkat kepalanya, matanya merah menyala.")
        tampilkan_teks("'KENAPA... DIDORONG...?'")
        bad_ending("Tidak Sopan")
    elif pilihan == 3:
        tampilkan_teks("Kamu mencoba berjingkat pelan melewatinya...")
        tampilkan_teks("Kamu berhasil! Kamu sudah di koridor.")
        tampilkan_teks("Tiba-tiba dari belakang terdengar isak tangis yang kencang.")
        tampilkan_teks("1. Kembali untuk mengecek.")
        tampilkan_teks("2. Tidak peduli, lari terus ke gerbang.")
        pilihan_nested = dapatkan_pilihan([1, 2])
        if pilihan_nested == 1:
            tampilkan_teks("Kamu kembali dan menemukan adik kelas itu menangis sendirian.")
            tampilkan_teks("Kamu menenangkannya dan mengantarnya pulang.")
            good_ending("Pahlawan Kesiangan")
        else:
            tampilkan_teks("Kamu terus lari... tapi suara tangisan itu terus terngiang di kepalamu.")
            tampilkan_teks("Bahkan setelah di rumah... kamu masih mendengarnya.")
            bad_ending("Dihantui Rasa Bersalah")
def adegan_periksa_tas():
    tampilkan_teks("Kamu merogoh tasmu... mencari sesuatu yang mungkin berguna.")
    tampilkan_teks("Kamu menemukan... sebuah SENTER kecil.")
    tampilkan_teks("Apa yang kamu lakukan dengan senter itu?")
    tampilkan_teks("1. Sorot ke arah gitar tua.")
    tampilkan_teks("2. Sorot ke arah pintu keluar.")
    tampilkan_teks("3. Simpan senter dan mainkan gitar (balik ke Cabang 1).")
    pilihan = dapatkan_pilihan([1, 2, 3])
    if pilihan == 1:
        tampilkan_teks("Kamu sorot gitar itu... Cahayanya menampakkan ukiran aneh di bodinya.")
        tampilkan_teks("Ukiran itu terlihat seperti simbol 'mata'.")
        tampilkan_teks("1. Menyentuh ukiran mata itu.")
        tampilkan_teks("2. Mengabaikan ukiran dan pergi.")
        pilihan_nested = dapatkan_pilihan([1, 2])
        if pilihan_nested == 1:
            tampilkan_teks("Saat kamu sentuh... ukiran itu bersinar lembut.")
            tampilkan_teks("Kamu merasa tenang. Sosok 'penjaga' kelas ini merestuimu.")
            tampilkan_teks("Kamu pulang dengan perasaan damai.")
            good_ending("Teman Gaib")
        else:
            tampilkan_teks("Kamu berbalik... tapi sentermu mendadak mati.")
            tampilkan_teks("Gitar itu berbunyi 'JRENG!' sangat keras di belakangmu.")
            bad_ending("Gitar Marah")
    elif pilihan == 2:
        tampilkan_teks("Kamu sorot pintu keluar. Tidak ada apa-apa. Aman.")
        tampilkan_teks("Kamu berjalan ke pintu... tapi dari sudut matamu, kamu lihat sesuatu di JENDELA.")
        tampilkan_teks("1. Langsung lari keluar pintu, jangan menoleh.")
        tampilkan_teks("2. Beranikan diri menyorot ke jendela.")
        pilihan_nested = dapatkan_pilihan([1, 2])
        if pilihan_nested == 1:
            tampilkan_teks("Kamu lari secepat mungkin keluar kelas, menyusuri koridor, dan keluar gerbang.")
            tampilkan_teks("Kamu tidak tahu apa itu, dan kamu tidak mau tahu.")
            good_ending("Lari Cepat")
        else:
            tampilkan_teks("Kamu arahkan senter ke jendela...")
            tampilkan_teks("Sepasang mata merah menatapmu dari balik kaca.")
            tampilkan_teks("Kaca itu retak.")
            bad_ending("Mata di Jendela")
    elif pilihan == 3:
        tampilkan_teks("Kamu menyimpan senter itu di sakumu... dan beralih ke gitar.")
        adegan_mainkan_gitar()
if __name__ == "__main__":
    mulai_cerita()
