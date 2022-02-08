import shutil


def escrever_arquivo(texto):
    arquivo = open('texto.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('texto.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo, 'local para a cópia')

def move_arquivo(nome_arquivo):
    import shutil
    shutil.move(nome_arquivo, 'local que será movido')