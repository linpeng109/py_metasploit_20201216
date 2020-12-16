import binascii
import sys

import pyDes

from py_config import ConfigFactory
from py_logging import LoggerFactory


class TDes:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

        self.secret_key = config.get('3des', 'secret_key').encode(config.get('3des', 'encode'))

    def des_encrpt(self, str):
        key = pyDes.des(self.secret_key, pyDes.triple_des, pad=None, padmode=pyDes.PAD_PKCS5)
        en = key.encrypt(str.encode('utf8'), padmode=pyDes.PAD_PKCS5)
        return binascii.b2a_base64(en)

    def des_descrpt(self, str):
        key = pyDes.des(self.secret_key, pyDes.triple_des, pad=None, padmode=pyDes.PAD_PKCS5)
        de = key.decrypt(binascii.a2b_base64(str))
        return de


if __name__ == '__main__':
    config = ConfigFactory(config='py_grabrobot.ini').getConfig()
    logger = LoggerFactory(config=config).getLogger()
    try:

        if len(sys.argv) >= 2:
            sec_xml = sys.argv[1]
            tdes = TDes(config, logger)

            en = b'mVbUkybTYtPzXEaS0HchD2kLAs3FRz76AUTmbR8Mat6KlYCUebpcY8wV1W50zFfFbWsYHjPAH6O+VJEsM41J5IrQHJqoMhBv8K2L7xzD3ewDHT9VczX6dLVUw9mxS9PlOZXWQEpXze+4m9JIE7KKVT2n58g4ew45PIM8TNEFonmOZwgLUfSJMA7wkPJq+MD5Euxctrqc5/YEGX8y5FkeTZBQKW8mG9lEDlr2Zkp4W+NPn5MpF7Mqn4jhW4DXDBMnes1Wqz3Fu57VXLQibOK5uxlMEerb2/FLqdT50SFnURIiU4cY4opGLh9Nhdu3NSUML/0opOxs3gLgapjAikGzSnsUgw1jttE+A50tiq5ofn6vw7aH5fUqLGI7YIzYdbuWHAhQW++xgTCTOncejlTvHMEulMclHxNteOkvGcuFDc7oe/4UqbLFCh2gy2ybw2nlN7oBCIBcHqPNT6ey2Qo5YREgPMzRD8auJhG581uzxf6cgwq2/poOB25LK/WgE2IMp1DDKO6/pJSEmfJsbwSDGn8lS2pMVfxw+A95nNzVZ7G1x0i53SBwoC8PpJQi4bsq3+VL8DCglwmQ6MH1Y9HXay1uto5I8qB2fv3rMFqoQ5D2sclvGe2AEOujV+B4CrJW4E52hTDpPaJU8e1WV7GqmdzesQhR9OdMexywQkelNQYMk8xGzXUFLh1nxW0eZAlRrmU3GxADYBRFBw7XRIhEBDSDzG2SQuDyZe4gzcC92G/a4XDcehOiz4SGgBaLF4ohGUwR6tvb8Uup1PnRIWdREnVv0nRdTacs9lFykAGTKm8=\n'
            de = tdes.des_descrpt(sec_xml)
            print('de=%s' % de)
        else:
            print('usage:  py_3des.exe <crypt_string>')
    except Exception as e:
        logger.error(e)
