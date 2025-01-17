import random
import math
import time
import os
import shutil



SYMBOLS = ["🍒", "🍋", "🍉", "⭐", "💎"]
CHANCE = [10, 20, 30, 5, 2]
DINHEIRO = 0
SALDO = 0

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
    global SALDO
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
    global SALDO
    while True:
        l = int(input('Bem vindo ao menu de levantamento. Prima "1" para proceder ao levantamento, ou prima "2" para sair. '))
        if l == 1:
            tirar = float(input('Quanto dinheiro pertendes levantar? '))
            SALDO -= tirar
            if SALDO < 0:
                SALDO = 0
            print('Levantou ', tirar , 'euros. E restam, ', SALDO, 'euros. ')
            print('Não tem saldo suficiente para efetuar o levantamento! ')
            print('A voltar para o menu principal... ')
            time.sleep(2)            
            break
        if l == 2:
            break
            
def versaldo():
    while True:
        global SALDO
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
    global SALDO
    print('💎Bem-vindo à SLOT-BONANZA!💎 ')
    print('Prima 1 para iniciar o jogo. ')
    print('Prima 2 para definir a quantidade da aposta. ')
    print('Prima 3 para sair do jogo. ')
    print('Prima 4 para ver as regras do jogo. ')
    print('')
    e_1 = int(input('Pressione um dos numeros do menu. '))
    while True:
        if e_1 == 1:
            game_logic()
                            
        elif e_1 == 2:
            while True:
                qntaposta = float(input('Quanto quer apostar? '))
                if qntaposta < SALDO:
                    print('Aposta: ', qntaposta, 'Saldo: ', SALDO)
                elif qntaposta > SALDO:
                    print('Não tem dinheiro suficiente. Faça um depósito para jogar.' )
                    print('A voltar para o menu principal... ')
                    time.sleep(2) 
                    break
                break
            break
        elif e_1 == 4:
            print('aaaaaaaaa')
            break
        elif e_1 == 3:
            break
        break
    


def game_logic(duration=2):
    global SALDO
    running = True
    while running:
        print('O seu saldo atual é: ', SALDO)
        space = input('Prima "barra de espaço para rodar" ou "sair" para voltar ao menu. ')
        
    
        if space.lower() == 'sair':
            print('Voltando para o menu principal. ')
            time.sleep(2)
            break
        if space == ' ':
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
            while end_time > time.time():
                reel1 = [[random.choice(SYMBOLS) for _ in range(num_columns)] for _ in range(num_lines)]
                os.system("cls" if os.name == "nt" else "clear")
                print("\n" * padding_top)
                print(" " * padding_left + horizontal_border)
                for reel in reel1:
                    row = "  |  ".join(reel)
                    print(" " * padding_left + row.center(frame_width))
                    
                print(" " * padding_left + horizontal_border)
            
                time.sleep(0.07)
            
def pagamento():
    global SALDO
    for x in SYMBOLS:
        if x[1] == x[2]:
            pass
            
            
def quantidadeaposta():
    global SALDO
    while True:
        qntaposta = float(input('Quanto quer apostar? '))
        if qntaposta < SALDO:
            print('Aposta: ', qntaposta, 'Saldo: ', SALDO)
        if qntaposta > SALDO:
            print('Não tem dinheiro suficiente. Volte para o menu de depositos.' )
        break
    
    
            




            

    
    

                
            
            
    
    
    
    
    
    

    




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
        elif menu == 6:
            quit()
            
            
main()           
        
    
    