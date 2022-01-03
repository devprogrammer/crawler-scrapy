from api.helpers.spiders.admin_doc_spider import AdminDocSpider


class ArlesSpider(AdminDocSpider):
    """
    Class to parse CA de Haguenau Website.
    In particular, this class is designed to allow another domain to be visited.
    """

    SPECIAL_URLS = "deliberations.arles.fr"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_domains.add(self.SPECIAL_URLS)
