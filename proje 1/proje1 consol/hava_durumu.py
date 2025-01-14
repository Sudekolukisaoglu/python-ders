import random

def kelime_bulmaca():
    kelimeler = ["python", "programlama", "yazılım", "bilgisayar", "kodlama"]
    kelime = random.choice(kelimeler)
    karisik_kelime = ''.join(random.sample(kelime, len(kelime)))
    
    print("Bulmacayı çözün: ", karisik_kelime)
    cevap = input("Cevabınızı girin: ")
    
    if cevap.lower() == kelime:
        print("Tebrikler, doğru cevabı buldunuz!")
    else:
        print(f"Yanlış cevap. Doğru cevap: {kelime}")
