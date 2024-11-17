class Ogrenci(): # Büyük veri tipi (sınıflar,nesnenin veri kalıbıdır)
    ad = "tanimsiz"
    tc = "yok"
    ortalamasi = 10

ogrenci1 = Ogrenci()  # object intialization / yeni bir nesne oluşturma
ogrenci1.ad = "Sude"   # bu ve sonraki 3 satır ile yeni nesne özellikleri ayarlanır.
ogrenci1.tc = "52968745921" 
ogrenci1.ortalamasi = 100
ogrenci1.disiplinNotu = 99
print(ogrenci1.disiplinNotu)  

ogrenci2 = Ogrenci()
ogrenci2.ad = "Rahime"
ogrenci2.tc = "89564512397"

print(ogrenci2.ortalamasi)