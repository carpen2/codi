import time
import pyupbit
import datetime

access = "your-access"
secret = "your-secret"

#변동성 돌파 전략으로 매수 목표가 조회
def get_target_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

#시작 시간 조회"""
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
    
#현재가 조회
def get_current_price(ticker):
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

#hold = False
op_mode = False

#자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(seconds=14400)

        if now.hour == 9 and now.minute == 0 and 1 <=now.second <= 10:
            op_mode = True
            time.sleep(10)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-AXS", 0.51)
            price = get_current_price("KRW-AXS")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    AXS = get_balance("AXS")
                    if AXS < 0.0001:
                        upbit.buy_market_order("KRW-AXS", 20000)
        else:
            AXS = get_balance("AXS")
            if AXS > 0.0001:
                upbit.sell_market_order("KRW-AXS", AXS)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-STX", 0.51)
            price = get_current_price("KRW-STX")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    STX = get_balance("STX")
                    if STX < 0.0001:
                        upbit.buy_market_order("KRW-STX", 20000)
        else:
            STX = get_balance("STX")
            if STX > 0.0001:
                upbit.sell_market_order("KRW-STX", STX)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-XEC", 0.51)
            price = get_current_price("KRW-XEC")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    XEC = get_balance("XEC")
                    if XEC < 0.0001:
                        upbit.buy_market_order("KRW-XEC", 20000)
        else:
            XEC = get_balance("XEC")
            if XEC > 0.0001:
                upbit.sell_market_order("KRW-XEC", XEC)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-SOL", 0.51)
            price = get_current_price("KRW-SOL")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    SOL = get_balance("SOL")
                    if SOL < 0.0001:
                        upbit.buy_market_order("KRW-SOL", 20000)
        else:
            SOL = get_balance("SOL")
            if SOL > 0.0001:
                upbit.sell_market_order("KRW-SOL", SOL)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-MATIC", 0.51)
            price = get_current_price("KRW-MATIC")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    MATIC = get_balance("MATIC")
                    if MATIC < 0.0001:
                        upbit.buy_market_order("KRW-MATIC", 20000)
        else:
            MATIC = get_balance("MATIC")
            if MATIC > 0.0001:
                upbit.sell_market_order("KRW-MATIC", MATIC)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-NU", 0.51)
            price = get_current_price("KRW-NU")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    NU = get_balance("NU")
                    if NU < 0.0001:
                        upbit.buy_market_order("KRW-NU", 20000)
        else:
            NU = get_balance("NU")
            if NU > 0.0001:
                upbit.sell_market_order("KRW-NU", NU)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-AAVE", 0.51)
            price = get_current_price("KRW-AAVE")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    AAVE = get_balance("AAVE")
                    if AAVE < 0.0001:
                        upbit.buy_market_order("KRW-AAVE", 20000)
        else:
            AAVE = get_balance("AAVE")
            if AAVE > 0.0001:
                upbit.sell_market_order("KRW-AAVE", AAVE)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-ALGO", 0.51)
            price = get_current_price("KRW-ALGO")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ALGO = get_balance("ALGO")
                    if ALGO < 0.0001:
                        upbit.buy_market_order("KRW-ALGO", 20000)
        else:
            ALGO = get_balance("ALGO")
            if ALGO > 0.0001:
                upbit.sell_market_order("KRW-ALGO", ALGO)
                           
    except Exception as e:
        print(e)
        time.sleep(1)