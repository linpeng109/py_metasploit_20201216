import json
import os
import sys
import time

from py_3des import TDes
from py_config import ConfigFactory
from py_ip import IPParser
from py_logging import LoggerFactory
from py_outlook_mail import OutlookMail


class GrabData(json.JSONEncoder):
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger



if __name__ == '__main__':
    config_path = 'py_grabrobot.ini'
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    resource_path = os.path.join(base_path, config_path)

    config = ConfigFactory(config=resource_path).getConfig()
    logger = LoggerFactory(config=config).getLogger()
    try:
        if len(sys.argv) >= 2:
            sec_xml = sys.argv[1]

            grab_data = GrabData(config=config, logger=logger)

            ip_parser = IPParser(config=config, logger=logger)
            tdes = TDes(config=config, logger=logger)
            outlook = OutlookMail(config=config, logger=logger)

            data = [{'hostname': ip_parser.get_hostname(),
                     'mac': ip_parser.get_mac_address(),
                     'wan': ip_parser.get_wan(),
                     'ip': ip_parser.get_ip(),
                     'time_samp': time.time(),
                     'sec_xml': sec_xml,
                     # 'sec_xml': r'PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPGFkbWluX3Jlc3BvbnNlPgogPGhhc3A+CiAgPHZlbmRvcmlkPjI4MDY5PC92ZW5kb3JpZD4KICA8aGFzcGlkPjE3OTIxNTQ3Mzg8L2hhc3BpZD4KICA8dHlwZW5hbWU+U2VudGluZWwgSEwgTmV0IDEwPC90eXBlbmFtZT4KICA8bG9jYWw+TG9jYWw8L2xvY2FsPgogIDxsb2NhbG5hbWU+TG9jYWw8L2xvY2FsbmFtZT4KIDwvaGFzcD4KIDxhZG1pbl9zdGF0dXM+CiAgPGNvZGU+MDwvY29kZT4KICA8dGV4dD5TTlRMX0FETUlOX1NUQVRVU19PSzwvdGV4dD4KIDwvYWRtaW5fc3RhdHVzPgo8L2FkbWluX3Jlc3BvbnNlPgoKCg=='
                     }]
            data_msg = json.dumps(data)
            grab_data.logger.debug(data_msg)
            sec_grab_data = tdes.des_encrpt(data_msg)
            sec_message = 'Subject:Data Grabbing Test\n\n data:\n %s' % sec_grab_data
            grab_data.logger.debug(sec_message)

            outlook.sendMail(sec_message)
        else:
            # print('usage:  py_grabrobot <sec_xml>')
            pass
    except Exception as e:
        logger.error(e)
