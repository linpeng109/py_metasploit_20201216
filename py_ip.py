import socket
import uuid

import requests

import re


class IPParser:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def get_hostname(self):
        hostname = socket.gethostname()
        return socket.getfqdn(hostname)

    def get_ip(self):
        hostname = self.get_hostname()
        return socket.gethostbyname(hostname)

    def get_mac_address(self):
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])

    def get_wan(self):
        html_text = requests.get("https://ip.cn/").text
        ip_text = re.search(u"<span>Your IP</span>: (.*?)</span>", html_text)
        return ip_text.group(1)
        # return html_text

    def get_domain(self):
        html_text = requests.get("https://site.ip138.com/").text
        # ip_text = re.search(u"<span>Your IP</span>: (.*?)</span>", html_text)
        # return ip_text.group(1)
        return html_text


if __name__ == '__main__':
    ipparser = IPParser()
    print(ipparser.get_mac_address())
    print(ipparser.get_hostname())
    print(ipparser.get_ip())
    print(ipparser.get_wan())
    # print(ipparser.get_domain())
