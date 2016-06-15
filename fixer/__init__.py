# Copyright (c) 2016 Julien Kieffer TISSIER <julien.kieffer@gadz.org>
# Released under the MIT license. See LICENSE file for details.
#
"""A simple wrapper for Fixer.io."""
from datetime import datetime
import requests

BASE_URL = 'http://api.fixer.io/'
CURRENCY_CHOICE = ["EUR", "AUD", "BGN", "BRL", "CAD", "CHF", "CNY", "CZK",
                   "DKK", "GBP", "HKD", "HRK", "HUF", "IDR", "ILS",
                   "INR", "JPY", "KRW", "MXN", "MYR", "NOK", "NZD",
                   "PHP", "PLN", "RON", "RUB", "SEK", "SGD", "THB",
                   "TRY", "USD", "ZAR"]


class Fixer(object):
    """The class for the interaction with the Fixer.io API.

        date:
                Either a date in "yyyy-mm-dd" format (available from 1999)
                either "latest" for latest date
                default = "latest"

        base:
                A currency in CURRENCY_CHOICE list.
                Will setup the base currency for conversion
                default = "EUR"

                Will raise a ValueError exception
    """

    def __init__(self, date="latest", base="EUR", symbols=None):
        """"Initialize the wrapper."""
        super(Fixer, self).__init__()
        self.symbols_string = ''

        if self.currency_available(base, "Base currency"):
            self.base = base

        if symbols:
            self.symbols = []

            for cur in symbols:
                if self.currency_available(cur, "Symbols currency"):
                    self.symbols.append(cur)

            self.symbols_string = 'symbols=' % ','.join(self.symbols)

        self.check_date(date)

    def currency_available(self, cur, method=""):
        """Check if the currency is available."""
        if cur not in CURRENCY_CHOICE:
            # Raise a ValueError exception
            raise ValueError("Currency %s not available through this API"
                             % cur, method)

        else:
            return True

    def check_date(self, dt):
        """"Check the given date."""
        if type(dt) == datetime:
            self.date = dt
        elif type(dt) == str:
            if dt == "latest":
                self.date = dt
            else:
                try:
                    self.date = datetime.strptime(dt, "%Y-%m-%d")
                except ValueError as error:
                    raise error

                if not self.date.year >= 1999:
                    raise ValueError("Data available from 1999, %s is to old"
                                     % self.date.strftime("%Y-%m-%d"))

                if self.date > datetime.now():
                    raise ValueError("%s is in the future, date can't be found"
                                     % self.date.strftime("%Y-%m-%d"))
        else:
            raise ValueError("%s does not match required date format" % dt)

    def convert(self):
        """"Get the data from the API."""
        url = '{}{}?{}&base={}'.format(BASE_URL, self.date,
                                       self.symbols_string, self.base)
        request = requests.get(url, timeout=10).json()

        if 'error' in request:
            raise ReferenceError(request['error'])
        return request
