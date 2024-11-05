def rehber_ekle():
    dosya = open("rehber.txt","a")
    print("\n\n Rehbere eklenecek bilgileri giriniz")
    ad = input("Ad : ")
    tel = input("Tel : ")
    dosya.write(f"{ad}#{tel}\n")
    dosya.close()
    print("\n\nRehberdekiler (yeni şekli):")
    rehber_listele()
def rehber_listele():
    print("\n\nRehberiniz:")
    dosya = open("rehber.txt")
    okunan = dosya.readlines()
    # print(okunan()
    # for a in okunan:
    for sira,a in enumerate(okunan):
        b = a.split("#")
        #  print(b[0],"\tTelefonu:",b[1])
        # print(sira+1," - ",b[0],"\t telefonu")
        print(f"{sira+1} - {b[0]},\t Telefonu: {b[1]}")

def rehber_sil():
    pass

def rehber_duzelt():
    pass        

def anamenu():
    print("╔═════════════════════╗")
    print("║ REHBER UYGULAMASI   ║")
    print("║═════════════════════║")
    print("║  1-Rehbere ekle     ║")
    print("║  2-Kişi Listesi     ║")
    print("║  3-Kişi düzenle     ║")
    print("║  4-Kişi silme       ║")
    print("║  5-Çıkış            ║")
    print("║                     ║")
    print("║  Seçimiz nedir?     ║")
    print("╚═════════════════════╝")
   
    secim = input()
    if secim == "1" : rehber_ekle(); anamenu()
    if secim == "2" : rehber_listele(); anamenu()
    if secim == "3" : rehber_duzelt(); anamenu()
    if secim == "4" : rehber_sil(); anamenu()
    if secim == "5" : rehber_ekle(); anamenu()

anamenu()    
