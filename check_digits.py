'''
 * Gerador de referências por check digits
 * 
 * @param ent	  	entidade
 * @param ref_id 	7 primeiros digitos da referência
 * @param val	 	valor para pagamento
 *
'''

def generate_ref(ent, ref_id, val):
	weights = [3, 30, 9, 90, 27, 76, 81, 34, 49, 5, 50, 15, 53, 45, 62, 38, 89, 17, 73, 51];

	# obrigar a ter sempre duas casas decimais, ex para que 2.00 nao fique 2.0 mas sim 2.00
	val_display = '{0:.2f}'.format(val)
	# remover decimal e preencher com zeros a esquerda para que tenha 8 chars
	val_tmp = val_display.replace('.', '').zfill(8)

	if(not val_tmp.isnumeric() or 1  > val > 1000000):
		return {'error': 1, 'message': 'Valor a pagar inválido'}

	ctrl_num = '{}{}{}'.format(ent, ref_id, val_tmp)
	if(len(ctrl_num) != 20):
		return {'error': 1, 'message': 'comprimento do num de controlo errado'}

	prods = 0;
	for key, value in enumerate(reversed(weights)):
		prods += int(ctrl_num[key]) * value # // produto do num na posicao x pelo correspondente nos $weights revertido

	# obrigar a ter sempre dois digitos, colocar zero à esquerda se o resultado tiver apenas um digito
	check_digits = str(98-(prods%97)).zfill(2)
	ref = '{}{}'.format(ref_id, check_digits)
	return {'error': 0, 'message': {'ENT': ent, 'VAL': val_display.replace('.', ','), 'REF':  ref}}

ent = '90150';
ref_id = '1231234';
val = '432.11';
print(generate_ref(ent, ref_id, float(val))); # {'message': {'REF': '123123451', 'ENT': '90150', 'VAL': '432,11'}, 'error': 0}