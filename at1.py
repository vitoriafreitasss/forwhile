#Peça ao usuário uma palavra e conte quantas vogais ela contém.

palavra = input("digite uma palavra")
vogais = "aeiouAEIOU"
contar = 0 
 
for letra in palavra:
 if letra in vogais:

  contar +=1  # contar=contar+
print(f" numero de vogais {contar}")