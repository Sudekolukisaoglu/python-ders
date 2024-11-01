def ritmik_sayma():
    baslangic = int(input("Ritmik saymaya başlamak için bir başlangıç sayısı girin: "))
    adim = int(input("Hangi sayıya kadar saymak istersiniz? "))
    atlama = int(input("Kaç sayı atlayarak saymak istersiniz? "))

    for i in range(baslangic, adim + 1, atlama):
        print(i)
