from .logger import Logger


class IPLocator:
    def __init__(self):
        self.logger = Logger(self.__class__.__name__)

    def locate(self, ip: str):
        pass
    # TODO: find a proper way to locate by IP


