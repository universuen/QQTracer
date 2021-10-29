# from ._logger import Logger
#
#
# class IPLocator:
#     def __init__(self):
#         self.logger = Logger(self.__class__.__name__)
#
#     def locate(self, ip: str):


if __name__ == '__main__':
    from geoip import geolite2
    print(geolite2.lookup('61.158.208.81').location)