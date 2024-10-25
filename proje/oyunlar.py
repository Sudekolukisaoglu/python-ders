import random

def oyun_oyna():
    kelimeler = ["zürafa", "radyo", "çiçek", "kurabiye", "ambulans", "tren", "sincap"]
    kelime = random.choice(kelimeler)
    tahminler = []
    deneme_hakki = 5
    kelime_tahmin = ["_" for _ in kelime]

    print("Adam Asmaca Oyununa Hoşgeldiniz!")

    while deneme_hakki > 0 and "_" in kelime_tahmin:
        print("\nKalan deneme hakkı:", deneme_hakki)
        print("Tahmin ettiğiniz kelime:", " ".join(kelime_tahmin))
        tahmin = input("Bir harf tahmin edin: ").lower()

        if len(tahmin) != 1 or not tahmin.isalpha():
            print("Lütfen sadece bir harf girin.")
            continue

        if tahmin in tahminler:
            print("Bu harfi zaten tahmin ettiniz.")
            continue

        tahminler.append(tahmin)

        if tahmin in kelime:
            for index, harf in enumerate(kelime):
                if harf == tahmin:
                    kelime_tahmin[index] = tahmin
            print("Tebrikler! Doğru tahmin.")
        else:
            deneme_hakki -= 1
            print("Üzgünüm, bu harf kelimede yok.")

    if "_" not in kelime_tahmin:
        print("Tebrikler! Kelimeyi buldunuz:", kelime)
    else:
        print("Kaybettiniz! Kelime:", kelime)

def matematik_oyunu():
    print("Matematik Oyununa Hoşgeldiniz!")
    puan = 0
    soru_sayisi = 5

    for _ in range(soru_sayisi):
        sayi1 = random.randint(1, 10)
        sayi2 = random.randint(1, 10)
        cevap = sayi1 + sayi2

        tahmin = int(input(f"{sayi1} + {sayi2} = ? "))

        if tahmin == cevap:
            print("Doğru cevap!")
            puan += 1
        else:
            print(f"Yanlış cevap! Doğru cevap: {cevap}")

    print(f"Oyun bitti! Toplam puanınız: {puan}/{soru_sayisi}")

def main():
    print("Oyun Seçenekleri:")
    print("1. Adam Asmaca")
    print("2. Matematik Oyunu")

    secim = input("Bir oyun seçin (1 veya 2): ")

    if secim == '1':
        oyun_oyna()
    elif secim == '2':
        matematik_oyunu()
    else:
        print("Geçersiz seçim!")

# Ana fonksiyonu çalıştır
if __name__ == "__main__":
    main()
