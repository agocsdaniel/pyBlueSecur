import asyncio
from pybluesecur.scan import scan

if __name__ == "__main__":
    addresses = asyncio.run(scan())
    print(addresses)