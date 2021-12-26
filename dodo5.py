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
            target = get_target_price("KRW-MOC", 0.51)
            price = get_current_price("KRW-MOC")
            buy_price = get_avg_buy_price("KRW-MOC")
            if price > buy_price * 1.015:
                MOC = get_balance("MOC")
                upbit.sell_market_order("KRW-MOC", MOC)
            if target < price and op_mode is True and hold is False and hold1 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    MOC = get_balance("MOC")
                    if MOC < 0.0001:
                        upbit.buy_market_order("KRW-MOC", 20000)
                        hold1 = True
                if krw < 20000:
                    hold = True
        else:
            MOC = get_balance("MOC")
            if MOC > 0.0001:
                upbit.sell_market_order("KRW-MOC", MOC)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-ENJ", 0.51)
            price = get_current_price("KRW-ENJ")
            buy_price = get_avg_buy_price("KRW-ENJ")
            if price > buy_price * 1.015:
                ENJ = get_balance("ENJ")
                upbit.sell_market_order("KRW-ENJ", ENJ)
            if target < price and op_mode is True and hold is False and hold2 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    ENJ = get_balance("ENJ")
                    if ENJ < 0.0001:
                        upbit.buy_market_order("KRW-ENJ", 20000)
                        hold2 = True
                if krw < 20000:
                    hold = True
        else:
            ENJ = get_balance("ENJ")
            if ENJ > 0.0001:
                upbit.sell_market_order("KRW-ENJ", ENJ)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-TFUEL", 0.51)
            price = get_current_price("KRW-TFUEL")
            buy_price = get_avg_buy_price("KRW-TFUEL")
            if price > buy_price * 1.015:
                TFUEL = get_balance("TFUEL")
                upbit.sell_market_order("KRW-TFUEL", TFUEL)
            if target < price and op_mode is True and hold is False and hold3 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    TFUEL = get_balance("TFUEL")
                    if TFUEL < 0.0001:
                        upbit.buy_market_order("KRW-TFUEL", 20000)
                        hold3 = True
                if krw < 20000:
                    hold = True
        else:
            TFUEL = get_balance("TFUEL")
            if TFUEL > 0.0001:
                upbit.sell_market_order("KRW-TFUEL", TFUEL)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-MANA", 0.51)
            price = get_current_price("KRW-MANA")
            buy_price = get_avg_buy_price("KRW-MANA")
            if price > buy_price * 1.015:
                MANA = get_balance("MANA")
                upbit.sell_market_order("KRW-MANA", MANA)
            if target < price and op_mode is True and hold is False and hold4 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    MANA = get_balance("MANA")
                    if MANA < 0.0001:
                        upbit.buy_market_order("KRW-MANA", 20000)
                        hold4 = True
                if krw < 20000:
                    hold = True
        else:
            MANA = get_balance("MANA")
            if MANA > 0.0001:
                upbit.sell_market_order("KRW-MANA", MANA)
            
        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-ANKR", 0.51)
            price = get_current_price("KRW-ANKR")
            buy_price = get_avg_buy_price("KRW-ANKR")
            if price > buy_price * 1.015:
                ANKR = get_balance("ANKR")
                upbit.sell_market_order("KRW-ANKR", ANKR)
            if target < price and op_mode is True and hold is False and hold5 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    ANKR = get_balance("ANKR")
                    if ANKR < 0.0001:
                        upbit.buy_market_order("KRW-ANKR", 20000)
                        hold5 = True
                if krw < 20000:
                    hold = True
        else:
            ANKR = get_balance("ANKR")
            if ANKR > 0.0001:
                upbit.sell_market_order("KRW-ANKR", ANKR)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-AERGO", 0.51)
            price = get_current_price("KRW-AERGO")
            buy_price = get_avg_buy_price("KRW-AERGO")
            if price > buy_price * 1.015:
                AERGO = get_balance("AERGO")
                upbit.sell_market_order("KRW-AERGO", AERGO)
            if target < price and op_mode is True and hold is False and hold6 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    AERGO = get_balance("AERGO")
                    if AERGO < 0.0001:
                        upbit.buy_market_order("KRW-AERGO", 20000)
                        hold6 = True
                if krw < 20000:
                    hold = True
        else:
            AERGO = get_balance("AERGO")
            if AERGO > 0.0001:
                upbit.sell_market_order("KRW-AERGO", AERGO)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-ATOM", 0.51)
            price = get_current_price("KRW-ATOM")
            buy_price = get_avg_buy_price("KRW-ATOM")
            if price > buy_price * 1.015:
                ATOM = get_balance("ATOM")
                upbit.sell_market_order("KRW-ATOM", ATOM)
            if target < price and op_mode is True and hold is False and hold7 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    ATOM = get_balance("ATOM")
                    if ATOM < 0.0001:
                        upbit.buy_market_order("KRW-ATOM", 20000)
                        hold7 = True
                if krw < 20000:
                    hold = True
        else:
            ATOM = get_balance("ATOM")
            if ATOM > 0.0001:
                upbit.sell_market_order("KRW-ATOM", ATOM)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-TT", 0.51)
            price = get_current_price("KRW-TT")
            buy_price = get_avg_buy_price("KRW-TT")
            if price > buy_price * 1.015:
                TT = get_balance("TT")
                upbit.sell_market_order("KRW-TT", TT)
            if target < price and op_mode is True and hold is False and hold8 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    TT = get_balance("TT")
                    if TT < 0.0001:
                        upbit.buy_market_order("KRW-TT", 20000)
                        hold8 = True
                if krw < 20000:
                    hold = True
        else:
            TT = get_balance("TT")
            if TT > 0.0001:
                upbit.sell_market_order("KRW-TT", TT)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-CRE", 0.51)
            price = get_current_price("KRW-CRE")
            buy_price = get_avg_buy_price("KRW-CRE")
            if price > buy_price * 1.015:
                CRE = get_balance("CRE")
                upbit.sell_market_order("KRW-CRE", CRE)
            if target < price and op_mode is True and hold is False and hold9 is False:
                krw = get_balance("KRW")
                if krw > 20000:
                    CRE = get_balance("CRE")
                    if CRE < 0.0001:
                        upbit.buy_market_order("KRW-CRE", 20000)
                        hold9 = True
                if krw < 20000:
                    hold = True
        else:
            CRE = get_balance("CRE")
            if CRE > 0.0001:
                upbit.sell_market_order("KRW-CRE", CRE)
                
    except Exception as e:
        print(e)
        time.sleep(1)
