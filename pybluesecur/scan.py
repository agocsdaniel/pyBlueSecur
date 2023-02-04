import asyncio

from bleak import BleakScanner
from pybluesecur.constants import MANUFACTURER_ID


async def scan(timeout=2):
    addresses = set()

    def new_device(dev, adv):
        if MANUFACTURER_ID in adv.manufacturer_data:
            addresses.add(dev.address)

    b = BleakScanner(detection_callback=new_device)

    await b.start()
    await asyncio.sleep(timeout)
    await b.stop()
    return list(addresses)



