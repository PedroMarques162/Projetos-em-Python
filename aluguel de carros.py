dias = int(input('Quantidades de dias alugados:'))
km = float(input('Quantidades de km rodados:'))
pago = (dias * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(pago))