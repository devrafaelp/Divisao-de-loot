from time import sleep
print(' == DIVISOR DE LOOT PARTY 4X ==')
total = int(input('Digite o balance total da hunt: '))
print('ANALISANDO O BALANCE...')
sleep(3)
gastoms = int(input('Insira o gasto do MS: '))
print('O gasto do MS foi de {}'.format(gastoms))
gastoek = int(input('Insira o gasto do EK: '))
print('O gasto do EK foi de {}'.format(gastoek))
gastoed = int(input('Insira o gasto do ED: '))
print('O gasto do ED foi de {}'.format(gastoed))
gastorp = int(input('Insira o gasto do RP: '))
print('O gasto do RP foi de {}'.format(gastorp))
gastototal= gastoms + gastoek + gastoed + gastorp
profit = total - gastototal
print('ANALISANDO GASTO TOTAL....')
sleep(2)
print('O total de loot foi de {}'.format(total))
print('A Hunt deu um profit de {} '.format(profit))
print('{} dividido por 4 é igual a {} pra cada'.format(profit, profit / 4))
print('MS gastou {}, então recebe {}'.format(gastoms, profit / 4 + gastoms))
print('EK gastou {}, então recebe {}'.format(gastoek, profit / 4 + gastoek))
print('ED gastou {}, então recebe {}'.format(gastoed, profit / 4 + gastoed))
print('RP gastou {}, então recebe {}'.format(gastorp, profit / 4 + gastorp))
if gastoms > 100:
    print('Ms gastao do kraio, sai da minha pt')
else:
    print('MS economico Xd')
print('Fim, obrigado por me usar {}!')
