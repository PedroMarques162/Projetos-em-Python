larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
área = larg * alt

print('A dimensão dessa parede de {}x{} tem uma área de {}m²'.format(larg,alt,área))

#Quantos litos de tintas seá usado para pintar uma área de 2m²?

tinta = área / 2

print('Para pintar essa parede voçê precisará de {}l de tinta'.format(tinta))