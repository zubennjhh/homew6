import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = 'https://www.playground.ru'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}


@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='item')
    games = []
    for item in items:
        try:
            games.append(
                {
                    'title_url': URL + item.find('a').get('href'),
                    'title_text': item.find('div', class_='media-heading title').get_text(),
                    'release_date': item.find('div', class_='meta-info').find('b').text,
                    'image': item.find('div', class_='gp-game-cover').find('img').get('src'),
                    'rating': item.find('span', class_='value js-game-rating-value').text,
                    'genre': item.find('div', class_='meta-info').find('a').get_text(),
                })
        except AttributeError:
            pass

    return games


@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        games_pg = []
        for page in range(0, 1):
            html = get_html(f'https://www.playground.ru/games', params=page)
            games_pg.extend(get_data(html.text))
        return games_pg
    else:
        raise Exception('Oops, something gone wrong......')
