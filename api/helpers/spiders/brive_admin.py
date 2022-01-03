# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

from api.helpers.spiders.admin_doc_spider import AdminDocSpider

from api.models.admin_doc_item import AdminDocItem
from config.definitions import Cst


class BriveAdminParser(AdminDocSpider):

    uid = "FRCOMM19031_1"
    name = "brive_admin"
    SPECIAL_URLS = [("http://scripting.brive.fr/brive/deliberations/ajax.php?SEA=annee{year}&rnd=1632892897")]

    headers = {
        "user-agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
        )
    }

    def parse(self, _):
        for i in range(2005, 2022) :
            response = requests.get(
                self.SPECIAL_URLS[0].format(year = i),
                headers=self.headers
            ).content

            soup = BeautifulSoup(response, 'html.parser')

            atags = soup.find_all("a")
            for atag in atags:
                if(".pdf" in atag["href"]) or (".PDF" in atag["href"]):
                    url = "http://www.brive.fr" + atag["href"]
                    self.logger.debug("Found an accepted document: %s", url)
                    self.add_to_collected_url(url)

                    yield AdminDocItem(
                        url=url,
                        responseMimeContentType=Cst.PDF_CONTENT_TYPE,
                        locations=self.locations,
                        dataProvider=self.start_url,
                        operationId=self.operation_uid,
                    )