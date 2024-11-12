import random

print("Rastgele güçlü şifre oluşturma programına hoş geldiniz!")
karakterler = [".","}","{","é",",",";","^",":","~","'","_","]","[","(",")","+","-","/","*","!","&","$","#","?","=","@","<",">","a","b","c","d","e","f","g","h","i","j","k","l","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]
uzunluk = input("Şifre uzunluğu kaç karakter olsun?: ")

if isinstance(uzunluk,str):
    uzunluk = len(uzunluk)
    print("Şifreniz girdiğiniz kelimenin uzunluğunda yazdırılacaktır")

sifre = ""

for i in range(uzunluk):
    rastgele_karakter = random.choice(karakterler)
    if rastgele_karakter in sifre:
        karakterler.remove(rastgele_karakter)
        sifre += random.choice(karakterler)

    else:
        sifre += rastgele_karakter
    
print(sifre)
