from bs4 import BeautifulSoup
from requests import get
from os import makedirs
from re import search, findall
import sys

user = sys.argv[1]
twitter_media_url = f'https://twitter.com/{user}/media'
try:
    dest = ''
    for agv in sys.argv:
        dest = search(r'-d', str(agv))
        if dest:
            dest_p = sys.argv.index(agv)
            destination = sys.argv[dest_p+1]
except:
    pass


try:
    html_page = get(twitter_media_url)
    soup = BeautifulSoup(html_page.text, 'html.parser')

    images = soup.find_all('img')

    profile_picture_list = []
    image_banner_list = []
    image_banner = ''
    profile_picture = ''

    for item in images:
        profile_picture_item = search(r'https://pbs\.twimg\.com/profile_images/.+jpg', str(item))
        profile_picture_list.append(profile_picture_item)
        image_banner_item = search(r'https://pbs\.twimg\.com/profile_banners/.+1500x500', str(item))
        image_banner_list.append(image_banner_item)

    for item in profile_picture_list:
        if item:
            profile_picture = item

    for item in image_banner_list:
        if item:
            image_banner = item

    private_profile = soup.find('span', class_='ProfileHeaderCard-badges')

    print('')

    if private_profile:
        print('Private Profile is not supported')
    if not private_profile:
        try:
            path = destination + f'/{user}_[twitter]'
        except NameError or IndexError:
            path = f'./{user}_[twitter]'

        try:
            makedirs(path)
        except FileExistsError:
            pass

        try:
            profile_picture_link = get(profile_picture.group())
            with open(f"{path}\\Profile.jpg", "wb") as code:
                code.write(profile_picture_link.content)
            print('Profile picture downloaded')
        except AttributeError:
            print('No Profile Pic')

        try:
            image_banner_link = get(image_banner.group())
            with open(f"{path}\\Banner.jpg", "wb") as code:
                code.write(image_banner_link.content)
            print('Banner downloaded')
        except AttributeError:
            print('No Banner')

        try:
            makedirs(f"{path}\\Media\\")
        except FileExistsError:
            pass

        media_posts = soup.findAll('img', src=True)
        i = 0
        count = 0
        for _ in media_posts:
            this_is_link = findall(r'https://pbs\.twimg\.com/media/.+.jpg', str(media_posts[i]))
            if this_is_link:
                for item in this_is_link:
                    count = count + 1
                    print(f'Downloading image #{count}')
                    media_post_link = get(item)
                    with open(f"{path}\\media\\{count}.jpg", "wb") as code:
                        code.write(media_post_link.content)
            i += 1

    print('Downloaded successfully!')
except IndexError:
    print('You must have entered the wrong username.')
