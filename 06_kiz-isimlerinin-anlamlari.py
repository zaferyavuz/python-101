# 05_kiz.txt dosyasındaki kız isimlerini açıklamalarını yazar, sözlük benzeri
import codecs
dosya = codecs.open('05_kiz.txt', encoding='utf-8', mode='r')
isimler = dosya.readlines()
anahtar = " "
while anahtar != "-1" :
    anahtar = input("Kelime : ")
    if anahtar == "-1" :
        break
    for satir in isimler :
        #print(satir)
        kelimeler = satir.split(sep='\t')
        isim = kelimeler[0]
        aciklama = kelimeler[1]
        if (anahtar == isim) :
            print(isim,aciklama,sep='=')

dosya.close()
