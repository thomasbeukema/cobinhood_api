# Copyright (c) 2018 Thomas Beukema, https://thomasbeukema.me/
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import requests
import time
import json

class Cobinhood_API:
    """ Cobinhood_API:

        This class wraps around the Cobinhood API, for communicating with them.

        Attributes:
            api_key: string for storing API key
            self.base_url: base url for the api
            self.public_endpoints: dict where all public API calls are stored
            self.private_endpoints: dict where all private API calls are stored
            self.wallet_endpoints: dict where all wallet API calls are stored
    """

    api_key = ""
    base_url = "https://api.cobinhood.com"

    public_endpoints = {
        "system_time": {
            "url": "/v1/system/time",
            "method": "GET"
        },
        "system_info": {
            "url": "/v1/system/info",
            "method": "GET"
        },
        "currency_info" : {
            "url": "/v1/market/currencies",
            "method": "GET"
        },
        "all_trading_pairs" : {
            "url": "/v1/market/trading_pairs",
            "method": "GET"
        },
        "order_book": {
            "url": "/v1/market/orderbooks/{pairId}",
            "method": "GET"
        },
        "trading_stats": {
            "url": "/v1/market/stats",
            "method": "GET"
        },
        "ticker": {
            "url": "/v1/market/tickers/{pairId}",
            "method": "GET"
        },
        "recent_trades": {
            "url": "/v1/market/trades/{pairId}",
            "method": "GET"
        },
        "candles": {
            "url": "/v1/chart/candles/{pairId}",
            "method": "GET"
        }
    }

    private_endpoints = {
        "get_order": {
            "url": "/v1/trading/orders/{orderId}",
            "method": "GET"
        },
        "trades_from_order": {
            "url": "/v1/trading/orders/{orderId}/trades",
            "method": "GET"
        },
        "all_orders": {
            "url": "/v1/trading/orders",
            "method": "GET"
        },
        "place_order": {
            "url": "/v1/trading/orders",
            "method": "POST"
        },
        "modify_order": {
            "url": "/v1/trading/orders/{orderId}",
            "method": "PUT"
        },
        "cancel_order": {
            "url": "/v1/trading/orders/{orderId}",
            "method": "DELETE"
        },
        "order_history": {
            "url": "/v1/trading/order_history",
            "method": "GET"
        },
        "get_trade": {
            "url": "/v1/trading/trades/{tradeId}",
            "method": "GET"
        },
        "trade_history": {
            "url": "/v1/trading/trades/{pair}/{limit}",
            "method": "GET"
        },
    }

    wallet_endpoints = {
        "balances": {
            "url": "/v1/wallet/balances",
            "method": "GET"
        },
        "ledger_entries": {
            "url": "/v1/wallet/ledger",
            "method": "GET"
        },
        "deposit_addresses": {
            "url": "/v1/wallet/deposit_addresses",
            "method": "GET"
        },
        "withdrawal_addresses": {
            "url": "/v1/wallet/withdrawal_addresses",
            "method": "GET"
        },
        "get_withdrawal": {
            "url": "/v1/wallet/withdrawals/{withdrawalId}",
            "method": "GET"
        },
        "all_withdrawals": {
            "url": "/v1/wallet/withdrawals",
            "method": "GET"
        },
        "get_deposit": {
            "url": "/v1/wallet/deposits/{depositId}",
            "method": "GET"
        },
        "all_deposits": {
            "url": "/v1/wallet/deposits",
            "method": "GET"
        }
    }

    def __init__(self, api_key):
        """ Inits Cobinhood_API with api_key """
        self.api_key = api_key

    def get_auth_headers(self, nonce=False):
        if not nonce:
            return {"authorization": self.api_key}
        else:
            return {"authorization": self.api_key, "nonce": str(round(time.time() * 1000))}

    def get_system_time(self):
        """ Retrieves system time in epoch millis """
        method = self.public_endpoints['system_time']['method']
        url    = self.base_url + self.public_endpoints['system_time']['url']
        req    = requests.request(method, url)
        res    = req.json()

        if res['success'] == True:
            return res['result']
        else:
            return res

    def get_system_info(self):
        """ Retrieves system info such as system version """
        method = self.public_endpoints['system_info']['method']
        url    = self.base_url + self.public_endpoints['system_info']['url']
        req    = requests.request(method, url)
        res    = req.json()

        if res['success'] == True:
            return res['result']
        else:
            return res

    def get_all_currencies(self):
        """ Retrieves info for all currencies currently supported by Cobinhood """
        method = self.public_endpoints['currency_info']['method']
        url    = self.base_url + self.public_endpoints['currency_info']['url']
        req    = requests.request(method, url)
        res    = req.json()

        if res['success'] == True:
            return res['result']
        else:
            return res

    def get_all_trading_pairs(self):
        """ Retrieves all trading pairs supported by Cobinhood """
        method = self.public_endpoints['all_trading_pairs']['method']
        url    = self.base_url + self.public_endpoints['all_trading_pairs']['url']
        req    = requests.request(method, url)
        res    = req.json()

        if res['success'] == True:
            return res['result']
        else:
            return res

    def get_order_book(self, pair):
        """ Retrieves all orders per trading pairs

            Args:
                pair: string containing the trading pair on Cobinhood; e.g. PAY-ETH
        """
        method = self.public_endpoints['order_book']['method']
        url    = self.base_url + self.public_endpoints['order_book']['url'].format(pairId=pair)
        req    = requests.request(method, url)
        res    = req.json()

        if res['success'] == True:
            return res['result']
        else:
            return res

    def get_trading_stats(self):
        """ Retrieves trading stats from Cobinhood """
        method = self.public_endpoints['trading_stats']['method']
        url    = self.base_url + self.public_endpoints['trading_stats']['url']
        req    = requests.request(method, url)
        res    = req.json()

        if res['success'] == True:
            return res['result']
        else:
            return res

    def get_ticker(self, pair):
        """ Retrieves ticker for trading pairs

            Args:
                pair: string containing the trading pair on Cobinhood; e.g. PAY-ETH
        """
        method = self.public_endpoints['ticker']['method']
        url    = self.base_url + self.public_endpoints['ticker']['url'].format(pairId=pair)
        req    = requests.request(method, url)
        res    = req.json()

        if res['success'] == True:
            return res['result']
        else:
            return res

    def get_recent_trades(self, pair):
        """ Retrieves recent trades for pair

            Args:
                pair: string containing the trading pair on Cobinhood; e.g. PAY-ETH
        """
        method = self.public_endpoints['recent_trades']['method']
        url    = self.base_url + self.public_endpoints['recent_trades']['url'].format(pairId=pair)
        req    = requests.request(method, url)
        res    = req.json()

        if res['success'] == True:
            return res['result']
        else:
            return res

    def get_candle_chart(self, pair):
        """ Retrieves candle chart data for pair

            Args:
                pair: string containing the trading pair on Cobinhood; e.g. PAY-ETH
        """
        method = self.public_endpoints['candles']['method']
        url    = self.base_url + self.public_endpoints['candles']['url'].format(pairId=pair)
        req    = requests.request(method, url)
        res    = req.json()

        if res['success'] == True:
            return res['result']
        else:
            return res

    def get_order(self, order):
        """ Retrieves order info

            Args:
                order: string containing the orderId for your order; e.g. 37f550a202aa6a3fe120f420637c894c
        """
        method = self.private_endpoints['get_order']['method']
        url    = self.base_url + self.private_endpoints['get_order']['url'].format(orderId=order)
        req    = requests.request(method, url, headers=self.get_auth_headers())
        res    = req.json()

        if res['success'] == True:
            return res['result']
        else:
            return res

    def get_trades_from_order(self, order):
        """ Retrieves all trades from orders

            Args:
                order: string containing the orderId for your order; ie; 37f550a202aa6a3fe120f420637c894c
        """
        method = self.private_endpoints['trades_from_order']['method']
        url    = self.base_url + self.private_endpoints['trades_from_order']['url'].format(orderId=order)
        req    = requests.request(method, url, headers=self.get_auth_headers())
        res    = req.json()

        if res['success'] == True:
            return res['result']
        else:
            return res

    def get_all_orders(self):
        """ Retrieves all orders """
        method = self.private_endpoints['all_orders']['method']
        url    = self.base_url + self.private_endpoints['all_orders']['url']
        req    = requests.request(method, url, headers=self.get_auth_headers())
        res    = req.json()

        if res['success'] == True:
            return res['result']
        else:
            return res

    def place_order(self, pair, side, ttype, size, price=0):
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
        possible_sides = ['bid','ask']
        possible_types = ['market', 'limit', 'stop', 'stop_limit']

        side  = side.lower()
        ttype = ttype.lower()

        if not side in possible_sides:
             raise ValueError("Side value invalid")

        if not ttype in possible_types:
            raise ValueError("Type value invalid")

        payload = {
            "trading_pair_id": str(pair),
            "side": str(side),
            "type": str(ttype),
            "size": str(size)
        }

        if not price == 0:
            payload['price'] = str(price)

        method = self.private_endpoints['place_order']['method']
        url    = self.base_url + self.private_endpoints['place_order']['url']
        req    = requests.request(method, url, headers=self.get_auth_headers(nonce=True), json=payload)
        res    = req.json()

        if res['success'] == True:
            return res['result']
        else:
            return res


    def modify_order(self, order, price, size):
        """ Modifies price and size on order with given orderId

            Args:
                order: string containing the orderId for your order; ie; 37f550a202aa6a3fe120f420637c894c
                size: the amount as a float or a string
                price: the price as a float or a string
        """
        request_params = {
            "price": str(price),
            "size": str(size)
        }

        method = self.private_endpoints['modify_order']['method']
        url    = self.base_url + self.private_endpoints['modify_order']['url'].format(orderId=order)
        req    = requests.request(method, url, headers=self.get_auth_headers(nonce=True), params=request_params)
        res    = req.json()

        if res['success'] == True:
            return True
        else:
            return res

    def cancel_order(self, order):
        """ Cancels order with given orderId

            Args:
                order: string containing the orderId for your order; ie; 37f550a202aa6a3fe120f420637c894c
        """
        method = self.private_endpoints['cancel_order']['method']
        url    = self.base_url + self.private_endpoints['cancel_order']['url'].format(orderId=order)
        req    = requests.request(method, url, headers=self.get_auth_headers(nonce=True))
        res    = req.json()

        if res['success'] == True:
            return True
        else:
            return res

    def get_order_history(self):
        """ Retrieves order history """
        method = self.private_endpoints['order_history']['method']
        url    = self.base_url + self.private_endpoints['order_history']['url']
        req    = requests.request(method, url, headers=self.get_auth_headers())
        res    = req.json()

        if res['success'] == True:
            return req['result']
        else:
            return res

    def get_trade(self, trade):
        """ Retrieves trade info

            Args:
                trade: string containing tradeId; e.g. 09619448-e48a-3bd7-3d49-3a4194f9020b
        """
        method = self.private_endpoints['get_trade']['method']
        url    = self.base_url + self.private_endpoints['get_trade']['url'].format(tradeId=trade)
        req    = requests.request(method, url, headers=self.get_auth_headers())
        res    = req.json()

        if res['success'] == True:
            return req['result']
        else:
            return res

    def get_trade_history(self, pair, limit=20):
        """ Retrieves trade history to the limit given

            Args:
                Required:
                    pair: string containing the trading pair on Cobinhood; e.g. PAY-ETH
                Optional:
                    limit: int or string which contains limit the amount of items you get. defaults to 20, max: 50
        """
        method = self.private_endpoints['trade_history']['method']
        url    = self.base_url + self.private_endpoints['trade_history']['url'].format(pair=pair, limit=str(limit))
        req    = requests.request(method, url, headers=self.get_auth_headers())
        res    = req.json()

        if res['success'] == True:
            return req['result']
        else:
            return res

    def get_wallet_balances(self):
        """ Retrieves all balances in your wallet """
        method = self.wallet_endpoints['balances']['method']
        url    = self.base_url + self.wallet_endpoints['balances']['url']
        req    = requests.request(method, url, headers=self.get_auth_headers())
        res    = req.json()

        if res['success'] == True:
            return res['result']
        else:
            return res

    def get_ledger_entries(self, currency="", limit=20):
        """ Retrieves balance mutations for the given currency. Returns as many results as limit specifies.

            Args:
                Optional:
                    currency: string of the currency; e.g. BTC; if none given then all will be retrieved
                    limit: the amount of results you want, defaults to 20, max 50
        """
        query = {
            "limit": str(limit)
        }

        if not currency == "":
            query['currency'] = str(currency)

        method = self.wallet_endpoints['ledger_entries']['method']
        url    = self.base_url + self.wallet_endpoints['ledger_entries']['url']
        req    = requests.request(method, url, headers=self.get_auth_headers(), params=query)
        res    = req.json()

        if res['success'] == True:
            return req['result']
        else:
            return res

    def get_deposit_addresses(self, currency=""):
        """ Retrieves deposit addresses

            Args:
                Optional:
                    currency: string containing desired currency; e.g. BTC
        """
        method = self.wallet_endpoints['deposit_addresses']['method']
        url    = self.base_url + self.wallet_endpoints['deposit_addresses']['url']

        if not currency == "":
            req = requests.request(method, url, headers=self.get_auth_headers(), params={"currency": str(currency)})
        else:
            req = requests.request(method, url, headers=self.get_auth_headers())

        res = req.json()

        if res['success'] == True:
            return req['result']
        else:
            return res

    def get_withdrawal_addresses(self, currency=""):
        """ Retrieves withdrawal addresses

            Args:
                Optional:
                    currency: string containing desired currency; e.g. BTC
        """
        method = self.wallet_endpoints['withdrawal_addresses']['method']
        url    = self.base_url + self.wallet_endpoints['withdrawal_addresses']['url']

        if not currency == "":
            req = requests.request(method, url, headers=self.get_auth_headers(), params={"currency": str(currency)})
        else:
            req = requests.request(method, url, headers=self.get_auth_headers())

        res = req.json()

        if res['success'] == True:
            return req['result']
        else:
            return res

    def get_withdrawal(self, withdrawal):
        """ Retrieves withdrawal info for given withdrawal

            Args:
                withdrawal: string containing withdrawalId; e.g. 62056df2d4cf8fb9b15c7238b89a1438
        """
        method = self.wallet_endpoints['get_withdrawal']['method']
        url    = self.base_url + self.wallet_endpoints['get_withdrawal']['url'].format(withdrawalId=withdrawal)
        req    = requests.request(method, url, headers=self.get_auth_headers())
        res    = req.json()

        if res['success'] == True:
            return req['result']
        else:
            return res

    def get_all_withdrawals(self, currency="", status="", limit=20):
        """ Retrieves all withdrawals

            Args:
                Optional:
                    currency: string containing desired currency; e.g. BTC
                    status: string indicating status of desired withdrawals; must be in ['tx_pending_two_factor_auth', 'tx_pending_email_auth', 'tx_pending_approval', 'tx_approved', 'tx_processing', 'tx_sent', 'tx_pending', 'tx_confirmed', 'tx_timeout', 'tx_invalid', 'tx_cancelled', 'tx_rejected']
                    limit: the amount of results you want, defaults to 20, max 50
        """
        possible_status = ['tx_pending_two_factor_auth', 'tx_pending_email_auth', 'tx_pending_approval', 'tx_approved', 'tx_processing', 'tx_sent', 'tx_pending', 'tx_confirmed', 'tx_timeout', 'tx_invalid', 'tx_cancelled', 'tx_rejected']
        status = status.lower()

        if not status in possible_status:
            raise ValueError("Status is invalid")

        query = {'limit':str(limit)}

        if not currency == "":
            query['currency'] = currency

        if not status == "":
            query['status'] = status

        method = self.wallet_endpoints['all_withdrawals']['method']
        url    = self.base_url + self.wallet_endpoints['all_withdrawals']['url']
        req    = requests.request(method, url, headers=self.get_auth_headers(), params=query)
        res    = req.json()

        if res['success'] == True:
            return req['result']
        else:
            return res

    def get_deposit(self, deposit):
        """ Retrieves deposit info for given deposit

            Args:
                deposit: string containing depositId; e.g. 62056df2d4cf8fb9b15c7238b89a1438
        """
        method = self.wallet_endpoints['get_deposit']['method']
        url    = self.base_url + self.wallet_endpoints['get_deposit']['url'].format(depositId=deposit)
        req    = requests.request(method, url, headers=self.get_auth_headers())
        res    = req.json()

        if res['success'] == True:
            return req['result']
        else:
            return res

    def get_all_deposit(self):
        """ Retrieves all deposits """
        method = self.wallet_endpoints['all_deposits']['method']
        url    = self.base_url + self.wallet_endpoints['all_deposits']['url']
        req    = requests.request(method, url, headers=self.get_auth_headers())
        res    = req.json()

        if res['success'] == True:
            return req['result']
        else:
            return res
