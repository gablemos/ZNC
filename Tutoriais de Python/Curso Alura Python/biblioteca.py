def gera_nome_convite(nome):
	parte2 = len(nome)	
	parte1 = len(nome) - 4
	return  nome[:3] + ' ' + nome[parte1:parte2]

def envia_convite(nome):
	print 'Enviando convite para %s' %(nome)

def processa_convite(nome):
	return envia_convite(gera_nome_convite(nome))

def paralelo(r1,r2):
	return ((r1*r2)/(r1+r2))

def serie(r1,r2):
	return r1+r2
