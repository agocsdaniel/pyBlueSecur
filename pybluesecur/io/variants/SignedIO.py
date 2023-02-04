import struct
import hmac
import time

from pybluesecur.ble_utils import _wrap_ble
from .EmptyIO import EmptyIO


class SignedIO(EmptyIO):
    def __init__(self, key, challenge):
        self._key = key
        self._challenge = challenge

    def write_command(self, command, root_id=1, timestamp=int(time.time())):
        fmt = '<HHHQ'
        sig_len = 32
        fmt_len = struct.calcsize(fmt) + sig_len
        command = command & 0xffff

        msg = struct.pack(fmt, root_id, command, fmt_len, timestamp)  # Packing message
        msg += hmac.new(self._key, msg + self._challenge, 'SHA256').digest()  # Signature
        msg = _wrap_ble(msg)
        return msg
