def mostrar_menu():
    print('\n Bem-vindo ao menu principal! ')
    print('\n')
    print('1 - Adicionar à lista.')
    print('2 - Remover da lista.')
    print('3 - Modificar a lista.')
    print('4 - Listar lista.')
    print('5 - Total de Elementos.')
    print('6 - Sair.')


def adicionar_lista(lista):
    while True:
        add = input('Diga o que quer adicionar. Quando tiver adicionado tudo escreva "sair" para voltar ao menu. ')
        if add.lower() == 'sair':
            break
        lista.append(add)
        print('A lista atual e: ', lista)


def remover_lista(lista):
    while True:
        print('A lista atual é a seguinte: ', lista)
        remove = input('Diga o que quer remover da lista, ou escreva "sair" para voltar ao menu: ')
        if remove.lower() == 'sair':
            break
        if remove in lista:
            lista.remove(remove)
        else:
            print('O elemento não está na lista.')


def modificar_lista(lista):
    while True:
        print('A lista atual é a seguinte: ', lista)
        print('O que deseja modificar nesta lista? ')
        print('1 - Alterar o índice de um elemento.')
        print('2 - Sair.')
        modificar = int(input('Escolha uma opção: '))

        if modificar == 2:
            break

        if modificar == 1:
            palavra = input('Introduza a palavra que pretende alterar: ')
            if palavra in lista:
                print('Escolheu a palavra - ', palavra)
                indice = int(input('Em que índice pretende colocar a palavra? '))
                if 0 <= indice <= len(lista):
                    lista.remove(palavra)
                    lista.insert(indice, palavra)
                    print('Moveu a palavra de sítio: ', lista)
                else:
                    print('Índice inválido.')
            else:
                print('A palavra não está na lista.')


def listar_lista(lista):
    print('A sua lista é a seguinte: ')
    print(lista)


def total_elementos(lista):
    while True:
        te = int(input('Bem-vindo ao menu "total de elementos. " Prima "1" para verificar quantos números contem a sua lista ou prima "2", para voltar ao menu principal. ' ))
        if te == 1:
            print('A tua lista atual tem', len(lista), 'elementos. ')
        elif te == 2:
            break
        else:
            print('Insere um número valido! ')
        


def main():
    lista = []

    while True:
        mostrar_menu()
        try:
            menu = int(input('Escolha uma opção: '))
        except ValueError:
            print('Insira um número válido!')
            continue

        if menu == 1:
            adicionar_lista(lista)
        elif menu == 2:
            remover_lista(lista)
        elif menu == 3:
            modificar_lista(lista)
        elif menu == 4:
            listar_lista(lista)
        elif menu == 5:
            total_elementos(lista)
        elif menu == 6:
            print('Até um dia destes!')
            break
        else:
            print('Insira um número de 1 a 6.')


main()