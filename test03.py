import asyncio
import time
import pyupbit
import datetime

access = "PLHmUf3gpoyKYzAqFzzxJ8vH042arYEQfcfdizx1"
secret = "mqsj8p9QYwd3A1Iich0KctXiz4ZJQrhDPxxA39DF"

#변동성 돌파 전략으로 매수 목표가 조회
def get_target_price(ticker):
    time.sleep(0.05)
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=2)
    target_price = df.iloc[1]['open'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * 0.52
    return target_price
#시작가
def get_open_price(ticker):
    time.sleep(0.05)
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=2)
    open_price = df.iloc[1]['open']
    return open_price
#최저가
def get_low_price(ticker):
    time.sleep(0.05)
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=2)
    low_price = df.iloc[1]['low']
    return low_price
#전날시가
def get_open1_price(ticker):
    time.sleep(0.05)
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=2)
    high_price = df.iloc[0]['open']
    return high_price
#전날종가
def get_close1_price(ticker):
    time.sleep(0.05)
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=2)
    close_price = df.iloc[0]['close']
    return close_price
#시작 시간 조회
def get_start_time(ticker):
    time.sleep(0.1)
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=2)
    start_time = df.index[1]
    return start_time
   
#잔고 조회
def get_balance(ticker):
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0
#현재가 조회
def get_current_price(ticker):
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]
#매수평균가
def get_avg_buy_price(ticker):
    buy_price = upbit.get_avg_buy_price(ticker)
    return buy_price
#이동평균선
def get_moving_average(window, ticker):
    try:
        time.sleep(0.05)
        df = pyupbit.get_ohlcv(ticker, interval="minute240")
        ma = df['close'].rolling(window=window).mean()
        return ma[-1]
    except Exception as e:
        time.sleep(1)      
#이전 이동평균선
def get_moving1_average(window, ticker):
    try:
        time.sleep(0.05)
        df = pyupbit.get_ohlcv(ticker, interval="minute240")
        ma = df['close'].rolling(window=window).mean()
        return ma[-2]
    except Exception as e:
        time.sleep(1)

#최고가 조회
def get_high_price(ticker):
    time.sleep(0.05)
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=1)
    high_price = df.iloc[0]['high']
    return high_price

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

op_mode = False
ori_tickers = pyupbit.get_tickers(fiat="KRW")

async def main():
    while True:
        try:
            for ticker in ori_tickers:
                bct_balances = upbit.get_balance(ticker)
                current_p = get_current_price(ticker) 
                now = datetime.datetime.now()
                start_time = get_start_time(ticker)
                end_time = start_time + datetime.timedelta(seconds=14400)
                await asyncio.sleep(1)
                if end_time - datetime.timedelta(seconds=300) < now < end_time:      
                    if bct_balances > (5000/current_p) and bct_balances > 0:
                        upbit.sell_market_order(ticker, bct_balances)
                        await asyncio.sleep(0.5)
                    if 0 < bct_balances < (5000/current_p):
                        upbit.buy_market_order(ticker, 5100)
                if bct_balances == None:
                    pass
                    await asyncio.sleep(0.3)
            await asyncio.sleep(1)
        except Exception as e:
            print(e)
            await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(main()))