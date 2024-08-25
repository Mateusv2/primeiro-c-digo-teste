
valor = int(input('Digite qual a velocidade do veiculo em km/h:'))

if valor > 80:
    contagem = (valor - 80) * 20
    print(f'Valor a ser pago é de {contagem} reais.')
else:
    print('Sem multas a pagar')
    


