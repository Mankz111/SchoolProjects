import random
import time
import os
import shutil



SYMBOLS = ["🍒", "🍋", "🍉", "⭐", "💎"]
PAYOUTS = {
    "🍒": 3,  # 3 cerejas seguidas pagam 3x a aposta
    "🍋": 2,   # 3 limões seguidos pagam 2x a aposta
    "🍉": 4,  # 3 melancias seguidas pagam 4x a aposta
    "⭐": 5,   # 3 estrelas seguidas pagam 5x a aposta
    "💎": 10  # 3 diamantes seguidos pagam 10x a aposta
}

DEPOSIT_TOTAL = 0.0    
WITHDRAW_TOTAL = 0.0  
TOTAL_BETS = 0.0       
TOTAL_WINS = 0.0       
APOSTA = 0.0
SALDO = 0.0

def menu_principal():
    print('\n Bem-vindo ao menu principal da slot! ')
    print('\n')
    print('1 - Escolha o montante a depositar! ')
    print('2 - Escolha o montante que pretende levantar. ')
    print('3 - Iniciar o jogo. ')
    print('4 - Verificar saldo. ')
    print('5 - Total de ganhos/percas.')
    print('6 - Sair.')
    
def deposito():
    global SALDO, DEPOSIT_TOTAL
    while True:
        try:
            e = int(input('Bem-vindo ao menu de deposito. Prima "1" para prosseguir para o deposito ou prima "2" para sair.'))
            if e > 2:
                print('Insira uma opção válida. "1 ou 2."')
                continue
            elif e < 1:
                print('Insira uma opção válida. "1 ou 2."')
                continue     
        except ValueError:
            print('Insira uma opção válida. "1 ou 2."')
            continue
            
            
        if e == 1:
            while True:
                try:
                    quantia = float(input('Insira o montande que pretende depositar. '))
                    if quantia <= 0:
                        print('Insira um valor positivo para o depósito.')
                        continue
                    elif quantia > 10000:
                        print('Essa quantia é muito alta. Não queremos a sua desgraça! ')
                        break
                    SALDO += quantia
                    DEPOSIT_TOTAL += quantia
                    print(f'O seu montante atual é: {SALDO:.2f} euros.')        
                except ValueError:
                    print('Insira um montante válido. ')
                    continue
                break
            
            while True:
                try:
                    continuar = int(input('Prima "1" para efetuar novo deposito ou "2" para voltar ao menu principal. '))
                    if continuar == 1:
                        try:
                            quantia = float(input('Insira o montande que pretende depositar. '))
                            print('O seu montante atual é: ', SALDO)
                            if quantia <= 0:
                                print('Insira um montante válido. ')
                                continue
                            elif quantia > 10000:
                                print('Essa quantia é muito alta. Não queremos a sua desgraça! ')
                                break
                            SALDO += quantia
                            DEPOSIT_TOTAL += quantia 
                            print('O seu montante atual é: ', SALDO)                               
                        except ValueError:
                            print('Insira um montante válido. Não pode apostar letras. ')       
                except ValueError:
                    print('Insira um montante válido. Não pode apostar letras. ')
                if continuar == 2:
                    break
                break
        if e == 2:
            break

        
    
        
def levantar():
    global SALDO, WITHDRAW_TOTAL
    while True:
        try:
            l = int(input('Bem vindo ao menu de levantamento. '
                          'Prima "1" para proceder ao levantamento, ou "2" para sair: '))
        except ValueError:
            print('Opção inválida. Tente novamente.')
            continue

        if l == 1:
            try:
                tirar = float(input('Quanto dinheiro pretendes levantar? '))
            except ValueError:
                print('Valor inválido.')
                continue

            if tirar <= 0:
                print('Valor de levantamento deve ser positivo.')
                continue

            if tirar > SALDO:
                print('Não tem saldo suficiente para efetuar o levantamento!')
                print('A voltar para o menu principal...')
                time.sleep(2)
                break
            else:
                SALDO -= tirar
                WITHDRAW_TOTAL += tirar
                print(f'Levantou {tirar} euros. Restam {SALDO:.2f} euros no saldo.')
                time.sleep(2)
            break
        elif l == 2:
            break
        else:
            print('Opção inválida. Tente novamente.')
            
def versaldo():
    global SALDO
    while True:
        print('O teu saldo atual é: ', SALDO)
        if SALDO < 0:
            SALDO = 0
        try:
            a = int(input('Prima 1 para voltar ao menu principal. '))
            if a == 1:
                break
            elif a < 1:
                print('Insira uma opção válida. ')
                time.sleep(2)
                continue
            elif a > 1:
                print('Insira uma opção válida. ')
                time.sleep(2)
                continue                 
        except ValueError:
                print('Insira uma opção válida. ')
                print('Tenta de novo... ')
                time.sleep(2)
                
               
    
        
def game_menu():
    global SALDO, APOSTA
    print('💎 Bem-vindo à SLOT-BONANZA! 💎')
    print('1 - Iniciar o jogo.')
    print('2 - Definir a quantidade da aposta.')
    print('3 - Sair do jogo.')
    print('4 - Ver as regras do jogo.')
    print('')

    try:
        e_1 = int(input('Pressione um dos números do menu: '))
    except ValueError:
        print('Opção inválida.')
        return

    while True:
        if e_1 == 1:
            game_logic()
        elif e_1 == 2:
            while True:
                try:
                    APOSTA = float(input('Insira o valor que pretendes apostar: '))
                except ValueError:
                    print('Valor inválido, tente novamente.')
                    continue

                if APOSTA <= 0:
                    print('A aposta deve ser maior que zero.')
                    continue
                if APOSTA > SALDO:
                    print('Não tem dinheiro suficiente. Faça um depósito para jogar.')
                    print('A voltar para o menu principal...')
                    time.sleep(2)
                    return
                else:
                    print(f'Aposta definida: {APOSTA:.2f}. Saldo: {SALDO:.2f}')
                    # Volta ao menu do jogo para iniciar
                    game_menu()
                break
        elif e_1 == 4:
            regras_do_jogo()
            time.sleep(2)
            return
        elif e_1 == 3:
            return
        break
    


def game_logic(duration=2):
    global SALDO, APOSTA, TOTAL_BETS, TOTAL_WINS

    running = True
    while running:
        if SALDO <= 0:
            print("Você não tem saldo suficiente para continuar a jogar.")
            time.sleep(2)
            break
        if APOSTA <= 0:
            print('Por favor, defina uma aposta antes de continuar.')
            time.sleep(2)
            break

        print(f"O teu saldo atual é: {SALDO:.2f}")
        # Desconta a aposta do saldo e soma no total apostado
        SALDO -= APOSTA
        TOTAL_BETS += APOSTA

        
        num_columns = 5
        num_lines = 5
        end_time = time.time() + duration

        horizontal_border = "✨" + "══" * (num_columns * 4 - 1) + "✨"
        frame_width = len(horizontal_border)
        terminal_size = shutil.get_terminal_size((80, 20))
        terminal_width = terminal_size.columns
        terminal_height = terminal_size.lines
        padding_left = (terminal_width - frame_width) // 2
        padding_top = (terminal_height - (num_lines + 2)) // 2

        while time.time() < end_time:
            reel = [[random.choice(SYMBOLS) for _ in range(num_columns)] for _ in range(num_lines)]
            os.system("cls" if os.name == "nt" else "clear")
            print("\n" * padding_top)
            print(" " * padding_left + horizontal_border)
            for linha in reel:
                row = "  |  ".join(linha)
                print(" " * padding_left + row.center(frame_width))
            print(" " * padding_left + horizontal_border)
            time.sleep(0.1)

        # Verifica ganhos após a "roda" parar
        ganho = verificar_ganho(reel)
        TOTAL_WINS += ganho  # Soma o que foi ganho
        SALDO += ganho       # Adiciona os ganhos ao saldo

        print(f"Você ganhou {ganho:.2f} nesta rodada.")
        print(f"Sua aposta foi {APOSTA:.2f}. O seu saldo atual é {SALDO:.2f}.")

        continuar = input('Pressione Enter para jogar novamente ou escreva "sair" para voltar ao menu principal: ')
        if continuar.lower() == 'sair':
            break
        
def regras_do_jogo():
    texto_regras = """
    ========================= REGRAS DO JOGO =========================
    1. Define o valor da tua aposta antes de iniciares o jogo.
    2. A slot vai girar 5 colunas, cada uma exibindo um símbolo aleatório.
    3. Se conseguires:
       - 3 símbolos iguais consecutivos na mesma linha, ganhas um multiplicador
         relativo a esse símbolo (por exemplo, 3 cerejas pagam 3x a tua aposta).
       - 5 símbolos iguais consecutivos na mesma linha, ganhas um prémio ainda maior
         (por exemplo, 5 símbolos iguais aplicam um multiplicador especial).
    4. Cada giro custa o valor da aposta definida. O teu saldo é atualizado a cada rodada.
    5. Se ficares sem saldo, terás de depositar novamente para continuares a jogar.
    6. Podes sair a qualquer momento, e o teu saldo ficará registado (desde que não o levantes).
    7. Diverte-te e joga com responsabilidade!
    ==================================================================
    """
    print(texto_regras)
            
                        
def quantidadeaposta():
    global SALDO
    while True:
        qntaposta = float(input('Quanto quer apostar? '))
        if qntaposta < SALDO:
            print('Aposta: ', qntaposta, 'Saldo: ', SALDO)
        if qntaposta > SALDO:
            print('Não tem dinheiro suficiente. Volte para o menu de depositos.' )
        break
    
def verificar_ganho(reel):
    global SALDO
    total_ganho = 0
    for linha in reel:
        # Verifica combinações de 3 símbolos consecutivos
        for i in range(3):  # Limita a verificação às colunas 1, 2 e 3 (índices 0, 1 e 2)
            if linha[i] == linha[i + 1] == linha[i + 2]:  # Verifica 3 consecutivos
                simbolo = linha[i]
                if simbolo in PAYOUTS:
                    ganho = PAYOUTS[simbolo] * APOSTA
                    total_ganho += ganho
                    print(f"Parabéns! Você ganhou {ganho:.2f} com a combinação: {linha[i]} {linha[i+1]} {linha[i+2]} (colunas {i+1}-{i+3})")

        # Verifica combinações de 5 símbolos consecutivos
        for i in range(1):  # Garante que a verificação está limitada à coluna 1 (índice 0)
            if linha[i] == linha[i + 1] == linha[i + 2] == linha[i + 3] == linha[i + 4]:
                simbolo = linha[i]
                if simbolo in PAYOUTS:
                    ganho = PAYOUTS[simbolo] * APOSTA * 10
                    total_ganho += ganho
                    print(f"Parabéns! Você ganhou {ganho:.2f} com a combinação: {linha[i]} {linha[i+1]} {linha[i+2]} {linha[i+3]} {linha[i+4]} (colunas {i+1}-{i+5})")

    return total_ganho

def ganhos_percas():

    global SALDO, DEPOSIT_TOTAL, WITHDRAW_TOTAL, TOTAL_BETS, TOTAL_WINS

    net_game = TOTAL_WINS - TOTAL_BETS
    net_overall = SALDO + WITHDRAW_TOTAL - DEPOSIT_TOTAL

    print('\n===== RELATÓRIO DE GANHOS/PERDAS =====')
    print(f'Valor total depositado:      {DEPOSIT_TOTAL:.2f}')
    print(f'Valor total levantado:       {WITHDRAW_TOTAL:.2f}')
    print(f'Total apostado (rodadas):    {TOTAL_BETS:.2f}')
    print(f'Total ganho em prêmios:      {TOTAL_WINS:.2f}')
    print(f'--------------------------------------')
    print(f'Lucro/Prejuízo do jogo:      {net_game:.2f}')
    print(f'Saldo atual:                 {SALDO:.2f}')
    print(f'Lucro/Prejuízo TOTAL:        {net_overall:.2f}\n')
    input('Pressione Enter para voltar ao menu principal... ')
    

    
    

def main():
    
    while True:
        menu_principal()
        try:
            menu = int(input('Escolhe uma opção: '))
            if menu <0:
                print('Insira uma opção válida. "De 1 a 6. "')
                print('Voltando ao menu principal...')
                time.sleep(2)
            elif menu > 6:
                print('Insira uma opção válida. "De 1 a 6. "')
                print('Voltando ao menu principal...')
                time.sleep(2)      
        except ValueError:
            print('Insira uma opção válida. "De 1 a 6. "')
            print('Voltando ao menu principal...')
            time.sleep(2)
            continue
        if menu == 1:
            deposito()
        elif menu == 2:
            levantar()
        elif menu == 3:
            game_menu()
        elif menu == 4:
            versaldo()
        elif menu == 5:
            ganhos_percas()    
        elif menu == 6:
            quit()
            
            
main()           
        
    
    