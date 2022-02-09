print('Escolha o(a) Guerreiro(a) para enfrentar o DRAGÃO!!!')
personagem = input('Digite -> C para Cavaleiro(a), M para Mago(a) ou A para Arqueiro(a): ')


while personagem != 'C' and personagem != 'M' and personagem != 'A':
    personagem = input('Digite -> C para Cavaleiro(a), M para Mago(a) ou A para Arqueiro(A): ')

print()
if personagem == 'C':
    print('Pelo poder das LÂMINAS!!!')
elif personagem == 'M':
    print('Pelo poder da LUZ!!!')
elif personagem == 'A':
    print('Pelo poder dos VENTOS!!!')

print()
print('Escolha, sabiamente, a sua arma para enfrentar o DRAGÃO e selar o seu destino!!!')
arma = input('Digite -> E para Espada, J para Cajado ou R para Arco: ')

if arma != 'E' and arma != 'J' and arma != 'R':
    print('GAME OVER: não escolheu sabiamente e virou churrasquinho de DRAGÃO. Um verdadeiro guerreiro está atento aos detalhes!')

##      DESTINO DO CAVALEIRO(A)
print()
if personagem == 'C' and arma == 'E':
    print('VENCEU: a verdade da espada concede a força necessária para vencer um dragão! YHAAAAA')
elif personagem == 'C' and arma =='R':
    print('MORREU: um arco depois de encher a cara na taverna?')
while personagem == 'C' and arma == 'J': #loopInfinito
    print('A guilda dos cavaleiros não se dá bem com magia. Bem-vindo ao vazio infinito!')

##      DESTINO MAGO(A)
print()
if personagem == 'M' and arma == 'E':
    print('MORREU: magia e aço é uma combinação perigosa. Um raio acertou a espada e fez Mago(a) frito(a).')
elif personagem == 'M' and arma == 'J':
    print('VENCEU: o poder da luz sempre prevalece sobre as trevas!')
while personagem == 'M' and arma =='R': #loopInfinito
    print('FUGIU: um portal mal feito te leva para a eternidade.')

##      DESTINO ARQUEIRO(A)
print()
if personagem == 'A' and arma == 'R':
    print('VENCEU: o coração é a parte fundamental da vida, seja ela maldosa ou bondosa. Um tiro certeiro!')
elif personagem == 'A' and arma == 'E':
    print('MORREU: você pagou com a vida para aprender que não se usa um arco para atirar uma espada!')
while personagem == 'A' and arma =='J': #loopInfinito
    print('Um portal se abre para a morte eterna. Bem-vindo à agonia do infinito')