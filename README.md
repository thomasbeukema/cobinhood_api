![Cobinhood logo](https://prnewswire2-a.akamaihd.net/p/1893751/sp/189375100/thumbnail/entry_id/1_yirc0bcz/def_height/100/def_width/750/version/100011/type/2/q/100)

# Cobinhood API

This is an API wrapper for Cobinhood written in Python. I made this in my spare time for a trade bot.

| Donations: | Address |
| ---------- | ------- |
| BTC | 1Bi1W26FE9gSS3SoY7fPHd1C9fMk8E11z2 |
| ETH | 0xc406ac84b93bd3fec4801f6dd77aff243cdc574a |
| XLM | GA6BIUPHPS476B227MUXDAN5TA32QG6J73XTIZS2CS2D2AWJABCIMZOI |
| ETN | etnk5waqRk725J6ybevSQY9BU2ggJuj1Whskypw9e4pZ85Hmcki2dJBfbF31aJZuBn8ZEou6cFuFCW4G2iYnUcze55V27ycAS3 |

# Installation
__IMPORTANT__

Use Python 3.x for this wrapper.

First, use pip to install:
```shell
pip install cobinhood_api
```

Then use it like this:
```python
from cobinhood_api import cobinhood
```

# Usage
This page will just give a brief overview of how to use this wrapper. For a more extensive usage of the api
you should take a look at [this](https://cobinhood.github.io/api-public/).

__IMPORTANT__

In the examples below, there is a typical response provided. The API will return only the 'result' object if succesful.

### Errors
If an error has occured, then the response would look something like this:
```JSON
{
    "success": false,
    "error": {
        "error_code": "some_error",
    }
}
```
### Dealing with errors
```python
""" This is how I would deal with errors in my script """
balances = api.get_wallet_balances()

if 'error' in balances:
    # Error
else:
    # You're fine
```

For the rest of the documentation we assume the response is successful with each request.

### Initialise the API
```python
from cobinhood_api import cobinhood

api = cobinhood.Cobinhood_API(<your_api_key>)
```
---
### System time
```python
""" Retrieves system time in epoch millis """
system_time = api.get_system_time()
```
### Response


```JSON
{
    "success": true,
    "result": {
        "time": 1505204498376
    }
}
```
---
### System info
```python
""" Retrieves system info such as system version """
system_info = api.get_system_info()
```
### Response
```JSON
{
    "success": true,
    "result": {
        "info": {
            "phase": "production",
            "revision": "480bbd"
        }
    }
}
```
---

### List all currencies
```python
""" Retrieves info for all currencies currently supported by Cobinhood """
all_currencies = api.get_all_currencies()
```

### Response
```JSON
{
    "success": true,
    "result": {
        "currencies": [
            {
                "currency": "BTC",
                "name": "Bitcoin",
                "min_unit": "0.00000001",
                "deposit_fee": "0",
                "withdrawal_fee": "22.6"
            },
        ]
    }
}
```
---
### List all trading pairs
```python
""" Retrieves all trading pairs supported by Cobinhood """
all_pairs = api.get_all_trading_pairs()
```
### Response
```JSON
{
    "success": true,
    "result": {
        "trading_pairs": [
            {
                "id": "BTC-USD",
                "base_currency_id": "BTC",
                "quote_currency_id": "USD",
                "base_min_size": "0.004",
                "base_max_size": "10000",
                "quote_increment": "0.1"
            },
        ]
    }
}
```
---
### Get the order book for specific pair
```python
""" Retrieves all orders per trading pairs

    Args:
        pair: string containing the trading pair on Cobinhood; e.g. PAY-ETH
"""
order_book = api.get_order_book('BTC-USD')
```
### Response
```JSON
{
    "success": true,
    "result": {
        "orderbook": {
            "sequence": 1938572,
            "bids": [
                [ "price", "count", "size" ],

            ],
            "asks": [
                [ "price", "count", "size" ],

            ]
        }
    }
}
```
---
### Trading statistics
```python
""" Retrieves trading stats from Cobinhood """
trading_stats = api.get_trading_stats()
```
### Response
```JSON
{
    "success": true,
    "result": {
        "BTC-USD": {
            "id": "BTC-USD",
            "last_price": "10005",
            "lowest_ask": "10005",
            "highest_bid": "15200.1",
            "base_volume": "0.36255776",
            "quote_volume": "4197.431917146",
            "is_frozen": false,
            "high_24hr": "16999.9",
            "low_24hr": "10000",
            "percent_changed_24hr": "-0.3417806461799593"
        }
    }
}
```
---
### Get ticker for specific pair
```python
""" Retrieves ticker for trading pairs

    Args:
        pair: string containing the trading pair on Cobinhood; e.g. PAY-ETH
"""
ticker = api.get_ticker('BTC-USD')
```
### Response
```JSON
{
    "success": true,
    "result": {
        "ticker": {
            "trading_pair_id": "COB-BTC",
            "timestamp": 1504459805123,
            "24h_high": "23.456",
            "24h_low": "10.123",
            "24h_open": "15.764",
            "24h_volume": "7842.11542563",
            "last_trade_price":"244.82",
            "highest_bid":"244.75",
            "lowest_ask":"244.76",
        },
    }
}
```
---
### Get recent trades for specific pair
```python
""" Retrieves recent trades for pair

    Args:
        pair: string containing the trading pair on Cobinhood; e.g. PAY-ETH
"""
recent_trades = api.get_recent_trades('COB-BTC')
```
### Response
```JSON
{
    "success": true,
    "result": {
        "trades": [
            {
                "id": "09619448e48a3bd73d493a4194f9020b",
                "price": "10.00000000",
                "size": "0.01000000",
                "maker_side": "buy",
                "timestamp": 1504459805123
            },

        ]
    }
}
```
---
### Get the candle chart data for specific pair
```python
""" Retrieves candle chart data for pair

    Args:
        pair: string containing the trading pair on Cobinhood; e.g. PAY-ETH
"""
chart_data = api.get_candle_chart('COB-ETH')
```
### Response
```JSON
{
    "success": true,
    "result": {
        "candles": [
            {
                "timestamp": 1507366756,
                "open": "4378.6",
                "close": "4379.0",
                "high": "4379.0",
                "low": "4378.3",
                "volume": "23.91460172"
            },

        ]
    }
}
```
---
### Get order by orderID
```python
""" Retrieves order info

    Args:
        order: string containing the orderId for your order; e.g. 37f550a202aa6a3fe120f420637c894c
"""
order = api.get_order('37f550a202aa6a3fe120f420637c894c')
```
### Response
```JSON
{
    "success": true,
    "result": {
        "order": {
            "id": "37f550a202aa6a3fe120f420637c894c",
            "trading_pair": "BTC-USD",
            "state": "open",
            "side": "bid",
            "type": "limit",
            "price": "5000.01",
            "size": "1.0100",
            "filled": "0.59",
            "timestamp": 1504459805123
        }
    }
}
```
---
### Get all trades involved with order
```python
""" Retrieves all trades from orders

    Args:
        order: string containing the orderId for your order; ie; 37f550a202aa6a3fe120f420637c894c
"""
trades_in_order = api.get_trades_from_order('37f550a202aa6a3fe120f420637c894c')
```
### Response
```JSON
{
    "success": true,
    "result": {
        "trades": [
            {
                "id": "09619448e48a3bd73d493a4194f9020b",
                "price": "10.00000000",
                "size": "0.01000000",
                "maker_side": "bid",
                "timestamp": 1504459805123
            },

        ]
    }
}
```
---
### Get all orders
```python
""" Retrieves all orders """
orders = api.get_all_orders()
```
### Response
```JSON
{
    "success": true,
    "result": {
        "trades": [
            {
                "id": "09619448e48a3bd73d493a4194f9020b",
                "price": "10.00000000",
                "size": "0.01000000",
                "maker_side": "bid",
                "timestamp": 1504459805123
            },

        ]
    }
}
```
---
### Place order
```python
""" Places a new order

    Args:
        Required:
            pair: string containing the trading pair on Cobinhood; e.g. PAY-ETH
            side: string with possible values: ['bid','ask']. Raises ValueError if the value is different.
            ttype: string with possible values: ['market', 'limit', 'stop', 'stop_limit']. Raises ValueError if the value is different.
            size: the amount as a float or a string
        Optional:
            price: if type is market this is optional, else you should give the price as a float or a string
"""
limit_order  = api.place_order('OMG-ETH', 'bid', 'limit', 200, price=0.0012) # limit order : supply price
market_order = api.place_order('OMG-ETH', 'bid', 'limit', 200) # market order: don't supply price
```
### Response
```JSON
{
    "success": true,
    "result": {
        "order": {
            "id": "37f550a202aa6a3fe120f420637c894c",
            "trading_pair": "BTC-USD",
            "state": "open",
            "side": "bid",
            "type": "limit",
            "price": "5000.01",
            "size": "1.0100",
            "filled": "0.59",
            "timestamp": 1504459805123,
            "eq_price": "5000.01",
        }
    }
}
```
---
### Modify order
```python
""" Modifies price and size on order with given orderId

    Args:
        order: string containing the orderId for your order; ie; 37f550a202aa6a3fe120f420637c894c
        size: the amount as a float or a string
        price: the price as a float or a string
"""
modified_order = api.modify_order('37f550a202aa6a3fe120f420637c894c', 0.0013, 400)
```
### Response
```python
True / False #depending on success
```
---
### Cancel order
```python
""" Cancels order with given orderId

    Args:
        order: string containing the orderId for your order; ie; 37f550a202aa6a3fe120f420637c894c
"""
canceled_order = api.cancel_order('37f550a202aa6a3fe120f420637c894c')
```
### Response
```python
True / False # depending on succes
```
---
### Order history
```python
""" Retrieves order history """
order_history = api.get_order_history()
```
### Response
```JSON
{
    "success": true,
    "result": {
        "order_history": [
            {
                "id": "37f550a202aa6a3fe120f420637c894c",
                "trading_pair": "BTC-USD",
                "state": "filled",
                "side": "bid",
                "type": "limit",
                "price": "5000.01",
                "size": "1.0100",
                "filled": "0.59",
                "timestamp": 1504459805123,
                "eq_price": "5000.01",
            },

        ]
    }
}
```
---
### Get trade by tradeID
```python
""" Retrieves trade info

    Args:
        trade: string containing tradeId; e.g. 09619448-e48a-3bd7-3d49-3a4194f9020b
"""
trade = api.get_trade('09619448-e48a-3bd7-3d49-3a4194f9020b')
```
### Response
```JSON
{
    "success": true,
    "result": {
        "trade": {
            "trading_pair_id": "BTC-USDT",   
            "id": "09619448-e48a-3bd7-3d49-3a4194f9020b",
            "maker_side": "bid",
            "price": "10.00000000",
            "size": "0.01000000",
            "timestamp": 1504459805123
        }
    }
}
```
---
### Get trade history
```python
""" Retrieves trade history to the limit given

    Args:
        Required:
            pair: string containing the trading pair on Cobinhood; e.g. PAY-ETH
        Optional:
            limit: int or string which contains limit the amount of items you get. defaults to 20, max: 50
"""
trade_history = api.get_trade_history() # no limit
trade_history = api.get_trade_history(limit=35) # limit of 35
```
### Response
```JSON
{
    "success": true,
    "result": {
        "trades": [
            {
                "trading_pair_id": "BTC-USDT",
                "id": "09619448e48a3bd73d493a4194f9020b",
                "maker_side": "ask",
                "price": "10.00000000",
                "size": "0.01000000",
                "timestamp": 1504459805123
            },

        ]
    }
}
```
---
### Get all balances
```python
""" Retrieves all balances in your wallet """
balances = api.get_balances()
```
### Response
```JSON
{
    "success": true,
    "result": {
        "balances": [
            {
                "currency": "BTC",
                "type": "exchange",
                "total": "1",
                "on_order": "0.4",
                "locked": false
            },
            {
                "currency": "ETH",
                "type": "exchange",
                "total": "0.0855175219863032",
                "on_order": "0.04",
                "locked": false
            },
            {
                "currency": "COB",
                "type":" exchange",
                "total": "100",
                "on_order": "20",
                "locked": false
            },

        ]
    }
}
```
---
### Get ledger entries
```python
""" Retrieves balance mutations for the given currency. Returns as many results as limit specifies.

    Args:
        Optional:
            currency: string of the currency; e.g. BTC; if none given then all will be retrieved
            limit: the amount of results you want, defaults to 20, max 50
"""
ledger_entries = api.get_ledger_entries() # no parameters
ledger_entries = api.get_ledger_entries(currency='BTC', limit=10) # both parameters
```
### Response
```JSON
{
    "success": true,
    "result": {
        "ledger": [
            {
                "action": "trade",
                "type": "exchange",
                "trade_id": "09619448e48a3bd73d493a4194f9020b",
                "currency": "BTC",
                "amount": "+635.77",
                "balance": "2930.33",
                "timestamp": 1504685599302,
            },
            {
                "action": "deposit",
                "type": "exchange",
                "deposit_id": "09619448e48a3bd73d493a4194f9020b",
                "currency": "BTC",
                "amount": "+635.77",
                "balance": "2930.33",
                "timestamp": 1504685599302,
            },
            {
                "action": "withdraw",
                "type": "exchange",
                "withdrawal_id": "09619448e48a3bd73d493a4194f9020b",
                "currency": "BTC",
                "amount": "-121.01",
                "balance": "2194.87",
                "timestamp": 1504685599302,
            },

        ]
    }
}
```
---
### Get deposit addresses
```python
""" Retrieves deposit addresses

    Args:
        Optional:
            currency: string containing desired currency; e.g. BTC
"""
deposit_addresses = api.get_deposit_addresses() # no parameters
deposit_addresses = api.get_deposit_addresses(currency='BTC') # currency specified
```
### Response
```JSON
{
    "success": true,
    "result": {
        "deposit_addresses": [
            {
                "currency": "BTC",
                "address": "0xbcd7defe48a19f758a1c1a9706e808072391bc20",
                "created_at": 1504459805123,
                "type": "exchange"
            },

        ]
    }
}
```
---
### Get withdrawal addresses
```python
""" Retrieves withdrawal addresses

    Args:
        Optional:
            currency: string containing desired currency; e.g. BTC
"""
withdrawal_addresses = api.get_withdrawal_addresses() # no parameters
withdrawal_addresses = api.get_withdrawal_addresses(currency='BTC') # currency specified
```
### Response
```JSON
{
    "success": true,
    "result": {
        "withdrawal_addresses": [
            {
                "id": "09619448e48a3bd73d493a4194f9020b",
                "currency": "BTC",
                "name": "Kihon's Bitcoin Wallet Address",
                "type": "exchange",
                "address": "0xbcd7defe48a19f758a1c1a9706e808072391bc20",
                "created_at": 1504459805123
            },

        ]
    }
}
```
---
### Get withdrawal
```python
""" Retrieves withdrawal info for given withdrawal

    Args:
        withdrawal: string containing withdrawalId; e.g. 62056df2d4cf8fb9b15c7238b89a1438
"""
withdrawal = api.get_withdrawal('62056df2d4cf8fb9b15c7238b89a1438')
```
### Response
```JSON
{
    "success": true,
    "result": {
        "withdrawal": {
            "withdrawal_id": "62056df2d4cf8fb9b15c7238b89a1438",
            "user_id": "62056df2d4cf8fb9b15c7238b89a1438",
            "status": "pending",
            "confirmations": 25,
            "required_confirmations": 25,
            "created_at": 1504459805123,
            "sent_at": 1504459805123,
            "completed_at": 1504459914233,
            "updated_at": 1504459914233,
            "to_address": "0xbcd7defe48a19f758a1c1a9706e808072391bc20",
            "txhash": "0xf6ca576fb446893432d55ec53e93b7dcfbbf75b548570b2eb8b1853de7aa7233",
            "currency": "BTC",
            "amount": "0.021",
            "fee": "0.0003"
        }
    }
}
```
---
### Get all withdrawals
```python
""" Retrieves all withdrawals

    Args:
        Optional:
            currency: string containing desired currency; e.g. BTC
            status: string indicating status of desired withdrawals; must be in ['tx_pending_two_factor_auth', 'tx_pending_email_auth', 'tx_pending_approval', 'tx_approved', 'tx_processing', 'tx_sent', 'tx_pending', 'tx_confirmed', 'tx_timeout', 'tx_invalid', 'tx_cancelled', 'tx_rejected']
            limit: the amount of results you want, defaults to 20, max 50
"""
withdrawals = api.get_all_withdrawals() # no parameters
withdrawals = api.get_all_withdrawals(currency='BTC', status='pending', limit=1) # all parameters specified
```
### Response
```JSON
{
    "success": true,
    "result": {
        "withdrawals": [
            {
                "withdrawal_id": "62056df2d4cf8fb9b15c7238b89a1438",
                "user_id": "62056df2d4cf8fb9b15c7238b89a1438",
                "status": "pending",
                "confirmations": 25,
                "required_confirmations": 25,
                "created_at": 1504459805123,
                "sent_at": 1504459805123,
                "completed_at": 1504459914233,
                "updated_at": 1504459914233,
                "to_address": "0xbcd7defe48a19f758a1c1a9706e808072391bc20",
                "txhash": "0xf6ca576fb446893432d55ec53e93b7dcfbbf75b548570b2eb8b1853de7aa7233",
                "currency": "BTC",
                "amount": "0.021",
                "fee": "0.0003"
            },

        ]
    }
}
```
---
### Get deposit
```python
""" Retrieves deposit info for given deposit

    Args:
        deposit: string containing depositId; e.g. 62056df2d4cf8fb9b15c7238b89a1438
"""
deposit = api.get_deposit('62056df2d4cf8fb9b15c7238b89a1438')
```
### Response
```JSON
{
    "success": true,
    "result": {
        "deposit": {
            "deposit_id": "62056df2d4cf8fb9b15c7238b89a1438",
            "user_id": "62056df2d4cf8fb9b15c7238b89a1438",
            "status": "pending",
            "confirmations": 25,
            "required_confirmations": 25,    
            "created_at": 1504459805123,
            "completed_at": 1504459914233,
            "from_address": "0xbcd7defe48a19f758a1c1a9706e808072391bc20",
            "txhash": "0xf6ca576fb446893432d55ec53e93b7dcfbbf75b548570b2eb8b1853de7aa7233",
            "currency": "BTC",
            "amount": "0.021",
            "fee": "0.0003"
        }
    }
}
```
---
### Get all deposits
```python
""" Retrieves all deposits """
deposits = api.get_all_deposits()
```
### Response
```JSON
{
    "success": true,
    "result": {
        "deposits": [
            {
                "deposit_id": "62056df2d4cf8fb9b15c7238b89a1438",
                "user_id": "62056df2d4cf8fb9b15c7238b89a1438",
                "status": "pending",
                "confirmations": 25,
                "required_confirmations": 25,    
                "created_at": 1504459805123,
                "completed_at": 1504459914233,
                "from_address": "0xbcd7defe48a19f758a1c1a9706e808072391bc20",
                "txhash": "0xf6ca576fb446893432d55ec53e93b7dcfbbf75b548570b2eb8b1853de7aa7233",
                "currency": "BTC",
                "amount": "0.021",
                "fee": "0.0003"
            },

        ]
    }
}
```
