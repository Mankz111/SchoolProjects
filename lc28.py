import random
import time
import os

SYMBOLS = ["🍒", "🍋", "🍉", "⭐", "💎"]
DINHEIRO = 0
SALDO = 0

def menu_principal():
    while True:
        print('\n💎 Bem-vindo ao menu principal da slot! 💎\n')
        print('1 - Escolha o montante a depositar.')
        print('2 - Escolha o montante que pretende levantar.')
        print('3 - Iniciar o jogo.')
        print('4 - Verificar saldo.')
        print('5 - Total de ganhos/percas (em desenvolvimento).')
        print('6 - Sair.')
        
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            deposito()
        elif opcao == '2':
            levantar()
        elif opcao == '3':
            game_menu()
        elif opcao == '4':
            versaldo()
        elif opcao == '5':
            print("Esta funcionalidade está em desenvolvimento.")
        elif opcao == '6':
            print("Obrigado por jogar! Até logo.")
            break
        else:
            print("Opção inválida! Tente novamente.")

def deposito():
    global SALDO
    while True:
        opcao = input('1 - Depositar dinheiro\n2 - Voltar ao menu principal\nEscolha uma opção: ')
        if opcao == '1':
            try:
                quantia = float(input('Insira o montante que pretende depositar: '))
                SALDO += quantia
                print(f'Seu saldo atual é: {SALDO:.2f} euros.')
            except ValueError:
                print("Por favor, insira um valor válido.")
        elif opcao == '2':
            break
        else:
            print("Opção inválida! Tente novamente.")

def levantar():
    global SALDO
    while True:
        opcao = input('1 - Levantar dinheiro\n2 - Voltar ao menu principal\nEscolha uma opção: ')
        if opcao == '1':
            try:
                quantia = float(input('Quanto deseja levantar? '))
                if quantia > SALDO:
                    print("Saldo insuficiente para este levantamento.")
                else:
                    SALDO -= quantia
                    print(f'Você levantou {quantia:.2f} euros. Saldo restante: {SALDO:.2f} euros.')
            except ValueError:
                print("Por favor, insira um valor válido.")
        elif opcao == '2':
            break
        else:
            print("Opção inválida! Tente novamente.")

def versaldo():
    print(f'Seu saldo atual é: {SALDO:.2f} euros.')

def game_menu():
    while True:
        print('\n🎰 Bem-vindo à SLOT-BONANZA! 🎰\n')
        print('1 - Iniciar o jogo.')
        print('2 - Definir a quantidade da aposta.')
        print('3 - Voltar ao menu principal.')
        print('4 - Ver as regras do jogo.\n')

        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            game_logic()
        elif opcao == '2':
            quantidadeaposta()
        elif opcao == '3':
            print("Voltando ao menu principal...")
            break
        elif opcao == '4':
            print('🎲 Regras do jogo:')
            print('- Combine os símbolos para ganhar.')
            print('- As apostas são deduzidas do saldo atual.')
            print('- Boa sorte!\n')
        else:
            print("Opção inválida! Tente novamente.")

def game_logic(duration=2):
    global SALDO
    while True:
        print(f'\nSeu saldo atual é: {SALDO:.2f} euros.')
        opcao = input('Pressione "barra de espaço" para rodar ou "sair" para voltar ao menu principal: ')
        
        if opcao.lower() == 'sair':
            print("Voltando ao menu principal...")
            break
        elif opcao == ' ':
            num_columns = 5
            num_lines = 3
            horizontal_border = "✨" + "═" * (num_columns * 4 - 1) + "✨"
            end_time = time.time() + duration
            
            while end_time > time.time():
                os.system("cls" if os.name == "nt" else "clear")
                reel1 = [[random.choice(SYMBOLS) for _ in range(num_columns)] for _ in range(num_lines)]
                for reel in reel1:
                    print(" | ".join(reel))
                    print(horizontal_border)
                time.sleep(0.07)
            print("\nRodada concluída!")
        else:
            print("Entrada inválida! Tente novamente.")

def quantidadeaposta():
    global SALDO
    while True:
        try:
            qntaposta = float(input('Quanto deseja apostar? '))
            if qntaposta > SALDO:
                print("Saldo insuficiente. Faça um depósito para continuar.")
            else:
                print(f'Aposta definida: {qntaposta:.2f} euros.')
                break
        except ValueError:
            print("Por favor, insira um valor válido.")

# Iniciar o programa
menu_principal()
    




