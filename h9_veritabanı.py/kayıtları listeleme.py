import mysql.connector
try:

    vts = mysql.connector.connect(host="localhost",user="root",password="1234",
    database="deneme1"
    ); print("Bağlantı tamam:")
    secilen = vts.cursor()
    alinan_liste = secilen.execute("select * from ogrenciler")
    # xxx = secilen.fetchone() # fetchone ile sadece bir kayıt alınır
    xxx = secilen.fetchall()
    # print(xxx)
    for a in xxx:
        print(a)


except:
    print("Veritabanına bağlanırken bir hata oluştu.")


