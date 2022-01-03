from api.helpers.spiders.admin_doc_spider import AdminDocSpider


class CAFougeresAgglomerationSpider(AdminDocSpider):
    """
    Class to parse CA Fougère Agglomération Website.
    In particular, this class is designed to allow another domain to be visited.
    """

    SPECIAL_URLS = "fougeres-agglo.bzh"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_domains.add(self.SPECIAL_URLS)
