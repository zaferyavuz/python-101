# 05_kiz.txt dosyasındaki kız isimlerini ve tersten yazımlarını listeler, en uzun ismi bulur
import codecs
dosya = codecs.open('kiz.txt', encoding='utf-8', mode='r')
isimler = dosya.readlines()
eb = 1
while anahtar != "-1" :
    for satir in isimler :
        kelimeler = satir.split(sep='\t')
        isim = kelimeler[0]
        if len(isim) > eb :
            eb = len(isim)
            eb_str = isim
        tersi = isim[::-1]
        print(isim,tersi,sep=',')
#print(eb_str)
dosya.close()
