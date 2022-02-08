from ex115_Criando_um_menu_python.lib.interface import *
from ex115_Criando_um_menu_python.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrarArq(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema
        cabecalho('Saindo do sistema... até logo!')
    else:
        # Digitou uma opção errada no menu
        cabecalho('Erro')
    sleep(2)