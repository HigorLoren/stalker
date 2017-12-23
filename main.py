from bs4 import BeautifulSoup
from random import randint
import requests, os, os.path, re, winshell, time


# Functions
def user_input_twitter():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n\tType the twitter username (exit to close)\n')
    user = input('User:\t')
    twitter(user)


def twitter(user):

    if user == 'exit':
        exit()
    twitter_media_url = 'https://twitter.com/' + user + '/media'

    os.system('cls' if os.name == 'nt' else 'clear')
    print('\tDownloading...')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\tThis may take a while...')

    try:
        html_page = requests.get(twitter_media_url)
        soup = BeautifulSoup(html_page.text, 'html.parser')

        soup_images = soup.find_all('img')
        profile_picture = re.search(r'https://pbs\.twimg\.com/profile_soup_images/.+jpg', str(soup_images[4]))
        profile_picture_link = requests.get(profile_picture.group())
        user_name = soup.find_all('a', class_='ProfileHeaderCard-nameLink u-textInheritColor js-nav')[0].get_text()

        session_code = str(randint(0, 999))

        os.makedirs(desktop_path + '/Profiles/@' + user + ' (' + user_name + ') #' + session_code)
        with open(desktop_path + "/Profiles/@" + user + " (" + user_name + ") #" + session_code + "/1profile.jpg", "wb") as code:
            code.write(profile_picture_link.content)

        image_banner = re.search(r'https://pbs\.twimg\.com/profile_banners/.+1500x500', str(soup_images[3]))
        if image_banner:
            image_banner_link = requests.get(image_banner.group())
            with open(desktop_path + "/Profiles/@" + user + " (" + user_name + ") #" + session_code + "/2banner.jpg", "wb") as code:
                code.write(image_banner_link.content)

        private_profile = soup.find('span', class_='ProfileHeaderCard-badges')

        comments = []

        if private_profile:
            comments.append('Private Profile')
        if not private_profile:
            os.makedirs(desktop_path + '/Profiles/@' + user + ' (' + user_name + ') #' + session_code + "/Media/")
            soup_posts_imgs = soup.findAll('img', src=True)
            i = 0
            count = 0
            for x in soup_posts_imgs:
                this_is_link = re.findall(r'https://pbs\.twimg\.com/media/.+.jpg', str(soup_posts_imgs[i]))
                if this_is_link:
                    for item in this_is_link:
                        count = count + 1
                        post_img_link = requests.get(item)
                        with open(desktop_path + "/Profiles/@" + user + " (" + user_name + ") #" + session_code + "/media/" + str(count) + ".jpg", "wb") as code:
                            code.write(post_img_link.content)
                i += 1
        for comment in comments:
            print(comment)

        title = None
        for i in range(0, len(soup.title.string)):
            title = soup.title.string.replace(" | Twitter", "")
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Profile picture, banner and ' + title + '\nsuccessfully downloaded!')
    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Oops, an error has occurred.')
        print('You must have entered the wrong username.')
        print('\nThe program will restart in seconds...')
        time.sleep(5)
        user_input_twitter()


# Program Start
desktop_path = winshell.desktop()
user_input_twitter()
