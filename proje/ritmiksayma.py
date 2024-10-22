baslangic = int(input("Ritmik saymaya başlamak için bir başlangıç sayısı girin: "))
bitis = int(input("Ritmik saymanın biteceği sayıyı girin: "))
artis = int(input("Her adımda kaç sayı atlamak istersiniz? "))

# Ritmik saymayı gerçekleştir
print(f"\nRitmik sayma {baslangic} ile {bitis} arasında:")
for sayi in range(baslangic, bitis + 1, artis):
    print(sayi)
