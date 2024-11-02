import random

meme_dict = {
            "LOL" : "komik bir şeye verilen cevap",
            "CRINGE" : "garip ya da utandırıcı bir şey",
            "ROFL" : "bir şakaya karşılık cevap",
            "SHEESH" : "onaylamamak",
            "CREEPY" : "korkunç",
            "AGGRO":  "agresifleşmek/sinirlenmek"
            }

memes = ["LOL","CRINGE","ROFL","SHEESH","CREEPY","AGGRO"]

print(memes)
print(" ")
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print( meme_dict[word])
else:
    print("Yazdığınız kelime sözlükte bulunmamakta lütfen tekrar deneyin")
