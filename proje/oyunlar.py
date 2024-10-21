def oyun_oyna():
    print("tahmin oyunu")

    tahmin = input("Bir sayı tahmin edin (1-10): ")
    if tahmin.isdigit() and 1 <= int(tahmin) <= 10:
        print(f"Tahmininiz: {tahmin}. Oyun başladı!")
    else:
        print("Lütfen 1 ile 10 arasında bir sayı girin.")


