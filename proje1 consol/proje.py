import hesapmakinesi
import oyunlar
import çizimler
import ritmiksayma
import çarpımtablosu
import nothesaplama
import hava_durumu 

print("\033[1;32;40m")
#print("╔"+"═"*20+"╗")
print("╔═════════════════════╗")
print("║\033[1;31;40m   öncüller app  \033[1;32;40m  ║")
print("║                     ║")
print("║  1-hesap makinesi   ║")
print("║  2-oyunlar          ║")
print("║  3-çizimler         ║")
print("║  4-ritmik sayma     ║")
print("║  5-çarpım tablosu   ║")
print("║  6-not hesaplama    ║")
print("║  7-hava durumu      ║") 
print("║                     ║")
print("║    Seçimiz nedir?   ║")
print("╚═════════════════════╝")

secim = input()

if secim == '1':
    hesapmakinesi.hesap_makinesi()  
elif secim == '2':
    oyunlar.oyun_oyna()  
elif secim == '3':
    çizimler.çiz() 
elif secim =='4':
    ritmiksayma.ritmik_sayma()
elif secim =='5':
    çarpımtablosu.çarpım_tablosu()
elif secim =='6':
    nothesaplama.not_hesapla() 
if secim == '7':
    hava_durumu.hava_durumu()




