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

hold = False
hold2 = False
hold3 = False
hold4 = False
hold5 = False
hold6 = False
hold7 = False
hold8 = False
hold9 = False
hold10 = False
op_mode = False

#자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(seconds=14400)

        if now.hour == 9 and now.minute == 0 and 1 <=now.second <= 10 or now.hour == 13 and now.minute == 0 and 1 <=now.second <= 10 or now.hour == 17 and now.minute == 0 and 1 <=now.second <= 10 or now.hour == 21 and now.minute == 0 and 1 <=now.second <= 10 or now.hour == 1 and now.minute == 0 and 1 <=now.second <= 10 or now.hour == 5 and now.minute == 0 and 1 <=now.second <= 10:
            op_mode = True
            hold = False
            hold2 = False
            hold3 = False
            hold4 = False
            hold5 = False
            hold6 = False
            hold7 = False
            hold8 = False
            hold9 = False
            hold10 = False
            time.sleep(10)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-XEM", 0.51)
            price = get_current_price("KRW-XEM")
            buy_price = get_avg_buy_price("KRW-XEM")
            if price > buy_price * 1.015:
                XEM = get_balance("XEM")
                upbit.sell_market_order("KRW-XEM", XEM)
            if target < price and op_mode is True and hold is False and hold1 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    XEM = get_balance("XEM")
                    if XEM < 0.0001:
                        upbit.buy_market_order("KRW-XEM", 20000)
                        hold1 = True
                if krw < 20000:
                    hold = True
        else:
            XEM = get_balance("XEM")
            if XEM > 0.0001:
                upbit.sell_market_order("KRW-XEM", XEM)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-QTUM", 0.51)
            price = get_current_price("KRW-QTUM")
            buy_price = get_avg_buy_price("KRW-QTUM")
            if price > buy_price * 1.015:
                QTUM = get_balance("QTUM")
                upbit.sell_market_order("KRW-QTUM", QTUM)
            if target < price and op_mode is True and hold is False and hold2 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    QTUM = get_balance("QTUM")
                    if QTUM < 0.0001:
                        upbit.buy_market_order("KRW-QTUM", 20000)
                        hold2 = True
                if krw < 20000:
                    hold = True
        else:
            QTUM = get_balance("QTUM")
            if QTUM > 0.0001:
                upbit.sell_market_order("KRW-QTUM", QTUM)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-LSK", 0.51)
            price = get_current_price("KRW-LSK")
            buy_price = get_avg_buy_price("KRW-LSK")
            if price > buy_price * 1.015:
                LSK = get_balance("LSK")
                upbit.sell_market_order("KRW-LSK", LSK)
            if target < price and op_mode is True and hold is False and hold3 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    LSK = get_balance("LSK")
                    if LSK < 0.0001:
                        upbit.buy_market_order("KRW-LSK", 20000)
                        hold3 = True
                if krw < 20000:
                    hold = True
        else:
            LSK = get_balance("LSK")
            if LSK > 0.0001:
                upbit.sell_market_order("KRW-LSK", LSK)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-STEEM", 0.51)
            price = get_current_price("KRW-STEEM")
            buy_price = get_avg_buy_price("KRW-STEEM")
            if price > buy_price * 1.015:
                STEEM = get_balance("STEEM")
                upbit.sell_market_order("KRW-STEEM", STEEM)
            if target < price and op_mode is True and hold is False and hold4 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    STEEM = get_balance("STEEM")
                    if STEEM < 0.0001:
                        upbit.buy_market_order("KRW-STEEM", 20000)
                        hold4 = True
                if krw < 20000:
                    hold = True
        else:
            STEEM = get_balance("STEEM")
            if STEEM > 0.0001:
                upbit.sell_market_order("KRW-STEEM", STEEM)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-XLM", 0.51)
            price = get_current_price("KRW-XLM")
            buy_price = get_avg_buy_price("KRW-XLM")
            if price > buy_price * 1.015:
                XLM = get_balance("XLM")
                upbit.sell_market_order("KRW-XLM", XLM)
            if target < price and op_mode is True and hold is False and hold5 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    XLM = get_balance("XLM")
                    if XLM < 0.0001:
                        upbit.buy_market_order("KRW-XLM", 20000)
                        hold5 = True
                if krw < 20000:
                    hold = True
        else:
            XLM = get_balance("XLM")
            if XLM > 0.0001:
                upbit.sell_market_order("KRW-XLM", XLM)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-ARDR", 0.51)
            price = get_current_price("KRW-ARDR")
            buy_price = get_avg_buy_price("KRW-ARDR")
            if price > buy_price * 1.015:
                ARDR = get_balance("ARDR")
                upbit.sell_market_order("KRW-ARDR", ARDR)
            if target < price and op_mode is True and hold is False and hold6 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    ARDR = get_balance("ARDR")
                    if ARDR < 0.0001:
                        upbit.buy_market_order("KRW-ARDR", 20000)
                        hold6 = True
                if krw < 20000:
                    hold = True
                    hold6 = True
        else:
            ARDR = get_balance("ARDR")
            if ARDR > 0.0001:
                upbit.sell_market_order("KRW-ARDR", ARDR)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-ARK", 0.51)
            price = get_current_price("KRW-ARK")
            buy_price = get_avg_buy_price("KRW-ARK")
            if price > buy_price * 1.015:
                ARK = get_balance("ARK")
                upbit.sell_market_order("KRW-ARK", ARK)
            if target < price and op_mode is True and hold is False and hold7 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    ARK = get_balance("ARK")
                    if ARK < 0.0001:
                        upbit.buy_market_order("KRW-ARK", 20000)
                        hold7 = True
                if krw < 20000:
                    hold = True
        else:
            ARK = get_balance("ARK")
            if ARK > 0.0001:
                upbit.sell_market_order("KRW-ARK", ARK)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-STORJ", 0.51)
            price = get_current_price("KRW-STORJ")
            buy_price = get_avg_buy_price("KRW-STORJ")
            if price > buy_price * 1.015:
                STORJ = get_balance("STORJ")
                upbit.sell_market_order("KRW-STORJ", STORJ)
            if target < price and op_mode is True and hold is False and hold8 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    STORJ = get_balance("STORJ")
                    if STORJ < 0.0001:
                        upbit.buy_market_order("KRW-STORJ", 20000)
                        hold8 = True
                if krw < 20000:
                    hold = True
        else:
            STORJ = get_balance("STORJ")
            if STORJ > 0.0001:
                upbit.sell_market_order("KRW-STORJ", STORJ)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-GRS", 0.51)
            price = get_current_price("KRW-GRS")
            buy_price = get_avg_buy_price("KRW-GRS")
            if price > buy_price * 1.015:
                GRS = get_balance("GRS")
                upbit.sell_market_order("KRW-GRS", GRS)
            if target < price and op_mode is True and hold is False and hold9 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    GRS = get_balance("GRS")
                    if GRS < 0.0001:
                        upbit.buy_market_order("KRW-GRS", 20000)
                        hold9 = True
                if krw < 20000:
                    hold = True
        else:
            GRS = get_balance("GRS")
            if GRS > 0.0001:
                upbit.sell_market_order("KRW-GRS", GRS)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-REP", 0.51)
            price = get_current_price("KRW-REP")
            buy_price = get_avg_buy_price("KRW-REP")
            if price > buy_price * 1.015:
                REP = get_balance("REP")
                upbit.sell_market_order("KRW-REP", REP)
            if target < price and op_mode is True and hold is False and hold10 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    REP = get_balance("REP")
                    if REP < 0.0001:
                        upbit.buy_market_order("KRW-REP", 20000)
                        hold10 = True
                if krw < 20000:
                    hold = True
        else:
            REP = get_balance("REP")
            if REP > 0.0001:
                upbit.sell_market_order("KRW-REP", REP)

    except Exception as e:
        print(e)
        time.sleep(1)