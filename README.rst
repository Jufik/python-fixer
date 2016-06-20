python-fixer
============
A Python wrapper for fixer.io_ which is a free JSON API for foreign exchange
rates and currency conversion.

It relies on the daily feeds published by the European Central Bank (ECB_).


Installation
------------
The quickest way to install ``python-fixer`` is to use PyPI_ and ``pip``. 
Change between ``pip``, ``pip3``, and ``pip3`` depending on your needs and 
system's specification.

.. code-block:: bash

    $ pip install fixerio

If you prefer to work with the upstream source, clone the repository and
install the wrapper.

.. code-block:: bash

    $ git clone https://github.com/Jufik/python-fixer.git
    $ cd python-fixer
    $ python setup.py install

Usage
-----
As a default the today's exchange rate for EUR is set. 

.. code-block:: python

    import fixerio

    exchange = fixerio.Fixer(base="CZK")

    for currency, rate in exchange.convert().get('rates').items():
        print('{} : {}'.format(currency, rate))


License
-------

``python-fixer`` is licensed under MIT, for more details check LICENSE.

.. _fixer.io: http://fixer.io/
.. _ECB: https://www.ecb.europa.eu/
.. _PyPI: https://pypi.python.org/pypi
