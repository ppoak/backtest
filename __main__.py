import bearalpha as ba
from .data import *
from .indicators import *
from .strategies import *


config = dict(
    datafetcher = market_daily,
    cash = 1000000,
    fetcherargs = dict(
        code = '600362',
        start = '20190101',
        end = '20220701',
    ),
    indicators = None,
    strategy = None,
    observers = None,
    analyzers = None,
)

if __name__ == "__main__":
    fetcher = config['datafetcher']
    data: ba.DataFrame = fetcher(**config['fetcherargs'])
    data.backtrader.run(SMACrossStrategy)
    