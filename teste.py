import random
import time

SYMBOLS = ["🍒", "🍋", "🍉", "⭐", "💎"]

def spinning_animation(duration=2):
    """Mostra uma animação simulando o giro dos rolos da slot."""
    end_time = time.time() + duration  # Define o tempo final para girar
    while time.time() < end_time:
        slots = [random.choice(SYMBOLS) for _ in range(5)]  # Gera símbolos aleatórios
        print("\r" + " | ".join(slots), end="")  # Sobrescreve a mesma linha
        time.sleep(0.1)  # Pausa curta para criar a animação
    print()  # Move para a próxima linha após a animação

def spin_slots():
    """Simula o resultado final da slot machine."""
    spinning_animation()  # Animação de giro
    result = [random.choice(SYMBOLS) for _ in range(3)]  # Resultado final
    print("Resultado final: " + " | ".join(result))  # Mostra o resultado
    return result

# Exemplo de uso
if __name__ == "__main__":
    print("🎰 Iniciando o jogo de slot...")
    spin_slots()