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
            target = get_target_price("KRW-XEM", 0.51)
            price = get_current_price("KRW-XEM")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    XEM = get_balance("XEM")
                    if XEM < 0.0001:
                        upbit.buy_market_order("KRW-XEM", 20000)                   
        else:
            XEM = get_balance("XEM")
            if XEM > 0.0001:
                upbit.sell_market_order("KRW-XEM", XEM)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-QTUM", 0.51)
            price = get_current_price("KRW-QTUM")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    QTUM = get_balance("QTUM")
                    if QTUM < 0.0001:
                        upbit.buy_market_order("KRW-QTUM", 20000)                   
        else:
            QTUM = get_balance("QTUM")
            if QTUM > 0.0001:
                upbit.sell_market_order("KRW-QTUM", QTUM)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-LSK", 0.51)
            price = get_current_price("KRW-LSK")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    LSK = get_balance("LSK")
                    if LSK < 0.0001:
                        upbit.buy_market_order("KRW-LSK", 20000)                   
        else:
            LSK = get_balance("LSK")
            if LSK > 0.0001:
                upbit.sell_market_order("KRW-LSK", LSK)               

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-STEEM", 0.51)
            price = get_current_price("KRW-STEEM")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    STEEM = get_balance("STEEM")
                    if STEEM < 0.0001:
                        upbit.buy_market_order("KRW-STEEM", 20000)                   
        else:
            STEEM = get_balance("STEEM")
            if STEEM > 0.0001:
                upbit.sell_market_order("KRW-STEEM", STEEM)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-XLM", 0.51)
            price = get_current_price("KRW-XLM")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    XLM = get_balance("XLM")
                    if XLM < 0.0001:
                        upbit.buy_market_order("KRW-XLM", 20000)                   
        else:
            XLM = get_balance("XLM")
            if XLM > 0.0001:
                upbit.sell_market_order("KRW-XLM", XLM)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-ARDR", 0.51)
            price = get_current_price("KRW-ARDR")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ARDR = get_balance("ARDR")
                    if ARDR < 0.0001:
                        upbit.buy_market_order("KRW-ARDR", 20000)                   
        else:
            ARDR = get_balance("ARDR")
            if ARDR > 0.0001:
                upbit.sell_market_order("KRW-ARDR", ARDR)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-ARK", 0.51)
            price = get_current_price("KRW-ARK")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ARK = get_balance("ARK")
                    if ARK < 0.0001:
                        upbit.buy_market_order("KRW-ARK", 20000)                   
        else:
            ARK = get_balance("ARK")
            if ARK > 0.0001:
                upbit.sell_market_order("KRW-ARK", ARK)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-STORJ", 0.51)
            price = get_current_price("KRW-STORJ")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    STORJ = get_balance("STORJ")
                    if STORJ < 0.0001:
                        upbit.buy_market_order("KRW-STORJ", 20000)                   
        else:
            STORJ = get_balance("STORJ")
            if STORJ > 0.0001:
                upbit.sell_market_order("KRW-STORJ", STORJ)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-GRS", 0.51)
            price = get_current_price("KRW-GRS")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    GRS = get_balance("GRS")
                    if GRS < 0.0001:
                        upbit.buy_market_order("KRW-GRS", 20000)                   
        else:
            GRS = get_balance("GRS")
            if GRS > 0.0001:
                upbit.sell_market_order("KRW-GRS", GRS)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-REP", 0.51)
            price = get_current_price("KRW-REP")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    REP = get_balance("REP")
                    if REP < 0.0001:
                        upbit.buy_market_order("KRW-REP", 20000)                   
        else:
            REP = get_balance("REP")
            if REP > 0.0001:
                upbit.sell_market_order("KRW-REP", REP)

    except Exception as e:
        print(e)
        time.sleep(1)            

