import hesapmakinesi
import oyunlar
import çizimler

print("\033[1;32;40m")
#print("╔"+"═"*20+"╗")
print("╔═════════════════════╗")
print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
print("║                     ║")
print("║  1-hesap makinesi   ║")
print("║  2-oyunlar          ║")
print("║  3-çizimler         ║")
print("║  4-ritmik sayma     ║")
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
     ritmiksayma = []  

