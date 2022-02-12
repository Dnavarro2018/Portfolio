print('='*30)
print('Calculadora de Juros Compostos')
print('='*30)
#a formula de juros compostos se dá por Fv=Pv*(1+i)^n
pv = float(input('Insira o valor disponível para investimento: R$'))
i = float(input('Insira o total de juros por período(meses):'))
n = float(input('Insira o tempo que deseja investir o capital: '))
fv = pv * (1 + i/100) ** n
print('O valor R${:.2f} em {:.2f} meses acumulará para {:.2f}'.format(pv, n, fv))