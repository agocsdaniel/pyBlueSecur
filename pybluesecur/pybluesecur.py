import asyncio

from bleak import BleakScanner, BleakClient, BleakGATTCharacteristic

from pybluesecur.cache import Cache
from pybluesecur.command import BlueSecurCommand
from pybluesecur.constants import BC_TX, BC_RX
from pybluesecur.io.IORouter import IORouter
from pybluesecur.log import Logger
from pybluesecur.scan import scan


class PyBlueSecur:
    Commands = BlueSecurCommand.Commands

    def __init__(self, address=None, key=None, register_key=None,
                 ble_client_backend=BleakClient, ble_scanner_backend=BleakScanner):
        self._logger = Logger().get_logger()
        self._cache = Cache()
        self._client: BleakClient = None

        self.scan = scan

        self.address = address

        self._key = bytearray.fromhex(key)
        if not self._key:
            self._logger.info('No authentication key specified, you have to set it to be able to connect')

    def notification_handler(self, characteristic: BleakGATTCharacteristic, data: bytearray):
        self._logger.debug(f"RECV notify: {characteristic.description} - {data.hex()}")
        if data[:3] == bytes.fromhex('010f00'):
            self._cache.challenge = data[3:][:8]
            # if _challenge != b'\0\0\0\0\0\0\0\0':
            #    challenge = _challenge
            self._logger.info(f'Challenge: {self._cache.challenge.hex()}')

    async def connect(self):
        if not self.address:
            self._logger.info('No address specified, you must scan and set it before connecting')
            return

        self._client = BleakClient(self.address)
        if not self._client.is_connected:
            await self._client.connect()
            await self._client.start_notify(BC_RX, self.notification_handler)

        while not self._cache.challenge:
            await asyncio.sleep(0.1)

    async def write_gatt(self, data):
        return await self._client.write_gatt_char(BC_TX, data)

    async def sendCommand(self, command: int):
        io = IORouter.IoServiceByAction(command)(key=self._key, challenge=self._cache.challenge)
        data = io.write_command(command=command)
        print('Sending', data.hex())
        try:
            await self.write_gatt(data)
        except BaseException as e:
            self._logger.exception(e)

    def setAddress(self, address):
        self.address = address

    async def disconnect(self):
        await self._client.stop_notify(BC_RX)
        await self._client.disconnect()
