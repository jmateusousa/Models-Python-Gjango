# Code Python
Exemplos de codificação em Python, Django e outras utilidades desta podera linguagem de programação.

LIS = []
LISr = [] 
ct = 0
unicos= []
print ("Questão 3°\n")

while(ct < 10):
	print("Digite um numero:")
	numero = input()
	LIS.append(numero)
	ct += 1

print ("")
for x in LIS:
	contador = LIS.count(x)
	if (contador > 1):
		LISr.append(x)
		unicos = list(set(LISr))

if (unicos == []):
	print ("Nenhum numero repetido")
else:	
	print ("Numero repetidos: %s\n" % unicos)

for indice, x in enumerate(LIS):
	contador = LIS.count(x)
	if (contador > 1):
		print ("Indice: %s Numero: %s" % (indice, x ))
		
