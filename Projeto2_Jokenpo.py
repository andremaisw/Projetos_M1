from os import system
system('cls')

# Utilizando os conceitos aprendidos até estruturas de repetição, crie um programa que jogue PEDRA, PAPEL e TESOURA (Jokenpô) com você. O programa tem que:
# • Permitir que eu decida quantas rodadas iremos fazer;
# • Ler a minha escolha (PEDRA, PAPEL ou TESOURA);
# • Decidir de forma aleatória a decisão do computador;
# • Mostrar quantas rodadas cada jogador ganhou;
# • Determinar quem foi o grande campeão de acordo com a quantidade de vitórias de cada um (computador e jogador);
# • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha de quantidade de rodadas, se não finalize o programa.


from random import randrange
jogador = maquina = empate = jogos = 0
nome = input('\nDigite o seu nome: ').strip().title()
system('cls')
while True:
    while True:
        for i in range(int(input('Digite quantas rodadas quer jogar: '))):
            system('cls')
            jogos += 1
            computador = randrange(3)
            jogada = input('\nDigite agora o que você quer: [PEDRA, PAPEL, TESOURA] ').upper().strip()
            if computador == 0:
                computador = 'PEDRA'
            elif computador == 1:
                computador = 'PAPEL'
            elif computador == 2:
                computador = 'TESOURA'
            
            # JOGOS EM QUE O COMPUTADOR VENCE
            if jogada == 'TESOURA' and computador == 'PEDRA':
                maquina += 1
                print(f'\nMáquina: {computador}\n{nome}: {jogada}\n\nA máquina venceu este jogo. \nPlacar: Máquina [ {maquina} ] x [ {jogador} ] {nome} ')
            elif jogada == 'PEDRA' and computador == 'PAPEL':
                maquina += 1
                print(f'\nMáquina: {computador}\n{nome}: {jogada}\n\nA máquina venceu este jogo. \nPlacar: Máquina [ {maquina} ] x [ {jogador} ] {nome} ')
            elif jogada == 'PAPEL' and computador == 'TESOURA':
                maquina += 1
                print(f'\nMáquina: {computador}\n{nome}: {jogada}\n\nA máquina venceu este jogo. \nPlacar: Máquina [ {maquina} ] x [ {jogador} ] {nome} ')
            
            # JOGOS EM QUE O COMPUTADOR VENCE
            elif computador == 'TESOURA' and jogada == 'PEDRA':
                jogador += 1
                print(f'\nMáquina: {computador}\n{nome}: {jogada}\n\nVocê venceu este jogo. \nPlacar: Máquina [ {maquina} ] x [ {jogador} ] {nome} ')
            elif computador == 'PEDRA' and jogada == 'PAPEL':
                jogador += 1
                print(f'\nMáquina: {computador}\n{nome}: {jogada}\n\nVocê venceu este jogo. \nPlacar: Máquina [ {maquina} ] x [ {jogador} ] {nome} ')
            elif computador == 'PAPEL' and jogada == 'TESOURA':
                jogador += 1
                print(f'\nMáquina: {computador}\n{nome}: {jogada}\n\nVocê venceu este jogo. \nPlacar: Máquina [ {maquina} ] x [ {jogador} ] {nome} ')
            else:
                empate += 1
                print(f'\nMáquina: {computador}\n{nome}: {jogada}\n\nVocês empataram este jogo. \nPlacar: Máquina [ {maquina} ] x [ {jogador} ] {nome} ')
            
            input('\n\nDigite ENTER para continuar\n\n')
        if input('\nDeseja finalizar o jogo? [S/N]').upper()[0] == 'S':
            break
    system('cls')    
    if maquina > jogador:
        vencedor = 'Máquina'
    elif jogador > maquina:
        vencedor = nome
    else:
        vencedor = 'Empate'
    print(f"""  RESULTADO:\n
        Total de partidas: {jogos}
        Grande vencedor: {vencedor} 
        Vitórias {nome}: {jogador}
        Vitórias Máquina: {maquina}
        Empates: {empate} \n""")
    if input('\nDeseja jogar novamente?').strip().upper()[0] == 'N':
        break
system('cls')
print(f'[Máquina]: Foi bom jogar com você, {nome}. Até a próxima!!\n')



  



