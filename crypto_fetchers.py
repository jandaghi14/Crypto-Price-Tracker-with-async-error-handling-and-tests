import asyncio
import aiohttp
from database import ConnectionClassDatabase
# Add imports you'll need

async def fetch_crypto_price(session, crypto_id, timeout=10):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    try:
        async with session.get(url , timeout = aiohttp.ClientTimeout(total= timeout)) as result: #in ghesmatesho hefz nabodam aiohttp.ClientTimeout(total= timeout)
            if result.status != 200:
                print(f"API error: status {result.status}")
                return None
            data = await result.json()
            return data
    except asyncio.TimeoutError:
        print("TimeOut Error!")
        return None
    except aiohttp.ClientError as e:
        print(f"Error in connecting : {e}")
        return None
    
    
async def fetch_all_prices():
    cryptos = ['bitcoin' , 'ethereum' , 'litecoin']
    async with aiohttp.ClientSession() as session:
        coins = [fetch_crypto_price(session , coin) for coin in cryptos]
        result = await asyncio.gather(*coins)
        print(result)            
        with ConnectionClassDatabase("DatabaseFile.db") as db:
            cursor = db.cursor()
            cursor.execute("""
                        CREATE TABLE IF NOT EXISTS cryptocache (
                            crypto_name TEXT,
                            price TEXT
                        )
                        """) 
            for i in result:
                if i is not None:
                    cursor.execute("""
                                    INSERT INTO cryptocache (crypto_name , price)
                                    VALUES (?,?)
                                    """,(list(i.keys())[0] , i[list(i.keys())[0]]['usd'])
                        )
                    
if __name__ == "__main__":
    asyncio.run(fetch_all_prices())

