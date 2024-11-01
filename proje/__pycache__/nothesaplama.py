def not_hesapla():
    notlar = []

    while True:
        not_gir = input("Notunuzu girin (çıkmak için 'q' yazın): ")
        if not_gir.lower() == 'q':
            break
        try:
            not_deger = float(not_gir)
            if 0 <= not_deger <= 100:
                notlar.append(not_deger)
            else:
                print("Not 0 ile 100 arasında olmalı.")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    if notlar:
        ortalama = sum(notlar) / len(notlar)
        print(f"Notlar: {notlar}")
        print(f"Not Ortalaması: {ortalama:.2f}")

        if ortalama >= 50:
            print("Geçtiniz!")
        else:
            print("Kaldınız.")
    else:
        print("Hiç not girmediniz.")
