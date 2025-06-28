from util.tools import *

def mainlist():
    arq = 'contatos.txt'
    try:
        open('contatos.txt').close()
    except FileNotFoundError:
        open('contatos.txt', 'at+').close()
        print('arquivo contatos foi criado.')
    else:
        print(f'Arquivo {arq} encontrado.')


    while True:
        opt = menu(['Adicionar contato', 'Apresentar contatos salvos', 'Sair'])
        if opt == 1:
            titulo('NOVO CONTATO')
            nome = str(input('Nome: '))
            tel = str(input('Telefone: '))
            mail = str(input('E-mail: '))
            cadastrar(arq, nome, tel, mail)
        elif opt == 2:
            abrir_lista(arq)
        elif opt == 3:
            titulo('FINALIZADO')
            break
if __name__ == '__main__':
    mainlist()
