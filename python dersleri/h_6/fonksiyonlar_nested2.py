import datetime
saat = int(datetime.datetime.now().strftime("%H"))

def selamla():
    def sabah():
        return "Günaydın"
    
    def ogle():
        return "İyi günler"
    
    print("Merhaba", sabah() if saat<9 else ogle())
   
selamla() 
