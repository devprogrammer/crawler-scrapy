import datetime
from bs4 import BeautifulSoup
import re
import requests

from api.helpers.spiders.admin_doc_spider import AdminDocSpider

from urllib.parse import urlencode

from api.models.admin_doc_item import AdminDocItem
from config.definitions import Cst


class BesaconSpider(AdminDocSpider):
    """
    Class to parse besacon Website. In particular, this class is designed to retrieve documents
    from the search engine.
    """

    SPECIAL_URLS = ["https://www.besancon.fr/la-ville/conseil-municipal/deliberations-ville-de-besancon/"]
    config = {
        'headers': {
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'iframe',
            'Referer': 'https://data.grandbesancon.fr/opendata/dataset/conseilsMunicipaux/embed/1',
            'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        }
    }

    def parse_special_url(self, response):
        """Parse response from the search engine."""
        now = datetime.datetime.now()
        year = now.year
        while True:

            try:
                response = requests.get(f'https://data.grandbesancon.fr/opendata/dataset/conseilsMunicipaux/embed/1/year/{year}', headers=self.config.headers)
                soup = BeautifulSoup(response.content, 'html.parser')
                
                table = soup.find('table', {
                    'class' : 'table table-condensed table-bordered table-hovered'
                })
                trs = table.find_all('tr')
            except AttributeError:
                break
            for tr in trs:
                link = tr.find('a')['href']
                yield self.yield_special_items(link)
            year = year - 1

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
