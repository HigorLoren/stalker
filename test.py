from stalker import DownloadMedia
import os


def twitter_window():
    print('Twitter\n')
    user = input('User: ')
    print(DownloadMedia.twitter(user))

    input('Enter to continue...')
    main_screen()


def facebook_window():
    print('Working on it\n')

    input('Enter to continue...')
    main_screen()


def instagram_window():
    print('Instagram\n')
    print('Login with your account [1]')
    print('Download pictures from an account [2]')
    print('\nClose [0]')
    option = input('\nYour option: ')

    if option == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            arquivo = open('login-insta.txt', 'r+')
            arquivo.truncate()
        except FileNotFoundError:
            arquivo = open('login-insta.txt', 'w+')

        print('\nYour account login and password:')
        login = input('\nUser: ')
        password = input('Password: ')
        print('Your data will be saved only in your computer in a text file')
        arquivo.write(f' -u {login} -p {password}')
        arquivo.close()

        input('Enter to continue...')
        main_screen()
    elif option == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        user = input('\nProfile that will be downloaded: ')
        print(DownloadMedia.instagram(user))
        input('Enter to continue...')
        main_screen()
    else:
        main_screen()


def main_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\nStalker\n')
    print('Twitter   [1]')
    print('Facebook  [2]')
    print('Instagram [3]')
    print('\nClose   [0]')
    opcao = input('\nYour option: ')

    os.system('cls' if os.name == 'nt' else 'clear')

    if opcao == '1':
        twitter_window()
    elif opcao == '2':
        facebook_window()
    elif opcao == '3':
        instagram_window()
    else:
        exit()


main_screen()
