# çift fibonacci sayılarının toplamı (10000 den küçük)
i = 2; toplam = 2
f = 1; s = 1;
print(f,s,end=' ')
while i < 100 :
    f,s = s,(f+s)
    if i%2 == 0 :
        toplam += s
    if s > 100000 :
        break
    print(s,end=' ')
    i += 1
print("\nToplam :",toplam)
