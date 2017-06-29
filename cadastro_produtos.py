#Inicializando um dicionario.
lista_produto = {}

class Calculos(object):
	
	""" classe responsavel em fazer os calculos de maior valor, menor valor, media aritimetica e o preço mais frequente """
	def __init__(self, preco):
		
		""" Metodo construtor que ira receber um argumento de preço """
		self.preco = preco
		
	def maiorP(self):
		
		""" Metodo responsavel em encontrar maior preço entre todos os produtos """
		mpreco = max(lista_produto, key=lista_produto.get)
		return lista_produto[mpreco]
		
	def menorP(self):
		
		""" Metodo responsavel em encontrar menor preço entre todos os produtos """
		mpreco = min(lista_produto, key=lista_produto.get)
		return lista_produto[mpreco]
		
	def mediaAri(self):
		
		""" Metodo responsavel de realizar a media aritimetrica entre os preços dos produtos """
		divisor = len(lista_produto)
		soma = 0
		for x in lista_produto:
			soma += lista_produto[x]
		resultado = soma/divisor	
		return resultado
		
	def precoF(self):
		
		""" Metodo responsavel em encontrar o preço que se repete mais vezes entre os produtos """
		lista = []
		nvd = {}
		for x in lista_produto:
			lista.append(lista_produto[x])
			
		for x in lista:
			contador = lista.count(x)
			nvd[x] = contador
			maxi = max(nvd, key=nvd.get)
		return maxi
		
print ("Quetão 2º")

#Repetição do menu até que a opção "C" seja escolhida.	
while (True):
	print ("")
	print ("Menu - Escolha uma ação:")
	print ("(A) Cadastrar Produto")
	print ("(B) Visualzar Produtos")
	print ("(C) Sair")
	escolha = input()
	
	#Opção "A" - realiza o cadastro do codigo e preço do produto.
	if (escolha == "A"):
		print ("Informe o Codigo do produto:")
		#Caso o codigo inserido não seja um numero inteiro, essa exceção tratara dele.
		try:
			codigo = int(input())
		except ValueError:
			print ("Por favor informe um numero inteiro!\n")
			continue
		#Validando se o produto ja esta cadastrado.
		if (codigo in lista_produto):
			print ("Produto ja cadastrado, insira um novo codigo")
			continue
			
		print ("Informe o preço do produto (Ex: 2.50):")
		preco = float(input())
		
		#Inserindo o codigo e preço do produto em um dicionario.
		lista_produto[codigo] = preco
		
		#cria o objeto calcpreco passando apenas preco como argumento.
		calcpreco = Calculos(preco)
	
	#Opção "B" - Retorna as informações do objeto calcpreco.
	elif(escolha == "B"):
		
		#Validando se existem produtos cadastrados no dicionario.
		if (lista_produto == {}):
			print ("Nenhuma produto cadatrado")
			
		#Caso tenhamos produtos cadastrados, exibimos suas informações.
		else:
			print ("=====================================")
			#For para exibição de todos os produtos Cadastrado.
			for x in lista_produto:
				print("Codigo do produto: [%s] Preço: R$ %0.2f" % (x, lista_produto[x]))
			print ("")
			print ("Maior preço: R$ %0.2f" % (calcpreco.maiorP()))
			print ("Menor preço: R$ %0.2f" % (calcpreco.menorP()))
			print ("Media de preço: R$ %0.2f" % (calcpreco.mediaAri()))
			print ("Preço com maior frequência: R$ %0.2f" % (calcpreco.precoF()))
			print ("=====================================")
			
	#Opção "C" - Retorna uma mensagem e encerra o While, finalizando o programa.	
	elif(escolha == "C"):
		print ("Volte sempre!")
		break

#desenvolvido por @jmateusousa
#email: contato.matthewd@gmail.com
