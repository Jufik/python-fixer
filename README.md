# python-fixer

A Python wrapper for [fixer.io](http://fixer.io/) which is a free JSON API for
foreign exchange rates and currency conversion.

It relies on the daily feeds published by the European Central Bank (ECB).


## Installation

Clone the repository and install the wrapper.

```bash
$ git clone https://github.com/Jufik/python-fixer.git
$ cd python-fixer
$ python setup.py install
```

## Usage
As a default the today's exchange rate for EUR is set. 

```python
import fixer

exchange = fixer.Fixer(base="CZK")

for currency, rate in exchange.convert().get('rates').items():
    print('{} : {}'.format(currency, rate))
```

## License

`python-fixer` is licensed under MIT, for more details check LICENSE.
