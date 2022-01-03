from scrapy.http import FormRequest

from api.helpers.spiders.admin_doc_spider import AdminDocSpider

from api.models.admin_doc_item import AdminDocItem
from config.definitions import Cst


class CAduPaysdeMontbeliardSpider(AdminDocSpider):

    SPECIAL_URLS = ["http://www.agglo-montbeliard.fr/#!/lagglo-kezako/les-instances-communautaires/les-actes"
                  "-administratifs.html"]
    BASE_URL = "http://www.agglo-montbeliard.fr/geideweb/deliberation.php"
    DOCUMENT_URL = "http://www.agglo-montbeliard.fr/geideweb/"

    formdata = {
        'criteres': '',
        'bureau': 'Délibération du bureau'.encode('ISO-8859-1'),
        'conseil': 'Délibération du conseil'.encode('ISO-8859-1'),
        'arretes': 'Arrêté'.encode('ISO-8859-1'),
        'recherche': '1'
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }

    def parse_response(self, response):
        if response.url in self.SPECIAL_URLS:
            yield FormRequest(
                url=self.BASE_URL,
                formdata=self.formdata,
                headers=self.headers,
                callback=self.yield_special_item,
            )
        super().parse_response(response)

    def yield_special_item(self, response):
        link_attrs = response.xpath(('//*[contains(@target, "_new")]/@href')).extract()

        for link_attr in link_attrs:
            download_url = self.DOCUMENT_URL + link_attr

            self.logger.debug("Found an accepted document: %s", download_url)
            self.add_to_collected_url(download_url)
            self.item_yielder.save_line(download_url)

            yield AdminDocItem(
                url=download_url,
                responseMimeContentType=Cst.PDF_CONTENT_TYPE,
                locations=self.locations,
                dataProvider=self.start_url,
                operationId=self.operation_uid,
            )

