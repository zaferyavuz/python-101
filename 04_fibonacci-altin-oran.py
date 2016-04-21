# ardışıl fibonacci sayılarının altın oranı verdiğini gösteren örnek
i = 2; toplam = 2
f = 1; s = 1;
altin_oran = (1 + 5 ** 0.5) / 2
print('0','1','???',altin_oran,sep=' \t ',end='\n')
print('1','1','1',altin_oran,sep=' \t ',end='\n')
while i <= 50 :
    f,s = s,(f+s)
    oran = s/f
    print(i,s,oran,altin_oran,sep=' \t ',end='\n')
    i += 1
