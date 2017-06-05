palavra = input("Escreva uma palavra: ")
palavra = palavra.isalpha()
if palavra = True:
    priseg = palavra[0,1]
    traducao = palavra[2:] + priseg
    print traducao
else:   
    print "Isso não é uma palavra"