class Personel():
    sicilNo = "--"
    adiSoyadi ="tanımsız"

class Idareci(Personel):
    idariGörevi = "tanımlanmamış"

class katPersoneli(Personel):
    gorevliOlduguKat = 4

class Veli():
    ogrencisininAdi = "---" 

class CokluYetkiliPersonel(Idareci, Veli):   
    pass    

personel1 = Idareci()
personel2 =CokluYetkiliPersonel()
personel2.idariGörevi = "Müdür yardımcısı"
personel2.ogrencisininAdi = "Ufuk ALTIN"

print(personel1.sicilNo)
# print(personel1.gorevliOlduguKat)

print("İdari görev:",personel2.idariGörevi, "\nÖgrenci adı:",personel2.ogrencisininAdi)