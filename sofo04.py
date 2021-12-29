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

        if now.hour == 21 and now.minute == 0 and 1 <=now.second <= 10:
            op_mode = True
            time.sleep(10)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-POLY", 0.52)
            price = get_current_price("KRW-POLY")
            buy_price = get_avg_buy_price("KRW-POLY")
            if price < buy_price * 0.98:
                POLY = get_balance("POLY")
                upbit.sell_market_order("KRW-POLY", POLY)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    POLY = get_balance("POLY")
                    if POLY < 0.0001:
                        upbit.buy_market_order("KRW-POLY", 20000)
        else:
            POLY = get_balance("POLY")
            if POLY > 0.0001:
                upbit.sell_market_order("KRW-POLY", POLY)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-ZRX", 0.52)
            price = get_current_price("KRW-ZRX")
            buy_price = get_avg_buy_price("KRW-ZRX")
            if price < buy_price * 0.98:
                ZRX = get_balance("ZRX")
                upbit.sell_market_order("KRW-ZRX", ZRX)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ZRX = get_balance("ZRX")
                    if ZRX < 0.0001:
                        upbit.buy_market_order("KRW-ZRX", 20000)
        else:
            ZRX = get_balance("ZRX")
            if ZRX > 0.0001:
                upbit.sell_market_order("KRW-ZRX", ZRX)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-LOOM", 0.52)
            price = get_current_price("KRW-LOOM")
            buy_price = get_avg_buy_price("KRW-LOOM")
            if price < buy_price * 0.98:
                LOOM = get_balance("LOOM")
                upbit.sell_market_order("KRW-LOOM", LOOM)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    LOOM = get_balance("LOOM")
                    if LOOM < 0.0001:
                        upbit.buy_market_order("KRW-LOOM", 20000)
        else:
            LOOM = get_balance("LOOM")
            if LOOM > 0.0001:
                upbit.sell_market_order("KRW-LOOM", LOOM)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-BCH", 0.52)
            price = get_current_price("KRW-BCH")
            buy_price = get_avg_buy_price("KRW-BCH")
            if price < buy_price * 0.98:
                BCH = get_balance("BCH")
                upbit.sell_market_order("KRW-BCH", BCH)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    BCH = get_balance("BCH")
                    if BCH < 0.0001:
                        upbit.buy_market_order("KRW-BCH", 20000)
        else:
            BCH = get_balance("BCH")
            if BCH > 0.0001:
                upbit.sell_market_order("KRW-BCH", BCH)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-BAT", 0.52)
            price = get_current_price("KRW-BAT")
            buy_price = get_avg_buy_price("KRW-BAT")
            if price < buy_price * 0.98:
                BAT = get_balance("BAT")
                upbit.sell_market_order("KRW-BAT", BAT)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    BAT = get_balance("BAT")
                    if BAT < 0.0001:
                        upbit.buy_market_order("KRW-BAT", 20000)
        else:
            BAT = get_balance("BAT")
            if BAT > 0.0001:
                upbit.sell_market_order("KRW-BAT", BAT)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-IOST", 0.52)
            price = get_current_price("KRW-IOST")
            buy_price = get_avg_buy_price("KRW-IOST")
            if price < buy_price * 0.98:
                IOST = get_balance("IOST")
                upbit.sell_market_order("KRW-IOST", IOST)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    IOST = get_balance("IOST")
                    if IOST < 0.0001:
                        upbit.buy_market_order("KRW-IOST", 20000)
        else:
            IOST = get_balance("IOST")
            if IOST > 0.0001:
                upbit.sell_market_order("KRW-IOST", IOST)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-RFR", 0.52)
            price = get_current_price("KRW-RFR")
            buy_price = get_avg_buy_price("KRW-RFR")
            if price < buy_price * 0.98:
                RFR = get_balance("RFR")
                upbit.sell_market_order("KRW-RFR", RFR)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    RFR = get_balance("RFR")
                    if RFR < 0.0001:
                        upbit.buy_market_order("KRW-RFR", 20000)
        else:
            RFR = get_balance("RFR")
            if RFR > 0.0001:
                upbit.sell_market_order("KRW-RFR", RFR)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-CVC", 0.52)
            price = get_current_price("KRW-CVC")
            buy_price = get_avg_buy_price("KRW-CVC")
            if price < buy_price * 0.98:
                CVC = get_balance("CVC")
                upbit.sell_market_order("KRW-CVC", CVC)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    CVC = get_balance("CVC")
                    if CVC < 0.0001:
                        upbit.buy_market_order("KRW-CVC", 20000)
        else:
            CVC = get_balance("CVC")
            if CVC > 0.0001:
                upbit.sell_market_order("KRW-CVC", CVC)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-IQ", 0.52)
            price = get_current_price("KRW-IQ")
            buy_price = get_avg_buy_price("KRW-IQ")
            if price < buy_price * 0.98:
                IQ = get_balance("IQ")
                upbit.sell_market_order("KRW-IQ", IQ)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    IQ = get_balance("IQ")
                    if IQ < 0.0001:
                        upbit.buy_market_order("KRW-IQ", 20000)
        else:
            IQ = get_balance("IQ")
            if IQ > 0.0001:
                upbit.sell_market_order("KRW-IQ", IQ)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-IOTA", 0.52)
            price = get_current_price("KRW-IOTA")
            buy_price = get_avg_buy_price("KRW-IOTA")
            if price < buy_price * 0.98:
                IOTA = get_balance("IOTA")
                upbit.sell_market_order("KRW-IOTA", IOTA)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    IOTA = get_balance("IOTA")
                    if IOTA < 0.0001:
                        upbit.buy_market_order("KRW-IOTA", 20000)
        else:
            IOTA = get_balance("IOTA")
            if IOTA > 0.0001:
                upbit.sell_market_order("KRW-IOTA", IOTA)

    except Exception as e:
        print(e)
        time.sleep(1)
