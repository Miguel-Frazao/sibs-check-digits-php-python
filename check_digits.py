'''
 * Gerador de referências por check digits
 * 
 * @param ent	  	entidade
 * @param ref_id 	7 primeiros digitos da referência
 * @param val	 	valor para pagamento
 *
'''

def generate_ref(ent, ref_id, val):
	weights = [51,73,17,89,38,62,45,53,15,50,5,49,34,81,76,27,90,9,30,3,10,1];

	# obrigar a ter sempre duas casas decimais, ex para que 2.00 nao fique 2.0 mas sim 2.00
	val = '{0:.2f}'.format(val)
	# remover decimal e preencher com zeros a esquerda para que tenha 8 chars
	val_tmp = val.replace('.', '').zfill(8)

	ctrl_num = '{}{}{}'.format(ent, ref_id, val_tmp)

	if(len(ctrl_num) != len(weights)-2):
		return False

	prods = 0;
	for key, value in enumerate(ctrl_num):
		prods += int(value) * weights[key]

	# obrigar a ter sempre dois digitos, colocar zero à esquerda se o resultado tiver apenas um digito
	check_digits = str(98-(prods%97)).zfill(2)
	ref = '{}{}'.format(ref_id, check_digits)
	return {'ENT': ent, 'VAL': val.replace('.', ','), 'REF':  ref}

ent = '90150';
ref_id = '1231234';
val = 432.11;
print(generate_ref(ent, ref_id, val)); # {'ENT': '90150', 'VAL': '432,11', 'REF': '123123451'}