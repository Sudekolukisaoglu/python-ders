import turtle

def kare_çiz():
    kalem = turtle.Turtle()
    for _ in range(4):
        kalem.forward(100)
        kalem.right(90)
    turtle.done()

def ucgen_çiz():
    kalem = turtle.Turtle()
    for _ in range(3):
        kalem.forward(100)
        kalem.right(120)
    turtle.done()

def daire_çiz():
    kalem = turtle.Turtle()
    kalem.circle(100)
    turtle.done()

def çiz():
    print("Çizimler: ")
    print("1. Kare çiz")
    print("2. Üçgen çiz")
    print("3. Daire çiz")
    
    secim = input("Bir şekil seçin (1/2/3): ")

    if secim == '1':
        kare_çiz()
    elif secim == '2':
        ucgen_çiz()
    elif secim == '3':
        daire_çiz()
    else:
        print("Geçersiz bir seçim yaptınız.")
