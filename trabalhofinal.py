import random
import math
import time
import os



SYMBOLS = ["🍒", "🍋", "🍉", "⭐", "💎"]
DINHEIRO = 0
SALDO = 0

def menu_principal():
    print('\n Bem-vindo ao menu principal da slot! ')
    print('\n')
    print('1 - Escolha o montante a depositar! .')
    print('2 - Escolha o montante que pretende levantar. ')
    print('3 - Iniciar o jogo. ')
    print('4 - Verificar saldo. ')
    print('5 - Total de ganhos/percas.')
    print('6 - Sair.')
    
def deposito():
    global SALDO
    while True:
        e = int(input('Bem-vindo ao menu de deposito. Prima "1" para prosseguir para o deposito ou prima "2" para sair.'))
        if e == 1:
            quantia = float(input('Insira o montande que pretende depositar. '))
            SALDO += quantia
            print('O seu montante atual é: ', SALDO)
            continuar = int(input('Prima "1" para efetuar novo deposito ou "2" para voltar ao menu principal. '))
            if continuar == 1:
                quantia = float(input('Insira o montande que pretende depositar. '))
                SALDO += quantia
                print('O seu montante atual é: ', SALDO)
                continue
            elif continuar == 2:
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
            print('Levantou ', tirar , 'euros. E restam, ', SALDO, 'euros. ')
        if l == 2:
            break
            
def versaldo():
    while True:
        global SALDO
        print('O teu saldo atual é: ', SALDO)
        a = int(input('Prima 1 para voltar ao menu principal. '))
        if a:
            break        
    
        
def game_menu():
    global SALDO
    print('💎Bem-vindo à SLOT-BONANZA!💎 ')
    print('Prima 1 para ver as regras do jogo. ')
    print('Prima 2 para definir a quantidade da aposta. ')
    print('Prima 3 para sair do jogo. ')
    print('Prima 4 para iniciar o jogo. ')
    print('')
    e_1 = int(input('Pressione um dos numeros do menu. '))
    while True:
        if e_1 == 1:
            print('aaaaaaaaa')
        if e_1 == 2:
            while True:
                qntaposta = float(input('Quanto quer apostar? '))
                if qntaposta < SALDO:
                    print('Aposta: ', qntaposta, 'Saldo: ', SALDO)
                if qntaposta > SALDO:
                    print('Não tem dinheiro suficiente. Volte para o menu de depositos.' )
                    break
        if e_1 == 4:
            while True:
                game_logic()
        
            break
        if e_1 == 3:
            break
        break

def game_logic(duration=2):
    global SALDO
    space = input('Prima barra de espaço para rodar! ')
    num_columns = 5
    num_lines = 5
    horizontal_border = "✨" + "═" * (num_columns * 4 - 1) + "✨"
    if space == ' ':
        end_time = time.time() + duration
        while end_time > time.time():
            reel1 = [[random.choice(SYMBOLS) for _ in range(num_columns)] for _ in range(num_lines)]
            linesto = reel1[num_lines // 2]
            os.system("cls" if os.name == "nt" else "clear")
            for reel in reel1:
                print(" | ".join(reel))
                print(horizontal_border)
            
            time.sleep(0.07)




            

    
    

                
            
            
    
    
    
    
    
    

    




def main():
    
    while True:
        menu_principal()
        try:
            menu = int(input('Escolhe uma opção: '))
        except ValueError:
            print('Insira uma opção válida. "De 1 a 6. "')
            continue
        if menu == 1:
            deposito()
        elif menu == 2:
            levantar()
        elif menu == 3:
            game_menu()
        elif menu == 4:
            versaldo()
            
            
main()           
        
    
    