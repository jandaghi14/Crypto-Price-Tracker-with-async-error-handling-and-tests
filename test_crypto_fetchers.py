from crypto_fetchers import fetch_crypto_price , fetch_all_prices 
from aioresponses import aioresponses
import pytest
import aiohttp
import asyncio


@pytest.mark.asyncio
async def test_fetch_crypto_success():
    with aioresponses() as mock:
        fake_response = {'ali': {'usd': 87899}}
        mock.get(f"https://api.coingecko.com/api/v3/simple/price?ids=ali&vs_currencies=usd" , payload = fake_response , status = 200)
        async with aiohttp.ClientSession() as session:
            response = await fetch_crypto_price(session, 'ali')
            assert response == fake_response
     
@pytest.mark.asyncio
async def test_fetch_crypto_bad_status():
    with aioresponses() as mock:
        mock.get(f"https://api.coingecko.com/api/v3/simple/price?ids=test&vs_currencies=usd" , status = 500)
        async with aiohttp.ClientSession() as session:
            response = await fetch_crypto_price(session , 'tets')
            assert response is None

@pytest.mark.asyncio
async def test_fetch_crypto_timeout():
    with aioresponses() as mock:
        mock.get("https://api.coingecko.com/api/v3/simple/price?ids=test&vs_currencies=usd" , exception = asyncio.TimeoutError() )
        async with aiohttp.ClientSession() as session:
            response = await fetch_crypto_price(session , "test")
            assert response == None

@pytest.mark.asyncio
async def test_fetch_crypto_network_error():
    with aioresponses() as mock:
        mock.get("https://api.coingecko.com/api/v3/simple/price?ids=test&vs_currencies=usd" , exception = aiohttp.ClientError())
        async with aiohttp.ClientSession() as session:
            response = await fetch_crypto_price(session , "test")
            assert response == None