from biblioteca import *


tipo_ligacao_resistores = raw_input('Tipo ligacao: ')

if tipo_ligacao_resistores == 'Paralelo':
	Req = paralelo(int(raw_input('Valor R1: ')),int(raw_input('Valor R2: ')))
	print Req
else:
	Req = serie(int(raw_input('Valor R1: ')),int(raw_input('Valor R2: ')))
	print Req

