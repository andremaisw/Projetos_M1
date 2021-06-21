# from time import sleep
# from os import system
# system('cls')

# input('Digite o seu nome: ')
# system('cls')



# r1 = input('\nVocê telefonou para a vítima? [S/N] ').strip().upper()
# r2 = input('\nVocê esteve no local do crime? [S/N] ').strip().upper()
# r3 = input('\nVocê mora perto da vítima? [S/N] ').strip().upper()
# r4 = input('\nVocê devia para a vítima? [S/N] ').strip().upper()
# r5 = input('\nVocê já trabalhou com a vítima? [S/N] ').strip().upper()
# contador = 0

# if r1[0] == 'S':
#     contador += 1
# if r2[0] == 'S':
#     contador += 1
# if r3[0] == 'S':
#     contador += 1
# if r4[0] == 'S':
#     contador += 1
# if r5[0] == 'S':
#     contador += 1

# if contador >= 0 and contador < 2:
#     print('\nInocente\n', contador)
# elif contador == 2:
#     print('Suspeita(a)', contador)
# elif contador >= 3 and contador <= 4:
#     print('\nCúmplice\n', contador)
# else:
#     print('\nAssassino(a)\n', contador)


# CÓDIGO PARA COLAB

from time import sleep
from random import randrange

# Recebenco nome do(a) JOGADOR(A)
nome = input('Antes de entrar nesta realidade paralela, informe o seu nome: ')
input("\nAVISO ⚠: ESTE JOGO PODE TRAZER SENSAÇÕES ESTRANHAS OU ALUCINAÇÕES!\n\n...deseja continuar? [Tecle ENTER] ")
sleep(1)

# Criando e selecionando ALEATORIAMENTE as informações do personagem do jogador.
locais = ['Hospital', 'Cemitério', 'Hotel', 'Lavanderia', 'Escritório']
local = locais[randrange(0,5)]
local_morte = locais[randrange(0,5)]
armas = ['Tesoura hospitalar', 'Enxada', 'Fio telefônico', 'Balde cheio de água', 'Martelo do júri']
arma = armas[randrange(0,5)]
profissoes = ['Enfermeiro(a)', 'Coveiro', 'Gerente de hotel', 'Lavandeiro(a)', 'Segurança num escritório de advocacia']
profissao = profissoes[randrange(0,5)]

# Criando as HISTÓRIAS que aconteceram ALEATORIAMENTE com o personagem do jogador.
h1 = f'''
[Narrador]: São 23:37h de uma sexta-feira. Você está estressado(a).
[Narrador]: Você está saindo do(a) {local} com algumas compras e vai direto para casa.
[Narrador]: Você assiste um filme e logo depois decide dormir... '''
h2 = f'''
[Narrador]: São 23:45h de uma sexta-feira. Você está calmo(a).
[Narrador]: Você está no(a) {local} resolvendo uns assuntos e logo vai para casa.
[Narrador]: Você chega bem cansado(a), toma um banho e então decide dormir... '''
h3 = f'''
[Narrador]: São 00:01h de uma sexta-feira. Você está nervoso(a).
[Narrador]: Você está no(a) {local} discutindo com alguém da recepção, mas sai de lá e vai para casa.
[Narrador]: Você chega e vai para a banheira relaxar... '''
h4 = f'''
[Narrador]: São 00:15h de uma sexta-feira. Você está triste.
[Narrador]: Você está no(a) {local} procurando sua carteira que acabou esquecendo por lá, não acha e logo vai para casa.
[Narrador]: Você chega desanimado, manda mensagens para amigos, informando o sumiço do item, e então decide dormir... '''
h5 = f'''
[Narrador]: São 00:27h de uma sexta-feira. Você está bêbado(a).
[Narrador]: Você está no(a) {local}, nem sabe o por quê, mas vai andando para casa.
[Narrador]: Você chega bem desnorteado(a), cai na cama e dorme... '''
historias = [h1,h2,h3,h4,h5]
historia = historias[randrange(0,5)]

# INÍCIO da história (evento aleatório)
print(historia)
input('Dormindo... \nTecle ENTER para continuar')
sleep(1)
input("""
[Narrador]: De repente, a campainha toca… você olha para o relógio: são 3:47h da madrugada; e fica se perguntando quem poderia ser uma hora dessas...
[Narrador]: Você, então, vai até a porta… \nTecle ENTER para olhar pelo olho mágico:  """)
sleep(1)
print('[Narrador]: É a polícia. Você abre a porta e fala: ')
print(f'[{nome} (você)]: Boa noite, policiais. O que aconteceu? Em que posso ajudá-los?')
sleep(1)
input(f'[Policial]: Você é o {nome}? Eu sou o Tenente Muralha. Seu amigo Stanislau foi assassinado ontem às 23:59h. \nPrecisamos fazer algumas perguntas. Pode nos acompanhar até a delegacia? \n[Tecle ENTER para continuar] ')
sleep(2)
print('[Narrador]: Você chegou a Delegacia! O delegado está te esperando e conduzirá o interrogatório.')

# Condução do INTERROGATÓRIO
r1 = input('[Delegado]: Você telefonou para a vítima? [Sim/Não]').strip().upper()
r2 = input(f'[Delegado]: Você esteve no no(a) {local_morte} (cena do crime)? [Sim/Não]').strip().upper()
r3 = input('[Delegado]: Você mora perto da vítima? [Sim/Não]').strip().upper()
r4 = input('[Delegado]: Você devia para a vítima? [Sim/Não]').strip().upper()
r5 = input('[Delegado]: Você já trabalhou com a vítima? [Sim/Não]').strip().upper()
contador = 0

# Computando respostas e adicionando +1 ao contador a cada 'SIM'
if r1[0] == 'S':
    contador += 1
if r2[0] == 'S':
    contador += 1
if r3[0] == 'S':
    contador += 1
if r4[0] == 'S':
    contador += 1
if r5[0] == 'S':
    contador += 1

if contador >= 0 and contador < 2:
    print('\nVocê foi considerado(a) Inocente\n', contador)
elif contador == 2:
    print('Suspeita(a)', contador)
elif contador >= 3 and contador <= 4:
    print('\nCúmplice\n', contador)
else:
    print('\nAssassino(a)\n', contador)
