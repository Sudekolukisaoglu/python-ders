sorular = [
    "Su yutmuş toprağa ne denir?",
    "Ağır suya ne denir?",
    "Ateş değil ama yanar,kanatları yok ama uçar,ayakları yok ama koşar",
    "Ramazan gelir sokaklarda dolaşır insanları onunla sahura kaldırırım.",
    "Derede tin tin, tepede tin tin, kemiksiz tin tin.",
    "Karşıdan baktım hiç yok, yanına vardım pek çok.",
    "",
    "",
]

cevaplar = [
    "Çamur",
    "Buz",
    "Güneş",
    "Davul",
    "Kelebek",
    "Karınca",
    "",
    "",
]    

def menu():
    print("\n"*5," *_* KOMİK BİLMECELER *_* ")
    print("     1- Bilmece sor       ")
    print("     2- Bilmece listesi   ")
    print("     3- Bilmece cevapları ")
    print("     4- Bilmece ekleme    ")
    print("     5- Bilmece silme     ")
    print("     Seciminiz?           ")

    secim = input()
    if secim == "1" : 
        pass 
    if secim == "2" :
        # print(sorular)
        print("\n\n Bilmece listesi: \n ════════════════════")
        # print(*sorular, sep="\n")
        sira = 1
        for xx in sorular:
            print (sira, "-", xx)
            sira +=1 
        
        menu()

    if secim == "3":
        print("\n\n Bilmece listesi: \n ════════════════════")
        sira = 1
        for xx in sorular:
            print (sira, "-", xx, " | Cevabı:", cevaplar[sira-1])
            sira +=1
        
        menu() 
    


menu()

