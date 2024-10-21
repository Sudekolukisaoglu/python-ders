import turtle

def kare_ciz():
    kalem = turtle.Turtle()
    for _ in range(4):
        kalem.forward(100)
        kalem.right(90)
    turtle.done()

def ucgen_ciz():
    kalem = turtle.Turtle()
    for _ in range(3):
        kalem.forward(100)
        kalem.right(120)
    turtle.done()

def daire_ciz():
    kalem = turtle.Turtle()
    kalem.circle(100)
    turtle.done()

def ciz():
    print("Çizimler: ")
    print("1. Kare çiz")
    print("2. Üçgen çiz")
    print("3. Daire çiz")
    
    secim = input("Bir şekil seçin (1/2/3): ")

    if secim == '1':
        kare_ciz()
    elif secim == '2':
        ucgen_ciz()
    elif secim == '3':
        daire_ciz()
    else:
        print("Geçersiz bir seçim yaptınız.")
