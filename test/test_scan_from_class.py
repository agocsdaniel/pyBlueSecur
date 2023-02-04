import asyncio
from pybluesecur import PyBlueSecur

pybluesecur = PyBlueSecur()

addresses = asyncio.run(pybluesecur.scan())
print(addresses)
