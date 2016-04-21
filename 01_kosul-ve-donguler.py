# 1000 sayısından küçük, 3 ve 5 in katları olan sayıların toplamı
i = 1; toplam = 0
while i < 1000 :
    if (i % 3 == 0) and (i % 5 == 0) :
       print(i,end='\n')
       toplam += i
    i += 1
print("Toplam",toplam,sep='=')
