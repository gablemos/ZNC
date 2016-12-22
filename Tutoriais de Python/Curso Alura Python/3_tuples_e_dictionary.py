#coding:UTF-8
#Tupla ou Tuple é uma lista imutavel

'''
	estacoes_do_ano = ('Verao','outono','inverno','primavera')

	print estacoes_do_ano
	print estacoes_do_ano[1]
	print estacoes_do_ano[:3]
	print estacoes_do_ano[1:1]

	estacoes_do_ano += ('outono/interno', 'primavera/verao',)
	print estacoes_do_ano

'''
'''

	#dictionary é um array onde cada chave possui um valor

	boletim = {'Gabriel' : 7.0, 'Ana' : 8.3, 'Julia' : 3.5}
	print boletim


	print boletim.keys()
	print boletim.values()





	pessoas = ['Ana','Carol','Marcela']
	del pessoas[1]
	print pessoas

	pessoas += ['Camila','Clarice']
	print pessoas

	estados_list_com_tumple = ('RJ', 'SP') + tuple(['MG', 'ES'])
	print estados

	estados_tumple_com_list = ['MG','ES'] + list(('RJ', 'SP'))
	print estados

'''

#list []
#tuple ()
#dictionary {key:value,}

lista = [2,4,8,16,32,64]
print max(lista)

tupla = ((1,2,3,7,11,13,17))
print min(tupla)

chamada = ['PT','PSDB','PSOL','PMDB','PCdoB','PA']
print sorted(chamada)


materias_com_peso = {'Equações Diofantinas' : 3, 'Álgebra Relacional' : 2, 'Português instrumental' : 4}
pesos = tuple(materias_com_peso.values())
print pesos