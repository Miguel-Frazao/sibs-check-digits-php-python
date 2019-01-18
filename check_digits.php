<?php
/**
 * Gerador de referências por check digits
 * 
 * @param $ent	  	entidade
 * @param $ref_id 	7 primeiros digitos da referência
 * @param $val	 	valor para pagamento
 *
 */
 
function generate_ref($ent, $ref_id, $val) {

	if(!is_numeric($val) || $val > 1000000 || $val < 1)
		return ['error' => 1, 'message' => 'Valor a pagar inválido'];

	$weights = [51,73,17,89,38,62,45,53,15,50,5,49,34,81,76,27,90,9,30,3,10,1];

	// remover decimal e preencher com zeros a esquerda para que tenha 8 chars
	$val_tmp = str_pad(number_format($val, 2, "", ""), 8, '0', STR_PAD_LEFT);

	$ctrl_num = $ent.$ref_id.$val_tmp; // concatenar os 3 parametros

	if(strlen($ctrl_num) != 20)
		return ['error' => 1, 'message' => 'comprimento do num de controlo errado'];

	$prods = 0;
	foreach (str_split($ctrl_num) as $key => $value) {
		$prods += $value*$weights[$key];
	}
	// obrigar a ter sempre dois digitos, colocar zero a esquerda se o resultado tiver apenas um digito
	$check_digits = str_pad(98-($prods%97), 2, '0', STR_PAD_LEFT);
	$ref = $ref_id.$check_digits;

	return ['error' => 0, 'message' => ['ENT' => $ent, 'VAL' => number_format($val, 2, ',', ''), 'REF' => $ref]];
}
$ent = '90150';
$ref_id = '1231234';
$val = 432.11;
print_r(generate_ref($ent, $ref_id, $val)); // Array ( [error] => 0 [message] => Array ( [ENT] => 90150 [VAL] => 432,11 [REF] => 123123451 ) )