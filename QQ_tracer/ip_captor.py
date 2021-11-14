import re

from pyshark import LiveCapture

from .logger import Logger


def _is_private_ip(ip: str):
    return re.search(
        pattern=r'(^127\.)|(^10\.)|(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)|(^192\.168\.)',
        string=ip,
    ) is not None


class IPCaptor:
    def __init__(self):
        self.logger = Logger(self.__class__.__name__)

    def capture(self) -> str:
        capture = LiveCapture(
            bpf_filter=f'udp',
            display_filter='udp.payload[0:3]==02:00:48',
        )
        for p in capture.sniff_continuously():
            ip_list = [p.ip.src, p.ip.dst]
            self.logger.debug(f'Captured a package with src_ip: {ip_list[0]}, dst_ip: {ip_list[1]}')
            for ip in ip_list:
                if _is_private_ip(ip):
                    continue
                return ip

