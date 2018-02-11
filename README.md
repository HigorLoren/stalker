# Stalker (web scraping)
A python script that searches and downloads informations about a person

## Getting Started

These instructions will get you a copy of the project up and running on your local machine

### Prerequisites

What things you need to run and how to install them

* Python obviously
* pip
  * bs4 ~> $ pip install bs4
  * resquests ~> $ pip install requests
  * instagram-scraper ~> $ pip install instagram-scraper

### Installing

A step by step that tell you how to use the library in your script

1. Move the [script](stalker.py) to your project folder

2. In your script call the library like this:  
```python
import stalker
```

## Usage

### Downloading Media from Twitter user

This function will **download**:
* Profile picture
* Banner image
* The last media images

```python
stalker.DownloadMedia.twitter(user)
```

### Downloading Media from Instagram user

This function will **download**:
* Profile picture
* Stories
* All the posts

```python
stalker.DownloadMedia.instagram(user)
```

### Getting Information from Twitter user

This function will get a **Dictionary** with:
* Name
* User
* Tweets Count
* Following Count
* Followers Count
* Media Count
* Bio

```python
stalker.GetInformation.twitter(user)
```
## Built With Help Of:
  * [instagram-scraper](https://github.com/rarcega/instagram-scraper) - The library used for instagram media download. Thanks [@rarcega](https://github.com/rarcega)

## Authors

* **Higor Cervelin** - *Initial work* - [HigorCervelin](https://github.com/HigorCervelin)

See also the list of [contributors](https://github.com/HigorCervelin/stalker/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
