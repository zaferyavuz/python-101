# en büyük asal çarpamı bulmak (72 için 3)
def is_prime(sayi) :
    i = 2; asal = 1
    while i*i <= sayi :
        if sayi%i == 0 :
            asal = 0
            break
        i+=1
    return asal
​
n = int(input("Sayı : "))
i = 1; eb = 1
while 2*i <= n :
    if n%i == 0 and i > eb and is_prime(i) == 1 :
        eb = i
    i+=1
print(n,"sayısının en büyük asal çarpanı :",eb)
