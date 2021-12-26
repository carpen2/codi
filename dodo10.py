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
            time.sleep(10)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-AXS", 0.51)
            price = get_current_price("KRW-AXS")
            buy_price = get_avg_buy_price("KRW-AXS")
            if price > buy_price * 1.015:
                AXS = get_balance("AXS")
                upbit.sell_market_order("KRW-AXS", AXS)
            if target < price and op_mode is True and hold is False and hold1 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    AXS = get_balance("AXS")
                    if AXS < 0.0001:
                        upbit.buy_market_order("KRW-AXS", 20000)
                        hold1 = True
                if krw < 20000:
                    hold = True
        else:
            AXS = get_balance("AXS")
            if AXS > 0.0001:
                upbit.sell_market_order("KRW-AXS", AXS)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-STX", 0.51)
            price = get_current_price("KRW-STX")
            buy_price = get_avg_buy_price("KRW-STX")
            if price > buy_price * 1.015:
                STX = get_balance("STX")
                upbit.sell_market_order("KRW-STX", STX)
            if target < price and op_mode is True and hold is False and hold2 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    STX = get_balance("STX")
                    if STX < 0.0001:
                        upbit.buy_market_order("KRW-STX", 20000)
                        hold2 = True
                if krw < 20000:
                    hold = True
        else:
            STX = get_balance("STX")
            if STX > 0.0001:
                upbit.sell_market_order("KRW-STX", STX)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-XEC", 0.51)
            price = get_current_price("KRW-XEC")
            buy_price = get_avg_buy_price("KRW-XEC")
            if price > buy_price * 1.015:
                XEC = get_balance("XEC")
                upbit.sell_market_order("KRW-XEC", XEC)
            if target < price and op_mode is True and hold is False and hold3 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    XEC = get_balance("XEC")
                    if XEC < 0.0001:
                        upbit.buy_market_order("KRW-XEC", 20000)
                        hold3 = True
                if krw < 20000:
                    hold = True
        else:
            XEC = get_balance("XEC")
            if XEC > 0.0001:
                upbit.sell_market_order("KRW-XEC", XEC)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-SOL", 0.51)
            price = get_current_price("KRW-SOL")
            buy_price = get_avg_buy_price("KRW-SOL")
            if price > buy_price * 1.015:
                SOL = get_balance("SOL")
                upbit.sell_market_order("KRW-SOL", SOL)
            if target < price and op_mode is True and hold is False and hold4 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    SOL = get_balance("SOL")
                    if SOL < 0.0001:
                        upbit.buy_market_order("KRW-SOL", 20000)
                        hold4 = True
                if krw < 20000:
                    hold = True
        else:
            SOL = get_balance("SOL")
            if SOL > 0.0001:
                upbit.sell_market_order("KRW-SOL", SOL)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-MATIC", 0.51)
            price = get_current_price("KRW-MATIC")
            buy_price = get_avg_buy_price("KRW-MATIC")
            if price > buy_price * 1.015:
                MATIC = get_balance("MATIC")
                upbit.sell_market_order("KRW-MATIC", MATIC)
            if target < price and op_mode is True and hold is False and hold5 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    MATIC = get_balance("MATIC")
                    if MATIC < 0.0001:
                        upbit.buy_market_order("KRW-MATIC", 20000)
                        hold5 = True
                if krw < 20000:
                    hold = True
        else:
            MATIC = get_balance("MATIC")
            if MATIC > 0.0001:
                upbit.sell_market_order("KRW-MATIC", MATIC)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-NU", 0.51)
            price = get_current_price("KRW-NU")
            buy_price = get_avg_buy_price("KRW-NU")
            if price > buy_price * 1.015:
                NU = get_balance("NU")
                upbit.sell_market_order("KRW-NU", NU)
            if target < price and op_mode is True and hold is False and hold6 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    NU = get_balance("NU")
                    if NU < 0.0001:
                        upbit.buy_market_order("KRW-NU", 20000)
                        hold6 = True
                if krw < 20000:
                    hold = True
        else:
            NU = get_balance("NU")
            if NU > 0.0001:
                upbit.sell_market_order("KRW-NU", NU)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-AAVE", 0.51)
            price = get_current_price("KRW-AAVE")
            buy_price = get_avg_buy_price("KRW-AAVE")
            if price > buy_price * 1.015:
                AAVE = get_balance("AAVE")
                upbit.sell_market_order("KRW-AAVE", AAVE)
            if target < price and op_mode is True and hold is False and hold7 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    AAVE = get_balance("AAVE")
                    if AAVE < 0.0001:
                        upbit.buy_market_order("KRW-AAVE", 20000)
                        hold7 = True
                if krw < 20000:
                    hold = True
        else:
            AAVE = get_balance("AAVE")
            if AAVE > 0.0001:
                upbit.sell_market_order("KRW-AAVE", AAVE)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-ALGO", 0.51)
            price = get_current_price("KRW-ALGO")
            buy_price = get_avg_buy_price("KRW-ALGO")
            if price > buy_price * 1.015:
                ALGO = get_balance("ALGO")
                upbit.sell_market_order("KRW-ALGO", ALGO)
            if target < price and op_mode is True and hold is False and hold8 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    ALGO = get_balance("ALGO")
                    if ALGO < 0.0001:
                        upbit.buy_market_order("KRW-ALGO", 20000)
                        hold8 = True
                if krw < 20000:
                    hold = True
        else:
            ALGO = get_balance("ALGO")
            if ALGO > 0.0001:
                upbit.sell_market_order("KRW-ALGO", ALGO)
                
    except Exception as e:
        print(e)
        time.sleep(1)