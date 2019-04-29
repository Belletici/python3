import sqlite3
vt=sqlite3.connect("veriler.db")
im=vt.cursor()

def TabloOlustur():
    im.execute("CREATE TABLE IF NOT EXISTS çalışan(adsoyad TEXT, pozisyon TEXT, maas INT)")
    vt.commit()
def VeriEkle(adsoyad,pozisyon,maas):
    im.execute("INSERT INTO çalışan VALUES (?,?,?)",(adsoyad,pozisyon,maas))
    vt.commit()
def VeriGuncelle(maas,yenimaas):
    im.execute("UPDATE çalışan SET maas= ? WHERE  maas= ?",(yenimaas,maas))
    vt.commit()
def VeriSil(silinen):
    im.execute("DELETE FROM çalışan WHERE adsoyad = ?",(silinen,))
    vt.commit()
def VeriGoster():
    im.execute("SELECT * FROM çalışan")
    for i in im.fetchall():
        print(i)

# TabloOlustur()
print("***************veri girme ekranı*************")

while True:
    secim=input("""
    Veri girmek için herhangi bir tuşa,
    Veri silmek için (s), liste için (l)
    Maaş Güncellemesi için (g) ye basınız:
    Çıkmak için ise (q) ya basınız,""")


    if secim == "q":
        break
    elif secim=="g":
        maas=int(input("Eski Maaş: "))
        yenimaas=int(input("Yeni Maaş: "))
        VeriGuncelle(maas,yenimaas)
        print("Maaş Güncellendi...")
        print("****************")
        continue
    elif secim=="s":
        silinen=input("Silinecek Kişi İsmi: ")
        VeriSil(silinen)
        print(silinen," Silindi.....")
        print("Yeni Liste:")
        VeriGoster()
        continue
    elif secim=="l":
        VeriGoster()
        print("****************")
        continue

    v1=input("Ad Soyad: ")
    v2=input("Pozisyon: ")
    v3=int(input("Maaş: "))

    VeriEkle(v1,v2,v3)
    print("Veri eklendi,veriler:")
    VeriGoster()
    print("****************")





