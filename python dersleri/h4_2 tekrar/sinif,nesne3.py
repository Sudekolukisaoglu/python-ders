class Ogrenci(): #kalıp
    adi = "--"
    ortalaması = 50
    # soyadi =""
    def __init__(aa,xx,yy): # aa = self = kendine ait şeyleri
        aa.adi = xx
        aa.ortalamasi = yy


# ogrenci1 = Ogrenci()  #Sınıftan nesne oluşturma
# ogrenci1.adi = "Buse DOĞAN"
# ogrenci1.ortalamasi = 80
ogrenci1 = Ogrenci("Buse AYDOĞAN",81) # sınıftan nesne oluşturma

# ogrenci2 = Ogrenci()
# ogrenci2.adi = "Ebru GÜNDEŞ"
# ogrenci2.ortalamasi =90
ogrenci2 = Ogrenci("Ebru GÜNDEŞŞ",91)

print(ogrenci2)
print(ogrenci2.adi)
# print(ogrenci2.soyadı)
print(Ogrenci.adi)                   




  


