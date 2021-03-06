'''
 * Gerador de referências por check digits
 * 
 * @param ent	  	entidade
 * @param ref_id 	7 primeiros digitos da referência
 * @param val	 	valor para pagamento
 *
'''

def generate_ref(ent, ref_id, val):

	weights = [51, 73, 17, 89, 38, 62, 45, 53, 15, 50, 5, 49, 34, 81, 76, 27, 90, 9, 30, 3]

	# obrigar a ter sempre duas casas decimais, ex para que 2.00 nao fique 2.0 mas sim 2.00
	val_display = '{:.2f}'.format(val)
	# remover decimal e preencher com zeros à esquerda para que tenha 8 chars
	val_tmp = val_display.replace('.', '').zfill(8)
	if(not val_tmp.isnumeric() or not 1 < val < 99999.99):
		return {'error': 1, 'message': 'Valor a pagar inválido'}

	base_num = '{}{}{}'.format(ent, ref_id, val_tmp)
	if(len(base_num) != 20):
		return {'error': 1, 'message': 'comprimento do num base errado'}

	prods = 0
	for val1, val2 in zip(weights, map(int, base_num)): # generator com [(51, 9), (73, 0), (17, 1), (89, 5), (38, 0), ....]
		prods += val1 * val2 # // produto do num na posicao x pelo correspondente nos weights

	# obrigar a ter sempre dois digitos, colocar zero à esquerda se o resultado tiver apenas um dígito
	check_digits = str(98-(prods%97)).zfill(2)
	ref = '{}{}'.format(ref_id, check_digits)
	return {'error': 0, 'message': {'ENT': ent, 'VAL': val_display.replace('.', ','), 'REF':  ref}}

ent = '90150'
ref_id = '1231234'
val = 432.11
print(generate_ref(ent, ref_id, float(val))) # {'message': {'REF': '123123451', 'ENT': '90150', 'VAL': '432,11'}, 'error': 0}