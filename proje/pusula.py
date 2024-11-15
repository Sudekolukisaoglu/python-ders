import random

def pusula():
    # Yönler listesi
    yonler = ["Kuzey", "Güney", "Doğu", "Batı", "Kuzeydoğu", "Kuzeybatı", "Güneydoğu", "Güneybatı"]
    secilen_yon = random.choice(yonler)  # Rastgele bir yön seç
    print(f"Pusula yönü: {secilen_yon}")
