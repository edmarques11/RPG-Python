from random import choice
import os

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def secret_box(carteira):
  itens_da_caixa = [50,-10,40,-20,30,-30,20,-40,10,-50,0]
  sorte = choice(itens_da_caixa)
  if carteira + sorte > 0:
      if sorte > 0:
          carteira = carteira+sorte
          print('Você ganhou R$ %d'%sorte)
      elif sorte == 0:
          print('Perda de tempo!')
      else:
          print('Você foi assaltado em R$ %d'%sorte)
          carteira += sorte
  return carteira
  


def gato():
  acoes_do_bicho = ['ignorar','morder']
  bicho_faz = choice(acoes_do_bicho)
  if bicho_faz == 'morder':
    print('O gato te mordeu e você voltou ao inicio!')
    return True
  else:
    print('Por sorte o gato te ignorou')
    return False



locais = {
	1 : {
		'nome' : 'ENTRADA',
		'sul' : 4,
		'leste' : 2,
    'oeste' : 5,
	},
	2 : {
		'nome' : 'LABORATÓRIO DE INFORMÁTICA',
		'norte' : 8,
    'oeste' : 1,
    'sul' : 3,
    'iem' : 'gato'
	},
	3 : {
		'nome' : 'LANCHONETE',
		'norte' : 2,
    'oeste' : 4,
		'item'  : 'pimenta'        
	},

	4 : {
		'nome' : 'PATIO',
		'norte' : 1,
    'leste' : 3,
    'oeste' : 6,
    'sul' : 10,
    'item' : 'gato'
	},

	5 : {
		'nome' : 'DIREÇÃO',
    'leste' : 1,
    'sul' : 6,
    'item' : 'caixa secreta'
	},

	6 : {
		'nome' : 'BIBLIOTECA',
		'norte' : 5,
    'leste' : 4,
    'oeste' : 7,
    'sul' : 11,
    'item' : 'caixa secreta'

	},

	7 : {
		'nome' : 'BANHEIRO',
    'leste' : 6,
    'sul' : 12,  
		'item'  : 'rosca'

	},

	8 : {
		'nome' : 'SALA  DOS PROFESSORES',
    'leste' : 9,
    'sul' : 2

	},

	9 : {
		'nome' : 'GARAGEM',
    'oeste' : 8,
    'item' : 'caixa secreta'
    
	},
	10 : {
		'nome' : 'SALA DE AULA',
    'norte' : 4,
    'oeste' : 11,
    'sul' : 15

	},

	11 : {
		'nome' : 'SALA DA NUTRICIONISTA',
    'norte' : 6,
    'leste' : 10,
    'oeste' : 12,
    'sul' : 14,
		'item' : 'nutricionista'

	},

	12 : {
		'nome' : 'REFEITÓTIO',
    'norte' : 7,
    'leste' : 11,
    'sul' : 13

	},

	13 : {
		'nome' : 'SALA DE JOGOS',
    'norte' : 12,
    'leste' : 14

	},

	14 : {
		'nome' : 'MAMBEE',
    'norte' : 11,
    'leste' : 15,
    'oeste' : 13,
		'item' : 'gato'

	},
	15 : {
		'nome' : 'SALA 2',
    'norte' : 10,
    'oeste' : 14,

	},
}


print ("")
print('             ||||||||||||||||||||||||||||||||||||||||||||||||||||||')
print("             ||||     ESSE JOGO FOI BASEADO EM FATOS REAIS     ||||") 
print('             ||||||||||||||||||||||||||||||||||||||||||||||||||||||')
print('')
print('')
print('')
print('')
print('HISTÓRIA')
print('APÓS ANOS DE PESQUISA ARQUEÓLOGOS CONSEGUIRAM A FORMULA SECRETA PARA O ELIXIR DA VIDA ')
print("               QUE ESTAVA ESCONDIDA NAS ANTIGAS PIRÂMIDES DO EGITO")
print("")
print('A PIMENTA!')
print("")
print("")
print('MAS UM SER DE GRANDE MALDADE NO CORAÇÃO NÃO GOSTAVA DOS PODERES QUE A PIMENTA PROPORCIONAVA AOS MORTAIS')
print("ENTÃO ESSE MOSTRO CHAMADO DE *NUTRICIONISTA* ROUBOU A PIMENTA E À DEIXOU ESCONDIDA EM UM LABIRINTO SEM LUZ")
print("")
print("")
print("POREM EXISTE UMA PROFECIA DE QUE UM(A) BRAVO(A) GUERREIRO(A) IRÁ RECUPERAR A PIMENTA ")
print("        E TRAZER PAZ MAIS UMA VEZ PARA TODAS AS BARRIGAS DOS PIMENTEIROs")
print("")
print("")
print(     "SEJA ESSE HERÓI, RECUPERE A PIMENTA E SALVE A HUMANIDADE!")
print("MAS CUIDADO! VOCÊ NÃO PODE SER PEGO(A) PELA TEERIVÉL *NUTRICIONISTA*")
print("")
print("")
print('Pressione enter para iniciar!\n')
a = str(input(""))
clear()


print( )
print('=' * 30)
#print('\033[42m'+'\033[1m'+'\033[33m'+''=' * 30'+'\033[0;0m')
print( )

#########################################################
print('\033[31m'+'██████████ Jogo de RPG ██████████'+'\033[0;0m')
print('=' * 30)
print( )
print('\033[32m'+'ir [direcao]'+'\033[0;0m')
print('\033[32m'+'pegar [item]'+'\033[0;0m')
print( )
print('=' * 30)
#print('\033[42;1;33m'+''=' * 30 '+'\033[0;0m')
print('\033[31m'+'Direções: Norte, Sul, Leste, Oeste'+'\033[0;0m')
print('=' * 30)
#print('\033[42;1;33m'+''=' * 30 '+'\033[0;0m')
print( )
print('\033[32m'+'Itens: Pimenta, Rosca, caixa secretas e gato'+'\033[0;0m')
print( )
print('\033[32m'+' Sua missão é pegar a Pimenta na Lanchonete,\n a Rosca no banheiro\n e chegar ao refeitório sem passar pela nutricionista,\n mas cuidado ao se deparar com um gato pelo campus.'+'\033[0;0m')
print( )
print('\033[32m'+' Você também pode encontrar dinheiro nas\n caixas secretas e subornar a nutricionista,\n caso tenha 50 reais, mas cuidado\n que você também pode ser assaltado\n fazendo com que não aconteça um suborno. '+'\033[0;0m')
print( )
print('=' * 30)
#print('\033[42m'+'\033[1m'+'\033[33m'+''=' * 30'+'\033[0;0m')
print( )
print('-'*40)
###########################################################

posicao_atual = locais[1]
inventario = []
carteira = 0
while(True):
  '''print('\033[31m'+'██████████ Jogo de RPG ██████████'+'\033[0;0m')
  print('=' * 30)
  print( )
  print('\033[32m'+'ir [direcao]'+'\033[0;0m')
  print('\033[32m'+'pegar [item]'+'\033[0;0m')
  print( )
  print('=' * 30)
  #print('\033[42;1;33m'+''=' * 30 '+'\033[0;0m')
  print('\033[31m'+'Direções: Norte, Sul, Leste, Oeste'+'\033[0;0m')
  print('=' * 30)
  #print('\033[42;1;33m'+''=' * 30 '+'\033[0;0m')
  print( )
  print('\033[32m'+'Itens: Pimenta, Rosca, caixa secretas e gato'+'\033[0;0m')
  print( )
  print('\033[32m'+' Sua missão é pegar a Pimenta na Lanchonete,\n a Rosca no banheiro\n e chegar ao refeitório sem passar pela nutricionista,\n mas cuidado ao se deparar com um gato pelo campus.'+'\033[0;0m')
  print( )
  print('\033[32m'+' Você também pode encontrar dinheiro nas\n caixas secretas e subornar a nutricionista,\n caso tenha 50 reais, mas cuidado\n que você também pode ser assaltado\n fazendo com que não aconteça um suborno. '+'\033[0;0m')
  print( )
  print('=' * 30)
  #print('\033[42m'+'\033[1m'+'\033[33m'+''=' * 30'+'\033[0;0m')
  print( )
  print('-'*40)'''
  print('>>>>> Você está no(a) {}'.format(posicao_atual['nome']))
  print('Inventário',inventario)
  print('Você tem R$ %d'%carteira)
  print('-'*40)
  entrada = input('> ').lower().split(' ')
  comando = entrada[0]
  clear()

######################################################
  print('\033[31m'+'██████████ Jogo de RPG ██████████'+'\033[0;0m')
  print('=' * 30)
  print( )
  print('\033[32m'+'ir [direcao]'+'\033[0;0m')
  print('\033[32m'+'pegar [item]'+'\033[0;0m')
  print( )
  print('=' * 30)
  #print('\033[42;1;33m'+''=' * 30 '+'\033[0;0m')
  print('\033[31m'+'Direções: Norte, Sul, Leste, Oeste'+'\033[0;0m')
  print('=' * 30)
  #print('\033[42;1;33m'+''=' * 30 '+'\033[0;0m')
  print( )
  print('\033[32m'+'Itens: Pimenta, Rosca, caixa secretas e gato'+'\033[0;0m')
  print( )
  print('\033[32m'+' Sua missão é pegar a Pimenta na Lanchonete,\n a Rosca no banheiro\n e chegar ao refeitório sem passar pela nutricionista,\n mas cuidado ao se deparar com um gato pelo campus.'+'\033[0;0m')
  print( )
  print('\033[32m'+' Você também pode encontrar dinheiro nas\n caixas secretas e subornar a nutricionista,\n caso tenha 50 reais, mas cuidado\n que você também pode ser assaltado\n fazendo com que não aconteça um suborno. '+'\033[0;0m')
  print( )
  print('=' * 30)
  #print('\033[42m'+'\033[1m'+'\033[33m'+''=' * 30'+'\033[0;0m')
  print( )
  print('-'*40)
##################################################################

  if comando == 'ir':
    direcao = entrada[1]
    if direcao in posicao_atual.keys():
      proximo_local = posicao_atual[direcao]			
      posicao_atual = locais[proximo_local]
    else:
      print('>>>>> Você não pode ir por esse caminho')
  elif comando == 'pegar':
    item = entrada[1]
    if item in posicao_atual.values():
      if item not in inventario:
        inventario.append(posicao_atual['item'])
    else:
      print('>>>>> Nesse local não existe itens!')
  else:
    print('>>>>> Comando inválido')
  if ('pimenta' in inventario) and ('rosca' in inventario) and posicao_atual['nome'] == 'REFEITÓTIO':
    print('Você conseguiu chegar ao refeitório com o molho de pimenta...')
    print('Você comeu a Rosca de quem não gostou do jogo! ')
    print('''\033[31m'+'

	______0000000000000000
 ____0000000000000000000000
_000000000__00000__0000000000
0000000000__00000__00000000000
0000000000__00000__00000000000
000000000000000000000000000000
000000000000000000000000000000
000000__________________000000
000000__________________000000
_000000_________________00000
__0000000_____________000000
____0000000_________0000000
______ 00000000000000000
'+'\033[0;0m''')
    print("VOCÊ VENCEU! ")
    break

	#Quando o jogador entrar em um cômodo com a nutriocionista, irá perder
	
  if 'item' in posicao_atual:
      if 'caixa secreta' in posicao_atual['item']:
          carteira = secret_box(carteira)

  if 'item' in posicao_atual:
      if 'gato' in posicao_atual['item']:
          if gato():
            posicao_atual = locais[1]
  if 'item' in posicao_atual:
    if 'nutricionista' in posicao_atual['item']:
      if carteira >= 50:
        carteira -= 50
        print('Você subornou a nutricionista e pode sair daqui')
      else:
        print('A nutricionista pegou você...')
        print("Você queimou a Rosca.")
        print('''\033[31m'+'
        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
        ████▌▄▌▄▐▐▌█████ 
        ████▌▄▌▄▐▐▌▀████ 
        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ 
        '+'\033[0;0m''')
        print("VOCÊ PERDEU! ")
        break

	#Quando o jogador chegar a cantina com o molho de pimenta e sem passar pela nutricionista ele vence