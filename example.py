#!/usr/bin/python3
#
# Copyright (c) 2016, Fabian Affolter <fabian@affolter-engineering.ch>
# Released under the MIT license. See LICENSE file for details.
#
import fixerio

# Our base currency is the Czech Koruna instead of the default (EUR).
BASE = 'CZK'

exchange = fixerio.Fixer(base=BASE)

print('Current exchange rates:')
for currency, rate in exchange.convert().get('rates').items():
    print('{} : {}'.format(currency, rate))

print('Current exchange rates for CHF:')
# Check if the target currency exists
if exchange.currency_available('CHF'):
    print(exchange.convert().get('rates')['CHF'])
