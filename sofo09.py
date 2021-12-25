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
            target = get_target_price("KRW-META", 0.51)
            price = get_current_price("KRW-META")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    META = get_balance("META")
                    if META < 0.0001:
                        upbit.buy_market_order("KRW-META", 20000)
        else:
            META = get_balance("META")
            if META > 0.0001:
                upbit.sell_market_order("KRW-META", META)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-FCT2", 0.51)
            price = get_current_price("KRW-FCT2")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    FCT2 = get_balance("FCT2")
                    if FCT2 < 0.0001:
                        upbit.buy_market_order("KRW-FCT2", 20000)
        else:
            FCT2 = get_balance("FCT2")
            if FCT2 > 0.0001:
                upbit.sell_market_order("KRW-FCT2", FCT2)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-CBK", 0.51)
            price = get_current_price("KRW-CBK")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    CBK = get_balance("CBK")
                    if CBK < 0.0001:
                        upbit.buy_market_order("KRW-CBK", 20000)
        else:
            CBK = get_balance("CBK")
            if CBK > 0.0001:
                upbit.sell_market_order("KRW-CBK", CBK)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-SAND", 0.51)
            price = get_current_price("KRW-SAND")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    SAND = get_balance("SAND")
                    if SAND < 0.0001:
                        upbit.buy_market_order("KRW-SAND", 20000)
        else:
            SAND = get_balance("SAND")
            if SAND > 0.0001:
                upbit.sell_market_order("KRW-SAND", SAND)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-HUM", 0.51)
            price = get_current_price("KRW-HUM")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    HUM = get_balance("HUM")
                    if HUM < 0.0001:
                        upbit.buy_market_order("KRW-HUM", 20000)
        else:
            HUM = get_balance("HUM")
            if HUM > 0.0001:
                upbit.sell_market_order("KRW-HUM", HUM)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-DOGE", 0.51)
            price = get_current_price("KRW-DOGE")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    DOGE = get_balance("DOGE")
                    if DOGE < 0.0001:
                        upbit.buy_market_order("KRW-DOGE", 20000)
        else:
            DOGE = get_balance("DOGE")
            if DOGE > 0.0001:
                upbit.sell_market_order("KRW-DOGE", DOGE)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-STRK", 0.51)
            price = get_current_price("KRW-STRK")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    STRK = get_balance("STRK")
                    if STRK < 0.0001:
                        upbit.buy_market_order("KRW-STRK", 20000)
        else:
            STRK = get_balance("STRK")
            if STRK > 0.0001:
                upbit.sell_market_order("KRW-STRK", STRK)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-PUNDIX", 0.51)
            price = get_current_price("KRW-PUNDIX")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    PUNDIX = get_balance("PUNDIX")
                    if PUNDIX < 0.0001:
                        upbit.buy_market_order("KRW-PUNDIX", 20000)
        else:
            PUNDIX = get_balance("PUNDIX")
            if PUNDIX > 0.0001:
                upbit.sell_market_order("KRW-PUNDIX", PUNDIX)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-FLOW", 0.51)
            price = get_current_price("KRW-FLOW")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    FLOW = get_balance("FLOW")
                    if FLOW < 0.0001:
                        upbit.buy_market_order("KRW-FLOW", 20000)
        else:
            FLOW = get_balance("FLOW")
            if FLOW > 0.0001:
                upbit.sell_market_order("KRW-FLOW", FLOW)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-DAWN", 0.51)
            price = get_current_price("KRW-DAWN")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    DAWN = get_balance("DAWN")
                    if DAWN < 0.0001:
                        upbit.buy_market_order("KRW-DAWN", 20000)
        else:
            DAWN = get_balance("DAWN")
            if DAWN > 0.0001:
                upbit.sell_market_order("KRW-DAWN", DAWN)            
    
    except Exception as e:
        print(e)
        time.sleep(1)