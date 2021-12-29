import time
import pyupbit
import datetime

access = "123"
secret = "123"

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

#매수평균가
def get_avg_buy_price(ticker):
    buy_price = upbit.get_avg_buy_price(ticker)
    return buy_price

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

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

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-HUNT", 0.52)
            price = get_current_price("KRW-HUNT")
            buy_price = get_avg_buy_price("KRW-HUNT")
            if price < buy_price * 0.98:
                HUNT = get_balance("HUNT")
                upbit.sell_market_order("KRW-HUNT", HUNT)
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

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-PLA", 0.52)
            price = get_current_price("KRW-PLA")
            buy_price = get_avg_buy_price("KRW-PLA")
            if price < buy_price * 0.98:
                PLA = get_balance("PLA")
                upbit.sell_market_order("KRW-PLA", PLA)
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
                
        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-DOT", 0.52)
            price = get_current_price("KRW-DOT")
            buy_price = get_avg_buy_price("KRW-DOT")
            if price < buy_price * 0.98:
                DOT = get_balance("DOT")
                upbit.sell_market_order("KRW-DOT", DOT)
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

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-SRM", 0.52)
            price = get_current_price("KRW-SRM")
            buy_price = get_avg_buy_price("KRW-SRM")
            if price < buy_price * 0.98:
                SRM = get_balance("SRM")
                upbit.sell_market_order("KRW-SRM", SRM)
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

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-MVL", 0.52)
            price = get_current_price("KRW-MVL")
            buy_price = get_avg_buy_price("KRW-MVL")
            if price < buy_price * 0.98:
                MVL = get_balance("MVL")
                upbit.sell_market_order("KRW-MVL", MVL)
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

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-STRAX", 0.52)
            price = get_current_price("KRW-STRAX")
            buy_price = get_avg_buy_price("KRW-STRAX")
            if price < buy_price * 0.98:
                STRAX = get_balance("STRAX")
                upbit.sell_market_order("KRW-STRAX", STRAX)
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

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-AQT", 0.52)
            price = get_current_price("KRW-AQT")
            buy_price = get_avg_buy_price("KRW-AQT")
            if price < buy_price * 0.98:
                AQT = get_balance("AQT")
                upbit.sell_market_order("KRW-AQT", AQT)
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

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-GLM", 0.52)
            price = get_current_price("KRW-GLM")
            buy_price = get_avg_buy_price("KRW-GLM")
            if price < buy_price * 0.98:
                GLM = get_balance("GLM")
                upbit.sell_market_order("KRW-GLM", GLM)
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

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-SSX", 0.52)
            price = get_current_price("KRW-SSX")
            buy_price = get_avg_buy_price("KRW-SSX")
            if price < buy_price * 0.98:
                SSX = get_balance("SSX")
                upbit.sell_market_order("KRW-SSX", SSX)
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

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-META", 0.52)
            price = get_current_price("KRW-META")
            buy_price = get_avg_buy_price("KRW-META")
            if price < buy_price * 0.98:
                META = get_balance("META")
                upbit.sell_market_order("KRW-META", META)
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

    except Exception as e:
        print(e)
        time.sleep(1)
