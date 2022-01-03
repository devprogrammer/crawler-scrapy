from api.helpers.spiders.admin_doc_spider import AdminDocSpider


class CASudSainteBaumeSpider(AdminDocSpider):
    """
    Class to parse CA Sud Sainte Baume Website.
    In particular, this class is designed to allow another domain to be visited.
    """

    SPECIAL_URLS = "cdn1.agglo-sudsaintebaume.fr"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_domains.add(self.SPECIAL_URLS)
