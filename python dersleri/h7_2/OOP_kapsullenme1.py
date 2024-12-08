class BankaKasasi():
    __KasadaKalanMiktar = 0 # __ ile kapsüllenmiş bilgi
    def kasadakiMiktar(self):
        return self.__KasadaKalanMiktar
    
    def kasayaParaEkle(self, miktar):
        self.__KasadaKalanMiktar += miktar

    def kasadanParaCikar(self, miktar):
        self.__KasadaKalanMiktar += miktar
        
class BankaMusterisi():


    adiSoyadi = "---"
    hesapNumarasi = "tanımlanmamış"
    kalanParasi = 0
    def __init__(self,ad,no,para):
        self.adiSoyadi = ad
        self.hesapNumarasi = no
        # self.kalanParasi = para

    def paraCek(self,cekilen):
        self.__kalanParasi -=cekilen
         # kasa1.__KasadaKalanMiktar -= cekilen
        kasa1.kasadanParaCikar(cekilen)

    def paraYatir(self,yatirilan):
        self.__kalanParasi += yatirilan
        # kasa1.__KasadaKalanMiktar += yatirilan
        kasa1.kasayaParaEkle(yatirilan)

    def kalanParaMiktariniGöster(self):
        return self.__kalanParasi

kasa1 = BankaKasasi()
kasa1.KasadaKalanMiktar = 50000

musteri1 = BankaMusterisi("Nurdan KARA","5489784","5000)

print(f"\n\nKasada kalan para miktarı : {kasa1.kasadaKalanMiktar}")

print(f"Müşteri Bilgileri\n\
      Adı: \t{musteri1.adiSoyadi}\n\
      Hesap No: \t{musteri1.hesapNumarasi}\n\

musteri1.adiSoyadi = "Ali AK"
# musteri1.__kalanParasi +=5000
musteri1.paraYatir(5000)

print(f"\n\nKasada kalan para miktarı : {kasa1.kasadaKalanMiktar}")

print(f"Müşteri Bilgileri\n\
      Adı: \t{musteri1.adiSoyadi}\n\
      Hesap No: \t{musteri1.hesapNumarasi}\n\
      
