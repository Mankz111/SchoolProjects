import random
import time
import shutil  # Para obter o tamanho do terminal dinamicamente

SYMBOLS = ["🍒", "🍋", "🍉", "⭐", "💎"]

def move_cursor_up(lines):
    print(f"\033[{lines}A", end="")  # Move o cursor para cima

def check_win(line):
    return all(symbol == line[0] for symbol in line)

def center_text(text, width):
    """Centraliza o texto baseado na largura do terminal."""
    padding = max((width - len(text)) // 2, 0)
    return " " * padding + text

def game_logic(duration=2):
    end_time = time.time() + duration
    num_lines = 5  # Quantidade de rolos
    num_columns = 5  # Quantidade de símbolos por rolo
    
    # Obter largura do terminal
    terminal_width = shutil.get_terminal_size().columns
    
    # Inicializar borda
    horizontal_border = "+" + "-" * (num_columns * 4 - 1) + "+"
    horizontal_border_centered = center_text(horizontal_border, terminal_width)
    
    while end_time > time.time():
        # Gerar os rolos
        reels = [[random.choice(SYMBOLS) for _ in range(num_columns)] for _ in range(num_lines)]
        
        # Escolher uma linha para destacar (linha central)
        line_to_check = reels[num_lines // 2]
        
        # Limpar a tela
        print("\033[H\033[J", end="")  # Limpar a tela sem flicker
        
        # Imprimir o conteúdo do jogo com borda e centralizado
        print(horizontal_border_centered)
        for i, reel in enumerate(reels):
            line_content = "| " + " | ".join(reel) + " |"
            if i == num_lines // 2:  # Destacar a linha central
                line_content = "> " + " | ".join(reel) + " <"
            print(center_text(line_content, terminal_width))
        print(horizontal_border_centered)
        
        # Verificar se a linha central é vencedora
        if check_win(line_to_check):
            result = "🎉 Parabéns! Você ganhou! 🎉"
        else:
            result = "💔 Não foi desta vez. Tente novamente!"
        print(center_text(result, terminal_width))
        
        # Pausa para o próximo ciclo
        time.sleep(0.5)

# Chamar o jogo
game_logic()