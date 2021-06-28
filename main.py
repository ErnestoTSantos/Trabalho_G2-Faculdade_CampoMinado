from Campo_Minado import campoMinado, testingCode

# Documento para chamar o jogo e a matriz teste
# Trás ao usuário a possibilidade de escolher qual das duas formas irá utilizar
# Laço feito para evitar que o usuário digite errado e encerre o processo
while True:
    game = input('Deseja acessar o jogo ou o teste? Teste/Jogo: ').upper().strip()
    # Faz o corte da primeira letra e assim utiliza ela para entrar no modo jogo
    game = game[0:1]
    if game == 'J':
        # Jogo principal, com os elementos escondidos trazendo a verdadeira emoção
        campoMinado()
        break
    elif game == 'T':
        # Jogo secundário, apenas para mostrar como a matriz está funcionando
        testingCode()
        break
    else:
        print('Digite uma informação válida!')