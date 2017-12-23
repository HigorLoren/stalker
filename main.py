# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from random import randint
import requests, os, os.path, re, winshell, time


# Funcoes
def entrada_dados_twitter():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n\tDigite o usuário do twitter (exit para sair)\n')
    usuario = input('Usuário:\t')
    twitter(usuario)


def twitter(usuario):

    if usuario == 'exit':
        exit()
    page_link = 'https://twitter.com/' + usuario + '/media'

    os.system('cls' if os.name == 'nt' else 'clear')
    print('\tBaixando...')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\tIsto pode demorar um pouco...')

    try:
        html_page = requests.get(page_link)
        soup = BeautifulSoup(html_page.text, 'html.parser')

        imagens = soup.find_all('img')
        imagem_perfil = re.search(r'https://pbs\.twimg\.com/profile_images/.+jpg', str(imagens[4]))
        imagem_perfil_link = requests.get(imagem_perfil.group())
        nome = soup.find_all('a', class_='ProfileHeaderCard-nameLink u-textInheritColor js-nav')[0].get_text()

        sessao = str(randint(0, 999))

        os.makedirs(desktop_caminho + '/Perfis/@' + usuario + ' (' + nome + ') #' + sessao)
        with open(desktop_caminho + "/Perfis/@" + usuario + " (" + nome + ") #" + sessao + "/1perfil.jpg", "wb") as code:
            code.write(imagem_perfil_link.content)

        imagem_banner = re.search(r'https://pbs\.twimg\.com/profile_banners/.+1500x500', str(imagens[3]))
        if imagem_banner:
            imagem_banner_link = requests.get(imagem_banner.group())
            with open(desktop_caminho + "/Perfis/@" + usuario + " (" + nome + ") #" + sessao + "/2banner.jpg", "wb") as code:
                code.write(imagem_banner_link.content)

        perfil_bloqueado = soup.find('span', class_='ProfileHeaderCard-badges')

        observacoes = []

        if perfil_bloqueado:
            observacoes.append('Perfil Privado')
        if not perfil_bloqueado:
            os.makedirs(desktop_caminho + '/Perfis/@' + usuario + ' (' + nome + ') #' + sessao + "/Media/")
            images_postadas = soup.findAll('img', src=True)
            i = 0
            cont = 0
            for x in images_postadas:
                this_is_link = re.findall(r'https://pbs\.twimg\.com/media/.+.jpg', str(images_postadas[i]))
                if this_is_link:
                    for item in this_is_link:
                        cont = cont + 1
                        imagem_postada_link = requests.get(item)
                        with open(desktop_caminho + "/Perfis/@" + usuario + " (" + nome + ") #" + sessao + "/media/" + str(cont) + ".jpg", "wb") as code:
                            code.write(imagem_postada_link.content)
                i += 1
        for observacao in observacoes:
            print(observacao)

        titulo = None
        for i in range(0, len(soup.title.string)):
            titulo = soup.title.string.replace(" | Twitter", "")
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Imagem de perfil, banner e ' + titulo + '\nbaixados com sucesso!')
    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Ops, aconteceu um erro')
        print('Você deve ter digitado o nome de usuário errado...')
        print('\nO programa irá reiniciar em segundos...')
        time.sleep(5)
        entrada_dados_twitter()


# Começo do algoritmo
desktop_caminho = winshell.desktop()
entrada_dados_twitter()
