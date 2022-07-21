import bearalpha as ba


@ba.Cache(prefix='backtest_market_daily', expire_time=18000)
def market_daily(
    code: str, 
    start: str, 
    end: str, 
) -> ba.DataFrame:
    data = ba.AkShare.market_daily(code=code, start=start, end=end)
    data = data.rename(columns={'复权开盘': 'open', '复权收盘': 'close', '复权最高': 'high',
        '复权最低': 'low', '成交量': 'volume'}).loc[:, ['open', 'close', 'high', 'low', 'volume']]
    data.index.name = 'datetime'
    data.index = ba.to_datetime(data.index)
    return data


if __name__ == '__main__':
    print(market_daily('000001.SZ', '2019-01-01', '2019-01-31'))