from .logger import Logger
from .ip_captor import IPCaptor


class QQTracer:
    def __init__(self):
        self.logger = Logger(self.__class__.__name__)
        self.ip_captor = IPCaptor()

    def run(self):
        ip = self.ip_captor.capture()
        self.logger.info(f'Captured IP: {ip}')
