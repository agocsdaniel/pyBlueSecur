import struct
import hmac
import time

from pybluesecur.ble_utils import _wrap_ble


def sign_command(key, challenge, command, root_id=1, timestamp=int(time.time()), wrap=True):
    fmt = '<HHHQ'
    sig_len = 32
    fmt_len = struct.calcsize(fmt) + sig_len

    msg = struct.pack(fmt, root_id, command, fmt_len, timestamp)  # Packing message
    msg += hmac.new(key, msg + challenge, 'SHA256').digest()  # Signature
    msg = _wrap_ble(msg)
    return msg
