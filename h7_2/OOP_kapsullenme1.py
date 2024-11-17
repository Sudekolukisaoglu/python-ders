class BankaMusterisi():
    adiSoyadi = "---"
    hesapNumarasi = "tanımlanmamış"
    kalanParasi = 0
    # def __init__():
    
kasa1 = BankaKasasi()
kasa1.KasadaKalanMiktar = 50000

musteri1 = BankaMusterisi()
musteri1.adiSoyadi = "Nurdan KARA"
musteri1.hesapNumarasi ="5489784"
musteri1.kalanParasi = "5000"

print(f"\n\nKasada kalan para miktarı : {kasa1.kasadaKalanMiktar}")

print(f"Müşteri Bilgileri\n\
      Adı: \t{musteri1.adiSoyadi}\n\
      Hesap No: \t{musteri1.adiSoyadi}\n\
      Kalan Parası: \t{musteri1.kalanParasi}")

musteri1.kalanParasi +=5000

print(f"\n\nKasada kalan para miktarı : {kasa1.kasadaKalanMiktar}")

print(f"Müşteri Bilgileri\n\
      Adı: \t{musteri1.adiSoyadi}\n\
      Hesap No: \t{musteri1.adiSoyadi}\n\
      Kalan Parası: \t{musteri1.kalanParasi}")
