from random import randint

i = 0
r = 0
numeros = []
escolha = 0
qtd_numeros = 0

while escolha != 4:
	
	print ("Escolha um jogo.")
	print ("(1) Mega Sena")
	print ("(2) Loto Mania")
	print ("(3) Loto Facil")
	print ("(4) Sair")	
	escolha = int(input())
	if escolha == 1:
		
		print ("Quantos numeros você vai apostar?")
		print ("[6] - [7] - [8] - [9] - [10] - [11] - [12] - [13] - [14] ou [15]")
		qtd_numeros = int(input())
		if qtd_numeros in range(6,16):
			while i != qtd_numeros:
				while len(numeros) != qtd_numeros:
					r = randint(1, 60)
					if r not in numeros:
						numeros.append(r)
						i += 1
			numeros.sort()
			print ("Os numeros da mega sena são: ", numeros, "\n")
		else:
			print ("Escolha uma quantidade entre 6 a 15 numeros.\n")
		
	elif escolha == 2:
		
		while i != 50:
			numeros.append(randint(0,99))
			i += 1
		numeros.sort()	
		print ("Os numeros da Loto Mania são: ", numeros)
		
	elif escolha == 3:
		print ("Quantos numeros você vai apostar?")
		print ("[15] - [16] - [17] ou [18]")
		qtd_numeros = int(input())
		if qtd_numeros in range(15,19):
			while i != qtd_numeros:
				while len(numeros) != qtd_numeros:
					r = randint(1, 25)
					if r not in numeros:
						numeros.append(r)
						i += 1
			numeros.sort()
			print ("Os numeros da Loto Mania são: ", numeros)
		else:
			print ("Escolha uma quantidade entre 15 a 18 numeros.\n")
	else: 
		print ("Boa Sorte!")
		break;
