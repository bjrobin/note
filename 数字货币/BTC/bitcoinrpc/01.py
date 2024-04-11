import asyncio
from bitcoinrpc import BitcoinRPC
async def main():
    async with BitcoinRPC.from_config("http://localhost:8333", ("a", "b")) as rpc:
        print(await rpc.getconnectioncount())
if __name__ == "__main__":
    asyncio.run(main())