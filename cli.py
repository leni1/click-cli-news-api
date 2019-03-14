from urllib.parse import urljoin

import click
import requests

from settings import API_KEY, SOURCES, TOP_HEAD


SOURCE_URL = urljoin(SOURCES, '?apiKey={}'.format(API_KEY))

# @click.command()
# @click.option('--choice', default='', help='Choose a news source')
sources = requests.get(SOURCE_URL)
if sources.ok:
    sources_list = [source['name'] for source in sources.json()['sources']]
    full_sources_list = {
        source['name']: source['id'] for source in sources.json()['sources']
    }


def get_news_items(choice, choices):
    if choice in choices:
        source_id = choices[choice]
        top_headlines = urljoin(
            TOP_HEAD, '?sources={}&apiKey={}'.format(source_id, API_KEY)
            )
        resp = requests.get(top_headlines).json()
        for news_item in resp['articles']:
            print(
                {
                    'title': news_item['title'],
                    'description': news_item['description'],
                    'url': news_item['url']
                }
            )
    else:
        return 'Invalid Choice'


if __name__ == '__main__':
    print(sources_list[:4])
    user_choice = input("Enter your choice: ").rstrip()
    get_news_items(user_choice, full_sources_list)
