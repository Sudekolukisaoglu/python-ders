import random
import os

def oyun_oyna():
    kelimeler = ["zürafa", "radyo", "çiçek", "kurabiye", "ambulans", "tren", "sincap"]
    kelime = random.choice(kelimeler)
    tahminler = []
    deneme_hakki = 10
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

def print_board(yilan, yem, boyut=10):
    os.system('cls' if os.name == 'nt' else 'clear')
    board = [['.' for _ in range(boyut)] for _ in range(boyut)]
    
    for (x, y) in yilan:
        board[y][x] = 'Y'  # Yılan
    board[yem[1]][yem[0]] = 'E'  # Yem

    for row in board:
        print(' '.join(row))
    print()

def yilan_oyunu():
    boyut = 10
    yilan = [(0, 0)]
    yem = (random.randint(0, boyut-1), random.randint(0, boyut-1))
    yön = (0, 1)  # Başlangıçta sağa hareket

    while True:
        print_board(yilan, yem, boyut)
        
        girdi = input("Yön (W/A/S/D): ").lower()
        if girdi == 'w':
            yön = (0, -1)
        elif girdi == 's':
            yön = (0, 1)
        elif girdi == 'a':
            yön = (-1, 0)
        elif girdi == 'd':
            yön = (1, 0)

        yeni_baş = (yilan[0][0] + yön[0], yilan[0][1] + yön[1])

        # Sınır kontrolü
        if (0 <= yeni_baş[0] < boyut and 0 <= yeni_baş[1] < boyut and yeni_baş not in yilan):
            yilan.insert(0, yeni_baş)  # Yılanı güncelle
            if yeni_baş == yem:
                yem = (random.randint(0, boyut-1), random.randint(0, boyut-1))  # Yeni yem
            else:
                yilan.pop()  # Yılanın sonunu çıkar
        else:
            print("Oyun Bitti!")
            break

def main():
    print("Oyun Seçenekleri:")
    print("1. Adam Asmaca")
    print("2. Yılan Oyunu")

    secim = input("Bir oyun seçin (1 veya 2): ")

    if secim == '1':
        oyun_oyna()
    elif secim == '2':
        yilan_oyunu()
    else:
        print("Geçersiz seçim!")


