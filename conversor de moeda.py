real = float(input('Quantos reais voçê tem na sua conta? R$'))

dolar = real / 5.62
euro = real / 6.23

print('O seu dinheiro em R${:.2f}, vale US${:.2f} e €{:.2f}' .format(real,dolar,euro))
