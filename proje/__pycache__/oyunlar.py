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

