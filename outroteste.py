import random
import time

SYMBOLS = ["🍒", "🍋", "🍉", "⭐", "💎"]

def move_cursor_up(lines):
    # Move o cursor para cima no terminal
    print(f"\033[{lines}A", end="")

def game_logic(duration=2):
    end_time = time.time() + duration
    num_lines = 5  # Quantidade de rolos a serem exibidos
    
    # Inicializar linhas no terminal
    reels = [[random.choice(SYMBOLS) for _ in range(5)] for _ in range(num_lines)]
    for reel in reels:
        print(" | ".join(reel))
    
    while end_time > time.time():
        # Atualizar os rolos
        reels = [[random.choice(SYMBOLS) for _ in range(5)] for _ in range(num_lines)]
        
        # Mover o cursor para o topo das linhas
        move_cursor_up(num_lines)
        
        # Imprimir os novos valores dos rolos
        for reel in reels:
            print(" | ".join(reel))
        
        # Pausa para criar o efeito de rotação
        time.sleep(0.1)

# Chamar o jogo
game_logic()