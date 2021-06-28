from random import randint
from os import system
from time import sleep

def menu():
    # Opções para funcionamento do programa
    system('cls')
    print('Desenvolvido por: \033[34mErnesto Santos, Gregory dos Santos e Wiliam da Silva\033[m')
    print('-=-' * 20)
    print(' ' * 17, '\033[31mVamos jogar campo minado!!\033[m')
    print('-=-' * 20)
    print('Leve o soldado até o ponto 0-19')
    while True:
        print('1 - Iniciar novo jogo')
        print('2 - Visualizar recordes armazenados')
        print('3 - Sair')
        userOption = int(input('Qual a sua opção? ').strip())
        print()
        
        if userOption >= 4 or userOption == 0:
            print('Por favor digite um valor válido!')
        elif userOption < 3 and userOption > 0:
            break
        elif userOption == 3:
            print('Até breve!')
            print('Encerrando jogo...')
            sleep(2)
            break
    
    # Retorna a opção selecionada pelo usuário
    return userOption

def lin():
    # Gera um valor de linha
    lin = randint(0, 19)
    return lin

def col():
    # Gera um valor de coluna
    col = randint(0, 19)
    return col

def lose():
    # Chama a finalização do jogo, apresentando informações para o usuário
    print('-=-' * 20)
    print(' ' * 10, 'Putzzzz, infelizmente você \033[31mperdeu\033[m!')
    print('-=-' * 20)
    print('Você andou pelo seguinte caminho: \n')

def createBomb():
    # Forma as posições das bombas a serem explodidas
    # Analisa se alguma está no ponto inicial ou no final, caso aconteça a função é chamada novamente até que seja sanado o problema.
    bomb = [{'linha':lin(), 'coluna':col()}]
    if bomb[0]['linha'] == 19 and bomb[0]['coluna'] == 0 or bomb[0]['linha'] == 0 and bomb[0]['coluna'] == 19:
        while True:
            bomb = [{'linha':lin(), 'coluna':col()}]
            if bomb[0]['linha'] != 19 and bomb[0]['coluna'] != 0 or bomb[0]['linha'] != 0 and bomb[0]['coluna'] != 19:
                break
    
    return bomb

def valorColLin(bomba, position):
    # Extrai o valor da linha e coluna de cada bomba
    bomb = bomba[0][position]
    return bomb

def showCamp(camp):
    # Função para apresentar o campo ao usuário
    val = 0
    print(' ' * 2, '  0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19')
    for i in camp:
        print(f'{val:2}', end=' ')
        val += 1
        for j in i:
            print(j, end='')
        print()

def somaLinPos(linBomb, colBomb):
    # Soma um a linha da bomba para colocar o 3
    soma = linBomb + 1
    if soma > 19:
        soma = None
        colBomb = None
    return [{'linha':soma, 'coluna':colBomb}]

def subtraiLinPos(linBomb, colBomb):
    # Subtrai um para colocar na linha superior o 3
    subtrai = linBomb - 1
    if subtrai < 0:
        subtrai = None
        colBomb = None
    return [{'linha':subtrai, 'coluna':colBomb}]

def somaColPos(linBomb, colBomb):
    # Soma um para colocar na coluna direita um 3
    soma = colBomb + 1
    if soma > 19:
        soma = None
        linBomb = None
    return [{'linha':linBomb, 'coluna':soma}]

def subtraiColPos(linBomb, colBomb):
    # Subtrai um para colocar o 3 na coluna da esquerda
    subtrai = colBomb - 1
    if subtrai < 0:
        subtrai = None
        linBomb = None
    return [{'linha':linBomb, 'coluna':subtrai}]


# Cria todas as bombas em posições diferentes
# Espalhando elas pelo campo
bomba_1 = createBomb()

bomba_2 = createBomb()

bomba_3 = createBomb()

bomba_4 = createBomb()

bomba_5 = createBomb()

bomba_6 = createBomb()

bomba_7 = createBomb()

bomba_8 = createBomb()

bomba_9 = createBomb()

bomba_10 = createBomb()

# Chama a função para coletar da lista de dicionário o valor das linhas e colunas
# Referentes a cada uma das 10 bombas
linBomb_1 = valorColLin(bomba_1, 'linha')
colBomb_1 = valorColLin(bomba_1, 'coluna')

linBomb_2 = valorColLin(bomba_2, 'linha')
colBomb_2 = valorColLin(bomba_2, 'coluna')

linBomb_3 = valorColLin(bomba_3, 'linha')
colBomb_3 = valorColLin(bomba_3, 'coluna')

linBomb_4 = valorColLin(bomba_4, 'linha')
colBomb_4 = valorColLin(bomba_4, 'coluna')

linBomb_5 = valorColLin(bomba_5, 'linha')
colBomb_5 = valorColLin(bomba_5, 'coluna')

linBomb_6 = valorColLin(bomba_6, 'linha')
colBomb_6 = valorColLin(bomba_6, 'coluna')

linBomb_7 = valorColLin(bomba_7, 'linha')
colBomb_7 = valorColLin(bomba_7, 'coluna')

linBomb_8 = valorColLin(bomba_8, 'linha')
colBomb_8 = valorColLin(bomba_8, 'coluna')

linBomb_9 = valorColLin(bomba_9, 'linha')
colBomb_9 = valorColLin(bomba_9, 'coluna')
        
linBomb_10 = valorColLin(bomba_10, 'linha')
colBomb_10 = valorColLin(bomba_10, 'coluna')

# Pega as linhas e colunas das bombas e coloca o número ao redor das bombas
# Cada um gera uma posição diferente no mapa
writeTree_1 = somaLinPos(linBomb_1, colBomb_1)
writeTree_2 = subtraiLinPos(linBomb_1, colBomb_1)
writeTree_3 = somaColPos(linBomb_1, colBomb_1)
writeTree_4 = subtraiColPos(linBomb_1, colBomb_1)
writeTree_5 = somaLinPos(linBomb_2, colBomb_2)
writeTree_6 = subtraiLinPos(linBomb_2, colBomb_2)
writeTree_7 = somaColPos(linBomb_2, colBomb_2)
writeTree_8 = subtraiColPos(linBomb_2, colBomb_2)
writeTree_9 = somaLinPos(linBomb_3, colBomb_3)
writeTree_10 = subtraiLinPos(linBomb_3, colBomb_3)
writeTree_11 = somaColPos(linBomb_3, colBomb_3)
writeTree_12 = subtraiColPos(linBomb_3, colBomb_3)
writeTree_13 = somaLinPos(linBomb_4, colBomb_4)
writeTree_14 = subtraiLinPos(linBomb_4, colBomb_4)
writeTree_15 = somaColPos(linBomb_4, colBomb_4)
writeTree_16 = subtraiColPos(linBomb_4, colBomb_4)
writeTree_17 = somaLinPos(linBomb_5, colBomb_5)
writeTree_18 = subtraiLinPos(linBomb_5, colBomb_5)
writeTree_19 = somaColPos(linBomb_5, colBomb_5)
writeTree_20 = subtraiColPos(linBomb_5, colBomb_5)
writeTree_21 = somaLinPos(linBomb_6, colBomb_6)
writeTree_22 = subtraiLinPos(linBomb_6, colBomb_6)
writeTree_23 = somaColPos(linBomb_6, colBomb_6)
writeTree_24 = subtraiColPos(linBomb_6, colBomb_6)
writeTree_25 = somaLinPos(linBomb_7, colBomb_7)
writeTree_26 = subtraiLinPos(linBomb_7, colBomb_7)
writeTree_27 = somaColPos(linBomb_7, colBomb_7)
writeTree_28 = subtraiColPos(linBomb_7, colBomb_7)
writeTree_29 = somaLinPos(linBomb_8, colBomb_8)
writeTree_30 = subtraiLinPos(linBomb_8, colBomb_8)
writeTree_31 = somaColPos(linBomb_8, colBomb_8)
writeTree_32 = subtraiColPos(linBomb_8, colBomb_8)
writeTree_33 = somaLinPos(linBomb_9, colBomb_9)
writeTree_34 = subtraiLinPos(linBomb_9, colBomb_9)
writeTree_35 = somaColPos(linBomb_9, colBomb_9)
writeTree_36 = subtraiColPos(linBomb_9, colBomb_9)
writeTree_37 = somaLinPos(linBomb_10, colBomb_10)
writeTree_38 = subtraiLinPos(linBomb_10, colBomb_10)
writeTree_39 = somaColPos(linBomb_10, colBomb_10)
writeTree_40 = subtraiColPos(linBomb_10, colBomb_10)

def verifiPossibiliti(verification):
    # Função para verificar se os valores das verifications estão dentro do estipulado
    # Se os valores forem maiores é retornado ao valor 19 e se forem menores retorna o 0
    if verification > 19:
        verification = 19
    elif verification < 0:
        verification = 0
    return verification

def campoMinado():
    # Chama o menu para receber a opção do usuário e iniciar o que ele deseja!
    iniciar = menu()

    # Pontuação do usuário por game
    pontuacao = 0

    if iniciar == 1:
        # Trás informações sobre o jogo ao player
        print('Você só poderá se mover na horizontal e vertical!')
        # Espera o comando do usuário para começar a trazer as informações
        input('Pressione enter para iniciar: ')

        # Limpa o prompt, para que apareça apenas o campo minado do jogador
        system('cls')

        # Gera a matriz principal com os valores
        campo = [
            ['  #  '] * 20, ['  #  '] * 20, ['  #  '] * 20, ['  #  '] * 20, ['  #  '] * 20, ['  #  '] * 20, ['  #  '] * 20, ['  #  '] * 20, ['  #  '] * 20, ['  #  '] * 20,
            ['  #  '] * 20, ['  #  '] * 20, ['  #  '] * 20, ['  #  '] * 20, ['  #  '] * 20, ['  #  '] * 20, ['  #  '] * 20, ['  #  '] * 20, ['  #  '] * 20, ['  #  '] * 20
            ]

        # Enumera o ponto inicial
        campo[19][0] = '  1  '

        # Apresenta ao usuário o campo minado inicial
        showCamp(campo)

        # Linha e coluna para basear os movimentos do jogador no decorrer do campo
        # A cada laço o valor dessas variáveis é alterado para a posição que o soldado esta
        initialLine = 19
        initialCol = 0

        while True:
            # Onde a verdadeira mágica acontece
            # Local onde o campo minado é escrito e avaliado para que o usuário possa jogar
            print()
            print('Lembrando, você só pode se mover na horizontal e vertical!')
            linUser = int(input('Digite uma linha. Ps: Valores laterais: ').strip())
            colUser = int(input('Digite uma coluna. Ps: Valores superiores: ').strip())
            print()

            moveUser = [{'linha':linUser, 'coluna':colUser}]
            finalLocale = [{'linha': 0, 'coluna': 19}]

            # Faz a soma e subtração das possibilidades para cada movimento do usuário
            # Verticais, horizontais e diagonais
            verification_1 = initialLine + 1
            verification_2 = initialLine - 1
            verification_3 = initialLine
            verification_4 = initialCol + 1
            verification_5 = initialCol - 1
            verification_6 = initialCol

            # Verifica se o usuário andou apenas uma linha ou coluna
            possibilit_1 = verification_1 == linUser and verification_6 == colUser
            possibilit_2 = verification_2 == linUser and verification_6 == colUser
            possibilit_3 = verification_3 == linUser and verification_4 == colUser
            possibilit_4 = verification_3 == linUser and verification_5 == colUser
            
            if linUser > 19 or colUser > 19 or linUser < 0 or colUser < 0:
                print('Por favor digite posições válidas!')
            elif possibilit_1 or possibilit_2 or possibilit_3 or possibilit_4:
                # Verifica se a posição é maior que 19 ou menor que 0 e ajusta
                # Salva a nova linha e coluna para que os movimentos continuem sendo feitos
                if possibilit_1:
                    verifiPossibiliti(verification_1)
                    verifiPossibiliti(verification_4)
                    initialLine = linUser
                    initialCol = colUser
                elif possibilit_2:
                    verifiPossibiliti(verification_1)
                    verifiPossibiliti(verification_5)
                    initialLine = linUser
                    initialCol = colUser
                elif possibilit_3:
                    verifiPossibiliti(verification_1)
                    verifiPossibiliti(verification_6)
                    initialLine = linUser
                    initialCol = colUser
                elif possibilit_4:
                    verifiPossibiliti(verification_2)
                    verifiPossibiliti(verification_4)
                    initialLine = linUser
                    initialCol = colUser

                if moveUser == finalLocale:
                    # Finalização do jogo, caso o usuário não caia em nehuma bomba chegará aqui, fazendo com que o seu jogo encerre e some os pontos e escreva no histórico de pontuação
                    
                    for i in range(20):
                        for j in range(20):
                            campo[i][j] = '  1  '
                    
                    system('cls')

                    for i in range(0, 20):
                        for j in range(0, 20):
                            position = [{'linha': i, 'coluna': j}]
                            if position == writeTree_1 or position == writeTree_2 or position == writeTree_3 or position == writeTree_4 or position == writeTree_5 or position == writeTree_6 or position == writeTree_7 or position == writeTree_8 or position == writeTree_9 or position == writeTree_10 or position == writeTree_11 or position == writeTree_12 or position == writeTree_13 or position == writeTree_14 or position== writeTree_15 or position == writeTree_16 or position == writeTree_17 or position == writeTree_18 or position == writeTree_19 or position == writeTree_20:
                                campo[i][j] = '  3  '
                            elif position == writeTree_21 or position == writeTree_22 or position == writeTree_23 or position == writeTree_24 or position == writeTree_25 or position == writeTree_26 or position == writeTree_27 or position == writeTree_28 or position == writeTree_29 or position == writeTree_30 or position == writeTree_31 or position == writeTree_32 or position == writeTree_33 or position == writeTree_34 or position == writeTree_35 or position == writeTree_36 or position == writeTree_37 or position == writeTree_38 or position == writeTree_39 or position == writeTree_40:
                                campo[i][j] = '  3  '

                    campo[linBomb_1][colBomb_1] = '  7  '
                    campo[linBomb_2][colBomb_2] = '  7  '
                    campo[linBomb_3][colBomb_3] = '  7  '
                    campo[linBomb_4][colBomb_4] = '  7  '
                    campo[linBomb_5][colBomb_5] = '  7  '
                    campo[linBomb_6][colBomb_6] = '  7  '
                    campo[linBomb_7][colBomb_7] = '  7  '
                    campo[linBomb_8][colBomb_8] = '  7  '
                    campo[linBomb_9][colBomb_9] = '  7  '
                    campo[linBomb_10][colBomb_10] = '  7  '
                    
                    print('\033[32mParabéns\033[m!! Você ganhou!')

                    nomeUser = input('Digite seu nome para o save: ')

                    with open('saveGame.txt', 'a') as arquivo:
                        arquivo.write(f'{nomeUser} pontuou: {pontuacao} \n')
                        arquivo.close()

                    print('As bombas no mapa estavam nas seguintes posições: ')
                    
                    # Mostra todas as posições aos usuários
                    showCamp(campo)

                    print('O seu score foi: {}'.format(pontuacao))

                    print('Encerrando o jogo...')
                    sleep(3)
                    print('Até a próxima!')
                    
                    break
                elif moveUser == bomba_1:
                    # Verificação da posição do usuário com a da bomba, fazendo com que a bomba exploda e chame o lose para finalizar o game
                    # Faz a mesma coisa nas 10 bombas
                    campo[linUser][colUser] = '  7  '
                    lose()
                    showCamp(campo)
                    break
                elif moveUser == bomba_2:
                    campo[linUser][colUser] = '  7  '
                    lose()
                    showCamp(campo)
                    break
                elif moveUser == bomba_3:
                    campo[linUser][colUser] = '  7  '
                    lose()
                    showCamp(campo)
                    break
                elif moveUser == bomba_4:
                    campo[linUser][colUser] = '  7  '
                    lose()
                    showCamp(campo)
                    break
                elif moveUser == bomba_5:
                    campo[linUser][colUser] = '  7  '
                    lose()
                    showCamp(campo)
                    break
                elif moveUser == bomba_6:
                    campo[linUser][colUser] = '  7  '
                    lose()
                    showCamp(campo)
                    break
                elif moveUser == bomba_7:
                    campo[linUser][colUser] = '  7  '
                    lose()
                    showCamp(campo)
                    break
                elif moveUser == bomba_8:
                    campo[linUser][colUser] = '  7  '
                    lose()
                    showCamp(campo)
                    break
                elif moveUser == bomba_9:
                    campo[linUser][colUser] = '  7  '
                    lose()
                    showCamp(campo)
                    break
                elif moveUser == bomba_10:
                    campo[linUser][colUser] = '  7  '
                    lose()
                    showCamp(campo)
                    break
                elif moveUser == writeTree_1 or moveUser == writeTree_2 or moveUser == writeTree_3 or moveUser == writeTree_4 or moveUser == writeTree_5 or moveUser == writeTree_6 or moveUser == writeTree_7 or moveUser == writeTree_8 or moveUser == writeTree_9 or moveUser == writeTree_10 or moveUser == writeTree_11 or moveUser == writeTree_12 or moveUser == writeTree_13 or moveUser == writeTree_14 or moveUser== writeTree_15 or moveUser == writeTree_16 or moveUser == writeTree_17 or moveUser == writeTree_18 or moveUser == writeTree_19 or moveUser == writeTree_20:
                    # Verificação das posições ao redor da bomba adicionando o número 3
                    # São duas possibilidades para verificar as posições do número 3, pois com uma só ficaria muito extenso e ruim de visualizar
                    campo[linUser][colUser] = '  3  '
                    pontuacao += 10
                elif moveUser == writeTree_21 or moveUser == writeTree_22 or moveUser == writeTree_23 or moveUser == writeTree_24 or moveUser == writeTree_25 or moveUser == writeTree_26 or moveUser == writeTree_27 or moveUser == writeTree_28 or moveUser == writeTree_29 or moveUser == writeTree_30 or moveUser == writeTree_31 or moveUser == writeTree_32 or moveUser == writeTree_33 or moveUser == writeTree_34 or moveUser == writeTree_35 or moveUser == writeTree_36 or moveUser == writeTree_37 or moveUser == writeTree_38 or moveUser == writeTree_39 or moveUser == writeTree_40:
                    # Verificação das posições ao redor da bomba adicionando o número 3
                    campo[linUser][colUser] = '  3  '
                    pontuacao += 10 
                else:
                    # Caso não caia em nenhum dos elementos, significa que o usuário está no caminho certo, assim enumarando sua posição possibilitando seu segmento no jogo
                    campo[linUser][colUser] = '  1  '
                    pontuacao += 10

                # Apresenta o campo com as modificações ao jogador
                showCamp(campo)
            else:
                print('Por favor realize um movimento válido!')
    
    elif iniciar == 2:
        # Faz a leitura do documento de save game para apresentar as informações ao usuário
        # Apresenta todos os recordes de jogos
        with open('saveGame.txt', 'r') as arquivo:
            for i in arquivo:
                print(i)
            arquivo.close()

def testingCode():
    opcao = menu()

    if opcao == 1:
        pontuacao = 0
        # Limpa o prompt, para que apareça apenas o campo minado do jogador
        system('cls')

        # Gera a matriz principal com os valores
        campo = [
            ['  1  '] * 20, ['  1  '] * 20, ['  1  '] * 20, ['  1  '] * 20, ['  1  '] * 20, ['  1  '] * 20, ['  1  '] * 20, ['  1  '] * 20, ['  1  '] * 20, ['  1  '] * 20,
            ['  1  '] * 20, ['  1  '] * 20, ['  1  '] * 20, ['  1  '] * 20, ['  1  '] * 20, ['  1  '] * 20, ['  1  '] * 20, ['  1  '] * 20, ['  1  '] * 20, ['  1  '] * 20
        ]

        campo[19][0] = '  *  '

        # Verifica as posições ao redor das bombas para posicionar os número 3
        for i in range(0, 20):
            for j in range(0, 20):
                position = [{'linha': i, 'coluna': j}]
                if position == writeTree_1 or position == writeTree_2 or position == writeTree_3 or position == writeTree_4 or position == writeTree_5 or position == writeTree_6 or position == writeTree_7 or position == writeTree_8 or position == writeTree_9 or position == writeTree_10 or position == writeTree_11 or position == writeTree_12 or position == writeTree_13 or position == writeTree_14 or position== writeTree_15 or position == writeTree_16 or position == writeTree_17 or position == writeTree_18 or position == writeTree_19 or position == writeTree_20:
                    campo[i][j] = '  3  '
                elif position == writeTree_21 or position == writeTree_22 or position == writeTree_23 or position == writeTree_24 or position == writeTree_25 or position == writeTree_26 or position == writeTree_27 or position == writeTree_28 or position == writeTree_29 or position == writeTree_30 or position == writeTree_31 or position == writeTree_32 or position == writeTree_33 or position == writeTree_34 or position == writeTree_35 or position == writeTree_36 or position == writeTree_37 or position == writeTree_38 or position == writeTree_39 or position == writeTree_40:
                    campo[i][j] = '  3  '

        # Adicionadas após os número 3 para que se possa ter um controle caso duas bombas fiquem lado a lado 
        campo[linBomb_1][colBomb_1] = '  7  '
        campo[linBomb_2][colBomb_2] = '  7  '
        campo[linBomb_3][colBomb_3] = '  7  '
        campo[linBomb_4][colBomb_4] = '  7  '
        campo[linBomb_5][colBomb_5] = '  7  '
        campo[linBomb_6][colBomb_6] = '  7  '
        campo[linBomb_7][colBomb_7] = '  7  '
        campo[linBomb_8][colBomb_8] = '  7  '
        campo[linBomb_9][colBomb_9] = '  7  '
        campo[linBomb_10][colBomb_10] = '  7  '

        showCamp(campo)

        initialLine = 19
        initialCol = 0

        while True:
            # Onde a verdadeira mágica acontece
            # Local onde o campo minado é escrito e avaliado para que o usuário possa jogar
            print()
            linUser = int(input('Digite uma linha. Ps: Valores númerados: ').strip())
            colUser = int(input('Digite uma coluna. Ps: Da esquerda para direita 0 a 19: ').strip())
            print()

            moveUser = [{'linha':linUser, 'coluna':colUser}]
            finalLocale = [{'linha': 0, 'coluna': 19}]

            verification_1 = initialLine + 1
            verification_2 = initialLine - 1
            verification_3 = initialLine
            verification_4 = initialCol + 1
            verification_5 = initialCol - 1
            verification_6 = initialCol

            # Verifica se o usuário andou apenas uma linha ou coluna
            possibilit_1 = verification_1 == linUser and verification_6 == colUser
            possibilit_2 = verification_2 == linUser and verification_6 == colUser
            possibilit_3 = verification_3 == linUser and verification_4 == colUser
            possibilit_4 = verification_3 == linUser and verification_5 == colUser
                
            if linUser > 19 or colUser > 19 or linUser < 0 or colUser < 0:
                print('Por favor digite posições válidas!')
            elif possibilit_1 or possibilit_2 or possibilit_3 or possibilit_4:

                # Verifica qual dos movimentos aconteceu e salva os valores entregues pelo usuário
                if possibilit_1:
                    verifiPossibiliti(verification_1)
                    verifiPossibiliti(verification_4)
                    initialLine = linUser
                    initialCol = colUser
                elif possibilit_2:
                    verifiPossibiliti(verification_1)
                    verifiPossibiliti(verification_5)
                    initialLine = linUser
                    initialCol = colUser
                elif possibilit_3:
                    verifiPossibiliti(verification_1)
                    verifiPossibiliti(verification_6)
                    initialLine = linUser
                    initialCol = colUser
                elif possibilit_4:
                    verifiPossibiliti(verification_2)
                    verifiPossibiliti(verification_4)
                    initialLine = linUser
                    initialCol = colUser
                
                if moveUser == finalLocale:
                    # Finalização do jogo, caso o usuário não caia em nehuma bomba chegará aqui, fazendo com que o seu jogo encerre e some os pontos e escreva no histórico de pontuacao
                    print('\033[32mParabéns\033[m!! Você ganhou!')

                    nomeUser = input('Digite seu nome para salvar: ')

                    # Salva os pontos do arquivo de teste, a cada novo jogo, salva um novo recode
                    with open('saveGameTest.txt', 'a') as arquivo:
                        arquivo.write(f'{nomeUser} pontuou: {pontuacao} \n')
                        arquivo.close()
                    
                    print('O seu score foi: {}'.format(pontuacao))

                    break
                elif moveUser == bomba_1:
                    # Verificão da posição do usuário com a da bomba, fazendo com que a bomba exploda e chame o lose para finalizar o game
                    # Faz a mesma coisa nas 10 bombas
                    campo[linUser][colUser] = '  %  '
                    lose()
                    showCamp(campo)
                    break
                elif moveUser == bomba_2:
                    campo[linUser][colUser] = '  %  '
                    lose()
                    showCamp(campo)
                    break
                elif moveUser == bomba_3:
                    campo[linUser][colUser] = '  %  '
                    lose()
                    showCamp(campo)
                    break
                elif moveUser == bomba_4:
                    campo[linUser][colUser] = '  %  '
                    lose()
                    showCamp(campo)
                    break
                elif moveUser == bomba_5:
                    campo[linUser][colUser] = '  %  '
                    lose()
                    showCamp(campo)
                    break
                elif moveUser == bomba_6:
                    campo[linUser][colUser] = '  %  '
                    lose()
                    showCamp(campo)
                    break
                elif moveUser == bomba_7:
                    campo[linUser][colUser] = '  %  '
                    lose()
                    showCamp(campo)
                    break
                elif moveUser == bomba_8:
                    campo[linUser][colUser] = '  %  '
                    lose()
                    showCamp(campo)
                    break
                elif moveUser == bomba_9:
                    campo[linUser][colUser] = '  %  '
                    lose()
                    showCamp(campo)
                    break
                elif moveUser == bomba_10:
                    campo[linUser][colUser] = '  %  '
                    lose()
                    showCamp(campo)
                    break
                elif moveUser == writeTree_1 or moveUser == writeTree_2 or moveUser == writeTree_3 or moveUser == writeTree_4 or moveUser == writeTree_5 or moveUser == writeTree_6 or moveUser == writeTree_7 or moveUser == writeTree_8 or moveUser == writeTree_9 or moveUser == writeTree_10 or moveUser == writeTree_11 or moveUser == writeTree_12 or moveUser == writeTree_13 or moveUser == writeTree_14 or moveUser== writeTree_15 or moveUser == writeTree_16 or moveUser == writeTree_17 or moveUser == writeTree_18 or moveUser == writeTree_19 or moveUser == writeTree_20:
                    campo[linUser][colUser] = '  #  '
                    pontuacao += 10
                elif moveUser == writeTree_21 or moveUser == writeTree_22 or moveUser == writeTree_23 or moveUser == writeTree_24 or moveUser == writeTree_25 or moveUser == writeTree_26 or moveUser == writeTree_27 or moveUser == writeTree_28 or moveUser == writeTree_29 or moveUser == writeTree_30 or moveUser == writeTree_31 or moveUser == writeTree_32 or moveUser == writeTree_33 or moveUser == writeTree_34 or moveUser == writeTree_35 or moveUser == writeTree_36 or moveUser == writeTree_37 or moveUser == writeTree_38 or moveUser == writeTree_39 or moveUser == writeTree_40:
                    campo[linUser][colUser] = '  #  '
                    pontuacao += 10
                else:
                    # Caso não caia em nenhum dos elementos, significa que o usuário está no caminho certo, assim enumarando sua posição possibilitando seu segmento no jogo
                    campo[linUser][colUser] = '  *  '
                    pontuacao += 10

                # Apresenta o campo com as mudanças ao jogador
                showCamp(campo)                
            else:
                print('Você só pode se movimentar na vertical ou horizontal!')
            
   
    elif opcao == 2:
        # Faz a leitura do arquivo de save dos testes
        # Apresenta todos os recordes contidos nele
        with open('saveGameTest.txt', 'r') as arquivo:
            for i in arquivo:
                print(i)
            arquivo.close()
