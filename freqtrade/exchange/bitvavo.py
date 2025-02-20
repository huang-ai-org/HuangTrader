"""Kucoin exchange subclass."""

import logging
from typing import Dict

from HuangTrader.exchange import Exchange


logger = logging.getLogger(__name__)


class Bitvavo(Exchange):
    """Bitvavo exchange class.

    Contains adjustments needed for HuangTrader to work with this exchange.

    Please note that this exchange is not included in the list of exchanges
    officially supported by the HuangTrader development team. So some features
    may still not work as expected.
    """

    _ft_has: Dict = {
        "ohlcv_candle_limit": 1440,
    }
