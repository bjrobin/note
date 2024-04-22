from httpx import AsyncClient, Timeout
from tronpy.providers.async_http import AsyncHTTPProvider
from tronpy.defaults import CONF_NILE
from tronpy import AsyncTron
from tronpy.keys import PrivateKey
async def transfer():
    _http_client = AsyncClient(limits=Limits(max_connections=100, max_keepalive_connections=20),
                               timeout=Timeout(timeout=10, connect=5, read=5))
    provider = AsyncHTTPProvider(CONF_NILE, client=_http_client)
    client = AsyncTron(provider=provider)
    print(client)

    priv_key = PrivateKey(bytes.fromhex("8888888888888888888888888888888888888888888888888888888888888888"))
    txb = (
        client.trx.transfer("TJzXt1sZautjqXnpjQT4xSCBHNSYgBkDr3", "TVjsyZ7fYF3qLF6BQgPmTEZy1xrNNyVAAA", 1_000)
        .memo("test memo")
        .fee_limit(100_000_000)
    )
    txn = await txb.build()
    print(txn)
    txn_ret = await txn.sign(priv_key).broadcast()

    print(txn_ret)
    print(await txn_ret.wait())
    await client.close()

if __name__ == '__main__':
    asyncio.run(transfer())