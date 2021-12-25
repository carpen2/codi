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
            target = get_target_price("KRW-MOC", 0.51)
            price = get_current_price("KRW-MOC")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    MOC = get_balance("MOC")
                    if MOC < 0.0001:
                        upbit.buy_market_order("KRW-MOC", 20000)                   
        else:
            MOC = get_balance("MOC")
            if MOC > 0.0001:
                upbit.sell_market_order("KRW-MOC", MOC)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-ENJ", 0.51)
            price = get_current_price("KRW-ENJ")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ENJ = get_balance("ENJ")
                    if ENJ < 0.0001:
                        upbit.buy_market_order("KRW-ENJ", 20000)                   
        else:
            ENJ = get_balance("ENJ")
            if ENJ > 0.0001:
                upbit.sell_market_order("KRW-ENJ", ENJ)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-TFUEL", 0.51)
            price = get_current_price("KRW-TFUEL")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    TFUEL = get_balance("TFUEL")
                    if TFUEL < 0.0001:
                        upbit.buy_market_order("KRW-TFUEL", 20000)
        else:
            TFUEL = get_balance("TFUEL")
            if TFUEL > 0.0001:
                upbit.sell_market_order("KRW-TFUEL", TFUEL)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-MANA", 0.51)
            price = get_current_price("KRW-MANA")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    MANA = get_balance("MANA")
                    if MANA < 0.0001:
                        upbit.buy_market_order("KRW-MANA", 20000)
        else:
            MANA = get_balance("MANA")
            if MANA > 0.0001:
                upbit.sell_market_order("KRW-MANA", MANA)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-ANKR", 0.51)
            price = get_current_price("KRW-ANKR")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ANKR = get_balance("ANKR")
                    if ANKR < 0.0001:
                        upbit.buy_market_order("KRW-ANKR", 20000)
        else:
            ANKR = get_balance("ANKR")
            if ANKR > 0.0001:
                upbit.sell_market_order("KRW-ANKR", ANKR)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-AERGO", 0.51)
            price = get_current_price("KRW-AERGO")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    AERGO = get_balance("AERGO")
                    if AERGO < 0.0001:
                        upbit.buy_market_order("KRW-AERGO", 20000)
        else:
            AERGO = get_balance("AERGO")
            if AERGO > 0.0001:
                upbit.sell_market_order("KRW-AERGO", AERGO)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-AERGO", 0.51)
            price = get_current_price("KRW-AERGO")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    AERGO = get_balance("AERGO")
                    if AERGO < 0.0001:
                        upbit.buy_market_order("KRW-AERGO", 20000)
        else:
            AERGO = get_balance("AERGO")
            if AERGO > 0.0001:
                upbit.sell_market_order("KRW-AERGO", AERGO)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-ATOM", 0.51)
            price = get_current_price("KRW-ATOM")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ATOM = get_balance("ATOM")
                    if ATOM < 0.0001:
                        upbit.buy_market_order("KRW-ATOM", 20000)
        else:
            ATOM = get_balance("ATOM")
            if ATOM > 0.0001:
                upbit.sell_market_order("KRW-ATOM", ATOM)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-TT", 0.51)
            price = get_current_price("KRW-TT")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    TT = get_balance("TT")
                    if TT < 0.0001:
                        upbit.buy_market_order("KRW-TT", 20000)
        else:
            TT = get_balance("TT")
            if TT > 0.0001:
                upbit.sell_market_order("KRW-TT", TT)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-CRE", 0.51)
            price = get_current_price("KRW-CRE")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    CRE = get_balance("CRE")
                    if CRE < 0.0001:
                        upbit.buy_market_order("KRW-CRE", 20000)
        else:
            CRE = get_balance("CRE")
            if CRE > 0.0001:
                upbit.sell_market_order("KRW-CRE", CRE)

    except Exception as e:
        print(e)
        time.sleep(1)