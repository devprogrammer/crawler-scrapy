import datetime
from bs4 import BeautifulSoup
import re
import requests

from api.helpers.spiders.admin_doc_spider import AdminDocSpider

import re
from urllib.parse import urlencode

from api.models.admin_doc_item import AdminDocItem
from config.definitions import Cst


class AmpMetropoleSpider(AdminDocSpider):
    """
    Class to parse ampmetropolespider Website. In particular, this class is designed to retrieve documents
    from the search engine.
    """

    SPECIAL_URLS = ["https://www.ampmetropole.fr/les-seances"]
    config = {
        'headers': {
            'authority': 'deliberations.ampmetropole.fr',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'iframe',
            'referer': 'https://deliberations.ampmetropole.fr/2?typeDocument=DELIBERATION&domaine=METROPOLE',
            'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'params' : (
                        ('typeDocument', 'DELIBERATION'),
                        ('domaine', 'METROPOLE'),
                    )
        }
    }

    def parse_special_url(self, response):
        """Parse response from the search engine."""
        i = 1
        while True:
            i = i+1
            response = requests.get(f'https://deliberations.ampmetropole.fr/{i}', headers=self.config.headers, params=self.config.params)

            soup = BeautifulSoup(response.content, 'html.parser')

            cards = soup.find_all('div', {
                'class' : 'card w-100'
            })
            if not len(cards):
                break

            for card in cards:
                links = card.find_all('p', {
                    'class' : 'm-1'
                })
                for link in links:

                    link = link.find('a')['href']
                    link = f'https://deliberations.ampmetropole.fr{link}'
                    yield self.yield_special_items(link)


    def yield_special_items(self, url):
        self.logger.debug("Found an accepted document: %s", url)
        self.add_to_collected_url(url)
        return AdminDocItem(
            url=url,
            responseMimeContentType=Cst.PDF_CONTENT_TYPE,
            locations=self.locations,
            dataProvider=self.start_url,
            operationId=self.operation_uid,
        )
