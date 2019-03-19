from random import sample
from urllib.parse import urljoin

import click
import requests

from .settings import API_KEY, SOURCES, TOP_HEAD

SOURCE_URL = urljoin(SOURCES, '?apiKey={}'.format(API_KEY))

# TODO: Try a deliberate failure to see how the remote API responds
# so that your code knows how to catch those exceptions properly,

sources = requests.get(SOURCE_URL)
if sources.ok:
    source_list = [source['name'] for source in sources.json()['sources']]
    full_sources_list = {
        source['name']: source['id'] for source in sources.json()['sources']
    }

    rand_list = sample(source_list, 4)


@click.command()
def get_news_items():
    """
    This is a script that takes in a choice from you
    our wonderful user and returns the top 10 news
    headlines of the day to you from your source
    of choice.

    choice: A string that should match the names of the sources
    shown on the screen.

    If not, you'll probably get an
    error of some sort. Ideally 'Invalid Choice' but
    you may get something more strange.

    The returned information will contain
    the title, description and link of said headline.
    This shall allow you to follow up on the story
    should you wish to.
    """
    choice = click.prompt(
        'Enter a valid news source from the list shown',
        type=click.Choice(rand_list)
    )

    if choice in rand_list:
        source_id = full_sources_list[choice]

        top_headlines = urljoin(
            TOP_HEAD, '?sources={}&apiKey={}'.format(source_id, API_KEY)
        )

        resp = requests.get(top_headlines).json()

        for news_item in resp['articles']:
            print({
                'title': news_item['title'],
                'description': news_item['description'],
                'url': news_item['url']
            })
    else:
        return 'Invalid Choice'
