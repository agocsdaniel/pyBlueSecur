import struct
from typing import Union


def _wrap_ble(data: Union[bytearray, bytes], identifier=1):
    outer_fmt = '<bH'
    outer_fmt_len = struct.calcsize(outer_fmt) + len(data)
    return struct.pack(outer_fmt, identifier, outer_fmt_len) + data
