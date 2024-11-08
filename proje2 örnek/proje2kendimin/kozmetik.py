def urun_ekle():
    with open("kozmetik_urunler.txt", "a") as dosya:
        print("\n\nKozmetik ürüne ait bilgileri giriniz")
        urun_adi = input("Ürün Adı: ")
        fiyat = input("Fiyat: ")
        tanitim = input("Ürün Tanıtımı: ")
        dosya.write(f"{urun_adi}#{fiyat}#{tanitim}\n")
    print("\n\nÜrün Listesi (güncel hali):")
    urun_listele()

def urun_listele():
    print("\n\nÜrünler:")
    with open("kozmetik_urunler.txt") as dosya:
        urunler = dosya.readlines()
    for sira, urun in enumerate(urunler):
        urun_bilgileri = urun.split("#")
        print(f"{sira+1} - Ürün Adı: {urun_bilgileri[0]}, Fiyat: {urun_bilgileri[1]}")

def urun_tanit():
    urun_listele()
    urun_no = int(input("Tanıtımını görmek istediğiniz ürün numarasını giriniz: ")) - 1
    with open("kozmetik_urunler.txt") as dosya:
        urunler = dosya.readlines()
    if 0 <= urun_no < len(urunler):
        urun_bilgileri = urunler[urun_no].split("#")
        print(f"\nÜrün Adı: {urun_bilgileri[0]}")
        print(f"Fiyat: {urun_bilgileri[1]}")
        print(f"Tanıtım: {urun_bilgileri[2]}")

def urun_duzelt():
    pass

def urun_sil():
    pass



def anamenu():
    print("╔═════════════════════╗")
    print("║ KOZMETİK UYGULAMASI ║")
    print("║═════════════════════║")
    print("║  1-Ürün Ekle        ║")
    print("║  2-Ürün Listesi     ║")
    print("║  3-Ürün Tanıt       ║")
    print("║  4-Ürün Düzenle     ║")
    print("║  5-Ürün Sil         ║")
    print("║  6-Çıkış            ║")
    print("╚═════════════════════╝")
   
    secim = input("Seçiminiz nedir? ")
    if secim == "1": urun_ekle(); anamenu()
    elif secim == "2": urun_listele(); anamenu()
    elif secim == "3": urun_tanit(); anamenu()
    elif secim == "4": urun_duzelt(); anamenu()
    elif secim == "5": urun_sil(); anamenu()
    elif secim == "6": urun_ekle(); anamenu()

anamenu()
