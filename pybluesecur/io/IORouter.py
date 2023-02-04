from .variants.EmptyIO import EmptyIO
from .variants.SignedIO import SignedIO
# from pybluesecur.io.EncryptedIO import EncryptedIO
# from pybluesecur.io.BlueControlIO import BlueControlIO


class IORouter:
    NONE = 0
    SIGNED_IO = 1
#    ENCRYPTED_IO = 2
#    BLUECONTROL_IO = 3

    _classes = {
        NONE: EmptyIO,
        SIGNED_IO: SignedIO
    }

    @staticmethod
    def IoServiceById(_id):
        if _id in IORouter._classes:
            return IORouter._classes[_id]

    @staticmethod
    def IoServiceByAction(action: int):
        return IORouter.IoServiceById(((16711680 & action) >> 16))
