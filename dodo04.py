import time
import pyupbit
import datetime

access = "PLHmUf3gpoyKYzAqFzzxJ8vH042arYEQfcfdizx1"
secret = "mqsj8p9QYwd3A1Iich0KctXiz4ZJQrhDPxxA39DF"

#변동성 돌파 전략으로 매수 목표가 조회
def get_target_price(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=2)
    target_price = df.iloc[1]['open'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * 0.52
    return target_price

#시작가
def get_open_price(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=2)
    open_price = df.iloc[1]['open']
    return open_price

#전날시가
def get_open1_price(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=2)
    high_price = df.iloc[0]['open']
    return high_price
#전날종가
def get_close1_price(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=2)
    close_price = df.iloc[0]['close']
    return close_price

#시작 시간 조회
def get_start_time(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=1)
    start_time = df.index[0]
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
#익절
def get_avg_buys_price(ticker):
    buy_price = upbit.get_avg_buy_price(ticker) * 1.03
    return buy_price
#손절
def get_avg_buym_price(ticker):
    buy_price = upbit.get_avg_buy_price(ticker) * 0.98
    return buy_price
    
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
        df = pyupbit.get_ohlcv(ticker, interval="minute240")
        ma = df['close'].rolling(window=window).mean()
        return ma[-1]
    except Exception as e:
        time.sleep(1)
        
#최고가 조회
def get_high_price(ticker):
    df2 = pyupbit.get_ohlcv(ticker, interval="minute240", count=1)
    high_price = df2.iloc[0]['high']
    return high_price
#매수 주문
def buy_order(ticker, volume):
    try:
        while True:
            buy_result = upbit.buy_market_order(ticker, volume)
            if buy_result == None or 'error' in buy_result:
                time.sleep(0.7)
            else:
                return buy_result
    except:
        pass
#매도 주문
def sell_order(ticker, volume):
    try:
        while True:
            sell_result = upbit.sell_market_order(ticker, volume)
            if sell_result == None or 'error' in sell_result:
                time.sleep(0.7)
            else:
                return sell_result
    except:
        pass
    
# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

op_mode = False

ori_tickers = ["KRW-POLY", "KRW-ZRX", "KRW-LOOM", "KRW-BCH", "KRW-BAT", "KRW-IOST", "KRW-RFR", "KRW-CVC", "KRW-IQ", "KRW-IOTA"]

# 자동매매 시작
while True:
    try:
        for ticker in ori_tickers:
            now = datetime.datetime.now()
            start_time = get_start_time(ticker)
            end_time = start_time + datetime.timedelta(seconds=14400)
            target_p = get_target_price(ticker)
            open_p = get_open_price(ticker)
            current_p = get_current_price(ticker)
            buy_p = get_avg_buy_price(ticker)
            bct_balances = upbit.get_balance(ticker)
            high_p = get_high_price(ticker)
            buys = get_avg_buys_price(ticker)
            buym = get_avg_buym_price(ticker)
            open1_p = get_open1_price(ticker)
            close1_p = get_close1_price(ticker)
            ma5 = get_moving_average(5, ticker)
            ma10 = get_moving_average(10, ticker)
            cash = upbit.get_balance()
            if now.hour == 9 and now.minute == 0 and 1 <=now.second <= 10 or \
                now.hour == 13 and now.minute == 0 and 1 <=now.second <= 10 or \
                now.hour == 17 and now.minute == 0 and 1 <=now.second <= 10 or \
                now.hour == 21 and now.minute == 0 and 1 <=now.second <= 10 or \
                now.hour == 1 and now.minute == 0 and 1 <=now.second <= 10 or \
                now.hour == 5 and now.minute == 0 and 1 <=now.second <= 10:
                op_mode = True
                target_p = get_target_price(ticker)
                start_time = get_start_time(ticker)                
                time.sleep(10)             
            if start_time < now < end_time - datetime.timedelta(seconds=30):
                if op_mode == True:
                    if target_p <= current_p <= target_p*1.01 and ma10 < ma5 and high_p * 0.98 <= current_p or\
                        target_p < current_p and close1_p < open1_p and open_p*1.04 <= current_p <= open_p*1.05 and high_p * 0.98 <= current_p:
                        if cash > 15500 and bct_balances < 0.0002:
                            buy_order(ticker, 15000)
                if buys <= current_p and bct_balances > 0.0002:
                    sell_order(ticker, bct_balances)
                if current_p <= buym and bct_balances > 0.0002:
                    sell_order(ticker, bct_balances)
            else:
                if cash > 0.0001:
                    upbit.sell_market_order(ticker, cash)
    except Exception as e:
        print(e)
        time.sleep(1)