import time
import pyupbit
import datetime

access = "PLHmUf3gpoyKYzAqFzzxJ8vH042arYEQfcfdizx1"
secret = "mqsj8p9QYwd3A1Iich0KctXiz4ZJQrhDPxxA39DF"

#변동성 돌파 전략으로 매수 목표가 조회
def get_target_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=2)
    target_price = df.iloc[0]['close'] + ((df.iloc[0]['high'] - df.iloc[0]['low']) * k)
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
        time.sleep(0.5)

        if now.hour == 9 and now.minute == 0 and 1 <=now.second <= 10:
            op_mode = True
            time.sleep(10)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-HIVE", 0.52)
            price = get_current_price("KRW-HIVE")
            buy_price = get_avg_buy_price("KRW-HIVE")
            if price < buy_price * 0.98:
                HIVE = get_balance("HIVE")
                upbit.sell_market_order("KRW-HIVE", HIVE)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    HIVE = get_balance("HIVE")
                    if HIVE < 0.0001:
                        upbit.buy_market_order("KRW-HIVE", 20000)
        else:
            HIVE = get_balance("HIVE")
            if HIVE > 0.0001:
                upbit.sell_market_order("KRW-HIVE", HIVE)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-KAVA", 0.52)
            price = get_current_price("KRW-KAVA")
            buy_price = get_avg_buy_price("KRW-KAVA")
            if price < buy_price * 0.98:
                KAVA = get_balance("KAVA")
                upbit.sell_market_order("KRW-KAVA", KAVA)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    KAVA = get_balance("KAVA")
                    if KAVA < 0.0001:
                        upbit.buy_market_order("KRW-KAVA", 20000)
        else:
            KAVA = get_balance("KAVA")
            if KAVA > 0.0001:
                upbit.sell_market_order("KRW-KAVA", KAVA)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-AHT", 0.52)
            price = get_current_price("KRW-AHT")
            buy_price = get_avg_buy_price("KRW-AHT")
            if price < buy_price * 0.98:
                AHT = get_balance("AHT")
                upbit.sell_market_order("KRW-AHT", AHT)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    AHT = get_balance("AHT")
                    if AHT < 0.0001:
                        upbit.buy_market_order("KRW-AHT", 20000)
        else:
            AHT = get_balance("AHT")
            if AHT > 0.0001:
                upbit.sell_market_order("KRW-AHT", AHT)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-LINK", 0.52)
            price = get_current_price("KRW-LINK")
            buy_price = get_avg_buy_price("KRW-LINK")
            if price < buy_price * 0.98:
                LINK = get_balance("LINK")
                upbit.sell_market_order("KRW-LINK", LINK)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    LINK = get_balance("LINK")
                    if LINK < 0.0001:
                        upbit.buy_market_order("KRW-LINK", 20000)
        else:
            LINK = get_balance("LINK")
            if LINK > 0.0001:
                upbit.sell_market_order("KRW-LINK", LINK)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-XTZ", 0.52)
            price = get_current_price("KRW-XTZ")
            buy_price = get_avg_buy_price("KRW-XTZ")
            if price < buy_price * 0.98:
                XTZ = get_balance("XTZ")
                upbit.sell_market_order("KRW-XTZ", XTZ)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    XTZ = get_balance("XTZ")
                    if XTZ < 0.0001:
                        upbit.buy_market_order("KRW-XTZ", 20000)
        else:
            XTZ = get_balance("XTZ")
            if XTZ > 0.0001:
                upbit.sell_market_order("KRW-XTZ", XTZ)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-BORA", 0.52)
            price = get_current_price("KRW-BORA")
            buy_price = get_avg_buy_price("KRW-BORA")
            if price < buy_price * 0.98:
                BORA = get_balance("BORA")
                upbit.sell_market_order("KRW-BORA", BORA)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    BORA = get_balance("BORA")
                    if BORA < 0.0001:
                        upbit.buy_market_order("KRW-BORA", 20000)
        else:
            BORA = get_balance("BORA")
            if BORA > 0.0001:
                upbit.sell_market_order("KRW-BORA", BORA)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-JST", 0.52)
            price = get_current_price("KRW-JST")
            buy_price = get_avg_buy_price("KRW-JST")
            if price < buy_price * 0.98:
                JST = get_balance("JST")
                upbit.sell_market_order("KRW-JST", JST)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    JST = get_balance("JST")
                    if JST < 0.0001:
                        upbit.buy_market_order("KRW-JST", 20000)
        else:
            JST = get_balance("JST")
            if JST > 0.0001:
                upbit.sell_market_order("KRW-JST", JST)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-CRO", 0.52)
            price = get_current_price("KRW-CRO")
            buy_price = get_avg_buy_price("KRW-CRO")
            if price < buy_price * 0.98:
                CRO = get_balance("CRO")
                upbit.sell_market_order("KRW-CRO", CRO)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    CRO = get_balance("CRO")
                    if CRO < 0.0001:
                        upbit.buy_market_order("KRW-CRO", 20000)
        else:
            CRO = get_balance("CRO")
            if CRO > 0.0001:
                upbit.sell_market_order("KRW-CRO", CRO)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-TON", 0.52)
            price = get_current_price("KRW-TON")
            buy_price = get_avg_buy_price("KRW-TON")
            if price < buy_price * 0.98:
                TON = get_balance("TON")
                upbit.sell_market_order("KRW-TON", TON)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    TON = get_balance("TON")
                    if TON < 0.0001:
                        upbit.buy_market_order("KRW-TON", 20000)
        else:
            TON = get_balance("TON")
            if TON > 0.0001:
                upbit.sell_market_order("KRW-TON", TON)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-SXP", 0.52)
            price = get_current_price("KRW-SXP")
            buy_price = get_avg_buy_price("KRW-SXP")
            if price < buy_price * 0.98:
                SXP = get_balance("SXP")
                upbit.sell_market_order("KRW-SXP", SXP)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    SXP = get_balance("SXP")
                    if SXP < 0.0001:
                        upbit.buy_market_order("KRW-SXP", 20000)
        else:
            SXP = get_balance("SXP")
            if SXP > 0.0001:
                upbit.sell_market_order("KRW-SXP", SXP)

    except Exception as e:
        print(e)
        time.sleep(1)
