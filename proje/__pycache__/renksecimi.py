def renk_secimi():
    print("Renk Seçimi")
    print("Aşağıdaki renklerden birini seçin:")
    print("1 - Kırmızı")
    print("2 - Yeşil")
    print("3 - Mavi")
    print("4 - Sarı")
    print("5 - Beyaz")
    
    secim = input("Seçiminiz (1-5): ")
    
    if secim == '1':
        renk = "\033[1;31m"  # Kırmızı
    elif secim == '2':
        renk = "\033[1;32m"  # Yeşil
    elif secim == '3':
        renk = "\033[1;34m"  # Mavi
    elif secim == '4':
        renk = "\033[1;33m"  # Sarı
    elif secim == '5':
        renk = "\033[1;37m"  # Beyaz
    else:
        print("Geçersiz seçim!")
        return

    print(f"{renk}Seçtiğiniz renk: {secim}\033[0m")  # Renkli mesaj
    input("Devam etmek için bir tuşa basın...")

# Fonksiyonu çağır
renk_secimi()
