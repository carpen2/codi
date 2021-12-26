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
            target = get_target_price("KRW-MBL", 0.51)
            price = get_current_price("KRW-MBL")
            buy_price = get_avg_buy_price("KRW-MBL")
            if price > buy_price * 1.015:
                MBL = get_balance("MBL")
                upbit.sell_market_order("KRW-MBL", MBL)
            if target < price and op_mode is True and hold is False and hold1 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    MBL = get_balance("MBL")
                    if MBL < 0.0001:
                        upbit.buy_market_order("KRW-MBL", 20000)
                        hold1 = True
                if krw < 20000:
                    hold = True
        else:
            MBL = get_balance("MBL")
            if MBL > 0.0001:
                upbit.sell_market_order("KRW-MBL", MBL)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-WAXP", 0.51)
            price = get_current_price("KRW-WAXP")
            buy_price = get_avg_buy_price("KRW-WAXP")
            if price > buy_price * 1.015:
                WAXP = get_balance("WAXP")
                upbit.sell_market_order("KRW-WAXP", WAXP)
            if target < price and op_mode is True and hold is False and hold2 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    WAXP = get_balance("WAXP")
                    if WAXP < 0.0001:
                        upbit.buy_market_order("KRW-WAXP", 20000)
                        hold2 = True
                if krw < 20000:
                    hold = True
        else:
            WAXP = get_balance("WAXP")
            if WAXP > 0.0001:
                upbit.sell_market_order("KRW-WAXP", WAXP)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-HBAR", 0.51)
            price = get_current_price("KRW-HBAR")
            buy_price = get_avg_buy_price("KRW-HBAR")
            if price > buy_price * 1.015:
                HBAR = get_balance("HBAR")
                upbit.sell_market_order("KRW-HBAR", HBAR)
            if target < price and op_mode is True and hold is False and hold3 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    HBAR = get_balance("HBAR")
                    if HBAR < 0.0001:
                        upbit.buy_market_order("KRW-HBAR", 20000)
                        hold3 = True
                if krw < 20000:
                    hold = True
        else:
            HBAR = get_balance("HBAR")
            if HBAR > 0.0001:
                upbit.sell_market_order("KRW-HBAR", HBAR)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-MED", 0.51)
            price = get_current_price("KRW-MED")
            buy_price = get_avg_buy_price("KRW-MED")
            if price > buy_price * 1.015:
                MED = get_balance("MED")
                upbit.sell_market_order("KRW-MED", MED)
            if target < price and op_mode is True and hold is False and hold4 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    MED = get_balance("MED")
                    if MED < 0.0001:
                        upbit.buy_market_order("KRW-MED", 20000)
                        hold4 = True
                if krw < 20000:
                    hold = True
        else:
            MED = get_balance("MED")
            if MED > 0.0001:
                upbit.sell_market_order("KRW-MED", MED)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-MLK", 0.51)
            price = get_current_price("KRW-MLK")
            buy_price = get_avg_buy_price("KRW-MLK")
            if price > buy_price * 1.015:
                MLK = get_balance("MLK")
                upbit.sell_market_order("KRW-MLK", MLK)
            if target < price and op_mode is True and hold is False and hold5 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    MLK = get_balance("MLK")
                    if MLK < 0.0001:
                        upbit.buy_market_order("KRW-MLK", 20000)
                        hold5 = True
                if krw < 20000:
                    hold = True
        else:
            MLK = get_balance("MLK")
            if MLK > 0.0001:
                upbit.sell_market_order("KRW-MLK", MLK)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-STPT", 0.51)
            price = get_current_price("KRW-STPT")
            buy_price = get_avg_buy_price("KRW-STPT")
            if price > buy_price * 1.015:
                STPT = get_balance("STPT")
                upbit.sell_market_order("KRW-STPT", STPT)
            if target < price and op_mode is True and hold is False and hold6 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    STPT = get_balance("STPT")
                    if STPT < 0.0001:
                        upbit.buy_market_order("KRW-STPT", 20000)
                        hold6 = True
                if krw < 20000:
                    hold = True
        else:
            STPT = get_balance("STPT")
            if STPT > 0.0001:
                upbit.sell_market_order("KRW-STPT", STPT)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-ORBS", 0.51)
            price = get_current_price("KRW-ORBS")
            buy_price = get_avg_buy_price("KRW-ORBS")
            if price > buy_price * 1.015:
                ORBS = get_balance("ORBS")
                upbit.sell_market_order("KRW-ORBS", ORBS)
            if target < price and op_mode is True and hold is False and hold7 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    ORBS = get_balance("ORBS")
                    if ORBS < 0.0001:
                        upbit.buy_market_order("KRW-ORBS", 20000)
                        hold7 = True
                if krw < 20000:
                    hold = True
        else:
            ORBS = get_balance("ORBS")
            if ORBS > 0.0001:
                upbit.sell_market_order("KRW-ORBS", ORBS)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-CHZ", 0.51)
            price = get_current_price("KRW-CHZ")
            buy_price = get_avg_buy_price("KRW-CHZ")
            if price > buy_price * 1.015:
                CHZ = get_balance("CHZ")
                upbit.sell_market_order("KRW-CHZ", CHZ)
            if target < price and op_mode is True and hold is False and hold8 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    CHZ = get_balance("CHZ")
                    if CHZ < 0.0001:
                        upbit.buy_market_order("KRW-CHZ", 20000)
                        hold8 = True
                if krw < 20000:
                    hold = True
        else:
            CHZ = get_balance("CHZ")
            if CHZ > 0.0001:
                upbit.sell_market_order("KRW-CHZ", CHZ)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-VET", 0.51)
            price = get_current_price("KRW-VET")
            buy_price = get_avg_buy_price("KRW-VET")
            if price > buy_price * 1.015:
                VET = get_balance("VET")
                upbit.sell_market_order("KRW-VET", VET)
            if target < price and op_mode is True and hold is False and hold9 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    VET = get_balance("VET")
                    if VET < 0.0001:
                        upbit.buy_market_order("KRW-VET", 20000)
                        hold9 = True
                if krw < 20000:
                    hold = True
        else:
            VET = get_balance("VET")
            if VET > 0.0001:
                upbit.sell_market_order("KRW-VET", VET)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-STMX", 0.51)
            price = get_current_price("KRW-STMX")
            buy_price = get_avg_buy_price("KRW-STMX")
            if price > buy_price * 1.015:
                STMX = get_balance("STMX")
                upbit.sell_market_order("KRW-STMX", STMX)
            if target < price and op_mode is True and hold is False and hold10 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    STMX = get_balance("STMX")
                    if STMX < 0.0001:
                        upbit.buy_market_order("KRW-STMX", 20000)
                        hold10 = True
                if krw < 20000:
                    hold = True
        else:
            STMX = get_balance("STMX")
            if STMX > 0.0001:
                upbit.sell_market_order("KRW-STMX", STMX)

    except Exception as e:
        print(e)
        time.sleep(1)