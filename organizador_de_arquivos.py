import os
import shutil

nolvl = "Livro "
caminho = r'C:\Users\xxxxx' # Aqui é o caminho do diretório onde vai ser organizado o(s) arquivo(s).

arquivos = []
for arquivo in os.listdir(caminho):
    # Monta o caminho completo ate o arquivo
    nomearquivo = os.path.join(caminho, arquivo)

    # Se o arquivo for arquivo mesmo, inclui na lista
    if os.path.isfile(nomearquivo):
        arquivos.append(arquivo)

for arquivo in arquivos:
    nomearquivo, nlv = os.path.splitext(arquivo)
    nolv, nlv, flv, elv = (nomearquivo.split('-'))

    nlv = nlv[1:]
    if os.path.exists(caminho + '/' +nolvl+ nlv):
        shutil.move(caminho + '/' + arquivo, caminho + '/' + nolvl + nlv)
    else:
        os.makedirs(caminho + '/' + nolvl + nlv)
        shutil.move(caminho + '/' + arquivo, caminho + '/' +nolvl + nlv)
