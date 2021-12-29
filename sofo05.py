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
            target = get_target_price("KRW-MFT", 0.52)
            price = get_current_price("KRW-MFT")
            buy_price = get_avg_buy_price("KRW-MFT")
            if price < buy_price * 0.98:
                MFT = get_balance("MFT")
                upbit.sell_market_order("KRW-MFT", MFT)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    MFT = get_balance("MFT")
                    if MFT < 0.0001:
                        upbit.buy_market_order("KRW-MFT", 20000)
        else:
            MFT = get_balance("MFT")
            if MFT > 0.0001:
                upbit.sell_market_order("KRW-MFT", MFT)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-ONG", 0.52)
            price = get_current_price("KRW-ONG")
            buy_price = get_avg_buy_price("KRW-ONG")
            if price < buy_price * 0.98:
                ONG = get_balance("ONG")
                upbit.sell_market_order("KRW-ONG", ONG)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ONG = get_balance("ONG")
                    if ONG < 0.0001:
                        upbit.buy_market_order("KRW-ONG", 20000)
        else:
            ONG = get_balance("ONG")
            if ONG > 0.0001:
                upbit.sell_market_order("KRW-ONG", ONG)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-GAS", 0.52)
            price = get_current_price("KRW-GAS")
            buy_price = get_avg_buy_price("KRW-GAS")
            if price < buy_price * 0.98:
                GAS = get_balance("GAS")
                upbit.sell_market_order("KRW-GAS", GAS)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    GAS = get_balance("GAS")
                    if GAS < 0.0001:
                        upbit.buy_market_order("KRW-GAS", 20000)
        else:
            GAS = get_balance("GAS")
            if GAS > 0.0001:
                upbit.sell_market_order("KRW-GAS", GAS)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-UPP", 0.52)
            price = get_current_price("KRW-UPP")
            buy_price = get_avg_buy_price("KRW-UPP")
            if price < buy_price * 0.98:
                UPP = get_balance("UPP")
                upbit.sell_market_order("KRW-UPP", UPP)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    UPP = get_balance("UPP")
                    if UPP < 0.0001:
                        upbit.buy_market_order("KRW-UPP", 20000)
        else:
            UPP = get_balance("UPP")
            if UPP > 0.0001:
                upbit.sell_market_order("KRW-UPP", UPP)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-ELF", 0.52)
            price = get_current_price("KRW-ELF")
            buy_price = get_avg_buy_price("KRW-ELF")
            if price < buy_price * 0.98:
                ELF = get_balance("ELF")
                upbit.sell_market_order("KRW-ELF", ELF)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ELF = get_balance("ELF")
                    if ELF < 0.0001:
                        upbit.buy_market_order("KRW-ELF", 20000)
        else:
            ELF = get_balance("ELF")
            if ELF > 0.0001:
                upbit.sell_market_order("KRW-ELF", ELF)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-KNC", 0.52)
            price = get_current_price("KRW-KNC")
            buy_price = get_avg_buy_price("KRW-KNC")
            if price < buy_price * 0.98:
                KNC = get_balance("KNC")
                upbit.sell_market_order("KRW-KNC", KNC)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    KNC = get_balance("KNC")
                    if KNC < 0.0001:
                        upbit.buy_market_order("KRW-KNC", 20000)
        else:
            KNC = get_balance("KNC")
            if KNC > 0.0001:
                upbit.sell_market_order("KRW-KNC", KNC)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-BSV", 0.52)
            price = get_current_price("KRW-BSV")
            buy_price = get_avg_buy_price("KRW-BSV")
            if price < buy_price * 0.98:
                BSV = get_balance("BSV")
                upbit.sell_market_order("KRW-BSV", BSV)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    BSV = get_balance("BSV")
                    if BSV < 0.0001:
                        upbit.buy_market_order("KRW-BSV", 20000)
        else:
            BSV = get_balance("BSV")
            if BSV > 0.0001:
                upbit.sell_market_order("KRW-BSV", BSV)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-THETA", 0.52)
            price = get_current_price("KRW-THETA")
            buy_price = get_avg_buy_price("KRW-THETA")
            if price < buy_price * 0.98:
                THETA = get_balance("THETA")
                upbit.sell_market_order("KRW-THETA", THETA)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    THETA = get_balance("THETA")
                    if THETA < 0.0001:
                        upbit.buy_market_order("KRW-THETA", 20000)
        else:
            THETA = get_balance("THETA")
            if THETA > 0.0001:
                upbit.sell_market_order("KRW-THETA", THETA)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-QKC", 0.52)
            price = get_current_price("KRW-QKC")
            buy_price = get_avg_buy_price("KRW-QKC")
            if price < buy_price * 0.98:
                QKC = get_balance("QKC")
                upbit.sell_market_order("KRW-QKC", QKC)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    QKC = get_balance("QKC")
                    if QKC < 0.0001:
                        upbit.buy_market_order("KRW-QKC", 20000)
        else:
            QKC = get_balance("QKC")
            if QKC > 0.0001:
                upbit.sell_market_order("KRW-QKC", QKC)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-BTT", 0.52)
            price = get_current_price("KRW-BTT")
            buy_price = get_avg_buy_price("KRW-BTT")
            if price < buy_price * 0.98:
                BTT = get_balance("BTT")
                upbit.sell_market_order("KRW-BTT", BTT)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    BTT = get_balance("BTT")
                    if BTT < 0.0001:
                        upbit.buy_market_order("KRW-BTT", 20000)
        else:
            BTT = get_balance("BTT")
            if BTT > 0.0001:
                upbit.sell_market_order("KRW-BTT", BTT)

    except Exception as e:
        print(e)
        time.sleep(1)
