""" Base error class for throwing scraping-specific errors """


class WebScraperError(Exception):

    @property
    def message(self):
        """ Returns provided message to construct error """
        return self.args[0]
