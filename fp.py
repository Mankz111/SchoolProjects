
l = []
while True:
    print()
    print( ' Bem-vindo ao menu principal! ')
    print()
    print()
    print('1 - Adicionar à lista. ')
    print('2 - Remover da lista. ')
    print('3 - Modificar a lista. ')
    print('4 - Listar lista. ')
    print('5 - Total de Elementos. ')
    print('6 - Sair. ')
    menu = int(input('Escolha uma opçao! '))
    
    if menu == 1:
        while True:
            add = input('Diga o que quer adicionar. Quando tiver adicionado tudo escreva sair para voltar ao menu. ')
            if add.lower() == 'sair':
                break
            l.append(add)
            
    if menu == 2:
        while True:
            print('A lista atual é a seguinte: ', l)
            remove = input('Diga o que quer remover da lista, quando tudo estiver removido prima "6" para voltar ao menu. ')
            if remove == '6':
                break
            l.remove(remove)
    
    if menu == 3:
        while True:
            print('A lista atual é a seguinte: ', l)
            print('O que deseja modificar nesta lista? ')
            print('Prima 1 - para mudar o indice. ')
            print('Prima 2 - para sair. ')
            modificar = int(input())
            if modificar == 2:
                break
            
            while modificar == 1:
                palavra = input('Introduza a palavra que pretende alterar! ')
                
                if palavra in l:
                    print('Escolheu a palavra - ', palavra)
                    indice = int(input('Em que indice pretende colocar a palavra? '))
                    print('Escolheu o indice', indice)
                    l.remove(palavra)
                    l.insert(indice, palavra)
                    print('Moveu a palavra de sitio. ', l)
                    break
                
    if menu == 4:
        while True:
            print('A sua lista é a seguinte: ')
            print(l)
            s = input('Prima 1 para voltar ao menu principal. ')
            if s == 1:
                break
            
    if menu == 5:
        while True:
            print('A sua lista atual tem estes elementos: ')
            print(len(l))
            s = input('Prima 1 para voltar ao menu principal. ')
            
    if menu == 6:
        print('Até um dia destes! ')        
        break
    else:
        print('Digita um número que esteja na lista! ')
        break
    
    

        
    
        
        
        
                
                
                
                
            
            
        
            
    
        




        














