LIS = []
LISr = [] 
unicos= []
ct = 0
print ("Questão 3°\n")

# repetição do menu até que sejam fornecidos 50 numeros.
while(ct < 50):
	print("Digite um numero:")
	numero = input()
	LIS.append(numero)
	ct += 1

# Verificação de quais numeros foram inseridos de forma repetida.
print ("")
for x in LIS:
	contador = LIS.count(x)
	if (contador > 1):
		LISr.append(x)
		unicos = list(set(LISr))
		
#Mostra quais numeros foram repetidos.
if (unicos == []):
	print ("Nenhum numero repetido")
else:	
	print ("Numero repetidos: %s\n" % unicos)

#mostra o numero e qual o indice ele foi inserido dentro da lista LIS.
for indice, x in enumerate(LIS):
	contador = LIS.count(x)
	if (contador > 1):
		print ("Indice: %s Numero: %s" % (indice, x ))
		
#desenvolvido por @jmateusousa
#email: contato.matthewd@gmail.com
