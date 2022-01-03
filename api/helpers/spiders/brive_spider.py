# -*- coding: utf-8 -*-
from scrapy.http.request import Request

from api.helpers.spiders.admin_doc_spider import AdminDocSpider

from api.models.admin_doc_item import AdminDocItem
from config.definitions import Cst


class BriveParser(AdminDocSpider):

    uid = "FRCOMM19031"
    name = "brive_spider"
    SPECIAL_URLS = ["http://www.brive.fr/"]
    urlMap = {"http://www.brive.fr/": True, "http://www.brive.fr": True}

    def parse_response(self, response):
        if response.url in self.SPECIAL_URLS:
            yield from self.parse_special_url(response)
        super().parse_response(response)

    def handle_pdf(self, url):
        if url not in self.urlMap:
            self.urlMap[url] = True
            self.add_to_collected_url(url)

            yield AdminDocItem(
                url=url,
                responseMimeContentType=Cst.PDF_CONTENT_TYPE,
                locations=self.locations,
                dataProvider=self.start_url,
                operationId=self.operation_uid,
            )

    def parse_special_url(self, response):
        urls = response.css("a::attr(href)").extract()
        row_data = zip(urls)

        file_pattern = "://"
        for item in row_data:
            if file_pattern in item[0]:
                url = item[0]
            else:
                url = "http://www.brive.fr/" + item[0]

            if ".pdf" in url:
                self.handle_pdf(url)

            if (
                (url not in self.urlMap)
                and (".jpg" not in url)
                and (".JPG" not in url)
                and (".mp3" not in url)
                and (".mp4" not in url)
                and (".png" not in url)
                and (".docx" not in url)
            ):
                yield Request(url, self.parse)
                self.urlMap[url] = True