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
    target_price = df.iloc[1]['open'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * 0.5
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
                start_time = get_start_time("KRW-BTC")
                end_time = start_time + datetime.timedelta(seconds=14400)                 
                target_p = get_target_price(ticker)
                high_p = get_high_price(ticker)
                open_p = get_open_price(ticker)
                await asyncio.sleep(0.2)
                current_p = get_current_price(ticker)
                low_p = get_low_price(ticker)
                await asyncio.sleep(0.2)
                ma5 = get_moving_average(5, ticker)
                ma10 = get_moving_average(10, ticker)
                man5 = get_moving1_average(5, ticker)
                man10 = get_moving1_average(10, ticker)
                await asyncio.sleep(0.2)
                open1_p = get_open1_price(ticker)
                close1_p = get_close1_price(ticker)
                krw = get_balance("KRW")
                bct_balances = upbit.get_balance(ticker)
                await asyncio.sleep(1)
                if start_time < now < end_time - datetime.timedelta(seconds=300) and \
                    target_p < current_p and ma10 < ma5 and open1_p < close1_p and man5 < ma5 and man10 < ma10:
                    #target_p < current_p and ma10 < ma5 and open_p * 1.02 < current_p
                    if krw > 10500 and bct_balances == 0:
                        await asyncio.sleep(0.2)
                        upbit.buy_market_order(ticker, 10000)
                    if krw < 10500:
                        pass
            await asyncio.sleep(1)
        except Exception as e:
            print(e)
            await asyncio.sleep(1)
while True:
    now = datetime.datetime.now() 
    if now.hour == 9 and now.minute == 0 and 1 <=now.second <= 10:                
        op_mode = True
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.gather(main()))
    if op_mode == True:
        break
