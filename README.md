# Crypto Price Tracker

A Python application that fetches cryptocurrency prices concurrently using async programming and stores them in a SQLite database.

## 🎯 Project Overview

This project demonstrates:
- **Async I/O**: Concurrent API calls using `asyncio` and `aiohttp`
- **Error Handling**: Timeout, network errors, and bad status codes
- **Context Managers**: Safe database connection handling
- **Testing**: Comprehensive test suite with mocked API responses

## 🚀 Features

- Fetches Bitcoin, Ethereum, and Litecoin prices simultaneously
- Error handling for timeouts, network failures, and API errors
- Stores price data in SQLite database
- Full test coverage with async testing
- Uses CoinGecko API (free, no authentication required)

## 🛠️ Technologies Used

- **Python 3.10+**
- **aiohttp**: Async HTTP client
- **asyncio**: Asynchronous programming
- **SQLite**: Lightweight database
- **pytest**: Testing framework
- **aioresponses**: For mocking async HTTP requests in tests

## 📁 Project Structure

```
crypto-price-tracker/
├── crypto_fetcher.py        # Main async fetching logic
├── database.py              # Context manager for database
├── test_crypto_fetcher.py   # Test suite
├── requirements.txt
└── README.md
```

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/crypto-price-tracker.git
cd crypto-price-tracker
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Fetch current prices
```bash
python crypto_fetcher.py
```

**Output:**
```
[{'bitcoin': {'usd': 87899}}, {'ethereum': {'usd': 2970.23}}, {'litecoin': {'usd': 78.02}}]
Connection created!
Connection committed and closed!
```

### Run tests
```bash
pytest test_crypto_fetcher.py -v
```

## 📝 Code Examples

### Async Price Fetching with Error Handling
```python
async def fetch_crypto_price(session, crypto_id, timeout=10):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=timeout)) as result:
            if result.status != 200:
                return None
            data = await result.json()
            return data
    except asyncio.TimeoutError:
        return None
    except aiohttp.ClientError:
        return None
```

### Concurrent Fetching
```python
async def fetch_all_prices():
    cryptos = ['bitcoin', 'ethereum', 'litecoin']
    async with aiohttp.ClientSession() as session:
        coins = [fetch_crypto_price(session, coin) for coin in cryptos]
        result = await asyncio.gather(*coins)
```

## ⚠️ Error Handling

The application handles:
- **Network timeouts**: Default 10 seconds per request
- **API errors**: Non-200 status codes
- **Connection failures**: Network unavailability
- **Invalid responses**: Returns None for failed requests

## 🧪 Testing

Test coverage includes:
- ✅ Successful API responses
- ✅ Timeout scenarios
- ✅ Bad status codes (500)
- ✅ Network errors

**Total tests**: 4 covering all critical paths

## 🎓 Learning Outcomes

This project demonstrates:
- **Concurrent Programming**: Fetching multiple prices simultaneously
- **Error Handling**: Robust timeout and exception handling
- **Resource Management**: Safe database connections with context managers
- **Test-Driven Development**: Mocking async HTTP calls

## 📊 API Used

**CoinGecko API**
- Endpoint: `https://api.coingecko.com/api/v3/simple/price`
- Free tier, no authentication required
- Rate limit: 10-50 requests/minute

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- Built as part of Day 68 Python learning journey
- API provided by CoinGecko