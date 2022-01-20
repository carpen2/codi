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
    target_price = df.iloc[1]['low'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * 0.52
    return target_price
#시작가
def get_open_price(ticker):
    time.sleep(0.05)
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=2)
    open_price = df.iloc[1]['open']
    return open_price
#종가
def get_close_price(ticker):
    time.sleep(0.05)
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=2)
    close_price = df.iloc[1]['close']
    return close_price
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
                now = datetime.datetime.now()
                start_time = get_start_time("KRW-BTC")
                end_time = start_time + datetime.timedelta(seconds=3600)                 
                target_p = get_target_price(ticker)
                current_p = get_current_price(ticker)
                ma5 = get_moving_average(5, ticker)
                ma10 = get_moving_average(10, ticker)
                man5 = get_moving1_average(5, ticker)
                krw = get_balance("KRW")
                bct_balances = upbit.get_balance(ticker)
                if target_p < current_p and man5 < ma5 and ma10 < ma5:
                    if krw > 26000 and bct_balances == 0:
                        upbit.buy_market_order(ticker, 5100)
                await asyncio.sleep(0.5)
        except Exception as e:
            print(e)

async def submain():
    while True:
        try:
            for ticker in ori_tickers:
                current_p = get_current_price(ticker)
                buy_p = get_avg_buy_price(ticker)
                bct_balances = upbit.get_balance(ticker)
                if 0 < bct_balances:
                    if current_p < buy_p * 0.965:
                        upbit.buy_market_order(ticker, bct_balances)
                    if current_p > buy_p * 1.02:
                        upbit.sell_market_order(ticker, bct_balances)
                await asyncio.sleep(0.5)
        except Exception as e:
            print(e)

while True:
    now = datetime.datetime.now()
    if now.hour == 7 and now.minute == 15 and 1 <=now.second <= 10:
        op_mode = True
        print("시작")
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.gather(main(), submain()))
    if op_mode == True:
        time.sleep(1)
        break
