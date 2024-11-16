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
    if not urunler:  # Eğer liste boşsa
        print("Kayıtlı ürün bulunmamaktadır.")
        return
    for sira, urun in enumerate(urunler):
        urun_bilgileri = urun.split("#")
        print(f"{sira+1} - Ürün Adı: {urun_bilgileri[0]}, Fiyat: {urun_bilgileri[1]}")

def urun_tanit():
    urun_listele()
    try:
        urun_no = int(input("Tanıtımını görmek istediğiniz ürün numarasını giriniz: ")) - 1
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")
        return
    with open("kozmetik_urunler.txt") as dosya:
        urunler = dosya.readlines()
    if not urunler or urun_no < 0 or urun_no >= len(urunler):
        print("Hatalı ürün numarası!")
        return
    urun_bilgileri = urunler[urun_no].strip().split("#")
    print(f"\nÜrün Adı: {urun_bilgileri[0]}")
    print(f"Fiyat: {urun_bilgileri[1]}")
    print(f"Tanıtım: {urun_bilgileri[2]}")

def urun_duzelt():
    urun_listele()
    try:
        urun_no = int(input("Düzenlemek istediğiniz ürün numarasını giriniz: ")) - 1
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")
        return
    with open("kozmetik_urunler.txt") as dosya:
        urunler = dosya.readlines()
    if not urunler or urun_no < 0 or urun_no >= len(urunler):
        print("Hatalı ürün numarası!")
        return
    urun_bilgileri = urunler[urun_no].strip().split("#")
    print(f"Mevcut bilgiler: {urun_bilgileri}")
    urun_adi = input(f"Yeni Ürün Adı ({urun_bilgileri[0]}): ") or urun_bilgileri[0]
    fiyat = input(f"Yeni Fiyat ({urun_bilgileri[1]}): ") or urun_bilgileri[1]
    tanitim = input(f"Yeni Tanıtım ({urun_bilgileri[2]}): ") or urun_bilgileri[2]
    urunler[urun_no] = f"{urun_adi}#{fiyat}#{tanitim}\n"
    with open("kozmetik_urunler.txt", "w") as dosya:
        dosya.writelines(urunler)
    print("Ürün başarıyla güncellendi!")

def urun_sil():
    urun_listele()
    try:
        urun_no = int(input("Silmek istediğiniz ürün numarasını giriniz: ")) - 1
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")
        return
    with open("kozmetik_urunler.txt", "r") as dosya:
        urunler = dosya.readlines()
    if not urunler or urun_no < 0 or urun_no >= len(urunler):
        print("Hatalı ürün numarası!")
        return
    silinecek_urun = urunler.pop(urun_no)
    with open("kozmetik_urunler.txt", "w") as dosya:
        dosya.writelines(urunler)
    print(f"\nÜrün başarıyla silindi: {silinecek_urun}")

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
    elif secim == "6":
        print("Çıkış yapılıyor...")
        exit()
    else:
        print("\nHatalı seçim! Lütfen tekrar deneyin.")
        anamenu()

anamenu()
