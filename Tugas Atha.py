def cek_syarat_diskon(total_belanja, jumlah_barang):
    if total_belanja > 200000 and jumlah_barang >= 5:
        return True
    else:
        return False

total_belanja = float(input("Masukkan total belanja Anda: "))
jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))

if cek_syarat_diskon(total_belanja, jumlah_barang):
    print("Selamat! Anda memenuhi syarat untuk mendapatkan diskon belanja.")
else:
    print("Maaf, Anda tidak memenuhi syarat untuk mendapatkan diskon belanja.")