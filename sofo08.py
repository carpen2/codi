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
            target = get_target_price("KRW-SXP", 0.51)
            price = get_current_price("KRW-SXP")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    SXP = get_balance("SXP")
                    if SXP < 0.0001:
                        upbit.buy_market_order("KRW-SXP", 20000)
        else:
            SXP = get_balance("SXP")
            if SXP > 0.0001:
                upbit.sell_market_order("KRW-SXP", SXP)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-HUNT", 0.51)
            price = get_current_price("KRW-HUNT")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    HUNT = get_balance("HUNT")
                    if HUNT < 0.0001:
                        upbit.buy_market_order("KRW-HUNT", 20000)
        else:
            HUNT = get_balance("HUNT")
            if HUNT > 0.0001:
                upbit.sell_market_order("KRW-HUNT", HUNT)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-PLA", 0.51)
            price = get_current_price("KRW-PLA")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    PLA = get_balance("PLA")
                    if PLA < 0.0001:
                        upbit.buy_market_order("KRW-PLA", 20000)
        else:
            PLA = get_balance("PLA")
            if PLA > 0.0001:
                upbit.sell_market_order("KRW-PLA", PLA)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-DOT", 0.51)
            price = get_current_price("KRW-DOT")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    DOT = get_balance("DOT")
                    if DOT < 0.0001:
                        upbit.buy_market_order("KRW-DOT", 20000)
        else:
            DOT = get_balance("DOT")
            if DOT > 0.0001:
                upbit.sell_market_order("KRW-DOT", DOT)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-SRM", 0.51)
            price = get_current_price("KRW-SRM")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    SRM = get_balance("SRM")
                    if SRM < 0.0001:
                        upbit.buy_market_order("KRW-SRM", 20000)
        else:
            SRM = get_balance("SRM")
            if SRM > 0.0001:
                upbit.sell_market_order("KRW-SRM", SRM)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-MVL", 0.51)
            price = get_current_price("KRW-MVL")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    MVL = get_balance("MVL")
                    if MVL < 0.0001:
                        upbit.buy_market_order("KRW-MVL", 20000)
        else:
            MVL = get_balance("MVL")
            if MVL > 0.0001:
                upbit.sell_market_order("KRW-MVL", MVL)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-STRAX", 0.51)
            price = get_current_price("KRW-STRAX")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    STRAX = get_balance("STRAX")
                    if STRAX < 0.0001:
                        upbit.buy_market_order("KRW-STRAX", 20000)
        else:
            STRAX = get_balance("STRAX")
            if STRAX > 0.0001:
                upbit.sell_market_order("KRW-STRAX", STRAX)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-AQT", 0.51)
            price = get_current_price("KRW-AQT")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    AQT = get_balance("AQT")
                    if AQT < 0.0001:
                        upbit.buy_market_order("KRW-AQT", 20000)
        else:
            AQT = get_balance("AQT")
            if AQT > 0.0001:
                upbit.sell_market_order("KRW-AQT", AQT)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-GLM", 0.51)
            price = get_current_price("KRW-GLM")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    GLM = get_balance("GLM")
                    if GLM < 0.0001:
                        upbit.buy_market_order("KRW-GLM", 20000)
        else:
            GLM = get_balance("GLM")
            if GLM > 0.0001:
                upbit.sell_market_order("KRW-GLM", GLM)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-SSX", 0.51)
            price = get_current_price("KRW-SSX")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    SSX = get_balance("SSX")
                    if SSX < 0.0001:
                        upbit.buy_market_order("KRW-SSX", 20000)
        else:
            SSX = get_balance("SSX")
            if SSX > 0.0001:
                upbit.sell_market_order("KRW-SSX", SSX)

    except Exception as e:
        print(e)
        time.sleep(1)