def fonksiyon1():
    yield "Hello"
    yield 51
    yield "Good Bye"

x = fonksiyon1()

print(x)

for z in x:
    print(z)