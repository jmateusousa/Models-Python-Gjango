#Inicializando um dicionario.
lista_alunos = {}

class Controle(object):
	""" Classe responsavel em calcular a media dos alunos """
	def __init__(self, nome, n1, n2 ,n3, n4):
		self.nome = nome
		self.n1 = n1
		self.n2 = n2
		self.n3 = n3
		self.n4 = n4
	def media(self):
		
		""" Metodo responsavel em calcular e retonar a media dos alunos """
		med = (self.n1 + self.n2 + self.n3 + self.n4) / 4
		lista_alunos[self.nome] = med
		return med
		
print ("Quetão 1º")
#Repetição do menu até que a opção "C" seja escolhida.
while (True):
	print ("")
	print ("Menu - Escolha uma ação:")
	print ("(A) Cadastrar avaliações")
	print ("(B) Visualzar resultados")
	print ("(C) Sair")
	escolha = input()
	
	#Opção "A" - realiza o cadastro das notas de cada aluno.
	if (escolha == "A"):
		print ("Informe o nome do aluno:")
		nome = input()
		#Validando se o aluno ja esta cadastrado.
		if (nome in lista_alunos):
			print ("Avaliação ja cadastrado para este aluno")
			continue
		print ("Informe a 1° nota:")
		n1 = float(input())
		print ("Informe a 2° nota:")
		n2 = float(input())
		print ("Informe a 3° nota:")
		n3 = float(input())
		print ("Informe a 4° nota:")
		n4 = float(input())
		
		#Cria o objeto aluno.
		aluno = Controle(nome,n1,n2,n3,n4)
		print ("Media de %s é %0.1f" % (nome, aluno.media()))
		
	#Opção "B" - Retorna as informações das avaliações de cada aluno.	
	elif(escolha == "B"):
		#Validando se existem alunos/avaliações cadastradas no dicionario.
		if (lista_alunos == {}):
			print ("Nenhuma avaliação cadatrada")
		else:
			print ("================================================")	
			for x in lista_alunos:
				#Regras de avaliação.
				if (lista_alunos[x] >= 7.0):
					print ("Aluno %s foi aprovado com media: %0.1f" % (x, lista_alunos[x]))
				elif (lista_alunos[x] < 4.0):
					print ("Aluno %s foi reprovado pois obteve media: %0.1f" % (x, lista_alunos[x]))
				elif (4.0 <= lista_alunos[x] < 7.0):
					print ("Aluno %s esta na prova final pois obteve media: %0.1f" % (x, lista_alunos[x]))
			print ("================================================")
				
	#Opção "C" - Retorna uma mensagem e encerra o While, finalizando o programa.				
	elif(escolha == "C"):
		print ("Volte sempre!")
		break

#criado por @jmateusousa
#email: contato.matthewd@gmail.com
