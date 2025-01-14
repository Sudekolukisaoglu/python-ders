import time

def zamanlayici():
    print("Zamanlayıcı başlatıldı!")
    saniye = int(input("Kaç saniye süre istiyorsunuz? "))
    time.sleep(saniye)
    print(f"{saniye} saniye geçti!")
