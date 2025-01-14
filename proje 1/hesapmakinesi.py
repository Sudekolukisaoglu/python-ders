def hesap_makinesi():
    print("Hesap Makinesi")
    print("İşlemler: ")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    
    secim = input("Bir işlem seçin (1/2/3/4): ")

    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))

    if secim == '1':
        print(f"Sonuç: {sayi1} + {sayi2} = {sayi1 + sayi2}")
    elif secim == '2':
        print(f"Sonuç: {sayi1} - {sayi2} = {sayi1 - sayi2}")
    elif secim == '3':
        print(f"Sonuç: {sayi1} * {sayi2} = {sayi1 * sayi2}")
    elif secim == '4':
        if sayi2 != 0:
            print(f"Sonuç: {sayi1} / {sayi2} = {sayi1 / sayi2}")
        else:
            print("Hata: Sıfıra bölme yapılamaz!")
    else:
        print("Geçersiz bir seçim yaptınız.")

